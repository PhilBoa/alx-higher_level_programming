// Wait for the DOM content to be fully loaded
$(document).ready(function () {
  // Add click event listener to the element with id 'red_header'
  $('#red_header').click(function () {
    // Add the class 'red' to the <header> element
    $('header').addClass('red');
  });
});
