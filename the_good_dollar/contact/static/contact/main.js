function sendEmail() {
    const contactUrl = "send_email";
    const contactForm = document.getElementById('contact-form');
    const nameInput = document.getElementById('name-input');
    const emailInput = document.getElementById('email-input');
    const subjectInput = document.getElementById('subject-input');
    const messageInput = document.getElementById('message-input');
    const sendEmailBtn = document.getElementById('send-email-btn');
    const emailSpinnerBox = document.getElementById('email-spinner-box');
    contactForm.addEventListener('submit', e => {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: contactUrl,
            data: {
                'csrfmiddlewaretoken': csrf[0].value,
                'name': nameInput.value,
                'email': emailInput.value,
                'subject': subjectInput.value,
                'message': messageInput.value,
            },
            dataType: 'json',
            beforeSend: function () {
                sendEmailBtn.classList.add('not-visible');
                emailSpinnerBox.classList.remove('not-visible');
            },
            success: function (response) {
                setTimeout(() => {
                    emailSpinnerBox.classList.add('not-visible');
                    sendEmailBtn.classList.remove('not-visible');

                    nameInput.value = "";
                    emailInput.value = "";
                    subjectInput.value = "";
                    messageInput.value = "";

                }, 1500);
                console.log(response.msg);
                // handleAlerts('center', 'Email Status', response.msg, response.type, response.confirmation)
            },
            error: function (error) {
                // handleAlerts('center', 'Error!', 'Oops...something went wrong', 'error', true)
            }
        });
    })

}

sendEmail();