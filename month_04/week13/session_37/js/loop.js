// constant variable
let PI = 3.14;
console.log(PI);

PI = 3.45;
console.log(PI);

// constant variable - ES6

const SPEED_OF_LIGHT = 299_792_458;
console.log(SPEED_OF_LIGHT);

// SPEED_OF_LIGHT = 300_000_000;
// console.log(SPEED_OF_LIGHT); 

// const a; forbidden болохгүй

const COLORS = ['yellow', 'red', 'green', 'purple', 'black'];

// Loop
for (let i = 0; i < 6; i++){
    console.log(`Color at index: ${i} = ${COLORS[i]}`);
}

// show colored span's
for(let i = 0; i < COLORS.length; i++){
    document.writeln(`
        <div style="background: ${COLORS[i]};
            height: 20px; width: 30px;
        "></div>`);
}

// Exercises
// 3 ширхэг зурагны линктэй array үүсгээд түүнийгээ
// HTML дээрээ доош нь цувуулж харуулна уу.
const imgs = ['', 'pic/im01.png', '']

for(let i = 0; i < imgs.length; i++){
    document.writeln(`<img src="${imgs[i]}"/>`);
}