from flask import session


# セッションにアンケート結果を保存
def save_survey_data(age, gender, skin_issues):
    session['age'] = age
    session['gender'] = gender
    session['skin_issues'] = skin_issues

# セッションからアンケート結果を取得
def get_survey_data():
    age = session.get('age', '')
    gender = session.get('gender', '')
    skin_issues = session.get('skin_issues', [])
    return age, gender, skin_issues



# **アドバイス辞書**
ADVICE_DICT = {
    "乾燥": "肌のうるおいを保つために、保湿ケアを徹底しましょう。",
    "肌荒れ": "バリア機能を守るため、低刺激のスキンケアを選びましょう。",
    "ニキビ": "皮脂の過剰分泌を防ぐために、洗顔と保湿を適切に行いましょう。",
    "透明感のなさ": "ビタミンC配合のスキンケアで肌の明るさを改善。",
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
    return [ADVICE_DICT.get(issue, "特にアドバイスはありません") for issue in skin_issues]


