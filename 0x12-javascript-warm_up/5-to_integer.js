#!/usr/bin/node
// Pprints My number: <first argument converted in integer> if the first argument can be converted to an integer.
const myVar = parseInt(process.argv[2]);
if (process.argv[2] === undefined || isNaN(myVar)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myVar);
}
