#!/usr/bin/node
// Returns the reversed version of a list
exports.esrever = function (list) {
  let firstPointer = 0;
  let lastPointer = list.length - 1;
  while (firstPointer <= lastPointer) {
    const temp = list[firstPointer];
    list[firstPointer] = list[lastPointer];
    list[lastPointer] = temp;
    firstPointer += 1;
    lastPointer -= 1;
  }
  return list;
};
