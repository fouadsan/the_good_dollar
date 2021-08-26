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