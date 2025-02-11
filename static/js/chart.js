document.addEventListener("DOMContentLoaded", function() {
    Chart.register(ChartDataLabels); 
    // HTMLの読み込みが完了した後に実行する
    
    // レーダーチャートを描画するためのコンテキストを取得
    const ctx = document.getElementById('radarChart')?.getContext('2d');
    if (!ctx) {
        console.error(" エラー: #radarChart が見つかりません！");
        return;
    }

    // **データ取得**
    const scores = [
        parseInt(document.getElementById("moisture_level").innerText) || 0,
        parseInt(document.getElementById("oil_level").innerText) || 0,
        parseInt(document.getElementById("brightness").innerText) || 0,
        parseInt(document.getElementById("spots").innerText) || 0,
        parseInt(document.getElementById("wrinkles").innerText) || 0,
        parseInt(document.getElementById("texture_fineness").innerText) || 0,
        parseInt(document.getElementById("dark_circles").innerText) || 0
    ];
    console.log(" 取得したスコア:", scores);

    

    // レーダーチャートを作成
    new Chart(ctx, {
        type: 'radar', // レーダーチャートの種類
        data: {
            labels: ["水分量", "皮脂バランス", "明るさ", "シミ", "シワ", "キメ", "くま"], 
            datasets: [{
                data: scores,
                fill: true, // 内部を塗りつぶす
                backgroundColor: "rgba(46, 107, 193, 0.2)", 
                borderColor: "#F6F8FB", // 全体の枠線
                pointBackgroundColor: [
                    "#7EBBCC", // 水分量（青）
                    "#8FBB6B", // 皮脂バランス（緑）
                    "#FFC858", // 明るさ（黄色）
                    "#5D535E", // シミ（茶色）
                    "#E29EA6", // シワ（ピンク）
                    "#6495ED", // キメ（青）
                    "#D4A017"  // くま（ゴールド）
                ], 
                pointRadius: 5 // ポイントのサイズ
            }]
        },
        options: {
            responsive: true, // レスポンシブ対応
            maintainAspectRatio: false, //  アスペクト比を調整して左右のズレを防ぐ
            layout: {
                padding: {
                    left: 10,
                    right: 10,
                    top: 20,
                    bottom: 20
                }
            },
            animation: {
                duration: 7000 // チャートが広がる速度
                },
                plugins: {
                    legend: {
                        display: false // 説明文を非表示
                        },
                        datalabels: {display: false, // チャート内部のスコアを非表示
                            }
                        },
                        scales: {
                            r: { // r（半径方向）のスケール設定
                            suggestedMin: 50, 
                            suggestedMax: 100, 
                            ticks: {
                                stepSize: 20, 
                                font:{
                                size: 14,family: "'Shippori Mincho'", 
                                }
                        }, // チャートのメモリ
                        pointLabels: { 
                            font: { size: 18, family: "'Shippori Mincho'" ,weight: "bold" }, // 「水分量」などの不穏とサイズ
                            color: "#333",
                            padding: 20, // スコアは外側に表示
                            callback: function(value, index, values) {
                                return scores[index] + "  " + value; // スコア → ラベルの順                            }
                            }
                        }
                    }
                }
            },
            plugins: [ChartDataLabels] // ここで ChartDataLabels を登録
            }); 
    console.log("チャート描画完了！");
});
          