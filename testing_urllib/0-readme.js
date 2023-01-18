#!/usr/bin/node

const fs = require('fs');
content = fsreadFileSync(process.argv[1], "utf-8");
console.log(content);