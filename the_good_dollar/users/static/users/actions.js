function updateProfile() {
const alertBox = document.getElementById('alert-box');
const spinnerBox = document.getElementById('spinner-box');
const saveProfilebox = document.getElementById('saveProfile-box');
const profileForm = document.getElementById('profile-form');

const fnameInput = document.getElementById('id_first_name');
const lnameInput = document.getElementById('id_last_name');
const emailInput = document.getElementById('id_email');
const phoneInput = document.getElementById('id_phone');
const addressInput = document.getElementById('id_address');
const cityInput = document.getElementById('id_city');


profileForm.addEventListener('submit', e => {
    e.preventDefault()

    var formData = new FormData()
    formData.append('csrfmiddlewaretoken', csrf[0].value);
    formData.append('first_name', fnameInput.value);
    formData.append('last_name', lnameInput.value);
    formData.append('email', emailInput.value);
    formData.append('phone', phoneInput.value);
    formData.append('address', addressInput.value);
    formData.append('city', cityInput.value);

    $.ajax({
        type: 'POST',
        url: '',
        enctype: 'multipart/form-data',
        data: formData,
        dataType: 'json',
        beforeSend: function () {
            saveProfilebox.classList.add('not-visible');
            spinnerBox.classList.remove('not-visible');
        },
        success: function (response) {
            console.log(response)
            setTimeout(() => {
                console.log('done');
                // imageInput.value = response.image 
                spinnerBox.classList.add('not-visible')
                saveProfilebox.classList.remove('not-visible')
                handleAlerts('top-end', 'Update', 'Your profile has been updated', 'success', false, 1500);
            }, 500);
        },
        error: function (error) {
            spinnerBox.classList.add('not-visible')
            saveProfilebox.classList.remove('not-visible')
            // handleAlerts('center', 'Error!', 'Oops...something went wrong', 'error', true)

        },
        processData: false,
        contentType: false,
        cache: false,
    })
})
}

updateProfile();