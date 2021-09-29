const reviewCardEl = document.querySelector('.reviews__card');
const _pId = reviewCardEl.id;

function addReview() {
    addReviewUrl =  `${rootUrl}\/shop\/add_review`;

    
    const reviewFormWrapper = document.querySelector('.review-form');    
    const addReviewForm = document.getElementById('add-review-form');
    const ReviewTextEl = document.getElementById('id_review_text');
    const ReviewRatEl = document.getElementById('id_review_rating');
    const noReviewsEl = document.getElementById('no-reviews-el');

    
    console.log(_pId);

    // const p_id = reviewCardEl.getAttribute('data-item');
    // console.log(p_id)
    
    if(addReviewForm != null) {
        addReviewForm.addEventListener('submit', e => {
            e.preventDefault()
        
            $.ajax({
                type: 'POST',
                url: addReviewUrl,
                data: {
                    'csrfmiddlewaretoken': csrf[0].value,
                    'id': _pId,
                    'review_text': ReviewTextEl.value,
                    'review_rating': ReviewRatEl.value,
                },
                
                success: function (response) {
                    console.log(response)
                    data = response.data
                    
                    const reviewRatEl = document.createElement('cite');
                    for (i=0; i<data.review_rating; i++) {
                        reviewRatEl.innerHTML += `
                            <i class="fa fa-star text-warning"></i>
                        `
                    }
                    reviewCardEl.insertAdjacentHTML('afterbegin', `
                        <div class="review-list review-list">
                            <div class="single-review justify-content-between d-flex">
                            <div class="user justify-content-between d-flex">
                                <div class="thumb">
                                    <img src="${rootUrl}\/static/assets/img/accounts/default.png" alt="">
                                    <h5 class="text-center">
                                        <a href="#">${data.user}</a>&nbsp;
                                    </h5>
                                </div>
                                <div class="desc">
                                    <blockquote class="d-flex flex-row justify-content-between generic-blockquote review">
                                        <div class="col-lg-9 col-md-8 col-sm-7 col-11">${data.review_text}</div>
                                        <div class="col-lg-2 col-md-3 col-sm-4">
                                            ${reviewRatEl.outerHTML}
                                        </div>
                                    </blockquote>
                                </div>
                            </div>
                            </div>
                        </div>
                    `);
                    reviewFormWrapper.classList.add('not-visible');
                    noReviewsEl.classList.add('not-visible');
                    handleAlerts('center', 'Success', 'Review Added', 'success', false, '2000');
                },
                error: function () {
                    console.log('oops, something went wrong');
                    handleAlerts('center', 'Error!', 'Oops...something went wrong', 'error', true);
                }
            });
        });
    }
    
}

addReview();




document.getElementById("zoom").addEventListener(
  "mousemove",
  function (e) {

    let original = document.getElementById("main-img"),
      magnified = document.getElementById("large-img"),
      style = magnified.style,
      x = e.pageX - this.offsetLeft,
      y = e.pageY - this.offsetTop,
      imgWidth = original.width,
      imgHeight = original.height,
      xperc = (x / imgWidth) * 100,
      yperc = (y / imgHeight) * 100;

    // Add some margin for right edge
    if (x > 0.01 * imgWidth) {
      xperc += 0.15 * xperc;
    }

    // Add some margin for bottom edge
    if (y >= 0.01 * imgHeight) {
      yperc += 0.15 * yperc;
    }

    // Set the background of the magnified image horizontal
    style.backgroundPositionX = xperc - 9 + "%";
    // Set the background of the magnified image vertical
    style.backgroundPositionY = yperc - 9 + "%";

    // Move the magnifying glass with the mouse movement.
    style.left = x - 50 + "px";
    style.top = y - 50 + "px";
  },
  false
);
