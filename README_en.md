<div align="center">
  <picture>
    <img src="https://raw.githubusercontent.com/emiche1108/LuminaScan/main/static/readme-images/logo.png" width="350" alt="LuminaScan Logo">
  </picture>  
  <br>

  <center>
    <a href="README.md">
      <img src="https://img.shields.io/badge/Japanese-🇯🇵-red?style=for-the-badge&logo=google-translate">
    </a>
    <a href="README_en.md">
      <img src="https://img.shields.io/badge/English-🇺🇸-blue?style=for-the-badge&logo=google-translate">
    </a>
  </center>
</div>


# Lumina Scan - 


### Table of Contents
- [💄 Application Description](#app-description)
- [🎯 Target Users](#target-user)
- [💡 Motivation for Development](#writing-motivation)
- [🏃‍♀️ Getting Started](#getting-started)
- [🛠️ Application Features](#app-features)
- [📈 Skills Improved Through Development](#gained-skills)
- [💻 Technologies Used](#tech-stack)
- [📊 Screen Flow](#screen-flow)
- [📂 Directory Structure](#directory-diagram)
<br>


## 💄 About the Application<a id="app-description"></a>
LuminaScan is a skin analysis application that uses image processing technology to quantify and visualize skin conditions.<br>
It analyzes facial images to assess factors such as moisture, oil balance, brightness, spots, wrinkles, texture, and dark circles.<br>
Based on these results, it provides appropriate skincare advice.<br>

Key Features
- Image Analysis: Facial recognition and image processing technology for skin condition assessment

- Score Display: Quantification of 7 skin indicators and visualization via graphs

- Advice Provision: Skincare recommendations based on diagnostic results
<br>


## 🎯 Target Users<a id="target-user"></a>
A skin diagnosis tool available for anyone regardless of gender or age.<br>
Recommended for business professionals who value cleanliness, as well as individuals concerned about changes in their skin.<br>
For those who want to integrate skincare into their daily lives more conveniently and smartly.
<br>


## 💡 Motivation for Development<a id="writing-motivation"></a>
While working in sales, I frequently engaged in data-driven decision-making, such as market analysis and customer demand forecasting.<br>
This experience deepened my fascination with demand prediction, and I gradually developed a desire to not just use data, but to build analytical systems myself.<br>
<br>
However, I found that developing and testing demand forecasting models independently was quite challenging.<br>
So, I sought a more accessible way to apply data analysis to a familiar topic.<br>
This led me to explore an approach that quantifies skin conditions through image analysis for objective evaluation, which became the foundation of 『Lumina Scan』<br>
<br>
This personal project allows me to deepen my understanding by learning the fundamentals of image processing and data analysis while applying them hands-on. My goal is to develop my technical skills and assess my aptitude as a programmer.<br>
<br>
<br>


---
---
## 🏃‍♀️ Getting Started<a id="getting-started"></a>
#### 1. Navigate to the directory
```
cd ~/Desktop/LuminaScan
```
#### 2. Set up a virtual environment (venv)
```
python -m venv venv
source venv/bin/activate    # On Windows, use `venv\Scripts\activate`
```
#### 3. Install required libraries
```
pip install --upgrade pip  
pip install flask opencv-python-headless pillow numpy
```
#### 4. Start the Flask application
```
python3 app.py
```
#### 5. If successful...
You will see Running on `http://127.0.0.1:5000/`. Open your browser and go to:
```
http://127.0.0.1:5000/
```

<br>
---
---



## 🛠️ Application Features<a id="app-features"></a>
#### ▶ Feature List

| Top Page | Service Description |
| ---------------- | ---------------- |
| [トップページ] | <img src="static/readme-images/index-image2.jpg" width="350" alt="3種メニュー"> |
| サービス内容の説明文を実装。 | 3種類の診断メニューのスタートボタンを実装。 |

| 肌に関するアンケート | 診断方法の選択 |
| ---------------- | ---------------- |
| <img src="static/readme-images/skinQ-image.jpg" width="350" alt="アンケート"> | <img src="static/readme-images/choose-image.jpg" width="350" alt="方法選択"> |
| 肌悩みの聞き取り機能を実装。 | **画像アップロード or カメラ撮影**<br>2種類の選択肢を実装。 |

| 写真撮影ページ | カメラ起動画面・顔認証 |
| ---------------- | ---------------- |
| <img src="static/readme-images/takephoto-image1.jpg" width="350" alt="写真"> | <img src="static/readme-images/takephoto-image2.jpg" width="350" alt="写真"> |
| カメラ起動前に注意事項を表示し、<br>撮影開始ボタンを押すとカメラが起動する<br>流れを実装。 | カメラ起動＋リアルタイムで顔認識システムを実装。<br>詳細はサンプル動画よりご覧下さい。 |

| 結果ページ | 7項目の説明|
| ---------------- | ---------------- |
| <img src="static/readme-images/report-image1.jpg" width="350" alt="チャート図"> | <img src="static/readme-images/report-image2.jpg" width="350" alt="詳細結果"> |
| 肌状態を採点し、7つの指標をもとに<br>レーダーチャートで視覚化する機能を実装。| アンケート結果と組み合わせて<br>適切なスキンケアアドバイスを表示|


#### ▶ Sample Feature Videos
| Sample Videos                         | Description               |
|---------------------------------------|---------------------------|
|<img src="https://github.com/emiche1108/LuminaScan/raw/main/static/readme-images/takephoto.gif" width="300" height="200" alt="リアルタイム顔認証">|【顔認識の流れ】<br>face-api.jsの学習済みモデルを使用し、顔認識を行う。<br><br>⚫︎ssdMobilenetv1 → カメラ映像から顔の位置を特定<br>⚫︎faceLandmark68Net → 目・鼻・口・輪郭など68箇所の特徴点を検出<br>⚫︎faceRecognitionNet → 類似度スコアを算出、特定の値以上でカメラ撮影を許可<br>|
|<img src="https://github.com/emiche1108/LuminaScan/raw/main/static/readme-images/report.gif" width="300" height="200" alt="アニメーション＆アドバイス表示">|【肌採点の流れ】<br>画像解析技術を用い、肌状態を数値化。<br><br>⚫︎画像解析 → 明度・彩度・色のバランスを分析し、肌の特徴を抽出<br>⚫︎特徴評価 → シミ・シワ・くま・水分量などを画像処理で測定し、数値化<br>⚫︎スコア算出 → 各評価を統合し、100点満点で肌状態を採点<br>|

<br>



## 📈 制作を通じて向上したスキル<a id="gained-skills"></a>
| Skill                        | Learning Content                   |
|------------------------------|------------------------------------|
|Web App Development            |Flask × OpenCV を活用した、画像処理 & Webアプリの実装       |
|Data Visualization             |Chart.js を用いた動的なデータの可視化|
|Front ↔ Back Integration       |JavaScript でのデータ取得・Chart.js への反映・Flaskとの連携　|
|Version Control with GitHub　  |効率的なバージョン管理・README作成・リポジトリの整理力向上      |
<br>

「この方法で良いのか？」「このコードはどこと連動しているのか？」と考える習慣が身につきました。<br>
試行錯誤を重ねる中で、要件定義の重要性を改めて実感するとともに、設計段階での見通しを立てる力が<br>向上したと感じています。<br>


### 制作期間
#### 2025年1月中旬〜2月中旬までの約30日間（README記入含む）<br>


### 今後の目標
ローカル環境だけでなく、Heroku や AWS にデプロイし「誰でも気軽に使えるアプリ」 を目指します。<br>
データベースを導入し、解析結果を蓄積・活用できる仕組み を構築したいと考えています。<br>
<br>


## 💻 Technologies Used<a id="tech-stack"></a>
| Category         | Technology Used              　|
|--------------|-----------------------------|
| Front-end    | HTML, CSS, JavaScript(Chart.js)    |
| Back-end     | python(Flask・OpenCV)         　   |
| Development Tools    | Visual Studio Code,GitHub, venv   |
<br>


### Screen Flow<a id="screen-flow"></a>
<img src="static/readme-images/UserFrow.png" width="650" alt="画面遷移図">



### ディレクトリー図<a id="directory-diagram"></a>
```
LuminaScan/
├── app.py             # Flaskアプリケーション（メイン処理）
├── process.py         # OpenCVを用いたオーバーレイ処理
├── trimming.py        # トリミング・グレースケール処理
├── skin_analysis.py   # 肌の解析（重要）
├── advice.py          # アンケート結果処理

├── templates/         # HTMLテンプレート（フロントエンド）
│   ├── index.html         # トップページ
│   ├── skinQ.html         # 肌悩みアンケート
│   ├── choose.html        # 画像アップロード or 撮影の選択
│   ├── upload_photo.html  # 画像アップロード
│   ├── take_photo.html    # 撮影ページ
│   ├── animation.html     # アニメーション
│   ├── error.html         # エラーページ
│   └── result.html        # 結果ページ

├── static/           # 静的ファイル（モデル・スクリプト・画像など）
│   ├── models/           
│   │   └── weights/      # 学習済みモデルデータ（JSON形式）
│   │        ├── ssdMobilenetv1
│   │        ├── faceLandmark68Net
│   │        ├── faceRecognitionNet
│   │        └── その他のモデルファイル
│
│   ├── js/              # JavaScript（フロントエンドの動作）
│   │   ├── face-api.js       # 顔認証API
│   │   ├── face-api.min.js   # 顔認証API（ミニファイド版）
│   │   ├── skinQ.js          # アンケートページのスクリプト
│   │   ├── take-photo.js     # 撮影ページ（顔認識 99点以上で合格）
│   │   ├── upload-photo.js   # アップロードページ（顔認識 90点以上で合格）
│   │   ├── animation.js      # アニメーション処理
│   │   ├── chart.js          # 結果ページのグラフ
│   │   └── result.js         # 結果ページの処理
│
│   ├── css/            # スタイルシート（デザイン関連）
│   │   ├── animation.css     # アニメーション専用CSS
│   │   └── style.css         # 全体のスタイル
│
│   ├── 01uploads/      # 元画像（撮影・アップロードされた画像）
│   │   └── image1.jpg
│
│   ├── 02trimmed/      # トリミング後の画像（顔部分のみ）
│   │   └── image1.jpg

│   ├── 03gray/         # グレースケール後の画像
│   │   └── image1.jpg
│
│   ├── 03final/        # オーバーレイ済みの画像
│   │   └── image1.jpg
│
│   ├── fixed-images/   # 固定画像（ヘッダー・フッターなど）
│   │   ├── header.jpeg
│   │   └── footer.jpeg
```

