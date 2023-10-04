// Wait for the DOM content to be fully loaded
$(document).ready(function () {
  // Add a click event listener to the element with id 'red_header'
  $('#red_header').click(function () {
    // Select the <header> element using jQuery and change its text color to red
    $('header').css('color', '#FF0000');
  });
});
