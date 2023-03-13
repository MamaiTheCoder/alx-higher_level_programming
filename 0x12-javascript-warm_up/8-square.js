#!/usr/bin/node
// import { argv } from 'node:process'

let charToPrintSqr = 'J';
const firstArg = parseInt(process.argv[2]);

if (process.argv[2] === undefined || isNaN(firstArg)) {
    console.log("Missing Size");
} else {
    for (let i = 0; i < firstArg; i++) {
        // charToPrintSqr += 'X'
        // for (let j = 0; j + i < firstArg; j++) {
        //     charToPrintSqr += 'X'
        // }
        console.log(charToPrintSqr)
        for (let j = 0; j + i < firstArg; j++) {
            charToPrintSqr += 'X'
        }

    }
    
}


