#!/usr/bin/node
const { argv } = require('process');

function factorial (n) {
  if (n !== n || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

let number = Number(argv[2]);
console.log(factorial(number));
