import flet as ft

from components.navbar import Navbar

from services.pokemonService import PokemonService


def PokemonView(page: ft.Page, controller):


    try:

        pokemon_name = page.session.pokemon

    except:

        pokemon_name = "pikachu"


    pokemon = PokemonService.obtener_pokemon(
        pokemon_name
    )



    return ft.View(

        route="/pokemon",

        scroll=ft.ScrollMode.AUTO,

        appbar=ft.AppBar(

            title=ft.Text("Pokémon"),

            bgcolor="#CAA1F8"

        ),

        controls=[

            Navbar(page),

            ft.Container(

                padding=20,

                content=ft.Column(

                    [

                        ft.Text(
                            "⚡ Pokémon asignado",
                            size=30,
                            weight="bold"
                        ),

                        ft.Image(
                            src=pokemon["imagen"],
                            width=220,
                            height=220
                        ),

                        ft.Text(
                            pokemon["nombre"].capitalize(),
                            size=28,
                            weight="bold"
                        ),

                        ft.Text(
                            f"Tipo: {pokemon['tipo']}",
                            size=20
                        ),

                        ft.Text(
                            f"Altura: {pokemon['altura']}",
                            size=18
                        ),

                        ft.Text(
                            f"Peso: {pokemon['peso']}",
                            size=18
                        )

                    ],

                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                    spacing=20

                )

            )

        ]

    )