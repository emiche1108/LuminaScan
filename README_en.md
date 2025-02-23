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
LuminaScan is a skin analysis app that quantifies and visualizes skin conditions using image processing technology.<br>
It analyzes facial images to assess factors such as moisture, oil balance, brightness, spots, wrinkles, texture, and dark circles.<br>
Based on these results, it provides personalized skincare advice.<br>

Key Features
- Image Analysis: Skin condition diagnosis using facial recognition and image processing technology<br>

- Score Display: Quantifies seven skin indicators and visualizes them in graphs<br>

- Advice Provision: Provides skincare recommendations based on diagnosis results<br>
<br>


## 🎯 Target Users<a id="target-user"></a>
A skin analysis tool for everyone, regardless of gender or age.<br>
Perfect for business professionals who care about their appearance and anyone noticing changes in their skin.<br>
For those who want to make skincare easy, smart, and part of their daily routine.<br>
<br>


## 💡 Motivation for Development<a id="writing-motivation"></a>
While working in sales, I frequently made data-driven decisions, such as market analysis and customer demand forecasting.<br>
Through this experience, I became fascinated by demand prediction and developed a desire to not just use data, <br>but to build analytical systems myself.<br>
<br>
However, I felt that the field of demand forecasting was too challenging to develop and test individually.<br>
So, I looked for a more accessible way to apply data analysis to a familiar topic.<br>
That’s when I came up with the idea of quantifying skin conditions using image analysis for objective evaluation,<br>
which led to the development of 『Lumina Scan』<br>
<br>
This personal project allows me to learn and apply image processing<br>
and data analysis hands-on strengthening my technical skills.<br>
It serves as both a learning experience and an opportunity to assess my potential as a programmer.<br>
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
source venv/bin/activate    # If you're using Windows, run `venv\Scripts\activate`
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
You will see Running on `http://127.0.0.1:5000/` Open your browser and go to
```
http://127.0.0.1:5000/
```
<br>


---
---
<br>


## 🛠️ Application Features<a id="app-features"></a>
#### ▶ Feature List

| Top Page | Service Description |
| ---------------- | ---------------- |
| [トップページ] | <img src="static/readme-images/index-image2.jpg" width="350" alt="Three diagnostic modes"> |
| Implemented a service description. | Implemented start buttons for three diagnostic modes. |

| Skincare Questionnaire | Select Diagnostic Method |
| ---------------- | ---------------- |
| <img src="static/readme-images/skinQ-image.jpg" width="350" alt="Questionn"> | <img src="static/readme-images/choose-image.jpg" width="350" alt="Select"> |
| Implemented a skin concern questionnaire feature.| **Image Upload or Camera Capture**<br>Implemented two options. |

| Take a Photo Page | Camera Launch・Face Recognition|
| ---------------- | ---------------- |
| <img src="static/readme-images/takephoto-image1.jpg" width="350" alt="Photo"> | <img src="static/readme-images/takephoto-image2.jpg" width="350" alt="Face Recognition"> |
|Implemented a feature to show a caution message<br>before launching the camera, then activate it<br>when the 'Start Shooting' button is pressed.|Implemented a real-time face recognition system. |

| Results Page | Explanation of 7 Items|
| ---------------- | ---------------- |
| <img src="static/readme-images/report-image1.jpg" width="350" alt="Chart"> | <img src="static/readme-images/report-image2.jpg" width="350" alt="Detailed Results"> |
|Implemented skin scoring to evaluate<br>skin condition. Visualized results<br>using a radar chart based on 7 indicators.| Implemented a feature to display<br>appropriate skincare advice.|


#### ▶ Sample Feature Videos
| Sample Videos                         | Description               |
|---------------------------------------|---------------------------|
|<img src="https://github.com/emiche1108/LuminaScan/raw/main/static/readme-images/takephoto.gif" width="300" height="200" alt="Face Recognition">|【Face Recognition Flow】<br>Face recognition is performed using pre-trained models from face-api.js.<br><br>⚫︎ssdMobilenetv1 → Detects facial positions from the camera feed.<br>⚫︎faceLandmark68Net →  Identifies 68 facial landmarks (eyes, nose, mouth, contours).<br>⚫︎faceRecognitionNet → Calculates similarity scores; allows capturing if above a certain threshold.<br>|
|<img src="https://github.com/emiche1108/LuminaScan/raw/main/static/readme-images/report.gif" width="300" height="200" alt="Animation & Advice Display">|【Skin Scoring Flow】<br>Utilizing image analysis technology to quantify skin condition.<br><br>⚫︎Image Analysis → Analyzes brightness, saturation, and color balance to extract skin features.<br>⚫︎Feature Evaluation → Measures and quantifies factors like spots, wrinkles, dark circles, and moisture levels through image processing.<br>⚫︎Score Calculation → Integrates all evaluations and assigns a skin score out of 100.<br>|
<br>



## 📈 Skills Improved Through Development<a id="gained-skills"></a>
| Skill                        | Learning Content                   |
|------------------------------|------------------------------------|
|Web App Development           |Implemented image processing & web app using Flask × OpenCV.  |
|Data Visualization            |Dynamic data visualization using Chart.js.　|
|Front ↔ Back Integration      |Data retrieval in JavaScript, integration with Chart.js, and interaction with Flask.|
|Version Control with GitHub　  |Improved version control efficiency, README creation, and repository organization skills. |
<br>

I developed a habit of questioning,<br>
"Is this the right approach?" and "Which part of the code does this interact with?"<br>

Through repeated trial and error, I reaffirmed the importance of requirement definition<br> 
and improved my ability to anticipate issues<br>
during the design phase.<br>


### Development Period
#### Approximately 30 days.<br>


### Next Steps
I aim to deploy the application not only in a local environment but also on Heroku and AWS, <br>
making it easily accessible to everyone.<br>
I plan to integrate a database to store and utilize analysis results effectively.<br>
<br>


## 💻 Technologies Used<a id="tech-stack"></a>
| Category         | Technology Used              　|
|--------------|-----------------------------|
| Front-end    | HTML, CSS, JavaScript(Chart.js)    |
| Back-end     | python(Flask・OpenCV)         　   |
| Development Tools  | Visual Studio Code,GitHub, venv   |
<br>


### Screen Flow<a id="screen-flow"></a>
<img src="static/readme-images/UserFrow.png" width="650" alt="screen-flow">



### Directory Diagram<a id="directory-diagram"></a>
```
LuminaScan/
├── app.py            
├── process.py         
├── trimming.py        
├── skin_analysis.py   
├── advice.py         

├── templates/         
│   ├── index.html        
│   ├── skinQ.html         
│   ├── choose.html        
│   ├── upload_photo.html  
│   ├── take_photo.html    
│   ├── animation.html   
│   ├── error.html        
│   └── result.html        

├── static/           
│   ├── models/           
│   │   └── weights/      # Pre-trained Model Data (JSON Format)
│   │        ├── ssdMobilenetv1
│   │        ├── faceLandmark68Net
│   │        ├── faceRecognitionNet
│   │        └── other model files
│
│   ├── js/              
│   │   ├── face-api.js      
│   │   ├── face-api.min.js   
│   │   ├── skinQ.js          
│   │   ├── take-photo.js     # Face Recognition: Pass with a Score of 99 or Higher
│   │   ├── upload-photo.js   # Face Recognition: Pass with a Score of 90 or Higher
│   │   ├── animation.js     
│   │   ├── chart.js          
│   │   └── result.js         
│
│   ├── css/            
│   │   ├── animation.css    
│   │   └── style.css         
│
│   ├── 01uploads/     
│   │   └── image1.jpg
│
│   ├── 02trimmed/      
│   │   └── image1.jpg

│   ├── 03gray/         
│   │   └── image1.jpg
│
│   ├── 03final/        
│   │   └── image1.jpg
│
│   ├── fixed-images/   
│   │   ├── header.jpeg
│   │   └── footer.jpeg
```

