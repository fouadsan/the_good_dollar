const imgs = document.getElementById('imgs');
const leftBtn = document.getElementById('left');
const rightBtn = document.getElementById('right');
const img = document.querySelectorAll('#imgs img');

let idx = 0;

let interval = setInterval(run, 2000);


function run() {
    idx++;
    changeImage(cardEls, productsContainer);
}

function changeImage(elements, wrapper) {
    if (idx > elements.length - 1) {
        idx = 0
    } else if (idx < 0) {
        idx = elements.length - 1
    }

    // wrapper.style.transform = `translateX(${-idx * 500}px)`
    wrapper.style.left = -idx * elements[0].clientWidth + "px";
}

function resetInterval() {
    clearInterval(interval);
    interval = setInterval(run, 2000);
}

rightBtn.addEventListener('click', () => {
    idx++
    changeImage();
    resetInterval();
})

leftBtn.addEventListener('click', () => {
    idx--
    changeImage();
    resetInterval();
})

function translateX(element) {
    //translate items
    element.style.left = -element.clientWidth + "px";
}


// setTimeout(() => {
//     productScroll();
// }, 3500);

// let slide = document.getElementById("slide");

// function productScroll() {
//   let slider = document.getElementById("slider");
//   let next = document.getElementsByClassName("pro-next");
//   let prev = document.getElementsByClassName("pro-prev");
  
//   let item = document.getElementById("slide");

//   for (let i = 0; i < next.length; i++) {
//     //refer elements by class name

//     let position = 0; //slider postion

//     prev[i].addEventListener("click", function() {
//       //click previos button
//       if (position > 0) {
//         //avoid slide left beyond the first item
//         position -= 1;
//         translateX(position); //translate items
//       }
//     });

//     next[i].addEventListener("click", function() {
//       if (position >= 0 && position < hiddenItems()) {
//         //avoid slide right beyond the last item
//         position += 1;
//         translateX(position); //translate items
//       }
//     });
//   }

//   function hiddenItems() {
//     //get hidden items
//     let items = getCount(item, false);
//     let visibleItems = slider.offsetWidth / productsContainer.clientWidth;
//     return items - Math.ceil(visibleItems);
//   }
// }

// function translateX(position) {
//   //translate items
//   slide.style.left = position * -productsContainer.clientWidth + "px";
// }

// function getCount(parent, getChildrensChildren) {
//   //count no of items
//   let relevantChildren = 0;
//   let children = parent.childNodes.length;
//   for (let i = 0; i < children; i++) {
//     if (parent.childNodes[i].nodeType != 3) {
//       if (getChildrensChildren)
//         relevantChildren += getCount(parent.childNodes[i], true);
//       relevantChildren++;
//     }
//   }
//   return relevantChildren;
// }


function carousel() {
    
}

