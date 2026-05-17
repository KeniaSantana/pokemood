import flet as ft


def LoginView(page: ft.Page, controller):

    correo_input = ft.TextField(
        label="Correo Electrónico",
        width=350,
        border_radius=10
    )

    password_input = ft.TextField(
        label="Contraseña",
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

    def login_click(e):

        if not correo_input.value or not password_input.value:

            mostrar_mensaje("Llena todos los campos")
            return

        correo = correo_input.value
        password = password_input.value

        try:

            user, msg = controller.login(
                correo,
                password
            )

            if user:

                page.session.set("user", user)

                mostrar_mensaje(" Inicio correcto")

                page.go("/dashboard")

            else:

                mostrar_mensaje(msg)

        except Exception as ex:

            print("ERROR LOGIN:", ex)

            mostrar_mensaje(f" Error: {ex}")

    login_button = ft.ElevatedButton(
        "Iniciar sesión",
        on_click=login_click,
        width=350,
        bgcolor="#F7ADC4",
        color="black"
    )

    registrar_button = ft.ElevatedButton(
        "Crear una nueva cuenta",
        bgcolor="#F7ADC4",
        color="black",
        width=350,
        on_click=lambda _: page.go("/registrarse")
    )

    password_input.on_submit = login_click

    return ft.View(

        route="/",

        vertical_alignment=ft.MainAxisAlignment.CENTER,

        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        appbar=ft.AppBar(
            title=ft.Text("POKEMOOD - Login"),
            bgcolor="#CAA1F8",
            color="black"
        ),

        controls=[

            ft.Column(

                [

                    ft.Text(
                        "Acceso al sistema",
                        size=24,
                        weight="bold"
                    ),

                    correo_input,

                    password_input,

                    login_button,

                    registrar_button,

                    ft.TextButton(
                        "¿Olvidaste la contraseña?",
                        on_click=lambda _: page.go("/recuperar")
                    )

                ],

                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        ]
    )