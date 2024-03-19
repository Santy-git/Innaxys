# ____________________________________________LIBRERIAS____________________________________________

from crearBase import creardb as db
import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent

# ____________________________________________LIBRERIAS____________________________________________

# ____________________________________________PALETA_DE_COLORES____________________________________________

colores = [
    '#f3f6f4',
    '#e1eae1',
    '#c5d5c6',
    '#9db8a0',
    '#729577',
    '#557c5c',
    '#3d5e44',
    '#314b37',
    '#293c2e',
    '#223226',
    '#121c14'
]
colores2 = [
    '#f2f7f4',
    '#dfece3',
    '#c0dacb',
    '#96bfaa',
    '#699e84',
    '#4b866b',
    '#356651',
    '#2b5141',
    '#244135',
    '#1e362d',
    '#101e19']

# ____________________________________________PALETA_DE_COLORES____________________________________________


# ____________________________________________Lista auxiliar_____________________
tetas = []

db()


# ________________________________________Comienzo de codigo _______________________________
def main(raiz: ft.Page):
    # seteo de la pagina
    raiz.window_prevent_close = True
    raiz.window_height = 700
    raiz.window_width = 500
    raiz.window_bgcolor = colores2[0]
    raiz.bgcolor = ft.colors.TRANSPARENT
    raiz.window_title_bar_hidden = True
    raiz.window_frameless = True
    raiz.window_resizable = False
    raiz.padding = 10
    # -------------------------------------
    #

    def logear(e):
        tetas.append(User.value)
        tetas.append(Password.value)
        print(tetas)

    # Appbar
    # Elementos
    nombre = ft.Container(content=Text(
        "Axys", color=colores[9],), bgcolor="BLACK", width=200, height=40, border_radius=ft.border_radius.all(10))
    nombre.alignment = ft.alignment.center
    # ------------------------
    raiz.appbar = ft.AppBar(
        title=nombre,
        center_title=True,
        bgcolor=colores2[8],
        actions=[
            ft.CupertinoSwitch(active_color=colores[1], track_color=colores[9],
                               value=True),
            ft.IconButton(ft.icons.EXIT_TO_APP_ROUNDED,
                          on_click=OFF, icon_size=35),
        ],
    )
    # ------------------------

    # LOGIN
    # def
    def validate(e: ControlEvent) -> None:
        if all([User.value, Password.value]):
            Button.disabled = False
        else:
            Button.disabled = True

        raiz.update()

    def sudmit(e: ControlEvent) -> None:

        raiz.clean()
        raiz.add(
            Row(
                controls=[Text(value=f'Welcome: {User.value}', size=20)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
    User.on_change = validate
    Password.on_change = validate
    Button.on_change = sudmit
    # -------
    # elementos
    User: TextField = TextField(
        label="User", text_align=ft.TextAlign.LEFT, width=200)
    Password: TextField = TextField(
        label="Password", text_align=ft.TextAlign.LEFT, width=200, password=True, can_reveal_password=True)
    Button: ElevatedButton = ElevatedButton(text="Sign Up", on_click=logear)

    Filas_login = Row(
        controls=[
            Column(
                [
                    User,
                    Password,
                    Button]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    contenedor_login = ft.Container(content=Filas_login, height=623, width=500, bgcolor="BLACK",
                                    border_radius=ft.border_radius.all(10), padding=ft.padding.only(top=70))

    raiz.add(contenedor_login)
    # ----------------------


ft.app(target=main)
