import cv2
import os
import numpy as np



# 解析結果を画像にオーバーレイ
def add_analysis_overlay(img, analysis_results):
    if img is None:
        print("[ERROR] `add_analysis_overlay()` に渡された画像が None です！オーバーレイ処理をスキップ。")
        return img  # `None` を返さず、元の画像をそのまま返す

    overlay_data = [
        {"position": (50, 50), "text": f"水分量: {analysis_results.get('水分量', 'N/A')}", "color": (0, 255, 255)},
        {"position": (50, 100), "text": f"皮脂バランス: {analysis_results.get('皮脂バランス', 'N/A')}", "color": (255, 165, 0)},
        {"position": (50, 150), "text": f"明るさ: {analysis_results.get('明るさ', 'N/A')}", "color": (255, 255, 0)},
        {"position": (100, 200), "text": f"シミ: {analysis_results.get('シミ', 'N/A')}", "color": (255, 0, 0)},
        {"position": (100, 250), "text": f"シワ: {analysis_results.get('シワ', 'N/A')}", "color": (0, 255, 0)},
        {"position": (100, 300), "text": f"キメ: {analysis_results.get('キメ', 'N/A')}", "color": (0, 0, 255)},
        {"position": (100, 350), "text": f"くま: {analysis_results.get('くま', 'N/A')}", "color": (255, 0, 255)},
    ]

    for data in overlay_data:
        cv2.putText(
            img,
            data["text"],
            data["position"],
            cv2.FONT_HERSHEY_SIMPLEX,
            1,  
            data["color"],  
            2,  
            cv2.LINE_AA,
        )

    print("[DEBUG] オーバーレイ処理完了！")
    return img



# 保存先の指示　(03final の中に `image1.png`を保存)
def save_final_image(img, filename="image1.png"):  
    processed_dir = os.path.join(os.getcwd(), 'static', '03final')
    os.makedirs(processed_dir, exist_ok=True)

    final_image_path = os.path.join(processed_dir, filename)   
    
    if img is None:
        print("[ERROR] `save_final_image()` に渡された画像が None です！保存できません。")
        return None
    print(f"[DEBUG] 画像保存を試行: {final_image_path}")  # 保存先確認

    success_final = cv2.imwrite(final_image_path, img)  

    if success_final:
        print(f"[DEBUG] 処理済み画像保存成功: {final_image_path}")  
    else:
        print(f"[ERROR] `cv2.imwrite()` に失敗しました！画像を保存できません: {final_image_path}") 

    return final_image_path if success_final else None



# メイン処理　トリミング画像に、オーバーレイ
def process_image(image_path, analysis_results):
    print(f"[DEBUG] 画像処理開始: {image_path}")

    # トリミング画像の読み込み
    trimmed_image_path = os.path.join("static", "02trimmed", os.path.basename(image_path))
    img = cv2.imread(trimmed_image_path)

    if img is None:
        print(f"[ERROR] `02trimmed/` の画像が読み込めませんでした: {trimmed_image_path}")
        return None
    print("[DEBUG] `02trimmed/` の画像を正常に読み込みました！")


    # オーバーレイ
    img_with_overlay = add_analysis_overlay(img, analysis_results)
    
    if img_with_overlay is None:
        print("[ERROR] `add_analysis_overlay()` の結果が None です。処理を中止します。")
        return None
    print("[DEBUG] オーバーレイ処理が完了しました！")


    # `03final/` に `image1.png` を保存
    processed_image_path = save_final_image(img_with_overlay, "image1.png")  # 名前はimage1のままで

    if processed_image_path is None:
        print("[ERROR] `03final/` に画像を保存できませんでした。")
        return None

    print(f"[DEBUG] 画像処理完了: {processed_image_path}")
    return processed_image_path
