// aba --> palindrom -- > aba  -- True
// hello -> not palindrom --> olleh -- False

function findPalindrom(input) {
  for (let i = 0; i < input.length; i++) {
    console.log(input[i]);
  }

  console.log("aba" === input);

  //
}

console.log(`Is it palindrom : ${findPalindrom("aba")}`); // true

function findPrimeNumber(number) {
  if (number <= 1) {
    return false;
  }
  for (let i = 2; i < number; i++) {
    if (number % i === 0) {
      return false;
    }
  }
  return true;
}

console.log(`the number is prime ${findPrimeNumber(7)}`); // true
console.log(`the number is prime ${findPrimeNumber(16)}`); // false
