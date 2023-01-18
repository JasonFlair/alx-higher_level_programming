#!/usr/bin/node

const fs = require('fs');
content = fs.readFileSync(process.argv[2], "utf-8");
console.log(content);
