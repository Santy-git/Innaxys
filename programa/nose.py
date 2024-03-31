"""
import flet as ft

def main(page: ft.Page):
    def valor(z):
        pera = ft.TextField(value=z,width=10)
        a = ft.Container(content=ft.Row([pera,ft.TextButton(text="+",on_click=lambda _:print(pera.value))]))
        return a
    images = ft.GridView(
        height=400,
        width=800,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )
    for i in range(0,60):
        images.controls.append(valor(i))
    page.add(images)
ft.app(target=main)


"""
from datetime import datetime

fecha_res = datetime.now().date()
print(fecha_res)