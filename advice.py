from flask import session


# セッションにアンケート結果を保存
def save_survey_data(age, gender, skin_issues):
    print(f"[DEBUG] 保存する `skin_issues`: {skin_issues}")

    # もし `skin_issues` がカンマ区切りの文字列だったらリスト化する
    if isinstance(skin_issues, str):
        skin_issues = skin_issues.split(",")
    
    session.permanent = True
    session['age'] = age
    session['gender'] = gender
    session['skin_issues'] = skin_issues
    session.modified = True 
    print(f"[DEBUG] セッションに保存された `skin_issues`: {session['skin_issues']}")



# セッションからアンケート結果を取得
def get_survey_data():
    age = session.get('age', '')
    gender = session.get('gender', '')
    skin_issues = session.get('skin_issues', [])

    print(f" [DEBUG] get_survey_data() の結果: age={age}, gender={gender}, skin_issues={skin_issues}")


    # もし `skin_issues` がカンマ区切りの文字列だったらリスト化する
    if isinstance(skin_issues, list):
        skin_issues = [issue.strip() for sublist in skin_issues for issue in sublist.split(",")]
    else:
        skin_issues = [issue.strip() for issue in skin_issues.split(",")]
    print(f" [DEBUG] `split()` 後の `skin_issues`: {skin_issues}")

    if not skin_issues:
        print("[WARNING] `skin_issues` が空です！データがセッションに保存されていない可能性があります。")

    return age, gender, skin_issues


# **アドバイス辞書**
ADVICE_DICT = {
    "乾燥": "肌のうるおいを保つために、保湿ケアを徹底しましょう。",
    "肌荒れ": "バリア機能を守るため、低刺激のスキンケアを選びましょう。",
    "ニキビ": "皮脂の過剰分泌を防ぐために、洗顔と保湿を適切に行いましょう。",
    "透明感のなさ": "ビタミンC配合のスキンケアを使用し、肌の明るさを改善しましょう。。",
    "毛穴の目立ち": "肌を引き締める化粧水を使いましょう。",
    "テカリ": "油分の少ないスキンケアを選び、皮脂バランスを整えましょう。",
    "シミ・ソバカス": "紫外線対策と美白成分を取り入れましょう。",
    "くま": "目元マッサージで血行を促進しましょう。",
    "シワ": "コラーゲン・ヒアルロン酸を取り入れ、ハリを与えましょう。",
    "たるみ": "顔の筋肉を鍛えるエクササイズを取り入れましょう。",
    "なし": "今のスキンケアを継続しましょう！"
}

# **アドバイス取得関数**
def get_advice(skin_issues):
    print(f" [DEBUG] `get_advice()` に渡された `skin_issues`: {skin_issues}")
    
    # もし `,` が残っていたら `split()` してリスト化
    if any("," in issue for issue in skin_issues):  
        print(" [ERROR] `skin_issues` に `,` が残っている！`split()` されていない！")
        skin_issues = [issue.strip() for sublist in skin_issues for issue in sublist.split(",")]
        print(f" [DEBUG] `split()` 修正後の `skin_issues`: {skin_issues}")
    
    if not skin_issues or "なし" in skin_issues:
        print("⚠️ [WARNING] `skin_issues` が空 or `なし` が含まれている → デフォルトメッセージを表示！")
        return ["特にアドバイスはありません。"]

    advice_list = [ADVICE_DICT.get(issue, "特にアドバイスはありません") for issue in skin_issues]
    
    print(f" [DEBUG] 生成されたアドバイス: {advice_list}")
    return advice_list





# 結果メッセージの生成
def generate_result_message(skin_issues, analysis_data):
    
    # **肌悩みメッセージ**
    if len(skin_issues) == 1:
        concerns_text = f"あなたは「{skin_issues[0]}」が気になるようですね。\n"
    elif len(skin_issues) >= 2:
        concerns_text = f"あなたは「{skin_issues[0]}」と「{skin_issues[1]}」が気になるようですね。\n"
    else:
        concerns_text = "あなたは特に気になる肌悩みはないようですね。\n"

    # **スコア別 肌状態**
    avg_score = sum(analysis_data.values()) / len(analysis_data) if analysis_data else 50  # デフォルト50
    if avg_score >= 80:
        skin_status = "肌状態は非常に良好です。この調子でスキンケアを続けましょう！\n"
    elif avg_score >= 60:
        skin_status = "肌状態は比較的良好です。\n"
    elif avg_score >= 50:
        skin_status = "肌状態はやや乱れがちです。\n"
    else:
        skin_status = "肌状態は要注意です。スキンケアを見直し、生活習慣にも気を配りましょう。\n"

    return f"{concerns_text}{skin_status}肌スコアを参考に、日々のスキンケアを継続しましょう。\n"

