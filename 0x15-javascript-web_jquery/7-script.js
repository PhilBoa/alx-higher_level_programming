// Wait for the DOM content to be fully loaded
$(document).ready(function () {
  // Make an AJAX request to fetch data from the URL
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    success: function (data) {
      // Extract the character name from the fetched data
      const characterName = data.name;
      // Display the character name in the HTML tag DIV#character
      $('#character').text(characterName);
    },
    error: function (error) {
      // Handle errors if the request fails
      console.log('Error:', error);
    }
  });
});
