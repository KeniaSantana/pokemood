import flet as ft
from views.loginView import login_view


def main(page: ft.Page):
    page.title = "Pokemood"
    page.window_width = 400
    page.window_height = 500

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        login_view(page)
    )


ft.app(target=main)