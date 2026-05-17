import flet as ft

def DashboardView(page: ft.Page, controller):

    user = page.session.get("user")

    if not user:

        page.go("/")
        return ft.View("/")

    nombre_usuario = user.get("nombre", "Usuario")

    def cerrar_sesion(e):

        page.session.remove("user")

        page.snack_bar = ft.SnackBar(
            ft.Text(" Sesión cerrada")
        )

        page.snack_bar.open = True

        page.go("/")

        page.update()

    return ft.View(

        route="/dashboard",

        appbar=ft.AppBar(
            title=ft.Text("POKEMOOD - Dashboard"),
            bgcolor="#CAA1F8",
            color="black",
            actions=[
                ft.IconButton(
                    icon=ft.Icons.LOGOUT,
                    tooltip="Cerrar sesión",
                    on_click=cerrar_sesion
                )
            ]
        ),

        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        controls=[

            ft.Container(
                content=ft.Column(

                    [

                        ft.Text(
                            f"Bienvenido {nombre_usuario}",
                            size=28,
                            weight="bold"
                        ),

                        ft.Text(
                            "Inicio de sesión exitoso",
                            size=18
                        ),

                        ft.Divider(),

                        ft.Card(
                            content=ft.Container(
                                content=ft.Column(
                                    [

                                        ft.Text(
                                            "📧 Correo:",
                                            weight="bold"
                                        ),

                                        ft.Text(
                                            user.get("correo", "")
                                        ),

                                        ft.Text(
                                            "📱 Teléfono:",
                                            weight="bold"
                                        ),

                                        ft.Text(
                                            user.get("telefono", "")
                                        )

                                    ],
                                    spacing=10
                                ),
                                padding=20
                            )
                        )

                    ],

                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20
                ),

                padding=30
            )
        ]
    )