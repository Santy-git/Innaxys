import threading
import flet as ft




def main(page: ft.Page):

    cl = ft.Column(
        spacing=10,
        height=200,
        width=500,
        scroll=ft.ScrollMode.ALWAYS,
        on_scroll_interval=0,
    )
    for i in range(0, 1000):
        cl.controls.append(ft.Container(width=100,height=100,bgcolor='red',content=ft.Text(value=i)))

    page.add(ft.Container(cl, border=ft.border.all(1)))

ft.app(main)