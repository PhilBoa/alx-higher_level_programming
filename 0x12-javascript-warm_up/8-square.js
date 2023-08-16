#!/usr/bin/node
const args = process.argv.slice(2);
const integerNumber = parseInt(args[0]);
if (Number.isInteger(integerNumber)) {
	  for (let i = 0; i < integerNumber; i++) {
		      let row = '';
		      for (let j = 0; j < integerNumber; j++) {
			            row += 'X';
			          }
		      console.log(row);
		    }
} else {
	  console.log('Missing size');
}
