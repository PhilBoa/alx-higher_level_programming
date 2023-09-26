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

// Construct the URL for the Star Wars API endpoint
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

// Make a GET request to the API endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // Print an error message if the request encounters an error
    console.error(error);
  } else if (response.statusCode === 200) {
    // Parse the JSON response and extract the movie title
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  } else {
    // Print an error message if the request returns a non-200 status code
    console.error(`Request failed with status code ${response.statusCode}`);
  }
});
