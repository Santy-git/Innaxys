import threading
import flet as ft




def main(page: ft.Page):

    cl = ft.Column(
        spacing=10,
        height=200,
        width=200,
        scroll=ft.ScrollMode.ALWAYS,
        on_scroll_interval=0,
    )
    for i in range(0, 50):
        cl.controls.append(ft.Container(width=100,height=100,bgcolor='red'))

    page.add(ft.Container(cl, border=ft.border.all(1)))

ft.app(main)