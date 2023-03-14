#!/usr/bin/node
// Prints x times “C is fun”.
let printXt = parseInt(process.argv[2]);
if (isNaN(printXt) || process.argv[2] === undefined) {
  console.log('Missing number of occurences');
} else {
  while (printXt > 0) {
    console.log('C is fun');
    printXt--;
  }
}
