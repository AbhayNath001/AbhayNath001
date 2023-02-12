// Select all the star elements
const stars = document.querySelectorAll(".fa-star");

// Add a click event listener to each star
stars.forEach(function(star) {
  star.addEventListener("click", function() {
    // Remove the selected class from all stars
    stars.forEach(function(star) {
      star.classList.remove("selected");
    });
    // Add the selected class to the clicked star
    this.classList.add("selected");
    // Get the rating value
    const rating = this.getAttribute("data-rating");
    // Send the rating value to the server
    sendRatingToServer(rating);
  });
});

// Hide and Show the password

const togglePassword = document.querySelector('#togglePassword');
  const password = document.querySelector('#id_password');

  togglePassword.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
});