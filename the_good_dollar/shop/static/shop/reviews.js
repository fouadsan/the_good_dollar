const csrf = document.getElementsByName('csrfmiddlewaretoken')

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

function addReview() {
    const addReviewForm = document.getElementById('add-review-form');
    const ReviewTextEl = document.getElementById('id_review_text');
    const ReviewRatEl = document.getElementById('id_review_rating');
    addReviewForm.addEventListener('submit', e => {
        e.preventDefault()
    
        $.ajax({
            type: 'POST',
            url: '',
            data: {
                'csrfmiddlewaretoken': csrf[0].value,
                'review_text': ReviewTextEl.value,
                'review_rating': ReviewRatEl.value,
            },
            success: function (response) {
                console.log(response)       
                // rowsBox.insertAdjacentHTML('afterbegin', `
                //     <tr id="${response.id}" data-item="${response.id}">
                //         <td id="id-${response.id}">${response.id}</td>
                //         <td id="name-${response.id}">${response.name}</td>
                //         <td id="article_num-${response.id}">${response.article_num}</td>
                //         <td id="category-${response.id}">${response.category}</td>
                //         <td id="instock-${response.id}">xxx</td>
                //         <td id="barcode-${response.id}">xxx</td>
                //         <td>
                //             <button type="button" id="update-btn" class="btn btn-icon btn-outline-warning"
                //             title="Edit" data-toggle="modal" data-target="#updateModal" data-item="${response.id}">
                //                 <i class="feather icon-edit-2"></i>
                //             </button>&nbsp;
                //             <button type="button" id="delete-btn" class="btn btn-icon btn-outline-danger"
                //             title="Remove" data-toggle="modal" data-target="#deleteModal"
                //                 data-item="${response.id}" data-item-name="${response.name}">
                //                 <i class="feather icon-trash"></i>
                //             </button>
                //         </td>
                //     </tr>
                // `);
                // $('#createModal').modal('hide')
                // handleModalAlerts('success', 'New Object added!');
  
                // createForm.reset();
            },
            // error: function () {
            //     handleModalAlerts('danger', 'ups...something went wrong')
            // }
        })
    })
}


addReview();