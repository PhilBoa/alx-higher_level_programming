#!/usr/bin/node

const request = require('request');
const path = require('path');

// Get the script name
const scriptName = path.basename(__filename);

// Check if the correct number of command-line arguments are provided
if (process.argv.length !== 3) {
  console.error('Usage: ./' + scriptName + ' <API-URL>');
  process.exit(1);
}

// Get the API URL from the command-line arguments
const apiUrl = process.argv[2];

// Make a GET request to the API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // Print an error message if the request encounters an error
    console.error(error);
  } else if (response.statusCode === 200) {
    // Parse the JSON response
    const filmData = JSON.parse(body);

    // Initialize a counter for films where Wedge Antilles is present
    let count = 0;

    // Character ID for Wedge Antilles
    const wedgeAntillesID = 18;

    // Iterate through the films and count how many times Wedge Antilles appears
    for (const film of filmData.results) {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesID}/`)) {
        count++;
      }
    }

    // Print the count
    console.log(count);
  } else {
    // Print an error message if the request returns a non-200 status code
    console.error(`Request failed with status code ${response.statusCode}`);
  }
});
