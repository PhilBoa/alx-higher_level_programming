#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const path = require('path');

// Get the script name
const scriptName = path.basename(__filename);

// Check if the correct number of command-line arguments are provided
if (process.argv.length !== 4) {
  console.error('Usage: ./' + scriptName + ' <URL> <file-path>');
  process.exit(1);
}

// Get the URL and file path from the command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the specified URL
request.get(url, (error, response, body) => {
  if (error) {
    // Print an error message if the request encounters an error
    console.error(error);
  } else if (response.statusCode === 200) {
    // Write the response body to the specified file path in utf-8 encoding
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        // Print an error message if there is an error while writing the file
        console.error(err);
      }
    });
  } else {
    // Print an error message if the request returns a non-200 status code
    console.error(`Request failed with status code ${response.statusCode}`);
  }
});
