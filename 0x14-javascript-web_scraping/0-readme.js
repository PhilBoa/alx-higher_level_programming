#!/usr/bin/node

// Import the 'fs' module for file operations
const fs = require('fs');
const path = require('path');

// Get the script name (name of the current script file)
const scriptName = path.basename(__filename);

// Check if the correct number of command-line arguments are provided
if (process.argv.length !== 3) {
  console.error('Usage: ./' + scriptName + ' <file-path>');
  process.exit(1);
}

// Get the file path from the command-line arguments
const filePath = process.argv[2];

// Read the content of the file in utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // Print the error object if an error occurred
    console.error(err);
  } else {
    // Print the content of the file
    console.log(data);
  }
});
