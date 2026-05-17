import flet as ft


def RecoveryView(page: ft.Page, controller):

    correo_input = ft.TextField(
        label="Correo Electrónico",
        width=350,
        border_radius=10
    )

    nueva_password_input = ft.TextField(
        label="Nueva Contraseña",
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

    def recuperar_click(e):

        if not correo_input.value or not nueva_password_input.value:

            mostrar_mensaje(" Completa todos los campos")
            return

        success = controller.model.recuperar_password(
            correo_input.value,
            nueva_password_input.value
        )

        if success:

            mostrar_mensaje("Contraseña actualizada")

            page.go("/")

        else:

            mostrar_mensaje(" Correo no encontrado")

    return ft.View(

        route="/recuperar",

        vertical_alignment=ft.MainAxisAlignment.CENTER,

        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        appbar=ft.AppBar(
            title=ft.Text("Recuperar Contraseña"),
            bgcolor="#CAA1F8",
            color="black"
        ),

        controls=[

            ft.Column(

                [

                    ft.Text(
                        "Recuperar Contraseña",
                        size=24,
                        weight="bold"
                    ),

                    correo_input,

                    nueva_password_input,

                    ft.ElevatedButton(
                        "Actualizar Contraseña",
                        on_click=recuperar_click,
                        width=350,
                        bgcolor="#F7ADC4",
                        color="black"
                    ),

                    ft.TextButton(
                        "Volver al login",
                        on_click=lambda _: page.go("/")
                    )

                ],

                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        ]
    )