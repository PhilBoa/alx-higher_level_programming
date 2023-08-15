#!/usr/bin/node
function factorial (number) {
  if (number === 1) {
    return 1;
  }
  return number * factorial(number - 1);
}
const args = process.argv.slice(2);
const myNumber = parseInt(args[0]);
if (Number.isInteger(myNumber)) {
  const result = factorial(myNumber);
  console.log(result);
} else {
  console.log(1);
}
