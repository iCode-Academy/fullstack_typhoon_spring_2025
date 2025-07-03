console.log('FETCH API');

// Application Programming Interface
// https://jsonplaceholder.typicode.com/users

const USER_API = 'https://jsonplaceholder.typicode.com/users';
const usersPromise = fetch(USER_API);
console.log(usersPromise);
const postData = [];

usersPromise
    .then((response) => {
        console.log(response);
        const data = response.json(); // Promise
        console.log(data);
        return data;
    })
    .then((data) => {
        for(let i = 0; i < data.length; i++){
            console.log(data[i].name)
               postData.push(data[i]);
            // document.writeln(`<li>${data[i].name}</li>`);
        }
        console.log(postData);
    })



function filter(input){
    // console.log(input.value);
    // console.log(postData);
    const testArray = ['hi', 'hello', 'hallo'];

    const result = testArray.filter((t) => t.includes(input.value));
    console.log(result);
}