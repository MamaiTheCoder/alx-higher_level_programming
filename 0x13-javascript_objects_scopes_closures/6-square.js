#!/usr/bin/node
// A class Square that defines a square and inherits from Square of 5-square.js.
const Sqr = require('./5-square');

class Square extends Sqr {
  charPrint (c) {
    // Prints the rectangle using the character c.
    if (c === undefined) {
      c = 'X';
    }
    
    for (let i = 0; i < this.height; i++) {
      let s = '';
        for (let j = 0; j < this.width; j++) {
          s += c;
        }
        console.log(s);
    }
  }
};

module.exports = Square;
