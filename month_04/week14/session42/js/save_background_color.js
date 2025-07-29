console.log(window);
window.addEventListener('DOMContentLoaded', function(){
    let savedColor = localStorage.getItem('background-color');
    if (savedColor){
        this.document.body.style.backgroundColor = savedColor;
    }

    const changeColorButton = this.document.getElementById('change-background');
    changeColorButton.addEventListener('click', function(){
        let newColor = prompt("Enter a color name or hex code (e.g., blue, #ff0000):");

        // Exercises хэрвээ хэрэглэгч гарнаас утга өгвөл тухайн өнгийг local storage дээр хадгалаад
        // дараа нь арын өнгийг нь өнгөний өөрчилдөг болгоно уу.
        // хуудсыг refresh хийх үед сүүлийн өнгөөр арын өнгө харагдах ёстой.
        if (newColor){
            localStorage.setItem('background-color', newColor);
        }
    });
})