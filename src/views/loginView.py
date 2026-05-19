import flet as ft


def LoginView(page: ft.Page, controller):

    correo_input = ft.TextField(
        label="Correo Electrónico",
        width=350
    )

    password_input = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=350
    )

    def mostrar_mensaje(texto):

        page.snack_bar = ft.SnackBar(
            ft.Text(texto)
        )

        page.snack_bar.open = True

        page.update()

    def login_click(e):

        if (
            not correo_input.value or
            not password_input.value
        ):

            mostrar_mensaje(
                "Llena todos los campos"
            )

            return

        user, msg = controller.login(

            correo_input.value,
            password_input.value

        )

        if user:

            mostrar_mensaje(
                "Inicio correcto"
            )

            page.go("/dashboard")

        else:

            mostrar_mensaje(msg)

    return ft.View(

        route="/",

        vertical_alignment=ft.MainAxisAlignment.CENTER,

        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        appbar=ft.AppBar(
            title=ft.Text("POKEMOOD Login"),
            bgcolor="#CAA1F8"
        ),

        controls=[

            ft.Column(

                [

                    ft.Text(
                        "Iniciar Sesión",
                        size=28,
                        weight="bold"
                    ),

                    correo_input,

                    password_input,

                    ft.ElevatedButton(
                        "Iniciar sesión",
                        on_click=login_click,
                        width=350,
                        bgcolor="#FC4848",
                        color="white"
                    ),

                    ft.ElevatedButton(
                        "Crear cuenta",
                        on_click=lambda _: page.go("/registrarse"),
                        width=350
                    ),

                    ft.TextButton(
                        "¿Olvidaste tu contraseña?",
                        on_click=lambda _: page.go("/recuperar")
                    )

                ],

                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        ]
    )