#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js <file1> <file2> <destination>');
  process.exit(1);
}

const file1 = process.argv[2];
const file2 = process.argv[3];
const destinationFile = process.argv[4];

fs.readFile(file1, 'utf8', (err1, data1) => {
  if (err1) {
    console.error(err1.message);
    process.exit(1);
  }

  fs.readFile(file2, 'utf8', (err2, data2) => {
    if (err2) {
      console.error(err2.message);
      process.exit(1);
    }

    const finalText = data1 + data2;

    fs.writeFile(destinationFile, finalText, (err3) => {
      if (err3) {
        console.error(err3.message);
        process.exit(1);
      }
    });
  });
});
