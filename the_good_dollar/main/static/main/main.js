const imgs = document.getElementById('imgs')
const leftBtn = document.getElementById('left')
const rightBtn = document.getElementById('right')

const img = document.querySelectorAll('#imgs img')

let idx1 = 0
let idx2 = 0

// let interval = setInterval(runImgCarousel, 2000)
let interval2 = setInterval(runProductCarousel, 2000);

function runImgCarousel() {
    idx1++
    changeImage(idx1, img, imgs, 500);
}

function runProductCarousel() {
    idx2++
    changeImage(idx2, cardEls, productsContainer, cardEls[0].clientWidth);
}

function changeImage(index, elements, wrapper, width) {
    if (index > elements.length - 1) {
        index = 0
    } else if (elements < 0) {
        index = elements.length - 1
    }
    wrapper.style.transform = `translateX(${-index * width}px)`;
    idx2 = index
    console.log("done")

}

function resetInterval() {
    clearInterval(interval);
    interval = setInterval(run, 2000);
}
