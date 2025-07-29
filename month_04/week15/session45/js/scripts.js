console.log("Pokemon API");

const POKEMON_URL = "https://pokeapi.co/api/v2/pokemon";
const mainElements = document.getElementsByTagName("main");
console.log(mainElements);
fetch(POKEMON_URL)
  .then((response) => response.json())
  .then((data) => {
    const pokemons = data.results;
    const mainElement = mainElements[0];
    const ulElement = document.createElement("ul");

    for (let i = 0; i < pokemons.length; i++) {
      const pokemonDetailContainer = document.createElement("div");
      pokemonDetailContainer.classList.add("pokemon-detail-container");

      const liElement = document.createElement("li");
      liElement.textContent = pokemons[i].name;

      const POKEMON_DETAIL_URL = pokemons[i].url;

      pokemonDetailContainer.appendChild(liElement);
      ulElement.appendChild(pokemonDetailContainer);

      fetch(POKEMON_DETAIL_URL)
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          const pokemonImageUrl =
            data.sprites.other["official-artwork"].front_default;
          console.log(pokemonImageUrl);
          const imgElement = document.createElement("img");
          imgElement.src = pokemonImageUrl;
          pokemonDetailContainer.appendChild(imgElement);
        })
        .catch((error) => {
          console.error(error);
        });
    }
    mainElement.appendChild(ulElement);
  })
  .catch((error) => {
    console.error(error);
  });
