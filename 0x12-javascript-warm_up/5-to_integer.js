#!/usr/bin/node
const { argv } = require('process');

let converted = Number(argv[2]);
if (converted === NaN) {
  console.log('Not a number');
} else {
  console.log(`My number: ${converted}`);
}
