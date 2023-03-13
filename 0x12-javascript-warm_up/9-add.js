#!/usr/bin/node

let firstDig = parseInt(process.argv[2]);
let secondDig = parseInt(process.argv[3]);

function add(a, b) {
    let sum = 0;
    sum = a + b;
    console.log(sum);
}

add(firstDig, secondDig);