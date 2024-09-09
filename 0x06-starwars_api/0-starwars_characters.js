#!/usr/bin/node
// Get characters frim star wars api
const args = process.argv[2];

async function getRequest () {
  const response = await fetch('https://swapi-api.alx-tools.com/api/films/');
  let j = 0;
  const result = await response.json();
  if (!result || !Array.isArray(result.results)) {
    console.error('No results found');
    return;
  }
  for (const movie of result.results) {
    j += 1;
    const q = String(j);
    if (q === args) {
      for (const url of movie.characters) {
        const newCheck = await fetch(url);
        const fetchJson = await newCheck.json();
        console.log(fetchJson.name);
      }
    }
  }
}

getRequest();
