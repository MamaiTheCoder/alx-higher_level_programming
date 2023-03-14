#!/usr/bin/node
// Prints a square with character X
let size = parseInt(process.argv[2]);
if (isNaN(size) || process.argv[2] === undefined) {
  // If the first argument can’t be converted to an integer, print “Missing size”.
  console.log('Missing size');
}
let pstr = 'X';
for (let i = 0; i < size - 1; i++) {
  pstr += 'X';
}
while (size > 0) {
  console.log(pstr);
  size--;
}

