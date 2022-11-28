#!/usr/bin/node

const argv = process.argv;
const character = 'X';
let i;
const argInt = parseInt(argv[2]);

if (!argv[2]) {
  console.log('Missing size');
} else if (isNaN(argInt)) {
  console.log('Missing size');
} else {
  for (i = 0; i < argInt; i++) {
    console.log(character.repeat(argInt));
  }
}
