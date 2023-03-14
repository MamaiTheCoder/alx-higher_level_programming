#!/usr/bin/node
// A class Rectangle that defines a rectangle.
class Rectangle {
  constructor (w, h) {
    // If w or h is equal to 0 or not a positive integer, create an empty object.
    if (typeof h === 'number' && typeof w === 'number' && h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    // Prints the rectangle using the character X.
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }
}

module.exports = Rectangle;
