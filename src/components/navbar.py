import flet as ft


def Navbar(page: ft.Page):

    return ft.Container(

        bgcolor="#F8423F",

        padding=10,

        content=ft.Row(

            [

                ft.TextButton(
                    "🏠 Inicio",
                    on_click=lambda _: page.go("/dashboard")
                ),

                ft.TextButton(
                    "🌈 Emociones",
                    on_click=lambda _: page.go("/emociones")
                ),

                ft.TextButton(
                    "⚡ Pokémon",
                    on_click=lambda _: page.go("/pokemon")
                ),

                ft.TextButton(
                    "👤 Perfil",
                    on_click=lambda _: page.go("/perfil")
                )

            ],

            alignment=ft.MainAxisAlignment.SPACE_AROUND

        )

    )