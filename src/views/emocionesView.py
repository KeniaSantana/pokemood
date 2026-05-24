import flet as ft
from components.navbar import Navbar


def EmocionesView(page: ft.Page, controller):

    emociones = [

        "😊 Feliz",
        "😡 Enojado",
        "🥺 Triste",
        "😴 Cansado",
        "😎 Motivado"

    ]

    return ft.View(

        route="/emociones",

        appbar=ft.AppBar(
            title=ft.Text("🌈 Emociones"),
            bgcolor="#CAA1F8"
        ),

        controls=[

            Navbar(page),

            ft.Container(

                padding=20,

                content=ft.Column(

                    [

                        ft.Text(
                            "¿Cómo te sientes hoy?",
                            size=28,
                            weight="bold"
                        ),

                        *[
                            ft.ElevatedButton(
                                emocion
                            )

                            for emocion in emociones
                        ]

                    ]

                )
            )
        ]
    )