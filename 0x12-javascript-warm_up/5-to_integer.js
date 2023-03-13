#!/usr/bin/node

const myVar = parseInt(process.argv[2]);
let numToPrint;
if (process.argv[2] === undefined || isNaN(myVar)) {
  numToPrint = 'Not a number';
} else {
  numToPrint = 'My number: ' + myVar;
}

console.log(numToPrint);
