// Wait for the DOM content to be fully loaded
$(document).ready(function () {
  // Make an AJAX request to fetch data from the URL
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    method: 'GET',
    dataType: 'json', // Specify the expected data type
    success: function (data) {
      // Display the translation of "hello" in the HTML tag DIV#hello
      $('#hello').text(data.hello);
    },
    error: function (error) {
      // Handle errors if the request fails
      console.log('Error:', error);
    }
  });
});
