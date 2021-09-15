#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

let count = 0;
function MakeRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        resolve(body);
      } else {
        reject(error);
      }
    });
  });
}

async function main () {
  let movies = await MakeRequest(argv[2]);
  movies = JSON.parse(movies).results;
  movies.forEach(element => {
    element.characters.forEach(element => {
      const CharacterId = element.slice(37, -1);
      if (CharacterId === '18') {
        count++;
      }
    });
  });
  console.log(count);
}

main();
