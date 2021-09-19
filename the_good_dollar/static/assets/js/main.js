const mediaQuery = window.matchMedia('(max-width: 991px)');

const heroCatAllEl = document.querySelector('.hero__categories__all');
const heroCatAllToggler = document.querySelector('.hero__categories__all i');

// Proloder 
function setPreloader() {
    window.addEventListener('load', () => {
        $(".loader").fadeOut();
        $("#preloder").fadeOut("slow");
    });
}

// Hamburger Menu
function getHamburger(e) {
    const hamburgerBtn = document.querySelector('.hamburger__open');
    const hamburgerWrapper = document.querySelector('.hamburger__menu__wrapper');
    const hamburgerOverlay = document.querySelector('.hamburger__menu__overlay');

    hamburgerBtn.addEventListener('click', () => {
        hamburgerWrapper.classList.add('show__hamburger__menu__wrapper');
        hamburgerOverlay.classList.add('active');
        document.body.classList.add('over_hid');
    })

    hamburgerOverlay.addEventListener('click', () => {
        hamburgerWrapper.classList.remove('show__hamburger__menu__wrapper');
        hamburgerOverlay.classList.remove('active');
        document.body.classList.remove('over_hid');
    })
}


   // Back to top
   function backToTop() {
        let backtotop = document.querySelector('.back-to-top');
        console.log("begin")
        if (backtotop) {
            function toggleBacktotop() {
            if (window.scrollY > 100) {
                backtotop.classList.add('active');
            } else {
                backtotop.classList.remove('active');
            }
            }
            window.addEventListener('load', toggleBacktotop);
            document.addEventListener('scroll', toggleBacktotop);
            backtotop.addEventListener('click', ToTop);
        }
   }

    function ToTop() {
        let body = document.body,
        html = document.documentElement;

        let height = Math.max( body.scrollHeight, body.offsetHeight, 
                        html.clientHeight, html.scrollHeight, html.offsetHeight );

        if (window.pageYOffset > 0) {
        window.scrollBy(0, -height);
        setTimeout(ToTop, 5000);
        }
    }


// Tooltip
// function toolTip() {
//     let ancherEls = document.querySelectorAll('a');
//     let buttonEls = document.querySelectorAll('button');

//     ancherEls.forEach(ancherEl => {
//         new bootstrap.Tooltip(ancherEl, { boundary: document.body, placement: 'bottom', delay: { "show": 500, "hide": 100 } })
//     });


//     buttonEls.forEach(buttonEl => {
//         new bootstrap.Tooltip(buttonEl, { boundary: document.body, placement: 'bottom', delay: { "show": 500, "hide": 100 } })
//     });
// }

// Nice Select
function applyNiceSelect() {

    var niceSelect = $('.nice__select');
    if (niceSelect.length) {
        niceSelect.niceSelect();

    }

}

// Nice Secroll  
function applyNiceScroll() {
    $(".nice-scroll").niceScroll({
        cursorcolor: "#0d0d0d",
        cursorwidth: "5px",
        background: "#e5e5e5",
        cursorborder: "",
        autohidemode: true,
        horizrailenabled: false
    });
}

// 5. Departements dropdown toggler
// function toggleDepartBtn() {
//     heroCatAllEl.addEventListener('click', () => {
//         heroCatAllToggler.classList.contains('fa-bars') ? heroCatAllToggler.classList.replace('fa-bars', 'fa-times') : heroCatAllToggler.classList.replace('fa-times', 'fa-bars');

//         $('.hero__categories ul').slideToggle(400);

//     })
// }

// Departements dropdown 
// function displayDepartementList() {
//     const departList = document.querySelector('.hero__categories ul');
//     if (window.location.href === window.location.origin) {
//         heroCatAllToggler.classList.remove('fa-bars');
//         heroCatAllToggler.classList.add('fa-times');
//         departList.style.display = "block";

//     } else {
//         departList.style.display = "none";
//     }

// }

function start() {
    setPreloader();
    backToTop();
    mediaQuery.addListener(getHamburger);
    getHamburger(mediaQuery);
    // toolTip();
    applyNiceSelect();
    applyNiceScroll();
    // toggleDepartBtn();
    // displayDepartementList();
}


start();


