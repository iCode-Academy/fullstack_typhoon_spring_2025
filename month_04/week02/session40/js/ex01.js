/**
 * Зөвхөн addEventListener ашиглаад 
 * дараах үйлдлийг хийдэг болгоно уу
 * Хэрвээ би цэнхэр дөрвөлжингүүд дээр click
 * хийвэл тухайн өнгө нь улаан өнгөтэй болно.
 */

const divElements = document.getElementsByTagName('div');
console.log(divElements);

for (let i = 0; i < divElements.length; i++){
    divElements[i].addEventListener('click', function(element){
        console.log(element.target);
        element.target.style.background = 'red';
    })
}