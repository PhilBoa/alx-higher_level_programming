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

// Make a GET request to the specified API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // Print an error message if the request encounters an error
    console.error(error);
  } else if (response.statusCode === 200) {
    // Parse the JSON response
    const tasks = JSON.parse(body);

    // Create an object to store the count of completed tasks for each user
    const completedTasksByUser = {};

    // Iterate through the tasks and count completed tasks for each user
    for (const task of tasks) {
      if (task.completed) {
        if (completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId]++;
        } else {
          completedTasksByUser[task.userId] = 1;
        }
      }
    }

    // Print the completed tasks by user ID
    console.log(completedTasksByUser);
  } else {
    // Print an error message if the request returns a non-200 status code
    console.error(`Request failed with status code ${response.statusCode}`);
  }
});
