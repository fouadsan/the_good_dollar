function addReview() {
    addReviewUrl =  `${rootUrl}\/shop\/add_review`;

    const reviewCardEl = document.querySelector('.reviews__card');
    const addReviewForm = document.getElementById('add-review-form');
    const ReviewTextEl = document.getElementById('id_review_text');
    const ReviewRatEl = document.getElementById('id_review_rating');
    const addReviewBtn = document.getElementById('add-review-btn');
    const addFirstRevEl = document.querySelector('.add__first__review');

    const _pId = reviewCardEl.id;
    console.log(_pId)

    // const p_id = reviewCardEl.getAttribute('data-item');
    // console.log(p_id)

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
                addFirstRevEl.style.display = "none";
                reviewCardEl.insertAdjacentHTML('afterbegin', `
                    <div class="card-body review-list" style="max-height: 400px; overflow: auto;">
                            <blockquote class="blockquote text-right">
                                <small>${data.review_text}</small>
                                <footer class="blockquote-footer">${data.user}
                                    ${reviewRatEl.outerHTML}
                                </footer>
                            </blockquote>
                            <hr>
                    </div>
                `);
                addReviewBtn.style.display = "none";
                $('#review-modal').modal('hide');
                // handleModalAlerts('success', 'New Object added!');
            },
            error: function () {
                console.log('oops, something went wrong');
                // handleModalAlerts('danger', 'oops...something went wrong')
            }
        })
    })
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