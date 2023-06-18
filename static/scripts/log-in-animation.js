let toRegisterButton = document.getElementsByTagName("button")[0];
let toLoginButton = document.getElementsByTagName("button")[1];
let tipText = document.querySelector('#authentic-main > p');
let allDiv = document.querySelector('#authentic-main > div');
let formDiv = document.querySelector('#authentic-main > div > div:nth-of-type(2)')
let paths = document.querySelectorAll('#wave-svg > path');
let authentic = document.querySelector('#authentic-background');
let dynamicBackground = document.getElementById('dynamic-background');
let dynamicDiv = document.querySelectorAll('#dynamic-background > div');

function formSwitch(){
    toRegisterButton.addEventListener('click', function(){
            allDiv.classList.remove('form-move-reverse');
            formDiv.classList.remove('form-change-reverse');
            tipText.classList.remove('form-text-move-reverse');
            paths[0].classList.remove('wave1-reverse');
            paths[1].classList.remove('wave2-reverse');
            paths[2].classList.remove('wave3-reverse');
            paths[3].classList.remove('wave4-reverse');
            paths[4].classList.remove('wave5-reverse');
            dynamicBackground.classList.remove('div-change2');
            authentic.classList.remove('div-color-reverse');

            allDiv.classList.add('form-move');
            formDiv.classList.add('form-change');
            tipText.classList.add('form-text-move');
            paths[0].classList.add('wave1');
            paths[1].classList.add('wave2');
            paths[2].classList.add('wave3');
            paths[3].classList.add('wave4');
            paths[4].classList.add('wave5');
            dynamicBackground.classList.add('div-change');
            authentic.classList.add('div-color');
            setTimeout(function(){tipText.textContent = '注册regis';}, 750);
            setTimeout(function(){
                dynamicDiv[0].style.backgroundColor="rgba(255, 172, 56, 0.3)";
                dynamicDiv[1].style.backgroundColor="rgba(255, 172, 56, 0.3)";
                dynamicDiv[2].style.backgroundColor="rgba(255, 172, 56, 0.3)";
                dynamicDiv[3].style.backgroundColor="rgba(255, 172, 56, 0.3)";
                dynamicDiv[4].style.backgroundColor="rgba(255, 172, 56, 0.3)";
                dynamicDiv[5].style.backgroundColor="rgba(255, 172, 56, 0.3)";
                dynamicDiv[6].style.backgroundColor="rgba(255, 172, 56, 0.3)";
                dynamicDiv[7].style.backgroundColor="rgba(255, 172, 56, 0.3)";
                dynamicDiv[8].style.backgroundColor="rgba(255, 172, 56, 0.3)";
                dynamicDiv[9].style.backgroundColor="rgba(255, 172, 56, 0.3)";
                dynamicDiv[10].style.backgroundColor="rgba(255, 172, 56, 0.3)";
                dynamicDiv[11].style.backgroundColor="rgba(255, 172, 56, 0.3)";
                dynamicDiv[12].style.backgroundColor="rgba(255, 172, 56, 0.3)";
                dynamicDiv[13].style.backgroundColor="rgba(255, 172, 56, 0.3)";
                dynamicDiv[14].style.backgroundColor="rgba(255, 172, 56, 0.3)";
                dynamicDiv[15].style.backgroundColor="rgba(255, 172, 56, 0.3)";
                dynamicDiv[16].style.backgroundColor="rgba(255, 172, 56, 0.3)";
                dynamicDiv[17].style.backgroundColor="rgba(255, 172, 56, 0.3)";
            }, 1000);
        });
            
    toLoginButton.addEventListener('click',function(){
            allDiv.classList.remove('form-move');
            formDiv.classList.remove('form-change');
            tipText.classList.remove('form-text-move');
            paths[0].classList.remove('wave1');
            paths[1].classList.remove('wave2');
            paths[2].classList.remove('wave3');
            paths[3].classList.remove('wave4');
            paths[4].classList.remove('wave5');
            dynamicBackground.classList.remove('div-change');
            authentic.classList.remove('div-color');

            allDiv.classList.add('form-move-reverse');
            formDiv.classList.add('form-change-reverse');
            tipText.classList.add('form-text-move-reverse');
            paths[0].classList.add('wave1-reverse');
            paths[1].classList.add('wave2-reverse');
            paths[2].classList.add('wave3-reverse');
            paths[3].classList.add('wave4-reverse');
            paths[4].classList.add('wave5-reverse');
            dynamicBackground.classList.add('div-change2');
            authentic.classList.add('div-color-reverse');
            setTimeout(function(){tipText.textContent = '登录login';}, 750);
            setTimeout(function(){
                dynamicDiv[0].style.backgroundColor="rgba(56, 165, 255, 0.3)";
                dynamicDiv[1].style.backgroundColor="rgba(56, 165, 255, 0.3)";
                dynamicDiv[2].style.backgroundColor="rgba(56, 165, 255, 0.3)";
                dynamicDiv[3].style.backgroundColor="rgba(56, 165, 255, 0.3)";
                dynamicDiv[4].style.backgroundColor="rgba(56, 165, 255, 0.3)";
                dynamicDiv[5].style.backgroundColor="rgba(56, 165, 255, 0.3)";
                dynamicDiv[6].style.backgroundColor="rgba(56, 165, 255, 0.3)";
                dynamicDiv[7].style.backgroundColor="rgba(56, 165, 255, 0.3)";
                dynamicDiv[8].style.backgroundColor="rgba(56, 165, 255, 0.3)";
                dynamicDiv[9].style.backgroundColor="rgba(56, 165, 255, 0.3)";
                dynamicDiv[10].style.backgroundColor="rgba(56, 165, 255, 0.3)";
                dynamicDiv[11].style.backgroundColor="rgba(56, 165, 255, 0.3)";
                dynamicDiv[12].style.backgroundColor="rgba(56, 165, 255, 0.3)";
                dynamicDiv[13].style.backgroundColor="rgba(56, 165, 255, 0.3)";
                dynamicDiv[14].style.backgroundColor="rgba(56, 165, 255, 0.3)";
                dynamicDiv[15].style.backgroundColor="rgba(56, 165, 255, 0.3)";
                dynamicDiv[16].style.backgroundColor="rgba(56, 165, 255, 0.3)";
                dynamicDiv[17].style.backgroundColor="rgba(56, 165, 255, 0.3)";
            }, 1000);
        });
}

addLoadEvent(formSwitch);