#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const films = JSON.parse(body).result;
    let count = 0;
    for (const i in films) {
      const chars = films[i].characters;
      for (const j in chars) {
        if (chars[j].includes('18')) {
          count++;
        }
      }
    }
    console.log('count');
  } else {
    console.log('ErrorCode' + response.statusCode);
  }
});
