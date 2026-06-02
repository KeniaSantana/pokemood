import flet as ft
from components.navbar import Navbar


def HistorialView(page: ft.Page, controller):

    return ft.View(

        route="/historial",

        appbar=ft.AppBar(
            title=ft.Text("📖 Historial"),
            bgcolor="#DB2626"
        ),

        controls=[

            Navbar(page),

            ft.Container(

                padding=20,

                content=ft.Column(

                    [

                        ft.Text(
                            "Historial emocional",
                            size=28,
                            weight="bold"
                        ),

                        ft.Text(
                            "Aquí aparecerá el historial."
                        )

                    ]

                )
            )
        ]
    )