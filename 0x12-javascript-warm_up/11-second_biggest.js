#!/usr/bin/node
const args = process.argv.slice(2);
const numbers = args.map(arg => parseInt(arg));
if (numbers.length <= 1) {
  console.log(0);
} else {
  const sorted = numbers.sort((a, b) => b - a);
  console.log(sorted[1]);
}
