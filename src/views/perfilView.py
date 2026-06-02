import flet as ft

from components.navbar import Navbar


def PerfilView(page: ft.Page, controller):


    try:

        user = page.client_storage.get("user")

    except:

        user = None

    if not user:

        user = {}



    nombre = user.get("nombre", "Sin nombre")

    apellido = user.get("apellido", "")

    correo = user.get("correo", "Sin correo")

    telefono = user.get("telefono", "Sin teléfono")


    return ft.View(

        route="/perfil",

        scroll=ft.ScrollMode.AUTO,

        appbar=ft.AppBar(

            title=ft.Text("Perfil"),

            bgcolor="#DB2626"

        ),

        controls=[

            Navbar(page),

            ft.Container(

                padding=20,

                content=ft.Column(

                    [

                        ft.Text(
                            "👤 Perfil del usuario",
                            size=30,
                            weight="bold"
                        ),

                        ft.Divider(),

                        ft.Text(
                            f"Nombre: {nombre} {apellido}",
                            size=20
                        ),

                        ft.Text(
                            f"Correo: {correo}",
                            size=20
                        ),

                        ft.Text(
                            f"Teléfono: {telefono}",
                            size=20
                        ),

                        ft.Divider(),

                        ft.ElevatedButton(
                            "Cerrar sesión",
                            bgcolor="#FC4848",
                            color="white",
                            on_click=lambda _: page.go("/")
                        )

                    ],

                    spacing=15

                )

            )

        ]

    )