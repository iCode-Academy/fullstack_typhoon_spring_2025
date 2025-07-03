console.log('callback functions');

function funcA(){
    setTimeout(() => {
        console.log('A')
    }, 1000);
}

function funcB(){
    setTimeout(() => {
        console.log('B')
    }, 2000);
}

function funcC(){
    setTimeout(() => {
        console.log('C')
    }, 3000)
}

funcB(); // B => A
funcA(); // A => B
funcC(); // C => C

// function dependent on function

function funcA1(){
    setTimeout(() => {
        console.log('A1');
    }, 1000)
}
// callback function function-д function-ыг параметраар өгсөн
// тэр аргыг хэлдэг
function funcA2(funA1){
    setTimeout(() => {
        funA1();
        console.log('A2');
    }, 2000)
}

// funcA3 гэдэг функц тодорхойлоод түүндээ funA2 гэдэг функц
// callback-аар өгөөд түүнийгээ A3 гэж хэвлэдэг болгоорой. 
// гэхдээ түүнийгээ бас funA2 гэдэг параметраар өгсөн
// callback функцуу дууддаг болгоорой.

function funcA3(funA2){
    setTimeout(()=>{
        funA2(funcA1);
        console.log('A3');
    }, 3000)
}

funcA3(funcA2);


const button = document.getElementById('click-me');

button.addEventListener('click', buttonClicked);


function buttonClicked(){
    console.log('button is clicked');
}