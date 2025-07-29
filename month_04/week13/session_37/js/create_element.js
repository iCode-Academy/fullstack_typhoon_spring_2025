const books = ['Tungalag Tamir', 'Dulguun Don', 'Harry Potter'];

const mainElement = document.getElementsByTagName('main');
console.log(mainElement);

// бүх номнуудын font size нь 30px
// өнгө нь цэнхэр
// border radius-тай бас бүх текстүүд нь төвдөө голдоо
// орохоор харуулна уу
for (let i = 0; i < books.length; i++){
    // new p element for showing book title
    const pElement = document.createElement('p');
    pElement.classList.add('books');
    
    //
    pElement.textContent = books[i];
    mainElement[0].appendChild(pElement);
}