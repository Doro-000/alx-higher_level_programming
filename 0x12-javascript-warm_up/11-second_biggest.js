#!/usr/bin/node
const { argv } = require('process');

if (argv.length <= 3) {
  console.log(0);
} else {
  const numbers = [];
  for (let i = 2; i < argv.length; i++) {
    numbers.push(Number(argv[i]));
  }
  numbers.sort();
  console.log(numbers[1]);
}
