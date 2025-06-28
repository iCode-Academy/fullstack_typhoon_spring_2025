let listOfScores = [10, 30, 455, 80];

// JSON - Javascript Object Notation
console.log('List Without JSON');

localStorage.setItem('scores', listOfScores);
console.log('Values stored in scores: ' + localStorage.scores);
console.log('Data types of local storage listOfScores: ' + typeof(localStorage.scores));
console.log('Second index of localStorage listOfScores: ' + localStorage.scores[2]);



// JSON Object - NOW using JSON
localStorage.setItem('scores', JSON.stringify(listOfScores));
console.log('With JSON: ');
console.log('Values stored in scores: ' + localStorage.scores);
console.log('Data type of stringified local storage list of scores: ' + typeof(localStorage.scores));
console.log('Data type of parsed local storage list of scores: ' + typeof(JSON.parse(localStorage.scores)));
console.log('Second index of parsed localStorage list of scores: ' + JSON.parse(localStorage.scores)[2]);

