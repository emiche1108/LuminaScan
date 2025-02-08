from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory, abort, jsonify
import os
import base64  # 写真撮影。Base64エンコードとデコードを行う
import json 
import cv2
from advice import save_survey_data, get_survey_data, get_advice #アドバイス
from advice import ADVICE_DICT  # アドバイス辞書は advice.py にある
from trimming import extract_face  # トリミング処理
import numpy as np
from skin_analysis import analyze_skin  # 解析結果
#from process import process_image # オーバーレイ



# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__, static_folder="static", template_folder="templates")
# 管理用の秘密鍵
app.secret_key = os.urandom(24)  

# 保存先フォルダ
UPLOAD_FOLDER = "static/01uploads"
TRIM_FOLDER = "static/02trimmed"
#PROCESSED_FOLDER = "static/03final"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TRIM_FOLDER'] = TRIM_FOLDER
#app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER


# 保存ファイルの名前(固定)
FILENAME = "image1.png"

# 許可するファイル形式（拡張子）の設定
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# ファイル拡張子の確認
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



# 顔認識学習済み情報の読み込み
@app.route('/models/weights/<filename>')
def serve_models(filename):
    return send_from_directory(os.path.join(app.root_path, 'static/models/weights'), filename)



# トップページ（index.html）→アンケートページ（skinQ.html）へ
@app.route('/')
def home():
    return render_template('index.html')



# アンケートページ（skinQ.html）→選択ページ（choose _image.html）へ
@app.route('/skinQ', methods=['GET', 'POST'])
def skinQ():
    if request.method == 'POST':
        age = request.form.get('age')
        gender = request.form.get('gender')
        skin_issues = request.form.getlist('skin_issues') or ['なし']

        # アンケート結果を保存
        save_survey_data(age, gender, skin_issues)

        # 次のページ（画像選択ページ）へリダイレクト
        return redirect(url_for('choose_image'))
    
    return render_template('skinQ.html')



# 選択ページ（choose_image.html）
@app.route('/choose_image')
def choose_image():
    return render_template('choose_image.html')



# 画像保存先の宣言
def save_image(photo_data):
    filepath = os.path.join(UPLOAD_FOLDER, FILENAME)
    
    try:
        with open(filepath, 'wb') as f:
            f.write(photo_data)
        print(f" 画像保存成功: {filepath}")
        return filepath  
    
    #ファイルのパスを返す
    except Exception as e:
        print(f" 画像保存エラー: {e}")
        abort(500, "画像保存に失敗しました")



# 顔認識処理を共通化（顔が認識できなかったらエラー JSON を返す）
def process_face(filepath):
    trimmed_path = os.path.join(TRIM_FOLDER, FILENAME)
    #processed_path = os.path.join(PROCESSED_FOLDER, FILENAME)

    try:
        face_region = extract_face(filepath)  # トリミング

        # 顔認識が失敗したらエラーページへ JSON で返す
        if face_region is None or not isinstance(face_region, np.ndarray):
            print(" 顔が認識できませんでした！")
            return jsonify({
                "error": "顔が認識できませんでした",
                "redirect_url": url_for('error_page', message="顔が認識できませんでした。別の写真を試してください。")
            }), 400  
        print(f" 保存前のファイル確認: {trimmed_path}, 存在する？ {os.path.exists(trimmed_path)}")

        # トリミング画像の保存
        cv2.imwrite(trimmed_path, face_region)
        if os.path.exists(trimmed_path):
            print(f" トリミング画像を保存成功: {trimmed_path}")
        else:
            print(f" [ERROR] トリミング画像の保存に失敗しました: {trimmed_path}")
            return jsonify({
                "error": "トリミング画像の保存に失敗しました",
                "redirect_url": url_for('error_page', message=f"トリミング画像の保存に失敗しました: {trimmed_path}")
            }),500
        
        # **処理済み画像を保存**
        #cv2.imwrite(processed_path, face_region)
        #if os.path.exists(processed_path):
            print(f" 処理済み画像を保存成功: {processed_path}")
        #else:
        #    print(f" [ERROR] 処理済み画像の保存に失敗しました: {processed_path}")

        return jsonify({
            "message": "画像処理完了",
            "redirect_url": url_for('result')
        })

    except Exception as e:
        print(f" トリミングエラー: {e}")
        return jsonify({
            "error": "顔のトリミングに失敗しました",
            "redirect_url": url_for('error_page', message="顔のトリミング中にエラーが発生しました")
        }),500



# ...写真撮影を選択した場合
@app.route('/take_photo_page', methods=['GET', 'POST'])
def take_photo_page():
    if request.method == 'GET':
        return render_template('take_photo.html')

    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "データが送信されていません"}), 400

        photo_data = data.get("photoData", "")
        if not photo_data:
            return jsonify({"error": "photoData が空です"}), 400

        # 画像保存
        photo_data = base64.b64decode(photo_data.replace("data:image/png;base64,", ""))
        filepath = save_image(photo_data)

        # 顔認識 & JSON 返却
        return process_face(filepath)

    except Exception as e:
        print(f" サーバーエラー: {e}")
        return jsonify({"error": "サーバー内部エラー"}), 500
    



# ...画像アップを選択した場合
@app.route('/upload_photo', methods=['GET', 'POST'])
def upload_photo_page():
    if request.method == 'GET':
        return render_template('upload_photo.html')

    try:
        if 'file' not in request.files:
            return jsonify({"error": "ファイルが送信されていません"}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "ファイルが選択されていません"}), 400

        # 画像を保存
        filepath = save_image(file.read())

        # 顔認識 & JSON 返却
        response_json = process_face(filepath)

        # **Flask のレスポンスをログ出力して確認**
        print(" Flask のレスポンス:", response_json)

        return response_json  # **JSON をそのまま返す**

    except Exception as e:
        print(f"サーバーエラー: {e}")
        return jsonify({"error": "サーバー内部エラー"}), 500



# エラー時のリンク
@app.route('/error')
def error_page():
    message = request.args.get("message", "不明なエラーが発生しました")
    return render_template('error.html', error_message=message)

# エラー時の日本語表記
def json_response(data, status=200):
    return app.response_class(
        response=json.dumps(data, ensure_ascii=False),  # ← ここで日本語を返せるようになる
        status=status,
        mimetype="application/json"
    )



# 解析
@app.route("/analyze", methods=["POST"])
def analyze():
    if "image" not in request.files:
        return jsonify({"error": "画像がアップロードされていません"}), 400

    file = request.files["image"]
    if file.filename == "":
        return jsonify({"error": "ファイルが選択されていません"}), 400

    image_path = os.path.join(UPLOAD_FOLDER, FILENAME)
    file.save(image_path)

    # `analyze_skin()` を呼び出す
    results = analyze_skin(image_path)

    # 解析後の画像を保存（仮の処理）
    #processed_image_path = os.path.join(PROCESSED_FOLDER, file.filename)
    #cv2.imwrite(processed_image_path, cv2.imread(image_path))

    # フロントエンド用のデータとして URL を追加
    #results["processed_image"] = f"/{processed_image_path}"

    return jsonify(results)



# アニメーション
@app.route('/animation')
def start_animation():
    print("🎬 アニメーションページを表示")  
    return render_template('animation.html')  



# 結果ページ
@app.route('/result')
def result():
    filename = "image1.png"  
    trimmed_path = os.path.join(TRIM_FOLDER, filename)  
    # processed_path = os.path.join(PROCESSED_FOLDER, filename)  

    print(f"🔍 確認: トリミング画像 → {trimmed_path}, 存在する？ {os.path.exists(trimmed_path)}")
    #print(f"🔍 確認: 解析済み画像 → {processed_path}, 存在する？ {os.path.exists(processed_path)}")

    if not os.path.exists(trimmed_path):
        return redirect(url_for('error_page', message=f"トリミング画像が見つかりません: {trimmed_path}"))

    # **Flask に渡す画像の URL**
    #processed_image_url = url_for('static', filename=f'03final/{filename}')
    #print(f"✅ Flask に渡す `processed_image` の URL → {processed_image_url}")  



     # **アンケートデータを取得（定義）**
    age, gender, skin_issues = get_survey_data()  

    # **解析データを取得**
    analysis_result = analyze_skin(trimmed_path) 
    print(f"[DEBUG] Flask に渡すデータ: {analysis_result}")

    analysis_data = analysis_result.get("scores", {})
    print(f"[DEBUG] Flask に渡すデータ: {analysis_result}")

    if "scores" not in analysis_result:
        return redirect(url_for('error_page', message="解析に失敗しました"))
    
    #`result.html` に渡す**
    analysis_data = analysis_result["scores"] 

    # **アドバイスを取得**
    advice_list = get_advice(skin_issues)



    return render_template(
        'result.html',
        filename=filename,
        # original_image=url_for('static', filename=f'01uploads/{filename}'),
        # trimming_image=url_for('static', filename=f'02trimmed/{filename}'),
        # processed_image=processed_image_url, 

        advice=advice_list ,
        age=age, gender=gender, skin_issues=skin_issues,
        
        moisture_level=analysis_data.get('水分量', 'N/A'),
        oil_balance=analysis_data.get('皮脂バランス', 'N/A'),
        brightness=analysis_data.get('明るさ', 'N/A'),
        spots=analysis_data.get('シミ', 'N/A'),
        wrinkles=analysis_data.get('シワ', 'N/A'),
        texture_fineness=analysis_data.get('キメ', 'N/A'),
        dark_circles=analysis_data.get('くま', 'N/A')
    )





if __name__ == '__main__':
    app.run(debug=True)
    