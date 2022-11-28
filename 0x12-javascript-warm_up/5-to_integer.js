#!/usr/bin/node

const argv = process.argv;
const firstArg = argv[2];
const argInt = parseInt(firstArg);

if (typeof argInt === 'number' && isNaN(argInt) === false) {
  console.log('My number: ' + argInt);
} else if (isNaN(argInt)) {
  console.log('Not a number');
}
