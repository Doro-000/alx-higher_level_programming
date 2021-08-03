#!/usr/bin/node
const dict = require('./101-data.js').dict;

let newDict = {};
for (const key in dict) {
  if (newDict[String(dict[key])] === undefined) {
    newDict[String(dict[key])] = [];
  }
  newDict[String(dict[key])].push(String(key));
}
console.log(newDict);