// Wait for the DOM content to be fully loaded
$(document).ready(function () {
  // Add click event listener to the element with id 'toggle_header'
  $('#toggle_header').click(function () {
    // Toggle the 'red' and 'green' classes on the <header> element
    $('header').toggleClass('red green');
  });
});
