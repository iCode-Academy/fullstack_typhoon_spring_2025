document.getElementById('change-background').addEventListener('click', function(){
    let color = prompt(`What color would you like to change 
        your background color the next time you visit the site?");`);

    if(localStorage.backgroundList) {
        let colorList = JSON.parse(localStorage.backgroundList);
        colorList.push(color);
        // save colorList to the local storage backgroundList key

    } else {
        let list = [color];
        // save list to the local storage backgroundList key
    }

    // хэрвээ backgroundList localStorage-д байвал #last-three гэдэг элементэд тухайн backgroundList
    // дээрх сүүлчийн 3-н өнгөний утгуудыг DOM-оор хэвлэж харуулна уу.
    // тэгээд хамгийн сүүлчийн өнгөөр тухайн HTML-ийн ар талын өнгийг нь будаж харуулаарай.
    
})