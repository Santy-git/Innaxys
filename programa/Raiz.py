colores=[
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

import flet as ft

def main(raiz: ft.Page):
    raiz.window_prevent_close = True 
    def OFF(e):    
        raiz.window_destroy()
          
    raiz.window_height = 700
    raiz.window_width = 1000
    raiz.window_bgcolor = colores2[0]
    raiz.bgcolor = ft.colors.TRANSPARENT
    raiz.window_title_bar_hidden = True
    raiz.window_frameless = True
    raiz.window_resizable = False

    raiz.appbar = ft.AppBar(
        title=ft.Text("Axys"),
        center_title=True,
        bgcolor=colores2[8],
        actions=[
            ft.IconButton(ft.icons.EXIT_TO_APP_ROUNDED, on_click=OFF),
        ],
    )
    raiz.add()
    

ft.app(target=main)

