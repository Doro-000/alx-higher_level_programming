#!/usr/bin/node
const ParentSquare = require('./5-Square.js');

class Square extends ParentSquare {
  charPrint (c) {
    let char = c;
    if (c === undefined) {
      char = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
