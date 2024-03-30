"""
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


"""


import flet as ft

name = "A simple DataTable"

def main(page: ft.Page):
    z = ft.Row
    page.add(ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("First name")),
                ft.DataColumn(ft.Text("Last name")),
                ft.DataColumn(ft.Text("Age"), numeric=True),
            ],
            z
        )
    )
    for i in range(0,30):
        rows.
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text("John")),
                ft.DataCell(ft.Text("Smith")),
                ft.DataCell(ft.Text("43")),
            ],
        )
ft.app(target=main)