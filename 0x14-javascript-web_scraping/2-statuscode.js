#!/usr/bin/node

const request = require('request');
const path = require('path');

// Get the script name (name of the current script file)
const scriptName = path.basename(__filename);

// Check if the correct number of command-line arguments are provided
if (process.argv.length !== 3) {
  console.error('Usage: ./' + scriptName + ' <URL>');
  process.exit(1);
}

// Get the URL to request from the command-line arguments
const url = process.argv[2];

// Send a GET request to the specified URL
request.get(url, (error, response) => {
  if (error) {
    // Print an error message if the request encounters an error
    console.error(error);
  } else {
    // Print the status code in the desired format
    console.log(`code: ${response.statusCode}`);
  }
});
