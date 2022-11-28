#!/usr/bin/node

function add (a, b) {
  return (a + b);
}

const digit1 = parseInt(process.argv[2]);
const digit2 = parseInt(process.argv[3]);
console.log(add(digit1, digit2));
