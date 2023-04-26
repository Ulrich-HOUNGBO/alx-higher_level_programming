#!/usr/bin/node

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const request = require('request');
request(url, function (err, response, body) {
    const characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
        request(characters[i], function (err, response, body) {
            console.log(JSON.parse(body).name);
        });
    }
}
