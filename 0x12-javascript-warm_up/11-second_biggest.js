#!/usr/bin/node
const { argv } = require('process');

if (argv.length <= 3) {
  console.log(0);
} else {
  let numbers = [];
  for (let i = 2; i < argv.length; i++) {
    numbers.push(Number(argv[i]));
  }
  let largest = numbers[0];
  let second_largest = numbers[0];
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > largest) {
      second_largest = largest;
      largest = numbers[i];
    }
  }
  console.log(second_largest);
}
  
