// Problem 
// Хүн гэдэг зүйлийг JS дээр илэрхийлэх гээд үзье

let firstName = 'Khangai';
let lastName = 'Uvgunkhuu';
let age = 43;

// let firstName = 'Buyanaa';
// let lastName = 'Boldbaatar';
// let age = 21;

// Solution - JS object

let khangai = {
    firstName: "Khangaikhuu",
    lastName: "Uvgunkhuu",
    age: 43,
    'favorite-animal': 'Dog'
}

let buyanaa = {
    firstName: "Buyandelger",
    lastName: "Boldbaatar",
    age: 21
}

console.log(khangai);
console.log(buyanaa);

// object with arrays
let dog = {
    name: "Banhar",
    age: 3,
    activities: ['Bell', 'Eat', 'Sleep', 'Play a Ball'],
    race: {
        origin: "Tibet",
        name: "Tibetian Dog"
    }
}

console.log(dog);

// accessing object property
// dot notation
console.log(buyanaa.age);
console.log(buyanaa.firstName);
console.log(buyanaa.lastName);

// bracket notation
console.log(khangai['firstName']);
console.log(khangai['age']);
console.log(khangai['lastName']);
// console.log(khangai.favorite-animal); <- wrong typing
console.log(khangai["favorite-animal"]);

// changing object property
khangai.age = 44;
buyanaa.age = 22;
dog['age'] = 4;

console.log(khangai);
console.log(buyanaa);
console.log(dog);

// adding object property
buyanaa['favorite-animal'] = 'Cat';
console.log(buyanaa);

// 
console.log(dog.race.origin);

// dog eat print
console.log(dog.activities[1]);

// for loop ашиглаад бүх activities хэвлэх
for (let i = 0; i < dog.activities.length; i++){
    console.log(dog.activities[i]);
}

