#!/usr/bin/node
// Searches the second biggest integer in the list of arguments.
if (process.argv.length < 4) {
  console.log('0');
} else {
  const size = process.argv.length;
  const ints = [];
  for (let i = 2; i < size; i++) {
    ints[i - 2] = parseInt(process.argv[i]);
  }
  ints.sort(function (a, b) { return b - a; });
  console.log(ints[1]);
}
