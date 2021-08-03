#!/usr/bin/node
const { argv } = require('process');
const { readFile, appendFile } = require('fs');

readFile(argv[2], 'utf-8', (err, data) => {
  if (err) {
    throw err;
  }
  appendFile(argv[4], data, 'utf-8', (err) => {
    if (err) {
      throw err;
    }
  });
});

readFile(argv[3], 'utf-8', (err, data) => {
  if (err) {
    throw err;
  }
  appendFile(argv[4], data, 'utf-8', (err) => {
    if (err) {
      throw err;
    }
  });
});
