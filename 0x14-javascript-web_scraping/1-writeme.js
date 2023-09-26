#!/usr/bin/node

const fs = require('fs');
const path = require('path');

// Get the script name (name of the current script file)
const scriptName = path.basename(__filename);

// Check if the correct number of command-line arguments are provided
if (process.argv.length !== 4) {
  console.error('Usage: ./' + scriptName + ' <file-path> <string-to-write>');
  process.exit(1); // Exit with a non-zero status code to indicate an error
}

// Get the file path and string to write from the command-line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the string to the file in utf-8 encoding
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    // Print the error object if an error occurred while writing
    console.error(err);
  }
});
