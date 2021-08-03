#!/usr/bin/node
const { argv } = require('process');
const { open, close, read, appendFileSync } = require('fs');

open(argv[2], 'r', (err, fd) => {
  if (err) {
    throw err;
  }
  read(fd, (err, bytes, buffer) => {
    if (err) {
      close(fd, (err) => {
        if (err) {
          throw err;
        }
      });
      throw err;
    }
    appendFileSync(argv[4], buffer.toString().slice(0, bytes));
  });
  close(fd, (err) => {
    if (err) {
      throw err;
    }
  });
});

open(argv[3], 'r', (err, fd) => {
  if (err) {
    close(fd, (err) => {
      if (err) {
        throw err;
      }
    });
    throw err;
  }
  read(fd, (err, bytes, buffer) => {
    if (err) {
      close(fd, (err) => {
        if (err) {
          throw err;
        }
      });
      throw err;
    }
    appendFileSync(argv[4], buffer.toString().slice(0, bytes));
  });
  close(fd, (err) => {
    if (err) {
      throw err;
    }
  });
});
