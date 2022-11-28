#!/usr/bin/node

const argv = process.argv;
let i;
const argCount = parseInt(argv[2]);
if (!argv[2]) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < argCount; i++) {
    console.log('C is fun');
  }
}
