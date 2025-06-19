/**
 * Зөвхөн JS ашиглаад дараах зураг шиг
 * хийх ажлаа оруулна уу
 * 
 * Нэмээд шинээр нэг мөр өөр долоо хоногийг 
 * JS-ээр оруулж ирнэ үү. tr гэсэн үг. 
 * Түүндээ элементүүд үүсгээд оруулаарай. 
 */
let weekOne = document.getElementById('tasks');
let daysOne = weekOne.children;

daysOne[0].innerHTML = 'clean my room';
daysOne[1].innerHTML = 'clean my room';
daysOne[2].innerHTML = 'clean my room';
daysOne[3].innerHTML = 'clean my room';
daysOne[4].innerHTML = 'clean my room';

let weekTwo = document.createElement('tr');
for (let i = 0; i < 5; i++){
    let baseTwo = document.createElement('td');
    baseTwo.innerHTML = 'Sleep';
    weekTwo.appendChild(baseTwo);
}

document.getElementById('chores').appendChild(weekTwo);