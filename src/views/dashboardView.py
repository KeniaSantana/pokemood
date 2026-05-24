import flet as ft

from components.navbar import Navbar


def DashboardView(page: ft.Page, controller):


    try:

        user = page.session.user

    except:

        user = None

    nombre = "Usuario"

    if user:

        nombre = user.get("nombre", "Usuario")


    return ft.View(

        route="/dashboard",

        scroll=ft.ScrollMode.AUTO,

        appbar=ft.AppBar(

            title=ft.Text("POKEMOOD"),

            bgcolor="#CAA1F8",

            actions=[

                ft.IconButton(
                    icon=ft.Icons.LOGOUT,
                    tooltip="Cerrar sesión",
                    on_click=lambda _: page.go("/")
                )

            ]

        ),

        controls=[

            Navbar(page),

            ft.Container(

                padding=20,

                content=ft.Column(

                    [


                        ft.Text(
                            f"✨ Bienvenida {nombre}",
                            size=30,
                            weight="bold"
                        ),

                        ft.Text(
                            "¿Cómo te sientes hoy?",
                            size=18
                        ),

                        ft.Divider(),


                        ft.ResponsiveRow(

                            [

                                ft.ElevatedButton(

                                    "😊 Feliz",

                                    width=180,

                                    bgcolor="#FFD966",

                                    on_click=lambda _: (
                                        setattr(
                                            page.session,
                                            "pokemon",
                                            "pikachu"
                                        ),
                                        page.go("/pokemon")
                                    )

                                ),

                                ft.ElevatedButton(

                                    "😴 Cansado",

                                    width=180,

                                    bgcolor="#A4C2F4",

                                    on_click=lambda _: (
                                        setattr(
                                            page.session,
                                            "pokemon",
                                            "snorlax"
                                        ),
                                        page.go("/pokemon")
                                    )

                                ),

                                ft.ElevatedButton(

                                    "😡 Enojado",

                                    width=180,

                                    bgcolor="#EA9999",

                                    on_click=lambda _: (
                                        setattr(
                                            page.session,
                                            "pokemon",
                                            "lucario"
                                        ),
                                        page.go("/pokemon")
                                    )

                                ),

                                ft.ElevatedButton(

                                    "🥺 Triste",

                                    width=180,

                                    bgcolor="#B4A7D6",

                                    on_click=lambda _: (
                                        setattr(
                                            page.session,
                                            "pokemon",
                                            "cubone"
                                        ),
                                        page.go("/pokemon")
                                    )

                                )

                            ]

                        ),

                        ft.Divider(),


                        ft.Text(
                            "⭐ Recomendación del día",
                            size=22,
                            weight="bold"
                        ),

                        ft.Card(

                            content=ft.Container(

                                padding=20,

                                content=ft.Column(

                                    [

                                        ft.Text(
                                            "⚡ Pikachu",
                                            size=25,
                                            weight="bold"
                                        ),

                                        ft.Text(
                                            "Hoy tienes una energía positiva."
                                        ),

                                        ft.ElevatedButton(
                                            "Ver Pokémon",
                                            on_click=lambda _: page.go("/pokemon")
                                        )

                                    ],

                                    spacing=10

                                )

                            )

                        ),

                        ft.Divider(),


                        ft.Text(
                            "🚀 Accesos rápidos",
                            size=22,
                            weight="bold"
                        ),

                        ft.ResponsiveRow(

                            [

                                ft.ElevatedButton(
                                    "🌈 Emociones",
                                    width=180,
                                    on_click=lambda _: page.go("/emociones")
                                ),

                                ft.ElevatedButton(
                                    "📖 Historial",
                                    width=180,
                                    on_click=lambda _: page.go("/historial")
                                ),

                                ft.ElevatedButton(
                                    "⚡ Pokémon",
                                    width=180,
                                    on_click=lambda _: page.go("/pokemon")
                                ),

                                ft.ElevatedButton(
                                    "👤 Perfil",
                                    width=180,
                                    on_click=lambda _: page.go("/perfil")
                                )

                            ]

                        )

                    ],

                    spacing=20

                )

            )

        ]

    )