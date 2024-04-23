import datetime
import flet as ft

def main(page: ft.Page):

    def change_date(e):
        x = date_picker.value
        print(x)

    def date_picker_dismissed(e):
        print(date_picker.value)

    date_picker = ft.DatePicker(
        on_change=change_date,
        on_dismiss=date_picker_dismissed,
    )

    page.overlay.append(date_picker)

    date_button = ft.ElevatedButton(
        "Pick date",
        icon=ft.icons.CALENDAR_MONTH,
        on_click=lambda _: date_picker.pick_date(),
    )

    page.add(date_button)

ft.app(target=main)