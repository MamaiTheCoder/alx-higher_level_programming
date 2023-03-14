#!/usr/bin/node
// A class Rectangle that defines a rectangle.
module.exports = class Rectangle {
  constructor(w, h) {
    // If w or h is equal to 0 or not a positive integer, create an empty object.
    if (typeof h === 'number' && typeof w === 'number' && h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print() {
    // Prints the rectangle using the character X.
    for (let i = 0; i < this.height; i++) {
      let j = 0;
      for (; j < this.width; ++j) {
        process.stdout.write('X');
      }

      if (j === this.width) {
        console.log('');
      }
    }
  }
}