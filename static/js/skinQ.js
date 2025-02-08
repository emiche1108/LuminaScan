document.addEventListener("DOMContentLoaded", function () {
    console.log(" スクリプト読み込みOK");

    // 年齢プルダウンの設定
    const dropdownContainer = document.querySelector(".custom-dropdown");
    const dropdownBtn = document.querySelector(".dropdown-btn");
    const dropdownList = document.querySelector(".dropdown-list");
    const ageInput = document.getElementById("age");

    if (!dropdownContainer || !dropdownBtn || !dropdownList || !ageInput) {
        console.error("⚠️ 必要な要素が見つかりません。HTMLを確認してください。");
        return;
    }

    const ageRanges = [
        "10-14歳", "15-19歳", "20-24歳", "25-29歳",
        "30-34歳", "35-39歳", "40-44歳", "45-49歳",
        "50-54歳", "55-59歳", "60歳以上"
    ];

    ageRanges.forEach(age => {
        let li = document.createElement("li");
        li.textContent = age;
        li.setAttribute("data-value", age);

        li.addEventListener("click", function () {
            dropdownBtn.textContent = age; // 選択した年齢をボタンに表示
            ageInput.value = age; // フォーム送信用の hidden input に値を設定
            dropdownList.style.display = "none"; // 選択後にリストを閉じる
            dropdownContainer.classList.add("selected"); // 枠色をピンクにする

            console.log(" 選択された年齢:", age);
        });

        dropdownList.appendChild(li);
    });


    // ボタンクリックでリスト開閉
    dropdownBtn.addEventListener("click", function (event) {
        event.stopPropagation();
        dropdownList.style.display = (dropdownList.style.display === "block") ? "none" : "block";
    });


    // 外部クリックでリストを閉じる
    document.addEventListener("click", function (event) {
        if (!dropdownBtn.contains(event.target) && !dropdownList.contains(event.target)) {
            dropdownList.style.display = "none";
        }
    });



    // 性別選択ボタン
    const genderButtons = document.querySelectorAll(".gender-btn");
    const genderInput = document.getElementById("gender");

    if (genderButtons.length > 0 && genderInput) {
        genderButtons.forEach(button => {
            button.addEventListener("click", function () {
                // 他のボタンの選択を解除
                genderButtons.forEach(btn => btn.classList.remove("selected"));
                
                // クリックしたボタンを選択状態にする
                this.classList.add("selected");

                // hidden input に値を設定（フォーム送信用）
                genderInput.value = this.getAttribute("data-value");

                console.log(" 選択された性別:", genderInput.value);
            });
        });
    }



    // 🔹 肌悩みボタン（最大2つ選択可能）
    const skinButtons = document.querySelectorAll(".skin-btn");
    const skinInput = document.getElementById("skinIssues");
    let selectedValues = [];

    if (skinButtons.length > 0 && skinInput) { 
        skinButtons.forEach(button => {
            button.addEventListener("click", function () {
                const value = this.getAttribute("data-value");

                if (selectedValues.includes(value)) {
                    selectedValues = selectedValues.filter(v => v !== value);
                    this.classList.remove("selected");
                } else {
                    if (selectedValues.length < 2) { // 最大2つまで選択可能
                        selectedValues.push(value);
                        this.classList.add("selected");
                    }
                }

                // hidden input に選択値をセット（フォーム送信用）
                skinInput.value = selectedValues.join(",");
                console.log("🎯選択された肌悩み:", skinInput.value);
            });
        });
    }
});