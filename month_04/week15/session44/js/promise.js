console.log("Promise JS");

const firstPromise = new Promise((resolved, rejected) => {
  const isTrue = true;
  if (isTrue) {
    return resolved("Success");
  } else {
    return rejected("Error");
  }
});

console.log(firstPromise);

console.log(new Promise((rej, res) => {}));

firstPromise
  .then((result) => {
    console.log(result);
    return 'B';
  })
  .then((result)=>{
    console.log(result);
    return 'C';
  })
  .then((result)=>{
    console.log(result);
    return 'D';
  })
  .catch((error) => {
    console.log(error);
  });


//   Шинээр exercisePromise үүсгээд түүнийгээ
// setTimeout ашиглан 
// A => 1 sec
// B => 2 secs
// C => 3 secs
// D => 4 secs дараагаар хэвлэдэг болгоно уу

const exercisePromise = new Promise((resolve, rejected)=>{
    setTimeout(() => {
        resolve('Ex01-A');
    }, 1000)
});

exercisePromise
    .then((result) => {
        console.log(result);
        return 'Ex01-B';
    })
    .then((result) => {
        setTimeout(()=>{
           console.log(result);
           return 'Ex01-C';
        }, 2000);
    }).then((result) => {
        console.log(result);
    })