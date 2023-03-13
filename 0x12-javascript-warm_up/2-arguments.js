#!/usr/bin/node

let num_args;

if (process.argv.length === 2) {
    num_args = "No argument";
} else if (process.argv.length === 3) {
    num_args = "Argument found";
} else {
    num_args = "Arguments found";
}

console.log(num_args);



