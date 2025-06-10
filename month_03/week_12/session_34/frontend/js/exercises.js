// different data type
var yourAge = 42;
var yourHeight = 1.65;
var isTrue = true;
var isFalse = false;
var undefinedVar; // undefined
var isNull = null;

console.log(yourAge);
console.log(yourHeight);
console.log(isTrue);
console.log(isFalse);
console.log(undefinedVar);
console.log(isNull);

// typeof - function
console.log(typeof(1.6));
console.log(typeof(yourAge));
console.log(typeof(yourHeight));
console.log(typeof(isTrue));
console.log(typeof(isFalse));
console.log(typeof(undefinedVar));
console.log(typeof(isNull));

// conversion of types
// number -> string 
// string -> number
// string -> boolean
// boolean -> string

// scope -> var problem 

// scope-тэй variable
let numberString = '1.6';
console.log(numberString); // 1.6
console.log(typeof numberString); // string

let parsedNumber = parseInt(numberString);
console.log(parsedNumber);
console.log(typeof parsedNumber);

// string concatenation
console.log('1.6' + '2.7');
console.log(1.6 + 2.7); // 4.300001
console.log('1.7' + 2); // 1.72
console.log(2 + '1.7'); // 21.7

// prompt-оор өөрийнхөө насыг аваад тэгээд 
// түүн дээр 1-ийг нэмээд 
// I will be next year 18 years old. гэж console дээр 
// хэвлээрэй.

var age = prompt('Give me your age');
console.log("I will be next year " + (parseInt(age)+ 1) + ' years old');

// fix the errors

console.log("Something is wrong with the code! Find the error and fix it!");
            
prompt("What is today's date?");
alert('Have a wonderful day!');

