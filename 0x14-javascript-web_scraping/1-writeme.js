#!/usr/bin/node
const { writeFile } = require('fs');
const { argv } = require('process');

writeFile(argv[2], argv[3], 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
