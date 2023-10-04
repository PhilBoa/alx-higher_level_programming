// Wait for the DOM content to be fully loaded
$(document).ready(function () {
  // Add click event listener to the element with id 'update_header'
  $('#update_header').click(function () {
    // Update the text of the <header> element to 'New Header!!!'
    $('header').text('New Header!!!');
  });
});
