#!/usr/bin/node
const { argv } = require('process');
const { open, close, read, appendFileSync } = require('fs');

open(argv[2], (err, fd) => {
  if (err) {
    throw err;
  }
  read(fd, (err, bytes, buffer) => {
    if (err) {
      close(fd);
      throw err;
    }
    appendFileSync(argv[4], buffer.toString().slice(0, bytes)+'\n');
  });
  close(fd);
});

open(argv[3], (err, fd) => {
  if (err) {
    throw err;
  }
  read(fd, (err, bytes, buffer) => {
    if (err) {
      close(fd);
      throw err;
    }
    appendFileSync(argv[4], buffer.toString().slice(0, bytes));
  });
  close(fd);
});
