// Wait for the DOM content to be fully loaded
$(document).ready(function () {
  // Make an AJAX request to fetch data from the URL
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function (data) {
      // Iterate over the movie data and extract titles
      data.results.forEach(function (movie) {
        // Create a new list item for each movie title
        const listItem = $('<li>').text(movie.title);
        // Append the list item to the HTML tag UL#list_movies
        $('#list_movies').append(listItem);
      });
    },
    error: function (error) {
      // Handle errors if the request fails
      console.log('Error:', error);
    }
  });
});
