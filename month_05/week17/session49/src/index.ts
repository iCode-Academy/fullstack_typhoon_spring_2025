let message: string = "Hello, Typescript!";
console.log(message);

// basic types
// JS: string, number, boolean

let frameWork: string = "Typescript";
let version: number = 5.0;
let isAwesome: boolean = true;

// arrays types
// array of numbers
let list: number[] = [1, 2, 3];

// array of booleans
let listBoolean: boolean[] = [true, false, true];

// alternative generic syntax
let anotherList: Array<number> = [1, 2, 3];

// string typed listOfString
let listOfString: Array<string> = ["Hi", "Hello"];

// Enums - named constants

enum Color {
  Red, // 0
  Green, // 1
  Blue, // 2
}

let c: Color = Color.Green;
console.log(c);

enum Direction {
  Up = 1,
  Down, // 2
  Left, // 3
  Right, // 4
}

// Special Types
// ANY type
let notSure: any = 4;
notSure = "maybe a string instead";
notSure = false; // okay definitely a boolean
console.log(notSure);

// Unknown Type
let value: unknown = "hello";
if (typeof value === "string") {
  console.log(value.toUpperCase());
}
// void - function return type
// null and undefined
// never
let neverHappen: never;

// union types
let id: string | number; // string or number
id = 101; // ok
id = "101-A"; // ok
console.log(id);

// type aliases
type StringOrNumber = string | number;
let customerId: StringOrNumber = "C123";
customerId = 123;
console.log(customerId);

// functions

function add(x: number, y: number): number {
  return x + y;
}

console.log(add(1, 2));

// 2 number array аваад түүнийг нэгтгээд буцаадаг
// функц бичнэ үү
function mergeArray(one: number[], two: number[]): Array<number> {
  return one.concat(two);
}

// subtract гэдэг 2 тоог хасаад буцаадаг функц
// бичнэ үү.
function subtract(x: number, y: number): number {
  return x - y;
}
// void function
function logMessages(message: string): void {
    console.log(message);
}

// Interfaces
interface User {
    name: string,
    id: number,
    isAdmin?: boolean,
    readonly email: string; // readonly prevents modification after creation
}

function createUser(user: User): void {
    console.log(`Creating user: ${user.name} with email ${user.email}`);
}

const newUser: User = {
    name: "Jane Doe",
    id: 1,
    email: "jane@example.com"
}
createUser(newUser);

interface Shape {
    getArea(): number;
}

class Circle implements Shape {
    constructor(public radius: number) {}

    getArea(): number {
        return Math.PI * this.radius ** 2;
    }
}

const human = {
    firstName: 'Khangaikhuu'
}
// classes
class Animal {
    private name: string;

    constructor(theName: string){
        this.name = theName;
    }

    public move(distanceInMeters: number): void {
        console.log(`${this.name} moved ${distanceInMeters}m.`);
    }
}

let cat = new Animal("Cat");
cat.move(10);
console.log(cat);

// Generics
function identity<T>(arg: T): T {
    return arg;
}

// we can call it with different types
let output1 = identity<string>("myString");
let output2 = identity<number>(100);
console.log(output1);
console.log(output2);
