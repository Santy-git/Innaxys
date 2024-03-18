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
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent
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
    raiz.padding = 50

    raiz.appbar = ft.AppBar(
        title=ft.Text("Axys"),
        center_title=True,
        bgcolor=colores2[8],
        actions=[
            ft.IconButton(ft.icons.EXIT_TO_APP_ROUNDED, on_click=OFF),
            #aca boton
        ],
    )
    raiz.add()
    login = ft.Container(
        bgcolor = colores[5],
        width=900,
        height=600,
        alignment = (0, 0))
        """content=Row(
            controls=[Column(
                    usuario = TextField(label="User", text_align=ft.TextAlign.LEFT, width= 200),
                    contraseña = TextField(label="Password", text_align=ft.TextAlign.LEFT, width= 200, password = True),
                    derechos = Checkbox(label="I agree to stuff",value = False),
                    boton = ElevatedButton(text="Sign Up"))],
        ))"""
    raiz.add(login)
    """def validate(e: ControlEvent) -> None:
        if all([Usuario.value,contraseña.value,derechos.value]):
            Button.disabled = False
        else:
            Button.disabled = True

        raiz.update()"""

    """def sudmit(e: ControlEvent) -> None:
        print("User:",usuario.value)

        raiz.clean()
        raiz.add(
            Row(
                controls=[Text(value=f'Welcome: {User.value}',size = 20)],
                alignment = f.MainAxisAlignment.CENTER
            )
        )
        
        Theme.on_change = theme
        checkbox.on_change = validate
        User.on_change = validate
        Password.on_change = validate
        Button.on_change = sudmit

        

        #Render bonito de la pagina skeree
       raiz.add(
            Row(
                controls=[
                    Column(
                        [
                        Usuario,
                        contraseña,
                        checkbox,
                        Button]
                    )
                ],
                alignment = ft.MainAxisAlignment.CENTER
            )
        )"""
        

        

ft.app(target=main)

