import flet as ft

from services.email_service import enviar_correo


def RecoveryView(page: ft.Page, controller):

    correo_input = ft.TextField(
        label="Correo Electrónico",
        width=350
    )

    def mostrar_mensaje(texto):

        page.snack_bar = ft.SnackBar(
            ft.Text(texto)
        )

        page.snack_bar.open = True

        page.update()

    def recuperar_click(e):

        if not correo_input.value:

            mostrar_mensaje(
                "Ingresa tu correo"
            )

            return

        nueva_password = "123456"

        success = controller.model.recuperar_password(

            correo_input.value,
            nueva_password

        )

        if success:

            enviado = enviar_correo(

                correo_input.value,
                nueva_password

            )

            if enviado:

                mostrar_mensaje(
                    "Correo enviado"
                )

                page.go("/")

            else:

                mostrar_mensaje(
                    "No se pudo enviar el correo"
                )

        else:

            mostrar_mensaje(
                "Correo no encontrado"
            )

    return ft.View(

        route="/recuperar",

        vertical_alignment=ft.MainAxisAlignment.CENTER,

        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        appbar=ft.AppBar(
            title=ft.Text("Recuperar Contraseña"),
            bgcolor="#F03333"
        ),

        controls=[

            ft.Column(

                [

                    ft.Text(
                        "Recuperar Contraseña",
                        size=28,
                        weight="bold"
                    ),

                    correo_input,

                    ft.ElevatedButton(
                        "Enviar correo",
                        on_click=recuperar_click,
                        width=350
                    ),

                    ft.TextButton(
                        "Volver",
                        on_click=lambda _: page.go("/")
                    )

                ],

                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        ]
    )