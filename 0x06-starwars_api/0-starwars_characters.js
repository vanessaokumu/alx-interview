#!/usr/bin/node
/**
 * Script to print all characters of a Star Wars movie.
 */

const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        return;
      }

      const charData = JSON.parse(charBody);
      console.log(charData.name);
    });
  });
});
