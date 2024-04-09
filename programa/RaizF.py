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
class program(ft.UserControl):
    def __init__(self):
        pass

def raiz(page: ft.Page):
    raiz.window_prevent_close = True
    raiz.window_height = 700
    raiz.window_width = 500
    raiz.window_bgcolor = colores2[0]
    raiz.bgcolor = ft.colors.TRANSPARENT
    raiz.window_frameless = True
    raiz.window_resizable = False
    raiz.padding = 10
    raiz.window_full_screen = True
    Plantilla = program()

    # add application's root control to the page
    raiz.add(Plantilla)


ft.app(target=raiz)