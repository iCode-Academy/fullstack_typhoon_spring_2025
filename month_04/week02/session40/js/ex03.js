console.log('cross of the task');
/**
 * crossOff гэдэг функц бичнэ үү.
 * Энэхүү функц нь тухайн item буюу таскийг дарах үед
 * text-decoration ашиглан дундуур нь зураастай болгоорой.
 * li элемент бүрийг addEventListener-ээр crossOff функцыг
 * дууддаг болгоорой.
 * Тэгээд хэрвээ тухайн таскийг хийсэн бол бас хийгээгүй болгоорой.
 * Үүнийг хийхдээ style гэдэг аттрибут байгаа эсэхийг шалгаад
 * тэгээд байгаа бол түүнийг байхгүй болгох байхгүй бол
 * байгаа болгодог логик оруулж ирж болно.
 */

function crossOff(){
    if (this.style.textDecoration){
        this.style = '';
    } else {
        this.style.textDecoration = 'line-through';
    }
}

const liElements = document.getElementsByTagName('li');
for (let i = 0; i < liElements.length; i++){
    liElements[i].addEventListener('click', crossOff);
}