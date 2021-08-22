let cardEls;
let visible = 3;
let is_listview = false;

let allData = [];
let size = 0;
let is_ordered = false;

const listViewClassName = 'product__listview';
const productsContainer = document.querySelector('.product_cards');
const mainSpinnerBox = document.getElementById('main-spinner-box');

const filterSpinnerBox = document.getElementById('filter-spinner-box');
const filtersContainer = document.getElementById('accordionPanelsStayOpenExample');



// Load Filters
function loadFilters() {
    loadHideElements(filterSpinnerBox, filtersContainer);
}

// Get Data
function getData(fData) {
    let productsUrl = `products/data/${visible}`;
    $.ajax({
        type: 'GET',
        url: productsUrl,
        data: fData ? {
            'filters-data': JSON.stringify(fData),
        } : null,
        success: function (response) {
            const data = response.data
            size = response.size
    
                hideElement(mainSpinnerBox)
                if (data.length) {
                    addDataToDom(data, size, visible);
                } else {
                    displayMsg(productsContainer, "No Product Found...");
                }

        }
    })

}

function addDataToDom(data, size, visible) {
    const productCountEl = document.getElementById('product-count-el');

    let cardSize;
    let listView;
    if (is_listview) {
        cardSize = 'col-lg-12';
        listView = listViewClassName;
    } else {
        cardSize = 'col-lg-4';
        listView = '';
    }

    productsContainer.classList.contains('not-visible') ? showElement(productsContainer) : null;

    data.forEach(el => {
        productsContainer.innerHTML += `
                <div class="card ${cardSize} col-md-12 col-sm-6 col-12">
                <div class="wrapper ${listView}">
                    <div class="product__header">
                        <div class="color__category animated-bg" id="category-color-${el.id}"></div>
                        <div class="img__product animated-bg" id="product-img-${el.id}"></div>
                    </div>
                    <div class="info__product">
                        <div class="product__header__text">
                            <p class="product__name animated-bg animated-bg-text" id="product-name-${el.id}">
                                &nbsp;
                            </p>
                            <p class="product__description animated-bg animated-bg-text" id="product-desc-${el.id}">
                                &nbsp;
                                <span class="animated-bg animated-bg-text">&nbsp;</span>
                                <span class="animated-bg animated-bg-text">&nbsp;</span>
                                <span class="animated-bg animated-bg-text">&nbsp;</span>
                            </p>
                        </div>
                        <div class="actions">
                            <div class="price__group">
                                <p class="product__price price__offer animated-bg animated-bg-text"
                                    id="product-old-price-${el.id}">&nbsp;</p>
                                <p class="product__price price__current animated-bg animated-bg-text"
                                    id="product-current-price-${el.id}">&nbsp;</p>
                            </div>
                            <div class="not-visible" id="action-el-${el.id}">
                                <div class="card__icon action card__wishlist">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
                                        <path
                                            d="M47 5c-6.5 0-12.9 4.2-15 10-2.1-5.8-8.5-10-15-10A15 15 0 0 0 2 20c0 13 11 26 30 39 19-13 30-26 30-39A15 15 0 0 0 47 5z">
                                        </path>
                                    </svg>
                                </div>
                                <div class="card__icon action card__cart">
                                    <svg class="in__cart" xmlns="http://www.w3.org/2000/svg"
                                        viewBox="0 0 64 64">
                                        <title>Remove from cart</title>
                                        <path d="M30 22H12M2 6h6l10 40h32l3.2-9.7"></path>
                                        <circle cx="20" cy="54" r="4"></circle>
                                        <circle cx="46" cy="54" r="4"></circle>
                                        <circle cx="46" cy="22" r="16"></circle>
                                        <path d="M53 18l-8 9-5-5"></path>
                                    </svg>
                                    <svg class="out__cart" xmlns="http://www.w3.org/2000/svg"
                                        viewBox="0 0 64 64">
                                        <title>Add to cart</title>
                                        <path d="M2 6h10l10 40h32l8-24H16"></path>
                                        <circle cx="23" cy="54" r="4"></circle>
                                        <circle cx="49" cy="54" r="4"></circle>
                                    </svg>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `
        visible <= size ? productCountEl.textContent = `Showing ${visible} of ${size} results` : productCountEl.textContent = `Showing ${size} of ${size} results`;
        cardEls = document.querySelectorAll('.product_cards .card');

        setTimeout(() => {
            let categoryColor = document.getElementById(`category-color-${el.id}`);
            let productImg = document.getElementById(`product-img-${el.id}`);
            let productName = document.getElementById(`product-name-${el.id}`);
            let productDesc = document.getElementById(`product-desc-${el.id}`);
            let oldPrice = document.getElementById(`product-old-price-${el.id}`);
            let currentPrice = document.getElementById(`product-current-price-${el.id}`);
            let actionsEl = document.getElementById(`action-el-${el.id}`);

            const animated_bgs = document.querySelectorAll('.animated-bg');
            const animated_bg_texts = document.querySelectorAll('.animated-bg-text');

            categoryColor.style.backgroundColor = el.category_color;
            productImg.classList.add('img__ready');
            productImg.style.backgroundImage = `url('${el.image}')`;
            productName.innerHTML = el.title;
            productDesc.innerHTML = el.detail;
            oldPrice.innerHTML = "$9,999";
            currentPrice.innerHTML = `$${el.price}`;
            oldPrice.style.textDecoration = "line-through";
            actionsEl.classList.remove('not-visible');

            animated_bgs.forEach((bg) => bg.classList.remove('animated-bg'));
            animated_bg_texts.forEach((bg) => bg.classList.remove('animated-bg-text'));



        }, 2500);

        !allData.includes(el) ? allData.push(el) : null;

        addToFav();
        addToCart();
    });
}

// View Sort
function typeView(viewBtn, oppositeEl, listViewClass) {
    viewBtn = document.getElementById(viewBtn);
    oppositeEl = document.getElementById(oppositeEl);

    viewBtn.addEventListener('click', () => {
        if (!viewBtn.classList.contains('active')) {
            if (!oppositeEl.lastElementChild.classList.contains('not-visible')) {
                oppositeEl.classList.remove('active');

                oppositeEl.lastElementChild.classList.toggle('not-visible');
                oppositeEl.firstElementChild.classList.toggle('not-visible');
            }
            viewBtn.firstElementChild.classList.toggle('not-visible');
            viewBtn.lastElementChild.classList.toggle('not-visible');

            viewBtn.firstElementChild.classList.contains('not-visible') ? viewBtn.classList.add('active') : viewBtn.classList.remove('active');

            listviewBtn = document.getElementById('listview-btn');

            cardEls.forEach(cardEl => {
                if (viewBtn == listviewBtn) {
                    cardEl.className = "card col-lg-12 col-md-12 col-sm-6 col-12";
                    cardEl.firstElementChild.classList.add(listViewClass);
                    is_listview = true;
                } else {
                    cardEl.className = "card col-lg-4 col-md-12 col-sm-6 col-12";
                    cardEl.firstElementChild.classList.remove(listViewClass);
                    is_listview = false;
                }

            });
        }


    })
}

//Grid View
function gridView() {
    typeView('gridview-btn', 'listview-btn', listViewClassName);
}

//List View
function listView() {
    typeView('listview-btn', 'gridview-btn', listViewClassName);
}

//Switch to Grid View for width < 992px
function hideListview() {
    const gridviewBtn = document.getElementById('gridview-btn');
    const listviewBtn = document.getElementById('listview-btn');

    function switchToGrid(e) {
        if (cardEls)
            cardEls.forEach(cardEl => {
                if (e.matches && cardEl.className == "card col-lg-12 col-md-12 col-sm-6 col-12" && cardEl.firstElementChild.classList.contains(listViewClassName)) {
                    cardEl.className = "card col-lg-4 col-md-12 col-sm-6 col-12";
                    cardEl.firstElementChild.classList.remove(listViewClassName);
                    listviewBtn.classList.remove('active');
                    gridviewBtn.firstElementChild.classList.add('not-visible');
                    gridviewBtn.lastElementChild.classList.remove('not-visible');
                    gridviewBtn.classList.add('active');

                } else {
                    gridView();
                    listView();

                }

            });

    }

    mediaQuery.addListener(switchToGrid);
    switchToGrid(mediaQuery);
}

function loadMoreData() {
    window.addEventListener('scroll', () => {
        const { scrollTop, scrollHeight, clientHeight } = document.documentElement;

        if (scrollTop + clientHeight >= scrollHeight) {
            visible += 3
            if (visible <= size) {
                getData();
                if (is_ordered)
                    setTimeout(() => {
                        reorderByPrice();
                    }, 3000);
            } else {

                if (productsContainer.lastElementChild && !productsContainer.lastElementChild.classList.contains('no__data')) {
                    const noDataMsgEl = document.createElement('div');
                    const noDataMsg = document.createElement('span');

                    noDataMsgEl.classList.add('no__data');
                    noDataMsg.textContent = "No More Data To Show...";
                    noDataMsgEl.appendChild(noDataMsg);

                    productsContainer.appendChild(noDataMsgEl);
                }
            }
        }
    })
}

// Reorder data by price
function reorderByPrice() {
    // Price Comparison
    function comparePrice(a, b) {
        if (a.price < b.price) {
            return -1;
        }
        if (a.price > b.price) {
            return 1;
        }
        return 0;
    }

    allData.sort(comparePrice);
    productsContainer.innerHTML = "";
    addDataToDom(allData, size, visible);
}

// Sort by price
function SwitchSortBy() {
    if (allData.length) {
        const sortEl = document.getElementById('sort-el');
        sortEl.addEventListener('change', (event) => {
            const result = event.target.value;
            if (result == 1) {
                reorderByPrice();
                is_ordered = true
            } else {
                productsContainer.innerHTML = "";
                visible = 3;
                allData = [];
                getData();
                is_ordered = false;
            }

        })
    }
}

function startDOM() {
    setTimeout(() => {
        loadFilters(filterSpinnerBox, filtersContainer);
        priceRange();
        hideListview();
        loadMoreData();
        SwitchSortBy();
        filterData();
    }, 2500);
}

getData();
startDOM();


