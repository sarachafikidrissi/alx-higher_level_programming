#!/usr/bin/node

function fact (a) {
  if (a === 0) return (1);
  return (a * fact(a - 1));
}

const arg = parseInt(process.argv[2]);

if (!arg || Number.isNaN(arg)) {
  console.log(1);
} else {
  console.log(fact(arg));
}
