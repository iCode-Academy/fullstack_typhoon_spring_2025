/** 
 * h4 tag үүсгээд түүнийгээ энэ оюутнуудын нэрний
 * өмнө талд оруулахдаа Typhoon Class гэдэг
 * тексттэй болгож оруулна уу.
 * Гэхдээ энэхүү текстийг h2 гэдэг tag-ийн 
 * доод талд нь оруулж харуулна уу.
 * үүндээ өмнө талд нь оруулах гэдэг insertBefore
 * гэдэг DOM элемент функцийг ашиглана уу
 * Тэгээд өөрийнхөө нэрийг хамгийн сүүлд нь 
 * оруулж өгөөрэй.
 */

let h4Element = document.createElement('h4');
h4Element.innerHTML = 'Typhoon Class';
const classList = document.getElementById('class-list');

let myNameElement = document.createElement('li');
myNameElement.innerHTML = 'Khangaikhuu';

classList.lastElementChild.appendChild(myNameElement);

const classWindow = document.getElementById('class-window');

classWindow.insertBefore(h4Element, classList);
