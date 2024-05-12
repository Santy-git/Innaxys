import threading
import flet as ft




def main(page: ft.Page):

    cg = ft.RadioGroup(
        content=ft.Column(
            [
                ft.Radio(value="red", label="Red"),
                ft.Radio(value="green", label="Green"),
                ft.Radio(value="blue", label="Blue"),
            ]
        )
    )

    page.add(cg)

ft.app(main)