#!/usr/bin/node
// Imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
const dict = require('./101-data.js').dict;
const newDict = {};

Object.keys(dict).map(key => {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
});

console.log(newDict);