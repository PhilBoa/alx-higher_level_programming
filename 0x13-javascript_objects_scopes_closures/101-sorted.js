#!/usr/bin/node
const data = require('./101-data.js');
const dict = data.dict;
const users = {};
for (const userId in dict) {
  const occurrences = dict[userId];
  if (!users[occurrences]) {
    users[occurrences] = [];
  }
  users[occurrences].push(userId);
}
console.log(users);
