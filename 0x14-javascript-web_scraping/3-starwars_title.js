#!/usr/bin/node

const url = "https://swapi-api.hbtn.io/api/films/" + process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
    if (error) {
        console.log(error);
    } else if (response.statusCode === 200) {
        console.log(JSON.parse(body).title);
    } else {
        console.log("ErrorCode" + response.statusCode);
    }
});
