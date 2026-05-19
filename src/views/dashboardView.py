import flet as ft


def DashboardView(page: ft.Page):

    return ft.View(

        route="/dashboard",

        vertical_alignment=ft.MainAxisAlignment.CENTER,

        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        appbar=ft.AppBar(
            title=ft.Text("Dashboard"),
            bgcolor="#A0E7E5"
        ),

        controls=[

            ft.Text(
                "Bienvenido al Dashboard",
                size=30,
                weight="bold"
            ),

            ft.ElevatedButton(
                "Cerrar sesión",
                on_click=lambda _: page.go("/")
            )

        ]
    )