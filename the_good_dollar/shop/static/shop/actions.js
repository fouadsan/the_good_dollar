// Filter Data
function filterData() {
    let filtersData = [];

    const filterEls = document.querySelectorAll('.form-check-input');

    filterEls.forEach(filterEl => {
        filterEl.addEventListener('change', () => {
            hideElement(productsContainer);
            showElement(mainSpinnerBox);
            // allData = [],
            setTimeout(() => {
                productsContainer.innerHTML = "";
                filterEl.classList.contains('checkmarked') ? filterEl.nextElementSibling.classList.toggle('not-visible') : null;
                if (filterEl.checked) {
                    !filtersData.includes(filterEl.id) ? filtersData.push(filterEl.id) : null;
                } else {
                    removeArr(filtersData, filterEl.id);
                }
                filtersData.length ? getData(filtersData) : getData();
            }, 500);
        })
    });

}

// Add Product to Wishlist or Cart
function addToWishOrCart(btnEl, class_name) {
    let cardEl = btnEl.parentElement;
    while (!cardEl.classList.contains('card'))
        cardEl = cardEl.parentElement;

    cardEl.classList.toggle(class_name);
}

//Add Product to Wishlist
function addToFav() {

    let favBtns = document.querySelectorAll('.card__wishlist');

    favBtns.forEach(favBtn => {
        favBtn.addEventListener('click', () => {
            addToWishOrCart(favBtn, "add__fav");
        });

    });

};

//Add Product to Cart
function addToCart() {

    let cartBtns = document.querySelectorAll('.card__cart');

    cartBtns.forEach(cartBtn => {
        cartBtn.addEventListener('click', () => {
            addToWishOrCart(cartBtn, "add__cart");
        });

    });

};