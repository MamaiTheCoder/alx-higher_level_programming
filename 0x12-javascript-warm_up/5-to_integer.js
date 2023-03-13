#!/usr/bin/node
// import { argv } from 'node:process';

const myVar = parseInt(process.argv[2]);

if (process.argv[2] === undefined || isNaN(myVar)) {
    num_to_print = "Not a number";
} else {
    num_to_print = "My number: " + myVar;
}

console.log(num_to_print);
