#!/usr/bin/node

const request = require('request');
const path = require('path');

// Get the script name
const scriptName = path.basename(__filename);

// Check if the correct number of command-line arguments are provided
if (process.argv.length !== 3) {
  console.error('Usage: ./' + scriptName + ' <movie-ID>');
  process.exit(1);
}

// Get the movie ID from the command-line arguments
const movieID = process.argv[2];

// Construct the URL for the Star Wars API endpoint for the specified movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

// Make a GET request to the API endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // Print an error message if the request encounters an error
    console.error(error);
  } else if (response.statusCode === 200) {
    // Parse the JSON response
    const movieData = JSON.parse(body);

    // Extract the character URLs from the movie data in the same order as the list
    const characterUrls = movieData.characters;

    // Function to fetch character names and print them
    const fetchAndPrintCharacterNames = (characterUrls, index = 0) => {
      if (index < characterUrls.length) {
        const characterUrl = characterUrls[index];
        request.get(characterUrl, (charError, charResponse, charBody) => {
          if (!charError && charResponse.statusCode === 200) {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
            fetchAndPrintCharacterNames(characterUrls, index + 1);
          } else {
            // Print an error message if there is an error while fetching character data
            console.error(`Error fetching character data: ${charError}`);
          }
        });
      }
    };

    // Start fetching and printing character names
    fetchAndPrintCharacterNames(characterUrls);
  } else {
    // Print an error message if the request returns a non-200 status code
    console.error(`Request failed with status code ${response.statusCode}`);
  }
});
