#!/usr/bin/node
// import { argv } from 'node:process'

const aboutC = 'C is fun';
const firstArg = parseInt(process.argv[2]);

if (process.argv[2] === undefined || isNaN(firstArg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < firstArg; i++) {
    console.log(aboutC);
  }
}
