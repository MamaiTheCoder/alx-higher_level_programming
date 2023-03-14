#!/usr/bin/node
// A class Rectangle that defines a rectangle.
module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
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

  rotate() {
    // Exchanges the width and the height of the rectangle.
    // [this.width, this.height] = [this.height, this.width];
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double() {
    // Multiples the width and the height of the rectangle by 2.
    this.width *= 2;
    this.height *= 2;
  }
}