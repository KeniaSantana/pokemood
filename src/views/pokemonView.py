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
    pokemones = PokemonService.obtener_todos()
    pokemones = sorted(
        pokemones,
        key=lambda p: p["nombre"] != pokemon_name
    )

    return ft.View(
        route="/pokemon",
        scroll=ft.ScrollMode.AUTO,
        appbar=ft.AppBar(
            title=ft.Text("Pokémon"),
            bgcolor="#DB2626"
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
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ),

            ft.Divider(),

            ft.Text(
                "Todos los Pokémon",
                size=24,
                weight="bold"
            ),

            ft.ResponsiveRow(
                controls=[
                    ft.Container(
                        col={"sm": 6, "md": 4, "lg": 3},
                        padding=10,
                        border_radius=10,
                        bgcolor="#000000",

                        content=ft.Column(
                            [
                                ft.Image(
                                    src=p["imagen"],
                                    width=120,
                                    height=120
                                ),

                                ft.Text(
                                    p["nombre"].capitalize(),
                                    size=18,
                                    weight="bold"
                                ),

                                ft.Text(
                                    f"Tipo: {p['tipo']}"
                                )
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        )
                    )

                    for p in pokemones
                ]
            )
        ]
    )