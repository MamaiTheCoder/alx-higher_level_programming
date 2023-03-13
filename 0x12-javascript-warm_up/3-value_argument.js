#!/usr/bin/node

let printFirstArg;

if (process.argv[2] === undefined) {
  printFirstArg = 'No argument';
} else {
  printFirstArg = process.argv[2];
}

console.log(printFirstArg);
