#!/usr/bin/node
const { argv } = require('process');

let converted = Number(argv[3]);
if (converted === NaN) {
  console.log('Not a number');
} else {
  console.log(`My number: ${converted}`);
}
