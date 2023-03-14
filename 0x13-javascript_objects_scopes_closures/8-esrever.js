#!/usr/bin/node
// Returns the reversed version of a list
exports.esrever = function (list) {
  let firstPointer = 0;
  let lastPointer = list.length - 1;
  while (firstPointer <= lastPointer) {
    let temp = list[firstPointer];
    list[firstPointer] = list[lastPointer];
    list[lastPointer] = temp;
    firstPointer += 1;
    lastPointer -= 1;
  }
  return list;
};

// list = [0,1,2,3,4,5,6,7,8,9];

// console.log(list[10]);