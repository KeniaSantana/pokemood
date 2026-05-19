import flet as ft

from controllers.authController import AuthController

from views.loginView import LoginView
from views.dashboardView import DashboardView
from views.registerView import RegisterView
from views.recoveryView import RecoveryView


def start(page: ft.Page):

    page.title = "Sistema de inicio de sesión"

    page.window_width = 450
    page.window_height = 700

    page.theme_mode = ft.ThemeMode.DARK

    auth_ctrl = AuthController()

    def route_change(e):

        page.views.clear()

        if page.route == "/":

            page.views.append(
                LoginView(
                    page,
                    auth_ctrl
                )
            )


        elif page.route == "/dashboard":

            page.views.append(
                DashboardView(
                    page,
                    auth_ctrl
                )
            )

        elif page.route == "/registrarse":

            page.views.append(
                RegisterView(
                    page,
                    auth_ctrl
                )
            )

        elif page.route == "/recuperar":

            page.views.append(
                RecoveryView(
                    page,
                    auth_ctrl
                )
            )
        else:

            page.views.append(

                ft.View(

                    route="/error",

                    vertical_alignment=ft.MainAxisAlignment.CENTER,

                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                    controls=[

                        ft.Text(
                            "Ruta no encontrada",
                            size=25,
                            color="white"
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

    print("Iniciando navegacion....")
    if page.route=="/":
        route_change(None)
    else:
        page.go("/")


def main():

    ft.app(target=start)


if __name__ == "__main__":

    main()