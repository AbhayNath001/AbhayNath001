emailjs.init("1x0vmxBtf8-ADHjLj");

function submitForm() {
    // Reset error messages
    document.querySelectorAll('.error-txt').forEach(function (error) {
        error.style.display = 'none';
    });

    // Perform client-side validation here if needed
    let isValid = true;

    // Validate each field
    const fieldsToValidate = ['name', 'email', 'subject', 'message'];
    fieldsToValidate.forEach(function (fieldId) {
        const value = document.getElementById(fieldId).value.trim();
        if (value === '') {
            isValid = false;
            const errorElement = document.querySelector(`#${fieldId} + .error-txt`);
            errorElement.style.display = 'block';
        }
    });

    if (!isValid) {
        // If any field is blank, do not proceed with submission
        return;
    }

    // Assuming all input is valid, prepare data for EmailJS
    const formData = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        phone: document.getElementById("phone").value,
        subject: document.getElementById("subject").value,
        message: document.getElementById("message").value
    };

    // Send data to EmailJS
    emailjs.send("service_nhyijnr", "template_oq4z37z", formData)
        .then(function (response) {
            console.log("Email sent successfully:", response);
            displayMessage('Message Sent Successfully!', 'success');

            // Reset the form after a successful submission
            document.getElementById('contactForm').reset();
        }, function (error) {
            console.error("Failed to send the email:", error);
            displayMessage('Failed to send the message. Please try again later.', 'error');
        });
}

// Add a new function to display messages
function displayMessage(message, messageType) {
    const messageContainer = document.getElementById('messageContainer');
    messageContainer.textContent = message;

    // Remove existing classes and add the appropriate class for styling
    messageContainer.classList.remove('success', 'error');
    messageContainer.classList.add(messageType);

    // Show the message container
    messageContainer.style.display = 'block';

    // Hide the message after a few seconds (adjust as needed)
    setTimeout(function () {
        messageContainer.style.display = 'none';
    }, 3000);
}