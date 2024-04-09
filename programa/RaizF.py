#....................Librerias....................
from crearBase import * 
import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent
from datetime import datetime
from functools import partial
import time
#.................................................

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
#....................................

class Plantilla:
    def __init__(self,raiz):
        self.raiz = raiz
    def ej(self):
        self.raiz.bgcolor = ft.colors.AMBER
        self.raiz.update()

    def OFF(self,e):    
        global cual    
        self.raiz.window_destroy()
        cual = 2

    def EnEs(self,e):
        global cual
        self.raiz.window_destroy()
        cual = 1

    def logear(self,e):
        global Nivel
        global z
        z =  login(self.User.value,self.Password.value)
        print("pera",z)
        try:
            if z[0]:
                Nivel = int(z[1])

        except TypeError: 
            dlg = ft.AlertDialog(
            title=ft.Text("Usuario Incorrecto"), on_dismiss=lambda e: print("Dialog dismissed!")
            )
            def open_dlg(e):
                self.raiz.dialog = dlg
                dlg.open = True
                self.raiz.update()
            open_dlg(e)

    def appbar(self):
        nombre = ft.Container(content=Text(
            "Axys", color=colores[9],), bgcolor=colores[3], width=200, height=40, border_radius=ft.border_radius.all(10))
        nombre.alignment = ft.alignment.center

        self.raiz.appbar = ft.AppBar(
            title=nombre,
            center_title=True,
            bgcolor=colores2[8],
            actions=[
                ft.IconButton(ft.icons.LANGUAGE,on_click=self.EnEs,icon_size=35,bgcolor=ft.colors.RED),
                ft.IconButton(ft.icons.EXIT_TO_APP_ROUNDED,on_click=self.OFF, icon_size=35,),
            ]

        )
        self.raiz.update()

    def login(self):
        self.User: TextField = TextField(label="User", text_align=ft.TextAlign.LEFT, width= 200)
        self.Password: TextField = TextField(label="Password", text_align=ft.TextAlign.LEFT, width= 200, password = True, can_reveal_password=True)
        Button: ElevatedButton = ElevatedButton(text="Sign Up")
        
        Filas_login = Row(
            controls=[
                Column(
                    [
                        self.User,
                        self.Password,
                        Button]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        contenedor_login = ft.Container(content=Filas_login, 
                height=623, width=500, bgcolor=colores[3], 
                border_radius=ft.border_radius.all(10), 
                padding=ft.padding.only(top=70),
                )
        self.raiz.add(contenedor_login)



def main(raiz: ft.Page):
    raiz.window_prevent_close = True 
    raiz.bgcolor = ft.colors.BLUE_GREY_100
    raiz.window_frameless = True
    raiz.window_resizable = False
    raiz.window_full_screen = True
    raiz.update()
    objeto = Plantilla(raiz)
    objeto.ej()
    z = objeto.appbar()
    print(z)
    objeto.login()


ft.app(target=main)