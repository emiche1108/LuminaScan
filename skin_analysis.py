import cv2
import numpy as np



# スコア算出関数
def normalize(value, min_val, max_val, inverse=False):
    """値を0~100のスコアに正規化する"""
    if value is None:
        return 0  # None が来たら 0 にする（エラー回避）
    
    score = 100 * (value - min_val) / (max_val - min_val)
    score = max(0, min(score, 100))  # 0~100の範囲に制限
    score = 100 - score if inverse else score  # 逆スコア
    return int(score)


# 肌診断関数
def analyze_skin(image_path):
    # 画像の読み込み
    face_img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if face_img is None:
        raise ValueError(f"画像が読み込めません: {image_path}")
    
    # BGR -> HSV 変換
    hsv = cv2.cvtColor(face_img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    
    # グレースケール変換
    gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
    


    # **1️⃣ 水分量（明度 + 青成分 + 彩度）**
    mean_brightness = np.mean(v)
    mean_blue = np.mean(face_img[:, :, 0])  # Bチャンネル（青色）
    mean_saturation = np.mean(s)
    moisture_level = normalize((mean_brightness * 0.4 + mean_blue * 0.3 + mean_saturation * 0.3), 50, 230)
    

    # **2️⃣ 皮脂バランス（光沢 + シャープネス + 彩度）**
    highlight_pixels = np.sum(v > 210) / (face_img.shape[0] * face_img.shape[1]) * 100
    sharpness = cv2.Laplacian(gray, cv2.CV_64F).var()
    oil_balance_score = normalize((highlight_pixels * 0.5 + sharpness * 0.3 + mean_saturation * 0.2), 5, 100)
    

    # **3️⃣ 明るさ（明度の平均）**
    brightness_score = normalize(mean_brightness, 50, 240)
    

    # **4️⃣ シミ（暗いピクセルの割合）**
    dark_pixels = np.sum(gray < 50) / (gray.shape[0] * gray.shape[1]) * 100
    spots_score = 100 if dark_pixels == 0 else normalize(dark_pixels, 0, 7, inverse=True)
    

    # **5️⃣ シワ（エッジ検出 + コントラスト）**
    edges = cv2.Canny(gray, 50, 150)
    wrinkles_intensity = np.mean(edges)
    wrinkles_score = normalize(wrinkles_intensity, 10, 150, inverse=True)
    

    # **6️⃣ キメ（テクスチャの滑らかさ）**
    texture_fineness = cv2.Laplacian(gray, cv2.CV_64F).var()
    texture_fineness_score = normalize(texture_fineness, 500, 5000)
    

    # **7️⃣ くま（目の上下の明るさの差）**
    upper_face = np.mean(gray[:gray.shape[0]//2, :])
    lower_face = np.mean(gray[gray.shape[0]//2:, :])
    dark_circles_score = normalize(upper_face - lower_face, 5, 40, inverse=True)
    
    

    # 解析結果
    analysis_results = {
        "水分量": moisture_level,  
        "皮脂バランス": oil_balance_score,
        "明るさ": brightness_score,
        "シミ": spots_score,
        "シワ": wrinkles_score,
        "キメ": texture_fineness_score,
        "くま": dark_circles_score
    }
    print(f"[DEBUG] 解析結果: {analysis_results}")
        
    # 画像にオーバーレイ
    # #output_path = process_image(face_img_path, analysis_results)


    # 修正: "scores" を含めた辞書として返す
    return {"scores": analysis_results}

