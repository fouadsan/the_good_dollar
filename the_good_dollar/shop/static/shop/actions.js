// Filter Data
function filterData() {
    
    let filtersData = [];

    const filterEls = document.querySelectorAll('.form-check-input');

    filterEls.forEach(filterEl => {
        filterEl.addEventListener('change', () => {
            // allData = [],
                productsContainer.innerHTML = "";
                if (filterEl.checked) {
                    if (filterEl.classList.contains('to_checkmark')) {
                        filterEl.nextElementSibling.style.display = 'inline-block';
                    } else {
                        filterEl.parentElement.style.color = 'red';
                    }
                    !filtersData.includes(filterEl.id) ? filtersData.push(filterEl.id) : null;
                } else {
                    if (filterEl.classList.contains('to_checkmark')) {
                        filterEl.nextElementSibling.style.display = 'none';
                    } else {
                        filterEl.parentElement.style.color = '#b7b7b7';
                    }
                    removeArr(filtersData, filterEl.id);
                }
                console.log(filtersData);
                getFilteredData(filtersData);
                    
        })
    });

}

// Price range
function priceRange() {
    
    let priceRange = [];

    (function ($) {
        "use strict";
        var DEBUG = false,
            PLUGIN_IDENTIFIER = "RangeSlider";

        var RangeSlider = function (element, options) {
            this.element = element;
            this.options = options || {};
            this.defaults = {
                output: {
                    prefix: '',
                    suffix: '',
                    format: function (output) {
                        return output;
                    }
                },
                change: function (event, obj) { }
            };

            this.metadata = $(this.element).data('options');
        };

        RangeSlider.prototype = {

            init: function () {
                if (DEBUG && console) console.log('RangeSlider init');
                this.config = $.extend(true, {}, this.defaults, this.options, this.metadata);

                var self = this;

                this.trackFull = $('<div class="track track--full"></div>').appendTo(self.element);
                this.trackIncluded = $('<div class="track track--included"></div>').appendTo(self.element);
                this.inputs = [];

                $('input[type="range"]', this.element).each(function (index, value) {
                    var rangeInput = this;

                    rangeInput.output = $('<output>').appendTo(self.element);

                    rangeInput.output.zindex = parseInt($(rangeInput.output).css('z-index')) || 1;

                    rangeInput.thumb = $('<div class="slider-thumb">').prependTo(self.element);

                    rangeInput.initialValue = $(this).val();

                    rangeInput.update = function () {
                        if (DEBUG && console) console.log('RangeSlider rangeInput.update');
                        var range = $(this).attr('max') - $(this).attr('min'),
                            offset = $(this).val() - $(this).attr('min'),
                            pos = offset / range * 100 + '%',
                            transPos = offset / range * -100 + '%',
                            prefix = typeof self.config.output.prefix == 'function' ? self.config.output.prefix.call(self, rangeInput) : self.config.output.prefix,
                            format = self.config.output.format($(rangeInput).val()),
                            suffix = typeof self.config.output.suffix == 'function' ? self.config.output.suffix.call(self, rangeInput) : self.config.output.suffix;


                        $(rangeInput.output).html(prefix + '' + format + '' + suffix);
                        $(rangeInput.output).css('left', pos);
                        $(rangeInput.output).css('transform', 'translate(' + transPos + ',0)');


                        $(rangeInput.thumb).css('left', pos);
                        $(rangeInput.thumb).css('transform', 'translate(' + transPos + ',0)');

                        self.adjustTrack();
                    };


                    rangeInput.sendOutputToFront = function () {
                        $(this.output).css('z-index', rangeInput.output.zindex + 1);
                    };


                    rangeInput.sendOutputToBack = function () {
                        $(this.output).css('z-index', rangeInput.output.zindex);
                    };

                    $(rangeInput.thumb).on('mousedown', function (event) {

                        self.sendAllOutputToBack();
                        rangeInput.sendOutputToFront();
                        $(this).data('tracking', true);
                        $(document).one('mouseup', function () {
                            $(rangeInput.thumb).data('tracking', false);
                            self.change(event);
                        });
                    });

                    $('body').on('mousemove', function (event) {
                        if ($(rangeInput.thumb).data('tracking')) {
                            var rangeOffset = $(rangeInput).offset(),
                                relX = event.pageX - rangeOffset.left,
                                rangeWidth = $(rangeInput).width();

                            if (relX <= rangeWidth) {
                                var val = relX / rangeWidth;
                                $(rangeInput).val(val * $(rangeInput).attr('max'));
                                rangeInput.update();
                            }
                        }
                    });

                    $(this).on('mousedown input change touchstart', function (event) {
                        if (DEBUG && console) console.log('RangeSlider rangeInput, mousedown input touchstart');
                        self.sendAllOutputToBack();
                        rangeInput.sendOutputToFront();
                        rangeInput.update();
                    });
                    $(this).on('mouseup touchend', function (event) {
                        if (DEBUG && console) console.log('RangeSlider rangeInput, change');
                        self.change(event);
                    });

                    self.inputs.push(this);
                });

                this.reset();

                return this;
            },

            sendAllOutputToBack: function () {
                $.map(this.inputs, function (input, index) {
                    input.sendOutputToBack();
                });
            },

            change: function (event) {
                if (DEBUG && console) console.log('RangeSlider change', event);
                var values = $.map(this.inputs, function (input, index) {
                    return {
                        value: parseInt($(input).val()),
                        min: parseInt($(input).attr('min')),
                        max: parseInt($(input).attr('max'))

                    };

                });

                priceRange[0] = values[0].value;
                priceRange[1] = values[1].value;

                // console.log(priceRange);
                productsContainer.innerHTML = "";
                getData(null, priceRange);
                // console.log(values[0].value) !!Important min value
                // console.log(values[1].value) !!Important max value

                values.sort(function (a, b) {
                    return a.value - b.value;
                });

                this.config.change.call(this, event, values);
            },

            reset: function () {
                if (DEBUG && console) console.log('RangeSlider reset');
                $.map(this.inputs, function (input, index) {
                    $(input).val(input.initialValue);
                    input.update();
                });
            },

            adjustTrack: function () {
                if (DEBUG && console) console.log('RangeSlider adjustTrack');
                var valueMin = Infinity,
                    rangeMin = Infinity,
                    valueMax = 0,
                    rangeMax = 0;

                $.map(this.inputs, function (input, index) {
                    var val = parseInt($(input).val()),
                        min = parseInt($(input).attr('min')),
                        max = parseInt($(input).attr('max'));

                    valueMin = (val < valueMin) ? val : valueMin;
                    valueMax = (val > valueMax) ? val : valueMax;

                    rangeMin = (min < rangeMin) ? min : rangeMin;
                    rangeMax = (max > rangeMax) ? max : rangeMax;
                });

                if (this.inputs.length > 1) {
                    this.trackIncluded.css('width', (valueMax - valueMin) / (rangeMax - rangeMin) * 100 + '%');
                    this.trackIncluded.css('left', (valueMin - rangeMin) / (rangeMax - rangeMin) * 100 + '%');
                } else {
                    this.trackIncluded.css('width', valueMax / (rangeMax - rangeMin) * 100 + '%');
                    this.trackIncluded.css('left', '0%');
                }

            }

        };

        RangeSlider.defaults = RangeSlider.prototype.defaults;

        $.fn.RangeSlider = function (options) {
            if (DEBUG && console) console.log('$.fn.RangeSlider', options);
            return this.each(function () {
                var instance = $(this).data(PLUGIN_IDENTIFIER);
                if (!instance) {
                    instance = new RangeSlider(this, options).init();
                    $(this).data(PLUGIN_IDENTIFIER, instance);
                }
            });
        };

    }
    )(jQuery);


    var rangeSlider = $('#facet-price-range-slider');
    if (rangeSlider.length > 0) {
        rangeSlider.RangeSlider({
            output: {
                format: function (output) {
                    return output.replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,");
                },
                suffix: function (input) {
                    return parseInt($(input).val()) == parseInt($(input).attr('max')) ? this.config.maxSymbol : '';
                }

            },
        });
    }

}

// Get Filtered Data
function getFilteredData(DataArr) {
    loadHideElements(filtersContainer, filterSpinnerBox);
    DataArr.length ? getData(DataArr) : getData();
    setTimeout(() => {
        loadFilters(filterSpinnerBox, filtersContainer);
    }, 2500);
}

// Add Product to Wishlist or Cart
function addToWishOrCart(btnEl, class_name, id) {
    let addUrl;
    let delUrl;
    let headerEls;
    let totalItems = 0;
    const _quantity = 1;

    let cardinfoEl = btnEl.parentElement;

    let _productImgEl = document.getElementById(`product-img-${id}`);
    _productImg = _productImgEl.style.backgroundImage.slice(4, -1).replace(/"/g, "");
    let _productName = document.getElementById(`product-name-${id}`).textContent;
    let _currentPrice = document.getElementById(`product-current-price-${id}`).textContent.slice(1);

    if (class_name == "add__cart") {
        addUrl = 'add_to_cart'
        delUrl = 'delete_from_cart'
        headerEls = document.querySelectorAll('.cart_num');
        
    } else {
        addUrl = 'add_to_wishlist'
        delUrl = 'delete_from_wishlist'
        headerEls = document.querySelectorAll('.wishlist_num');
    }

    while (!cardinfoEl.classList.contains('card'))
        cardinfoEl = cardinfoEl.parentElement;

    cardinfoEl.classList.toggle(class_name);

    if (cardinfoEl.classList.contains(class_name)){
        $.ajax({
            type: 'GET',
            url: addUrl,
            data: {
                'id' : id,
                'image' : _productImg,
                'title': _productName,
                'quantity': _quantity,
                'price': _currentPrice,
            },
            dataType: 'json',
            success: function (response) {
                console.log(response)
                totalItems = response.total_items
                headerEls.forEach(headerEl => {
                    headerEl.textContent = totalItems;
                });
            }
        })

    } else {

        $.ajax({
            type: 'GET',
            url: delUrl,
            data: {
                'id' : id,
                'quantity': _quantity,
            },
            dataType: 'json',
            success: function (response) {
                // delete
                console.log(response)
                if (response.total_items)
                    totalItems = response.total_items;
                headerEls.forEach(headerEl => {
                   headerEl.textContent = totalItems;
                });
            }
        })

    }
    
    
}


//Add Product to Cart
function addToCart() {

    let cartBtns = document.querySelectorAll('.card__cart');

    cartBtns.forEach(cartBtn => {
        cartBtn.addEventListener('click', () => {
            addToWishOrCart(cartBtn, "add__cart", cartBtn.id);
        });

    });

};

//Add Product to Wishlist
function addToFav() {

    let favBtns = document.querySelectorAll('.card__wishlist');

    favBtns.forEach(favBtn => {
        favBtn.addEventListener('click', () => {
            addToWishOrCart(favBtn, "add__fav", favBtn.id);
        });

    });

};


