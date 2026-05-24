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