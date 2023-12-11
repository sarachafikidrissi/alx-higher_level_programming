#!/usr/bin/node

const arg = process.argv[2];

let num = Number.parseInt(arg);

if (!arg | isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  while (num > 0) {
    console.log('C is fun');
    num--;
  }
}
