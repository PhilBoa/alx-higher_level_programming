// Wait for the DOM content to be fully loaded
$(document).ready(function () {
  // Add item to the list when #add_item is clicked
  $('#add_item').click(function () {
    // Create a new <li> element
    const newItem = $('<li>').text('Item');
    // Append the new <li> element to UL.my_list
    $('.my_list').append(newItem);
  });

  // Remove the last item from the list when #remove_item is clicked
  $('#remove_item').click(function () {
    // Select the last <li> element inside UL.my_list and remove it
    $('.my_list li:last-child').remove();
  });

  // Clear all items from the list when #clear_list is clicked
  $('#clear_list').click(function () {
    // Remove all <li> elements inside UL.my_list
    $('.my_list').empty();
  });
});
