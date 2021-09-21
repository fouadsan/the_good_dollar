const imgs = document.getElementById('imgs')
const leftFeatProdBtn = document.getElementById('prev-feat-btn');
const rightFeatProdBtn = document.getElementById('next-feat-btn');

const img = document.querySelectorAll('#imgs img')

let idx1 = 0
let idx2 = 0


let interval1 = setInterval(runImgCarousel, 2000);

function runImgCarousel() {
    idx1++;
    changeImage();
}


function changeImage() {
    if(idx1 > img.length - 1) {
        idx1 = 0
    } else if(idx1 < 0) {
        idx1 = img.length - 1
    }

    translateX(imgs, idx1, 500);
}

function changeProduct() {
    if(idx2 > cardEls.length - 1) {
        idx2 = 0
    } else if(idx2 < 0) {
        idx2 = cardEls.length - 1
    }

    translateX(productsContainer, idx2, cardEls[0].clientWidth);
}


function translateX(wrapper, index, width) {
    wrapper.style.transform = `translateX(${-index * width}px)`;
}

function manualCarousel(btn1, btn2) {
    btn1.addEventListener('click', () => {
        moveProduct("add");
    })
    btn2.addEventListener('click', () => {
        moveProduct("sub");
    })
}

function moveProduct(op) {
    op == "add" ? idx2++ : idx2--;
    changeProduct();
}

manualCarousel(rightFeatProdBtn, leftFeatProdBtn);

