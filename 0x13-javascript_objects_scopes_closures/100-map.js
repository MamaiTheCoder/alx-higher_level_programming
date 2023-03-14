#!/usr/bin/node
// Imports an array and computes a new array.

const oldList = require('./100-data.js').list;

const newList = oldList.map((num, idx) => {
  return num * idx;
});

console.log(oldList);
console.log(newList);
