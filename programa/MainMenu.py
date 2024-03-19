# Tenemos 3 tipos de usuarios al ingresar

# Super user
# Empleado

a = [1,2,3,4,5]

s = a[1]
# Nivel de acceso 
# Empleado nivel 5, Tiene x menues

# Asignar tipo de usuario TODO

# _________________________________________LIBRERIAS_________________________________________
import flet as f
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent
# _________________________________________LIBRERIAS_________________________________________

# _________________________________________FLET_________________________________________


# _________________________________________VentanaPrincipal_________________________________________


def main(page:f.Page) -> None:
    page.title="INNAXYS"
    page.theme_mode = f.ThemeMode.DARK
    page.window_full_screen
    page.window_resizable = False
    

    rail = f.NavigationRail(
        selected_index=0,
        label_type=f.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        leading=f.FloatingActionButton(icon=f.icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            f.NavigationRailDestination(
                icon=f.icons.FAVORITE_BORDER, selected_icon=f.icons.FAVORITE, label="First"
            ),
            f.NavigationRailDestination(
                icon_content=f.Icon(f.icons.BOOKMARK_BORDER),
                selected_icon_content=f.Icon(f.icons.BOOKMARK),
                label="Second",
            ),
            f.NavigationRailDestination(
                icon=f.icons.SETTINGS_OUTLINED,
                selected_icon_content=f.Icon(f.icons.SETTINGS),
                label_content=f.Text("Settings"),
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )
    page.add(f.Row(
            [
                rail,
                f.VerticalDivider(width=1),
                f.Column([ f.Text("Body!")], alignment=f.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
    )
# _________________________________________VentanaPrincipal_________________________________________

    # RailMenu = f.NavigationBar(
    #     selected_index=0,
    #     label_type=f.NavigationRailLabelType.ALL,
    #     min_widht=100,
    #     min_extended_width=400,
    #     destinations=[
    #         f.NavigationRailDestination(
    #             icon=f.icons.FAVORITE_BORDER, selected_icon=f.icons.FAVORITE, label="First"
    #         )
    #     ]
    #     on_change=lambda e: print("Selected destination", e.control.selected_index),

    # )

f.app(target=main)
# _________________________________________FLET_________________________________________
