#!/usr/bin/node
import { argv } from 'process';

try {
  console.log(argv[3]);
} catch (error) {
  console.log('No argument');
}
