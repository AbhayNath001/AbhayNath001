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

function sendRatingToServer(rating) {
  // Use an HTTP request to send the rating value to the server
  // for example: fetch("/rating", { method: "POST", body: rating });
  // You can use any library or method to send the data to the server.
  console.log("rating sent to server:", rating);
}