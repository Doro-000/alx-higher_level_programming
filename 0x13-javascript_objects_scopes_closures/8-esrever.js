#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  for (let i = 0; i > list.length * -1; i--) {
    if (i === 0) {
      newList.push(list.slice(-1)[0]);
    } else {
      newList.push(list.slice(i - 1, i)[0]);
    }
  }
  return newList;
};
