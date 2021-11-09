const  bannerTextEl = document.getElementById("banner-text-el");

const imgs = document.getElementById('imgs')

const leftFeatProdBtn = document.getElementById('prev-feat-btn');
const rightFeatProdBtn = document.getElementById('next-feat-btn');

const leftBrandBtn = document.getElementById('prev-brand-btn');
const rightBrandBtn = document.getElementById('next-brand-btn');

const imgEls = document.querySelectorAll('#imgs img');

const brandEls = document.querySelectorAll('.brand__img');

const brandWrapper = document.querySelector('.brand__wrapper');

let idx1 = 0;
let idx2 = 0;
let idx3 = 0;


let interval1 = setInterval(runImgCarousel, 5000);

function runImgCarousel() {
    idx1++;
    changeImage();
}


function changeImage() {
    if(idx1 > imgEls.length - 1) {
        idx1 = 0
    } else if(idx1 < 0) {
        idx1 = imgEls.length - 1
    }

    translateX(imgs, idx1, imgs.clientWidth);
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

function manualCarousel(btn1, btn2, func) {
    btn1.addEventListener('click', () => {
        func("add");
    })
    btn2.addEventListener('click', () => {
        func("sub");
    })
}

function moveProduct(op) {
    op == "add" ? idx2++ : idx2--;
    changeProduct();
}

function changeBrand() {
    if(idx3 > brandEls.length - 1) {
        idx3 = 0
    } else if(idx3 < 0) {
        idx3 = brandEls.length - 1
    }

    translateX(brandWrapper, idx3, brandEls[0].clientWidth);
}


function moveBrand(op) {
    op == "add" ? idx3++ : idx3--;
    changeBrand();
}


function fadeIn(bannerTextEl, time) {
  bannerTextEl.style.opacity = 0;

  var last = +new Date();
  var tick = function() {
    bannerTextEl.style.opacity = +bannerTextEl.style.opacity + (new Date() - last) / time;
    last = +new Date();

    if (+bannerTextEl.style.opacity < 1) {
      (window.requestAnimationFrame && requestAnimationFrame(tick)) || setTimeout(tick, 16);
    }
  };

  tick();
}

fadeIn(bannerTextEl, 3000);


manualCarousel(rightFeatProdBtn, leftFeatProdBtn, moveProduct);
manualCarousel(rightBrandBtn, leftBrandBtn, moveBrand);

