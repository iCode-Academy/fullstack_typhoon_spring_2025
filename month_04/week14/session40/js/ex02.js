/**
 * changeColor гэдэг функц бичээд хэрэглэгчээс
 * өнгийг нь авдаг болгоорой.
 * тэгээд тухайн өгөгдсөн div-ний өнгийг нь хэрэглэгчийн 
 * өгсөн өнгөөр нь сольдог болгоорой.
 * getElementById гэдэг selector хэрэглэхгүй.
 * this гэдэг түлхүүр үг ашиглан аль div нь вэ гэдгийг
 * олоорой.
 */


// function changeColor (element){
//     let color = prompt('Give me color!');
//     element.target.style.background = color;
// }

function changeColor(){
    let color = prompt('Give me color!');
    this.style.background = color;
}

const divElements = document.getElementsByTagName('div');

// function callback
for (let i = 0; i < divElements.length; i++){
    divElements[i].addEventListener('click', changeColor);
}
