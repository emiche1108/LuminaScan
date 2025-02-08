// モデルのパスを指定(takephotoでも定義済みなので回避)
if (typeof MODEL_URL === "undefined") {
    var MODEL_URL = '/static/models/weights';
}



// アップロードボタンの設定
document.addEventListener("DOMContentLoaded", async () => {
    console.log("📌 upload-photo.js 読み込み完了");

    // モデルのロード
    await loadModels();

    const uploadButton = document.getElementById('upload-button');
    if (!uploadButton) {
        console.error(" `#upload-button` が見つかりません！");
        return;
    }

    uploadButton.addEventListener('click', async () => {
        console.log("　アップロードボタンがクリックされました");

        const fileInput = document.getElementById('file-upload');
        const file = fileInput.files[0];
        
        if (!file) {
            console.warn(" ファイルが選択されていません");
            alert("ファイルを選択してください");
            return;
        }

        try {
            // **ボタンを無効化して二重送信を防ぐ**
            uploadButton.disabled = true;
            uploadButton.innerText = "アップロード中...";

            console.log(" 画像の顔認識をチェック...");
            await validateFaceBeforeUpload(file);

            console.log(" 顔が認識されました。アップロードを開始します...");
            await uploadFile(file);  // アップロード実行

        } catch (error) {
            console.error(" 顔認識エラー:", error);

            // **🔥 エラーページにリダイレクト**
            window.location.href = `/error?message=${encodeURIComponent(error)}`;

            // **ボタンを元に戻す**
            uploadButton.disabled = false;
            uploadButton.innerText = "アップロード";
        }
    });
});



// **✅ モデルのロードを関数化**
async function loadModels() {
    try {
        await Promise.all([
            faceapi.nets.ssdMobilenetv1.loadFromUri(MODEL_URL), // 顔の検出
            faceapi.nets.faceLandmark68Net.loadFromUri(MODEL_URL), // 68個の座標の検出
            faceapi.nets.faceExpressionNet.loadFromUri(MODEL_URL), // 表情検出
            faceapi.nets.faceRecognitionNet.loadFromUri(MODEL_URL) // 顔認識
        ]);
        console.log(" モデルの読み込みが完了しました！");
    } catch (err) {
        console.error(" モデルの読み込みに失敗しました:", err);
    }
}


// **✅ アップロード前に顔を認識する関数**
async function validateFaceBeforeUpload(file) {
    return new Promise((resolve, reject) => {
        const img = document.createElement("img");
        img.src = URL.createObjectURL(file);

        img.onload = async () => {
            const canvas = document.createElement("canvas");
            const context = canvas.getContext("2d");

            canvas.width = img.width;
            canvas.height = img.height;
            context.drawImage(img, 0, 0, img.width, img.height);

            const detections = await faceapi.detectAllFaces(canvas)
                .withFaceLandmarks()
                .withFaceDescriptors();

            console.log(" 画像内の顔検出結果:", detections);

            if (detections.length === 0 || detections[0].detection.score < 0.99) {
                reject(" 顔が認識できません。別の画像を試してください。");
            } else {
                resolve(true);
            }
        };

        img.onerror = () => {
            reject(" 画像の読み込みに失敗しました。");
        };
    });
}


//  画像を Flask に送信する
async function uploadFile(file) {
    const uploadButton = document.getElementById('upload-button');

    //  ファイルの再取得を防ぐため、一度 `file` を固定
    const fixedFile = file;  

    const formData = new FormData();
    formData.append("file", fixedFile);

    try {
        console.log(" Flask に画像をアップロード中...");

        const response = await fetch('/upload_photo', {
            method: 'POST',
            body: formData
        });

        console.log(" Flask へのリクエスト送信完了！ステータス:", response.status);

        const data = await response.json();
        console.log(" 受信データ:", data);

        if (!response.ok) {
            console.error(" 画像送信エラー:", response.statusText);
            alert("サーバーエラーが発生しました。もう一度試してください。");
            uploadButton.disabled = false;
            uploadButton.innerText = "アップロード";
            return;
        }

        if (data.redirect_url) {
            console.log(" リダイレクト先:", data.redirect_url);
            setTimeout(() => {
                try {
                    window.location.href = data.redirect_url;
                } catch (redirectError) {
                    console.error(" リダイレクト時のエラー:", redirectError);
                    alert("リダイレクト中にエラーが発生しました。");
                    window.location.href = "/error?message=リダイレクトに失敗しました";
                }
            }, 500);
        } else {
            console.error("リダイレクトURLが取得できません:", data);
            alert("エラーが発生しました。");

            // ** エラーページに遷移**
            window.location.href = "/error?message=リダイレクトURLが取得できませんでした";
        }
    } catch (error) {
        console.error(" ネットワークエラー:", error);
        alert("ネットワークエラーが発生しました。もう一度試してください。");

        // ** ネットワークエラー時もエラーページに遷移**
        window.location.href = "/error?message=ネットワークエラーが発生しました";

        uploadButton.disabled = false;
        uploadButton.innerText = "アップロード";
    }
}