document.addEventListener("DOMContentLoaded", function () {
    console.log(" JavaScript が正しく読み込まれました！");
});



// ランダムな位置を生成する関数
function getRandomPosition() {
    const x = Math.random() * 500 - 250; // -250px～250pxの範囲でランダム移動
    const y = Math.random() * 400 - 200; // -200px ～ 200px
    const scale = Math.random() * 0.6 + 0.7; // 70% ～ 130% の大きさ
    return `translate(${x}px, ${y}px)`;
}

// サークルを動かす関数
function animateCircles() {
    const circles = document.querySelectorAll(".circle");
    circles.forEach(circle => {
        circle.style.transform = getRandomPosition();
    });
}
//1秒毎にランダムに動く
setInterval(animateCircles, 1000); 


// 10秒後にアニメーションを終了する
setTimeout(() => {
    const loadingScreen = document.getElementById("loading-screen");
    if (loadingScreen) {
        loadingScreen.style.display = "none";
    }

    // 直に `/result` にリダイレクト
    window.location.href = `/result`;
}, 10000);
