import React from "react";


// ex01
// Fetch List гэдэг функцэн component үүсгээд
// түүнийгээ posts api-гаас эхний 10 постыг
// аваад харуулдаг болгоно уу

// ex02
// RefreshRandomPost гэдэг функцэн component
// үүсгээд түүнийгээ random post-ийг id-гаар
// https://jsonplaceholder.typicode.com/posts/1
// авдаг болгоорой.
// Math.floor(Math.random()...
// гэхдээ энэхүү компонент нь 
// Fetch new Random Post гэдэг button 
// дарах үед доор нь харуулж байгаа постыг
// нь өөрчилж харуулна. (1 - 100)
// Жишээ нь:
// (id: 92) ratione ex tenetur perferendis 
// гэх мэтээр title болон body доторх агуулгыг нь харуулдаг байна.

// ex03
// FetchBasedOnUserInput гэдэг component үүсгээд түүнийгээ 
// хэрэглэгч input дээр тухайн постны id-г (1-100) хүртэлх тоог оруулахад 500миллисекундын дараа 
// тухайн id-гаар нь олсон постыг харуулна.