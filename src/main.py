import flet as ft
from controllers.authController import AuthController
from views.loginView import LoginView
from views.registerView import RegisterView
from views.dashboardView import DashboardView


def main(page: ft.Page):
    page.title = "Pokemood"
    page.window_width = 450
    page.window_height = 700
    page.window_resizable = False

    # Inicializar controladores
    auth_ctrl = AuthController()

    def route_change(e):
        page.views.clear()

        if page.route == "/":
            page.views.append(
                LoginView(page, auth_ctrl)
            )

        elif page.route == "/dashboard":
            page.views.append(
                DashboardView(page, auth_ctrl)
            )

        elif page.route == "/registrarse":
            page.views.append(
                RegisterView(page, auth_ctrl)
            )

        else:
            page.views.append(
                ft.View(
                    route="/",
                    controls=[
                        ft.Text("Ruta no encontrada", size=30),
                        ft.ElevatedButton(
                            "Volver al inicio",
                            on_click=lambda _: page.go("/")
                        )
                    ]
                )
            )

        page.update()

    def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Iniciar navegación
    print("Iniciando navegación....")
    page.go("/")


if __name__ == "__main__":
    ft.app(target=main)