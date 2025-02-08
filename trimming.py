import os
from PIL import Image
import cv2
import numpy as np




# 顔検出＆トリミング
def extract_face(image_path):
    # OpenCVで画像を読み込み
    img = cv2.imread(image_path,cv2.IMREAD_UNCHANGED)

    # OpenCVでの読み込みに失敗した場合、PILで読み込んでOpenCV形式に変換
    if img is None:
        try:
            print(f" OpenCV で画像を開けなかったため、PIL で開きます: {image_path}")
            img_pil = Image.open(image_path).convert("RGB")  # PNG対応
            img = np.array(img_pil)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # OpenCV形式に変換
            print("✅ PIL で画像を開いて OpenCV に変換成功！")
        except Exception as e:
            print(f"❌ [ERROR] PIL でも画像を開けませんでした: {e}")
            return None
    
    print(f"✅ 画像の読み込み成功: {image_path}, 画像サイズ: {img.shape}")


    # **RGBA の場合、BGR に変換**
    if img.shape[-1] == 4:  
        print("🔍 透明チャンネルを削除します")
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    #  顔認識モデルのパス
    face_cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    if not os.path.exists(face_cascade_path):
        print(f"❌ [ERROR] 顔認識モデルが見つかりません: {face_cascade_path}")
        return None

    #  顔認識モデルを読み込む
    face_cascade = cv2.CascadeClassifier(face_cascade_path)    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #  顔の検出
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
    
    if len(faces) == 0:
        print("❌ [ERROR] 顔が検出されませんでした")
        print("🔍 考えられる原因:明るさ・コントラスト・角度")
        return None


    # 顔をトリミング
    for (x, y, w, h) in faces:
         if w < 50 or h < 50:  # 小さすぎる顔は誤検出の可能性があるので無視
            continue
         face_region = img[y:y+h, x:x+w]  
         break  

    if face_region is None or face_region.size == 0:
        print("❌ [ERROR] 顔の切り抜きが失敗しました！")
        return None

    return face_region  # `face_region` を `process_face()` に渡す