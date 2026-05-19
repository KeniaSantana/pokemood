import flet as ft


def RegisterView(page: ft.Page, controller):

    nombre_input = ft.TextField(
        label="Nombre",
        width=350
    )

    apellido_input = ft.TextField(
        label="Apellido",
        width=350
    )

    correo_input = ft.TextField(
        label="Correo",
        width=350
    )

    telefono_input = ft.TextField(
        label="Teléfono",
        width=350
    )

    password_input = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=350
    )

    confirmar_input = ft.TextField(
        label="Confirmar contraseña",
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

    def registrar_click(e):

        if (

            not nombre_input.value or
            not apellido_input.value or
            not correo_input.value or
            not telefono_input.value or
            not password_input.value or
            not confirmar_input.value

        ):

            mostrar_mensaje(
                "Completa todos los campos"
            )

            return

        if password_input.value != confirmar_input.value:

            mostrar_mensaje(
                "Las contraseñas no coinciden"
            )

            return

        success, msg = controller.registrar_usuario(

            nombre_input.value,
            apellido_input.value,
            correo_input.value,
            password_input.value,
            telefono_input.value

        )

        mostrar_mensaje(msg)

        if success:

            page.go("/")

    return ft.View(

        route="/registrarse",

        vertical_alignment=ft.MainAxisAlignment.CENTER,

        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        appbar=ft.AppBar(
            title=ft.Text("Registro"),
            bgcolor="#FF6666"
        ),

        controls=[

            ft.Column(

                [

                    ft.Text(
                        "Crear Cuenta",
                        size=28,
                        weight="bold"
                    ),

                    nombre_input,
                    apellido_input,
                    correo_input,
                    telefono_input,
                    password_input,
                    confirmar_input,

                    ft.ElevatedButton(
                        "Registrarse",
                        on_click=registrar_click,
                        width=350
                    ),

                    ft.TextButton(
                        "Volver",
                        on_click=lambda _: page.go("/")
                    )

                ],

                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            )
        ]
    )