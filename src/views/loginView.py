import flet as ft
from controllers.authController import AuthController

controller = AuthController()


def loginView(page: ft.Page):

    correo = ft.TextField(label="Correo", width=300)
    contraseña = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=300
    )

    mensaje = ft.Text("", color="red")

    def iniciar_sesion(e):
        usuario = controller.login(
            correo.value,
            contraseña.value
        )

        if usuario:
            mensaje.value = f"Bienvenido {usuario['nombre']}"
            mensaje.color = "green"
        else:
            mensaje.value = "Correo o contraseña incorrectos"
            mensaje.color = "red"

        page.update()

    btn_login = ft.ElevatedButton(
        text="Iniciar Sesión",
        on_click=iniciar_sesion
    )

    return ft.Column(
        controls=[
            ft.Text(
                "POKEMOOD",
                size=30,
                weight="bold"
            ),
            correo,
            contraseña,
            btn_login,
            mensaje
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )