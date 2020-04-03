function cupClick(evt) {
    let poziom = Number(this.getAttribute('poziom'));
    poziom += 24;
    if(poziom <=96){
        this.style.backgroundPosition = "0 " + poziom + "%";
        this.setAttribute('poziom', poziom);
    } else {
        this.style.cursor = "not-allowed";
    }
}

let cups = document.querySelectorAll('.cup');
cups.forEach(cup => {
    cup.addEventListener('click', cupClick)
})