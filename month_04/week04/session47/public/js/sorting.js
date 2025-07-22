let numbers = [40, 10, 100, 20, 5];

// Ascending - Өсгөх
let ascending = numbers.slice().sort((a, b) => a - b);
console.log('Ascending : ', ascending); // [5, 10, 20, 40, 100]


// Descending - Буурах
let descending = numbers.slice().sort((a, b) => b - a);
console.log('Descending : ', descending); // [100, 40, 20, 10, 5]

let myProducts = [
  { name: 'Phone', price: 800 },
  { name: 'Laptop', price: 1200 },
  { name: 'Tablet', price: 600 }
];

// sort by price (low to high)
let byPriceAsc = myProducts.slice().sort((a, b) => a.price - b.price);
console.log('Ascending: ', byPriceAsc);

// sort by price (high to low)
let byPriceDesc = myProducts.slice().sort((a, b) => b.price - a.price);
console.log('Descending: ', byPriceDesc);

// sort by name (A to Z)
let byName = myProducts.slice().sort((a, b) => b.name.localeCompare(a.name));
console.log('Name: A-Z:', byName);