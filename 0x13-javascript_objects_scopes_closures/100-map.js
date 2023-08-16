#!/usr/bin/node
const data = require('./100-data.js');
const initialList = data.list;
const newList = initialList.map((value, index) => value * index);
console.log(initialList);
console.log(newList);
