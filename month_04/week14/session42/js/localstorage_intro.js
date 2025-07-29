// visits
let numberOfVisits = localStorage.getItem('visits');

if (numberOfVisits == null){
    numberOfVisits = 0;
} else {
    numberOfVisits = parseInt(numberOfVisits, 10);
}

console.log(numberOfVisits);

// add by one visit numbers
numberOfVisits++;

localStorage.setItem('visits', numberOfVisits);


// student
let student = localStorage.getItem('student');
if (student == null){
    student = 'Khangai';
} else {
    student = student;
}
localStorage.setItem('student', student);
// show student name to the DOM on the HTML

// animal - dog

// hobbies - football, basketball

// activities - swimming, laundry