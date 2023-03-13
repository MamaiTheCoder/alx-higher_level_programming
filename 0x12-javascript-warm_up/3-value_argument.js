#!/usr/bin/node
// import { argv } from 'node:process'

let print_first_arg;

if (process.argv[2] === undefined) {
    print_first_arg = "No argument";
} else {
    print_first_arg = process.argv[2];
}

console.log(print_first_arg);
