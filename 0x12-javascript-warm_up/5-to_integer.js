#!/usr/bin/node

const argv = process.argv;
const first_arg = argv[2];
const arg_int = parseInt(first_arg);

if (typeof arg_int === 'number' && isNaN(arg_int) === false) {
  console.log(arg_int);
} else if (isNaN(arg_int)) {
	console.log('Not a number')
}
