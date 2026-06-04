import requests


class PokemonService:

    @staticmethod
    def obtener_pokemon(nombre):
        url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return {
                "nombre": data["name"],
                "imagen": data["sprites"]["front_default"],
                "tipo": data["types"][0]["type"]["name"],
                "altura": data["height"],
                "peso": data["weight"]
            }
        return None

    @staticmethod
    def obtener_todos():
        """
        Devuelve una lista de diccionarios con los Pokémon.
        Cada diccionario contiene: nombre, imagen, tipo, altura y peso.
        """
        url = "https://pokeapi.co/api/v2/pokemon?limit=100"  
        response = requests.get(url)

        if response.status_code != 200:
            return []

        data = response.json()
        pokemones = []

        for p in data["results"]:
            pokemon = PokemonService.obtener_pokemon(p["name"])
            if pokemon:
                pokemones.append(pokemon)

        return pokemones