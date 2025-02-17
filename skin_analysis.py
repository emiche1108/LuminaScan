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
    #光沢が強い& シャープネスが高いほど、皮脂が多いと判定する。
    highlight_pixels = np.sum(v > 180) / (face_img.shape[0] * face_img.shape[1]) * 100  # 光沢V値が180 以上
    sharpness = np.clip(cv2.Laplacian(gray, cv2.CV_64F).var(), 10, 500)  # 500以上にならないように
    oil_balance_score = normalize((highlight_pixels * 0.5 + sharpness * 0.3 + mean_saturation * 0.2), 10, 250)  


    # **3️⃣ 明るさ（明度の平均）**
    brightness_score = normalize(mean_brightness, 50, 240) #Vチャンネルの平均値（明度） を利用



    # **4️⃣ シミ（肌との差を考慮した色素沈着検出）**
    skin_median = np.median(hsv, axis=(0,1))

    # 影の影響を減らすために、肌の基準色を顔の中央部分で測定
    center_region = hsv[hsv.shape[0]//3:hsv.shape[0]//2, hsv.shape[1]//3:hsv.shape[1]//2, :]
    center_skin_median = np.median(center_region, axis=(0,1))

    hue_diff = np.abs(h - center_skin_median[0])
    sat_diff = np.abs(s - center_skin_median[1])
    val_diff = np.abs(v - center_skin_median[2])

    # 色の違いとコントラストを統合
    color_diff = hue_diff * 0.4 + sat_diff * 0.4 + val_diff * 0.2
    contrast_map = cv2.absdiff(gray, cv2.GaussianBlur(gray, (5,5), 0))

    # シミスコア
    spots_score = normalize(np.mean(color_diff) * 0.6 + np.mean(contrast_map) * 0.4, 1, 30, inverse=True)



    # **5️⃣ シワ（エッジ検出 + コントラスト）**
    edges = cv2.Canny(gray, 50, 150)
    wrinkles_intensity = np.mean(edges)
    wrinkles_score = normalize(wrinkles_intensity, 10, 150, inverse=True)
    


    # **6️⃣ キメ（ガボールフィルタ + 局所コントラスト）**
    image = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)).apply(gray)  # 局所コントラスト補正
    gabor = cv2.filter2D(image, -1, cv2.getGaborKernel((9,9), 5.0, 0, 8.0, 0.5, 0, ktype=cv2.CV_32F))

    # ガボールフィルタの分散とヒストグラムの標準偏差を計算
    gabor_var = np.var(gabor)
    hist_std = np.std(cv2.calcHist([image], [0], None, [256], [0,256]))

    # スコア計算（正規化関数を適用）
    raw_score = gabor_var * 0.7 + hist_std * 0.3
    texture_fineness_score = normalize(raw_score, min_val=100, max_val=5000)  # 100~5000で正規化=5000以上は全部100点

    # 最終スコアの範囲を 0~100 に制限
    texture_fineness_score = np.clip(texture_fineness_score, 0, 100)

    print(f"[DEBUG] キメスコア: {texture_fineness_score}")



    # **7️⃣ くま（目の上下の明るさの差 - 目の部分だけ）**
    eye_upper = gray[gray.shape[0]//3 - gray.shape[0]//10 : gray.shape[0]//3 + gray.shape[0]//20, :]
    eye_lower = gray[gray.shape[0]//2 - gray.shape[0]//20 : gray.shape[0]//2 + gray.shape[0]//10, :]
    
    #中央値の計算
    upper_median = np.median(eye_upper)
    lower_median = np.median(eye_lower)

    dark_circle_diff = upper_median - lower_median  # 明るさの差
    dark_circle_std = np.std(eye_lower)  # 目の下の標準偏差
    dark_circles_score = normalize(dark_circle_diff * 0.7 + dark_circle_std * 0.3, 5, 30, inverse=True)
    # 差分 + 標準偏差を考慮



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


    # "scores" を含めて返す
    return {"scores": analysis_results}

