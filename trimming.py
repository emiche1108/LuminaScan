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
            img_pil = Image.open(image_path).convert("RGB")  # PNG対応
            img = np.array(img_pil)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # OpenCV形式に変換
        except Exception as e:
            print(f"❌ [ERROR] 画像の読み込みに失敗しました: {e}")
            return None

    print(f"✅ 画像の読み込み成功: {image_path}, サイズ: {img.shape}")

    # **RGBA の場合、BGR に変換**
    if img.shape[-1] == 4:  
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    # **顔認識モデルのパス**
    face_cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    if not os.path.exists(face_cascade_path):
        print(f"❌ [ERROR] 顔認識モデルが見つかりません: {face_cascade_path}")
        return None

    # **顔認識モデルを読み込む**
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # **デバッグ用: グレースケール画像を保存**
    debug_gray_path = "debug_gray_image.png"
    cv2.imwrite(debug_gray_path, gray)
    print(f"📝 `debug_gray_image.png` にグレースケール画像を保存しました。顔が適切に映っているか確認してください。")

    # **顔の検出**
    print("🔍 顔検出を実行中...")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
    
    if len(faces) == 0:
        print("❌ [ERROR] 顔が検出されませんでした")
        return None

    # **最も大きな顔領域のみを選択**
    faces = sorted(faces, key=lambda x: x[2] * x[3], reverse=True)  # 面積順でソート
    x, y, w, h = faces[0]  # 一番大きな顔だけ取得
    print(f"✅ 顔検出成功！座標: x={x}, y={y}, w={w}, h={h}")


    # **誤検出防止（小さすぎる顔は無視）**
    if w < 100 or h < 100:
        print("❌ [ERROR] 検出された顔が小さすぎます。誤検出の可能性があります。")
        return None

    # **顔領域を切り抜き**
    face_region = img[y:y+h, x:x+w]

    # **データ型を uint8 に統一**
    if face_region.dtype != np.uint8:
        print(f"⚠️ [WARNING] `face_region` の dtype が {face_region.dtype} のため、uint8 に変換します")
        face_region = face_region.astype(np.uint8)

    print(f"✅ 顔のトリミング成功！サイズ: {face_region.shape}")
    return face_region



