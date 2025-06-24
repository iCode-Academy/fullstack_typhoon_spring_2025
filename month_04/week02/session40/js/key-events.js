document.body.addEventListener('keydown', makeText);

function makeText(e){
    console.log(e);
    let div = document.getElementById('textbox');
    if (e.key != 'Shift'){
        let keyText = e.key;
        let text = div.innerHTML;
        text += keyText;
        div.innerHTML = text;
    }
}
