import flet as ft
from components.navbar import Navbar


def EmocionesView(page: ft.Page, controller):

    emociones = [
        ("😊 Feliz", "pikachu"),
        ("😎 Motivado", "lucario"),
        ("😡 Enojado", "primeape"),
        ("🤬 Furioso", "gyarados"),
        ("🥺 Triste", "cubone"),
        ("😣 Frustrado", "psyduck"),
        ("😴 Cansado", "snorlax"),
        ("🤔 Pensativo", "alakazam"),
        ("😱 Asustado", "gastly"),
        ("💪 Con energía", "machamp"),
        ("🥰 Enamorado", "sylveon"),
        ("🎉 Emocionado", "jigglypuff"),
        ("🔥 Inspirado", "charizard"),
        ("🌊 Relajado", "lapras"),
        ("⚡ Impaciente", "jolteon"),
        ("🌙 Melancólico", "umbreon"),
    ]


    def seleccionar_pokemon(nombre_pokemon):

        if not hasattr(page, "session_data"):
            page.session_data = {}
        page.session_data["pokemon"] = nombre_pokemon
        page.go("/pokemon")

    return ft.View(
        route="/emociones",
        appbar=ft.AppBar(
            title=ft.Text("🌈 Emociones"),
            bgcolor="#DB2626",
        ),
        controls=[
            Navbar(page),

            ft.Container(
                padding=20,
                content=ft.Column(
                    controls=[
                        ft.Text(
                            "¿Cómo te sientes hoy?",
                            size=28,
                            weight=ft.FontWeight.BOLD,
                        ),

                        *[
                            ft.ElevatedButton(
                                emocion,
                                width=250,
                                on_click=lambda e, p=pokemon: seleccionar_pokemon(p)
                            )
                            for emocion, pokemon in emociones
                        ]
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10,
                ),
            ),
        ],
    )