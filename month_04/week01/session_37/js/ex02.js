/* Дасгал: Дараах шаардлагатай код бич:
1. Тоглогч 1-6 хүртэлх санамсаргүй тоо орж ирнэ
2. Тоглогч 3 оролдлого хийж болно
3. Зөв тоо таасан бол "Та яллаа!" гэж хэвлэ
4. Оролдлого дууссан бол "Та хожигдлоо" гэж хэвлэ
5. Таах тоо нь 4 байг */

const randomNumber = Math.floor(Math.random() * 6 + 1);
document.writeln(randomNumber);
let oroldlogo = 1;

while (oroldlogo <= 3) {
  let too = prompt("Too");
  if (parseInt(too) === randomNumber) {
    console.log("You won");
    break;
  }
  if (oroldlogo === 3) {
    console.log("You lost");
  }
  oroldlogo++;
}

function fibonnaci(number) {
  if (number === 0) {
    return 0;
  }
  if (number === 1) {
    return 1;
  }
  return fibonnaci(number - 1) + fibonnaci(number - 2);
}

for (let i = 0; i < 10; i++) {
  console.log(fibonnaci(i));
}

function fibonacciLoop(number) {
  let fibN1 = 0;
  let fibN2 = 1;
  let fibN;
  let counter = 2;
  if (number === 0) {
    return fibN1;
  } else if (number === 1) {
    return fibN2;
  } else {
    while (counter <= number) {
      fibN = fibN1 + fibN2;
      fibN1 = fibN2;
      fibN2 = fibN;
      counter++;
    }
    return fibN2;
  }
}
console.log("fibonacci while loop");
// fibonacciLoop(5); // 5
for (let i = 0; i < 10; i++) {
  console.log(fibonacciLoop(i));
}
