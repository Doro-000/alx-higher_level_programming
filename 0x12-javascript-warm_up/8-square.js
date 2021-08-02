#!/usr/bin/node
const { argv } = require('process');

let arg = Number(argv[2]);

if (arg === NaN) {
  console.log('Missing size');
} else {
  let repeat = 'X'.repeat(arg);
  for (let i = 0; i < arg; i++) {
    console.log(repeat);
  }
}
