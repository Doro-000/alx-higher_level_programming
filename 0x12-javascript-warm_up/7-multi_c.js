#!/usr/bin/node
const { argv } = require('process');

let number_loop = Number(argv[2]);

if (number_loop === NaN) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < number_loop; i++) {
    console.log('C is fun');
  }
}
