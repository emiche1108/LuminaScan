<div align="center">
   <picture>
   https://raw.githubusercontent.com/emiche1108/skincheck/main/readme_assets/ファイル名.png
   </picture>
</div>


### 目次
- [💄アプリケーションのご説明](#app-description)
- [🎯ターゲットユーザー](#target-user)
- [💡アプリケーションの作成動機](#writing-motivation)
- [🏃‍♀️スタートガイド（環境構築 & 起動手順）](#getting-started)
- [🛠️アプリケーションの機能紹介](#app-features)
- [📈制作を通じて向上したスキル](#gained-skills)
- [💻使用技術](#tech-stack)
- ER図
- [ディレクトリー図](#directory-diagram)
<br>


## 💄アプリケーションについて<a id="app-description"></a>

SkinCheckは、AI顔認識技術を活用した肌診断アプリ です。  
顔画像を解析し、水分量・皮脂バランス・明るさ・シミ・シワ・キメ・くま などの肌状態を数値化。  
その結果に基づいて、適切なスキンケアアドバイスを提供します。  

【主な特徴】  
- AI解析: 顔認識と画像処理技術を活用した肌コンディション診断
- スコア表示: 7つの肌指標を数値化し、グラフで可視化
- アドバイス提供: 診断結果に基づいたスキンケアの推奨
<br>


## 🎯ターゲットユーザー<a id="target-user"></a>
性別や年齢を問わず誰でも使える肌診断ツールです。  
清潔感を大切にしたいビジネスパーソンや、肌の変化が気になり始めた方にもおすすめです。  
スキンケアをもっと手軽に、スマートに取り入れたい方へ。  
<br>


## 💡作成したキッカケ<a id="writing-motivation"></a>
前職では、AIを活用した需要予測業務に携わっていました。  

業務以外でも 歯科医院のAIシミュレーター や 化粧品店のAIメイクシミュレーター など、  
身近な場面でAIに触れる機会が増え、AI技術の幅広い活用を実感しました。  

こうした経験を通じて「未来予測」への関心 が高まった結果
自らもAIを活用したシステムを開発してみたいと考えるようになりました。

AIの活用方法を深く理解することを目的 に、
実験的な個人プロジェクト としてこのアプリを開発しました。
<br>
<br>
<br>

---
---
## 🏃‍♀️スタートガイド（環境構築 & 起動手順）<a id="getting-started"></a>
以下の手順に従って ローカル環境 で実行できます。

#### 1. ZIPファイルをダウンロード
まずはアプリケーションのダウンロードと解凍してください。

#### 2. ディレクトリへ移動します。 
```
cd ~/Desktop/LuminaScan
```

#### 3. 仮想環境のセットアップ（venv）
```
$ python -m venv venv
$ source venv/bin/activate    # Windowsの場合は `venv\Scripts\activate`
```

#### 4. 必要なライブラリのインストール
```
pip install --upgrade pip  
pip install flask opencv-python-headless pillow numpy
```

#### 5. Flask アプリの起動  
```
$ python3 app.py
```

#### 6.成功すると…
Running on `http://127.0.0.1:5000/` と表示されます。<br> 
ブラウザを開いて以下のURLにアクセスしてください。
``` 
http://127.0.0.1:5000 
```
<br>

---
---

## 🛠️アプリケーション機能のご紹介<a id="app-features"></a>
#### ▶ 機能一覧
| トップページ |　サービス内容 |
| ---- | ---- |
| ![トップページ] | ![内容] |
|  | 3つのサービスの紹介 |

| 診断方法の選択 |　写真撮影|
| ---- | ---- |
| ![新規登録画面] | ![]|
| 新規アカウント登録機能を実装。 | マンダラシート形式でデータを表形式で表示する機能を実装（印刷可能）。 |

| 顔認証システム |　解析画面 |
| ---- | ---- |
| ![Mandalaチャート作成イントロ画面] | ![　PDF出力画面] |
| Mandalaチャートを作成する機能を実装。 |ユーザー同士で目標達成を応援し合う掲示板機能を実装。 |

| 顔認証システム |　解析画面 |
| ---- | ---- |
| ![Mandalaチャート作成イントロ画面] | ![　PDF出力画面] |
| Mandalaチャートを作成する機能を実装。 |ユーザー同士で目標達成を応援し合う掲示板機能を実装。 |



#### ▶ 機能サンプル動画
| サンプル動画                          | 説明                      |
|---------------------------------------|---------------------------|
| <img src="sample_videos/VisionGrid_sample_myPage.gif" width="400" alt="顔認証"> | カメラ撮影時のリアルタイム顔認証 |
| <img src="sample_videos/VisionGrid_sample_MandalaCreation.gif" width="400" alt="アニメーション"> | 解析中のアニメーション |
| <img src="sample_videos/VisionGrid_sample_MandalaCreation.gif" width="400" alt="アニメーション"> | 診断結果 |

<br>


## 📈 制作を通じて向上したスキル<a id="gained-skills"></a>
| スキル                         | 学習内容                           |
|------------------------------|------------------------------------|
|Webアプリ開発	                 |Flask × OpenCV を活用した、画像処理 & Webアプリの実装　　　　|
|データ可視化	                    |Chart.js を用いた動的なデータの可視化|
|フロントエンド ↔ バックエンド連携   |JavaScript でのデータ取得・Chart.js への反映・Flaskとの連携　|
|GitHub運用による、バージョン管理　　|効率的なバージョン管理・README作成・リポジトリの整理力向上　　　|

「この方法で良いのか？」「このコードはどこと連動しているのか？」と考える習慣がついたと思います。<br>
試行錯誤を繰り返す中で、要件定義の重要性を改めて実感しました。<br>


### 今後の目標
ローカル環境だけでなく、Heroku や AWS にデプロイし「誰でも気軽に使えるアプリ」 を目指します。<br>
データベースを導入し、解析結果を蓄積・活用できる仕組み を構築したいと考えています。
<br>


## 💻使用技術<a id="tech-stack"></a>
| 分類         | 使用技術                     　　|
|--------------|-----------------------------|
| フロントエンド | HTML, CSS, JavaScript(Chart.js)    |
| バックエンド   | python(Flask・OpenCV)         　   |
| 開発ツール     | Visual Studio Code,GitHub, venv   |
<br>


### ER図
<br>


### ディレクトリー図<a id="directory-diagram"></a>
```
LuminaScan/
├── app.py             # Flaskアプリケーション（メイン処理）
├── process.py         # OpenCVを用いたオーバーレイ処理
├── trimming.py        # 顔のトリミング処理
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
│
│   ├── 03final/        # オーバーレイ済みの最終画像
│   │   └── image1.jpg
│
│   ├── fixed-images/   # 固定画像（ヘッダー・フッターなど）
│   │   ├── header.jpeg
│   │   └── footer.jpeg
```







