let paragraphs = document.getElementById('paragraphs');

// console дээр эхний мөрийг хэвлэе
console.log(`the first element of paraphs is: ${paragraphs.firstElementChild.innerHTML}`);

// console дээр сүүлчийн мөрийг хэвлэх
console.log(`the last element of paragraphs is: ${paragraphs.lastElementChild.innerHTML}`);

// console дээр paragraph-ийн эцгийг нь хэвлэх
console.log(`the parent of paragraphs element is: ${paragraphs.parentElement.id}`);

// console дээр бүх paragraph-уудын текстийг хэвлэе
// without getElementsByTagName 

let childParagraphs = paragraphs.children;
console.log(childParagraphs);
// for loop ашиглаад бүх параграфуудыг доош нь дугаарлаж консоль дээр хэвлэнэ үү

for (let i = 0; i < childParagraphs.length; i++){
    console.log(`${i+1}: ${childParagraphs[i].innerHTML}`);
}