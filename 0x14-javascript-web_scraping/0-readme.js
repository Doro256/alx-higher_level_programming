#!/usr/bin/node
//  This script reads and prints the content of a file

const fs = require('fs');
const filepath = process.argv[2];

fs.readFile(filepath, 'utf-8', function (err, contents) {
  if (err) {
    console.log(err);
  } else {
    console.log(contents);
  }
});
