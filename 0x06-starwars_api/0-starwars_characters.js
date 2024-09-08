#!/usr/bin/
const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

async function fetchFilm (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Status: ${response.statusCode}`));
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

async function fetchCharacter (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Status: ${response.statusCode}`));
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

async function main () {
  try {
    const film = await fetchFilm(url);
    const characters = film.characters;
    console.log(characters);

    const characterData = await Promise.all(characters.map(fetchCharacter));

    characterData.forEach((character) => {
      console.log(character.name);
    });
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
