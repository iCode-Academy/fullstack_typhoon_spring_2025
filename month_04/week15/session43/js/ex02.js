const changeButton = document.getElementById('user-info');

changeButton.addEventListener('click', function(){
    let existingUserName = prompt('Give me your name');

    // хэрэглэгчээс хэрвээ тухайн нэртэй json 
    // object байна уу гэдгийг асууна. 
    // тэгээд хэрвээ тухайн object байвал түүнийг
    // html DOM дээр харуулна.

    // хэрвээ хэрэглэгч байхгүй байвал тухайн 
    // хэрэглэгчийн нэрийг асуугаад 
    // өндрийг асуугаад
    // тэгээд дуртай амьтныг нь асуугаад
    // дараа нь түүнийгээ 
    // let buyanaa = {
    ///. name: "Buyanaa"
    //   height: "140",
    // favorite-animal: "Cat"
    // }
    // гэж LocalStorage дээр хадгална уу

    if(localStorage.getItem(existingUserName)){
        let user = JSON.parse(localStorage.getItem(existingUserName));
        const welcome = document.getElementById('welcome');
        welcome.innerHTML += "<h2>Welcome back " + user.name + "</h2>";
        welcome.innerHTML += "<p> Your height is: " + user.height + "</p>";
        welcome.innerHTML += "<p>Your favorite Animal is: " + user['favorite-animal'] + "</p>";
    } else {
        let nameOfUser = prompt('What is your name?');
        let heightOfUser = prompt('What is your height?');
        let userFavoriteAnimal = prompt('What is your favourite animal?');

        let person = {
            name: nameOfUser,
            height: heightOfUser,
            'favorite-animal': userFavoriteAnimal
        }

        localStorage.setItem(existingUserName, JSON.stringify(person));
    }
})