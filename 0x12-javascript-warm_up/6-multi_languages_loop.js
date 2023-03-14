#!/usr/bin/node
// Prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop.
const myStr = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let idx = 0;

while (idx < 3) {
  console.log(myStr[idx]);
  idx++;
}

