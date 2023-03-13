#!/usr/bin/node
// import { argv } from 'node:process'

const aboutC = "C is fun";

let first_arg = parseInt(process.argv[2]);

if (process.argv[2] === undefined || isNaN(first_arg)) {
    console.log("Missing number of occurrences");
} else {
    for (let i = 0; i < first_arg; i++) {
        console.log(aboutC);
    }
}