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

// Load Element 
// Load Filters
function loadHideElements(element1, element2) {
    hideElement(element1);
    showElement(element2);
}


// Poppup Alert Messages
const handleAlerts = (position, title, msg, type, boolConfirmBtn, timer) => {
    Swal.fire({
        position: position,
        title: title,
        text: msg,
        icon: type,
        showConfirmButton: boolConfirmBtn,
        timer: timer,
        confirmButtonText: 'Ok'
    })
}

const searchForm = document.getElementById('search-form');
const searchInput = document.getElementById('search-input');
const resultsBox = document.getElementById('results-box');

const searchUrl = `${rootUrl}\/shop\/search`;

const sendSearchData = (product) => {
    $.ajax({
        type: 'POST',
        url: searchUrl,
        data: {
            'csrfmiddlewaretoken': csrf[0].value,
            'product': product,
        },
        success: (response) => {
            console.log(response);
        },
        error: (error) => {
            console.log(error);
        }
    })
}

searchInput.addEventListener('keyup', e => {
    if (resultsBox.classList.contains('not-visible')) {
        resultsBox.classList.remove('not-visible');
    }
    
    sendSearchData(e.target.value);
})

getCopyDate()