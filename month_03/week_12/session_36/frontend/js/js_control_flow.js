function welcome() {
  // нэрийг асуугаад хадгалаад
  let yourName = prompt("Give me your name?");

  // welcome id-тай элемент дээр харуулна уу
  // string concatenation
  document.getElementById("welcome").textContent =
    "Welcome " + yourName + " to the Javascript.";
}

function changeColor() {
  // 1. надаас ямар өнгөөр хуудасны өнгийг будахыг асууна
  let givenColor = prompt("Give me website background color.");
  // 2. Хэрвээ тэр өнгө нь хар өнгө байвал уучлаарай та өөр өнгө өгнө үү гээд дахиад өөр өнгө асууна
  console.log(givenColor);
  // ternary operator
  givenColor =
    givenColor === "black"
      ? prompt("Black is not allowed. Give me different color.")
      : givenColor;
  // 3. Хэрвээ хараас өөр өнгө байвал харин тухайн өнгийг хуудасны ар талын өнгөөр нь солино.
  // элементийн css буюу стайлыг нь өөрчлөх
  document.getElementById("main-content").style.backgroundColor = givenColor; // assignment
}


//1.  html дээрээ шинээр button үүсгээд түүнийгээ ask-age гэдэг id-тэй болгоод findTeenage гэдэг функцыг дарах
// үед нь дууддаг болгоорой.
// шинээр энэ button-ы доор нь is-teenager гэдэг id-тай div элемент үүсгэнэ.

// 2. JS дээрээ ask-age гэдэг id-тэй button дарах үед нас асуугаад дараах нөхцлийг шалгаж байгаад
// таны ямар насны ангилалд орохыг харуулдаг болгоно. Үүндээ is-teenager гэдэг div элементээ ашиглаарай

// 3. ternary operator ашиглан хэрвээ өгөгдсөн нас нь 0-13 насны хооронд байвал "You are baby"
// 13-19 насны хооронд "You are teenager"
// 20 - 65 насны хооронд "You are an adult"
// 65 - 99 насны хооронд "You are a senior"
// 100-аас дээш бол "You are a dinosaur" гэж хуудсан дээр харуулдаг болгоно.

function calculateNaadam(horsePlaces, bukhColor, howManyWins) {
    let point = 0;

    // Морины байр шалгах
    switch(horsePlaces) {
        case 1:
            point += 50;
            break;
        case 2:
            point += 40;
            break;
        case 3:
            point += 30;
            break;
        case 4:
        case 5:
            point += 20;
            break;
        default:
            console.log("Буруу байр");
            return;
    }
    // Бөхийн өнгө шалгах
    if (bukhColor === "red") {
        if (howManyWins >= 4) {
            point *= 2;
        } else if (howManyWins >= 2) {
            point += 20;
        }
    } else if (howManyWins === "цэнхэр") {
        if (howManyWins >= 3) {
            point += 30;
        } else {
            point += 10;
        }
    }
    return point;
}