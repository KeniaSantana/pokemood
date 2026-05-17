import flet as ft


def RegisterView(page: ft.Page, controller):

    nombre_input = ft.TextField(
        label="Nombre",
        width=350,
        border_radius=10
    )

    apellido_input = ft.TextField(
        label="Apellido",
        width=350,
        border_radius=10
    )

    correo_input = ft.TextField(
        label="Correo Electrónico",
        width=350,
        border_radius=10
    )

    telefono_input = ft.TextField(
        label="Teléfono",
        width=350,
        border_radius=10,
        keyboard_type=ft.KeyboardType.NUMBER
    )

    password_input = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=350,
        border_radius=10
    )

    confirmar_password_input = ft.TextField(
        label="Confirmar Contraseña",
        password=True,
        can_reveal_password=True,
        width=350,
        border_radius=10
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
            not confirmar_password_input.value
        ):

            mostrar_mensaje("Completa todos los campos")
            return

        if password_input.value != confirmar_password_input.value:

            mostrar_mensaje("Las contraseñas no coinciden")
            return

        try:

            success, msg = controller.registrar_usuario(
                nombre_input.value,
                apellido_input.value,
                correo_input.value,
                password_input.value,
                telefono_input.value
            )

            if success:

                mostrar_mensaje(msg)

                page.go("/")

            else:

                mostrar_mensaje(msg)

        except Exception as ex:

            print("ERROR REGISTRO:", ex)

            mostrar_mensaje(f"Error: {ex}")

    registrar_button = ft.ElevatedButton(
        "Registrarse",
        on_click=registrar_click,
        width=350,
        bgcolor="#F7ADC4",
        color="black"
    )

    volver_button = ft.TextButton(
        "Volver al login",
        on_click=lambda _: page.go("/")
    )

    return ft.View(

        route="/registrarse",

        vertical_alignment=ft.MainAxisAlignment.CENTER,

        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        appbar=ft.AppBar(
            title=ft.Text("POKEMOOD - Registro"),
            bgcolor="#CAA1F8",
            color="black"
        ),

        controls=[

            ft.Column(

                [

                    ft.Text(
                        "Crear Cuenta",
                        size=24,
                        weight="bold"
                    ),

                    nombre_input,

                    apellido_input,

                    correo_input,

                    telefono_input,

                    password_input,

                    confirmar_password_input,

                    registrar_button,

                    volver_button

                ],

                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            )
        ]
    )