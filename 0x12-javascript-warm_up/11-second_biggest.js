#!/usr/bin/node

if (process.argv.length < 4) {
    console.log(0);
} else {
    const size = process.argv.length;
    const arrayOfInts = [];

    for (let i = 2; i < size; i++) {
        arrayOfInts[i - 2] = parseInt(process.argv[i]);
    }
    arrayOfInts.sort(function (a, b) { return b - a; });
    console.log(arrayOfInts[1]);
}