#!/usr/bin/node
// Returns the number of occurrences in a list.
exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      num += 1;
    }
  }
  return num;
};
