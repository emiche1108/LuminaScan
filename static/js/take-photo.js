// モデルのパスを指定
const MODEL_URL = '/static/models/weights';

// モデルのロード
Promise.all([
    faceapi.nets.ssdMobilenetv1.loadFromUri(MODEL_URL), //顔の検出
    faceapi.nets.faceLandmark68Net.loadFromUri(MODEL_URL), //68個の座標の検出
    faceapi.nets.faceExpressionNet.loadFromUri(MODEL_URL), // 表情検出
    faceapi.nets.faceRecognitionNet.loadFromUri(MODEL_URL) // 顔認識
]).then(() => {
    console.log(" モデルの読み込みが完了しました！");
    document.getElementById('start-camera').addEventListener('click', startCamera);
}).catch((err) => {
    console.error(" モデルの読み込みに失敗しました:", err);
});



// カメラを起動する関数
async function startCamera() {
    const video = document.getElementById('video');
    const cameraContainer = document.getElementById('camera-container');
    const startButton = document.getElementById('start-camera');

    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        video.srcObject = stream;
        video.style.display = 'block';
        cameraContainer.style.display = 'block';
        startButton.style.display = 'none';
        
        detectFace();  // 顔認識開始
    } catch (err) {
        console.error(' カメラの起動に失敗しました', err);
    }
}



// 顔認識
async function detectFace() {
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    const takePhotoButton = document.getElementById('take-photo');
    const warningMessage = document.getElementById('error-message');

    
    video.addEventListener('play', async () => {
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;

        setInterval(async () => {
            const detections = await faceapi.detectAllFaces(video)
                .withFaceLandmarks()
                .withFaceDescriptors();

            context.clearRect(0, 0, canvas.width, canvas.height);

            faceapi.draw.drawDetections(canvas, detections);
            faceapi.draw.drawFaceLandmarks(canvas, detections);

        
            const detection = detections[0];
            // 99点以上で顔認識
            if (detection) {
                const score = detection.detection.score;
                if (score < 0.99) {
                    takePhotoButton.style.display = 'none';
                    document.getElementById('error-message').innerText = '顔が認識できません。位置を調整してください。';
                    document.getElementById('error-message').style.display = 'block';
                } else {
                    takePhotoButton.style.display = 'block';
                    document.getElementById('error-message').style.display = 'none';
                }
            }
        }, 1000);
    });
}



//  撮影ボタンが押されたら写真を撮る
async function capturePhoto() {
    const canvas = document.getElementById('photo-canvas');
    const context = canvas.getContext('2d');
    const video = document.getElementById('video');
    const takePhotoButton = document.getElementById('take-photo');
  
    if (!takePhotoButton) {
        console.error("❌ 撮影ボタンが見つかりません！");
        return;
    }

    // 撮影ボタンを一時的に無効化（連続クリック防止）
    takePhotoButton.disabled = true;

    // 写真撮影
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    // Base64形式で取得
    const photoData = canvas.toDataURL('image/png');

    // Flask に送信するデータ
    const requestData = JSON.stringify({
        photoData: photoData,
        filename: "image1.png"
    });
    

    //Flask に送信
    try {
        const response = await fetch('/take_photo_page', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: requestData
        });
        console.log("📩 Flask へのリクエスト送信完了！ステータス:", response.status);

        // レスポンスが正常かチェック
        if (!response.ok) {
            const errorText = await response.text();
            console.error(` 画像送信エラー: ${response.status} - ${errorText}`);
            alert(`画像の送信に失敗しました: ${errorText}`);
            takePhotoButton.disabled = false;
            return;
        }

        let responseData = await response.json();
        console.log("✅ Flask からのレスポンス:", responseData);

        
        if (responseData.redirect_url) {
            console.log("🔄 画像送信成功！アニメーションへ移動");

            // 🔥 4️⃣ アニメーションページ (`/animation`) に遷移
            window.location.assign('/animation');

            // アニメーションページで 10 秒後にリザルトへ遷移する処理は Flask 側 or animation.js で制御
        } else {
            console.error("❌ `redirect_url` がレスポンスに含まれていません！", responseData);
            alert("エラー: リダイレクトURLが見つかりません。");
            takePhotoButton.disabled = false;
        }
    } catch (error) {
        console.error("❌ ネットワークエラー:", error);
        alert("ネットワークエラーが発生しました。接続を確認してください。");
        takePhotoButton.disabled = false;
    }
}



// HTMLに `capturePhoto` を紐付け
document.getElementById('take-photo').addEventListener('click', capturePhoto);
