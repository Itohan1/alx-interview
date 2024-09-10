#!/usr/bin/node
// Get characters frim star wars api
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response, body) {
  if (error) throw err;
  const role = JSON.parse(body).characters;
  exactOrder(role, 0);
});

const exactOrder = (role, x) => {
  if (x === role.length) return;
  request(role[x], function (error, response, body) {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    exactOrder(role, x + 1);
  });
};
