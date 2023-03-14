#!/usr/bin/node
// Imports an array and computes a new array.

const array = require('./100-data.js').list;

const newList = array.map((num, idx) => {
  return num * idx;
});

console.log(array);
console.log(newList);