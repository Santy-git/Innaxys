
import flet as ft

def main(page: ft.Page):
    images = ft.GridView(
        height=400,
        width=400,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )
    for i in range(0,60):
        images.controls.append(ft.Container(width=100,height=100,bgcolor=ft.colors.AMBER,content= ft.Text(value=i,bgcolor=ft.colors.GREEN),alignment=ft.alignment.center))
    page.add(images)



ft.app(target=main)

