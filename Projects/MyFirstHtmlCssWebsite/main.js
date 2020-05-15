const time = 5000;

let active = 0;

// const slideList = [{
//         img: 'img/sad.jpg'
//     },
//     {
//         img: 'img/pole.jpg'
//     },
//     {
//         img: 'img/ziolko.jpg'
//     }
// ];

const slideList = ['img/sad.jpg', 'img/pole.jpg', 'img/ziolko.jpg'];

const header = document.getElementById("slide");

const dots = [...document.querySelectorAll('.dots span')];

const changeDot = () => {
    const activeDot = dots.findIndex(dot => dot.classList.contains('active'));

    dots[activeDot].classList.remove('active');
    dots[active].classList.add('active');
};


const changeSlide = () => {
    active++;

    if (active === slideList.length) {
        active = 0;
    }
    // header.style.backgroundImage = `url(${slideList[0].img})`;
    header.style.backgroundImage = `url(${slideList[active]})`;

    changeDot()
};

let indexInterval = setInterval(changeSlide, time);

const keyChangeSlide = (e) => {
    if (e.keyCode == 37 || e.keyCode == 39) {
        clearInterval(indexInterval);
        e.keyCode == 37 ? active-- : active++;

        if (active === slideList.length) {
            active = 0;
        } else if (active < 0) {
            active = slideList.length - 1;
        };
        header.style.backgroundImage = `url(${slideList[active]})`;
        changeDot();
        indexInterval = setInterval(changeSlide, time);
    }
}

window.addEventListener('keydown', keyChangeSlide);