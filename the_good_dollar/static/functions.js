const date = new Date().getFullYear();
const copyrightEl = document.getElementById('copyright-el');
function getCopyDate() {
    copyrightEl.innerHTML = `
        <p>
            Copyright &copy;${date} All rights reserved | Developped by <a href="https://fouadben.herokuapp.com" target="_blank">Fouad B.</a>
        </p>
    `
}

const rootUrl = window.location.origin
const currentUrl = window.location.href;

const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

const csrf = document.getElementsByName('csrfmiddlewaretoken');

// Switch element visiblity
function hideElement(elem) {
    elem.classList.add('not-visible');
}
function showElement(elem) {
    elem.classList.remove('not-visible');
}

// Display System Msg
function displayMsg(container, msg) {
    const msgRow = document.createElement('div');
    const noProductMsgEl = document.createElement('p');
    noProductMsgEl.textContent = `${msg}`;
    msgRow.classList.add('no__data');
    msgRow.appendChild(noProductMsgEl);
    container.appendChild(msgRow);
}

// Remove from array
function removeArr(arr) {
    var what, a = arguments, L = a.length, ax;
    while (L > 1 && arr.length) {
        what = a[--L];
        while ((ax = arr.indexOf(what)) !== -1) {
            arr.splice(ax, 1);
        }
    }
    return arr;
}

// Load and Hide Element 
function loadHideElements(element1, element2) {
    hideElement(element1);
    showElement(element2);
}

const searchForm = document.getElementById('search-form');
const searchInput = document.getElementById('search-input');
const resultsBox = document.getElementById('results-box');

const select = document.getElementById('category-select');
let category;

select.addEventListener('change', () => {
    category = select.options[select.selectedIndex].value;
    if (category == "All Categories") {
        category = null;
    } else {
        category = parseInt(category);
        console.log(category);
    }
})

// Poppup Alert Messages
function handleAlerts(position, title, msg, type, boolConfirmBtn, timer) {
    Swal.fire({
        position: position,
        title: title,
        text: msg,
        icon: type,
        showConfirmButton: boolConfirmBtn,
        timer: timer,
        confirmButtonText: 'Ok'
    });
    // alertBox.innerHTML = `
    //     <div class="alert alert-${type}" role="alert">
    //         ${msg}
    //     </div>
    // `
}

const searchUrl = `${rootUrl}\/shop\/search`;

const sendSearchData = (product) => {
    $.ajax({
        type: 'POST',
        url: searchUrl,
        data: {
            'csrfmiddlewaretoken': csrf[0].value,
            'product': product,
            'category_id': isNaN(category) ? null : category, 
        },
        success: (response) => {
            const resp = response.resp
        
            if (Array.isArray(resp)) {
                resultsBox.innerHTML = "";

                resp.forEach(el => {
                    resultsBox.innerHTML += `
                        <a href="${rootUrl}\/shop\/${el.slug}/${el.id}">
                            <div class="row">                       
                                <div class="col-lg-3 col-md-3 col-sm-6 col-6 mt-2 mb-2">
                                    <img src="${el.image}" class="product__img">
                                </div>
                                <div class="col-lg-9 col-md-9 col-sm-6 col-6 mt-4 mb-2">
                                    <h6>${el.title}</h6>
                                </div>
                            </div>
                        </a>
                    `
                });
            } else {
                if (searchInput.value.length > 0) {
                    resultsBox.innerHTML = `<b>${resp}</b>`;
                } else {
                    resultsBox.classList.add('not-visible');
                }
            }
        },
        error: (error) => {
            console.log(error);
        }
    })
}

searchInput.addEventListener('input', e => {
    if (resultsBox.classList.contains('not-visible')) {
        resultsBox.classList.remove('not-visible');
    }

    sendSearchData(e.target.value);
})

getCopyDate()