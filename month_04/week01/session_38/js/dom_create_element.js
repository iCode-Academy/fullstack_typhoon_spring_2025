console.log('we are building a new button');
let text = prompt('What would you like to say the button');

let button = document.createElement('button');
button.innerHTML = text;

// add into button-box
const buttonBox = document.getElementById('button-box');
buttonBox.appendChild(button);


// text area болон input-тэй 2 төрлийн элемент оруулаад 
// button-box дээр оруулж ирнэ үү.
// энэ элементүүд нь үндсэн текстүүдтэй байна.

const textArea = document.createElement('textarea');
textArea.placeholder = 'This is text area text';
buttonBox.appendChild(textArea);

const inputElement = document.createElement('input');
inputElement.placeholder = 'This is input text';
buttonBox.appendChild(inputElement);

