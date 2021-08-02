#!/usr/bin/node
const { argv } = require('process');

const arg = Number(argv[2]);

if (isNaN(arg)) {
  console.log('Missing size');
} else {
  const repeat = 'X'.repeat(arg);
  for (let i = 0; i < arg; i++) {
    console.log(repeat);
  }
}
