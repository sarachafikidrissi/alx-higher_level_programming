#!/usr/bin/node

const arg = process.argv[2];
if (!arg) console.log('Not a number');

else {
  const num = Number.parseInt(arg);

  if (!isNaN(num)) {
    console.log('My number:', num);
  } else console.log('Not a number');
}
