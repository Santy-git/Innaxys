# ____________________________________________LIBRERIAS____________________________________________

from crearBase import * 
import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent


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

creardb()
e = 0
d = 0
#_____________________________________________IDIOMA___________________________________________
cual = 0
class Maestro:
    def __init__(self):
        pass
    def Ingles(e):

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
            
            def OFF(e):    
                global cual    
                raiz.window_destroy()
                cual = 2
        
            def logear(e):
                global Nivel
                z =  login(User.value,Password.value)
                print(z)
                try:
                    if z[0]:
                        Nivel = int(z[1])
                        Menu()
                except TypeError: 
                    dlg = ft.AlertDialog(
                    title=ft.Text("Usuario Incorrecto"), on_dismiss=lambda e: print("Dialog dismissed!")
                    )
                    def open_dlg(e):
                        raiz.dialog = dlg
                        dlg.open = True
                        raiz.update()
                    open_dlg(e)

            def EnEs(e):
                global cual
                raiz.window_destroy()
                cual = 1
            # -------------------------------------
            #----------------Appbar---------------------
            
            nombre = ft.Container(content=Text(
                "Axys", color=colores[9],), bgcolor=colores[3], width=200, height=40, border_radius=ft.border_radius.all(10))
            nombre.alignment = ft.alignment.center

            raiz.appbar = ft.AppBar(
                title=nombre,
                center_title=True,
                bgcolor=colores2[8],
                actions=[
                    ft.IconButton(ft.icons.LANGUAGE,on_click=EnEs, icon_size=35,bgcolor=ft.colors.RED),
                    ft.IconButton(ft.icons.EXIT_TO_APP_ROUNDED,on_click=OFF, icon_size=35,),
                ]

            )


            # ------------CONTENEDOR------------
            def validate(e: ControlEvent) -> None:
                if all([User.value, Password.value]):
                    Button.disabled = False
                else:
                    Button.disabled = True

                raiz.update()
            

            User: TextField = TextField(label="User", text_align=ft.TextAlign.LEFT, width= 200)
            Password: TextField = TextField(label="Password", text_align=ft.TextAlign.LEFT, width= 200, password = True, can_reveal_password=True)
            Button: ElevatedButton = ElevatedButton(text="Sign Up",on_click=logear)
            
            User.on_change = validate
            Password.on_change = validate
            

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

            contenedor_login = ft.Container(content=Filas_login, height=623, width=500, bgcolor=colores[3], border_radius=ft.border_radius.all(10), padding=ft.padding.only(top=70))

            raiz.add(contenedor_login)

            #_______________________________SUB MENUS______________________________________
            def Menu0():
                print("Menu0")
            def Menu1():
                print("Menu1")
            def Menu2():
                print("Menu2")
            def Menu3():
                print("Menu3")
            def Menu4():
                print("Menu4")
            
            def Selector(a):
                Indices_menus = {0:Menu0,1:Menu1,2:Menu2,3:Menu3,4:Menu4}
                Indices_menus[a]()
            #_____________________________formatos de los sub menus_________________________
                
            # ________________________________MENU__________________________________________
            def Menu():
                formatsubmenus=[]
                listofsubmenus=[
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER,color=ft.colors.BLACK),
                    selected_icon_content=ft.Icon(ft.icons.BOOKMARK,color=ft.colors.BLACK),
                    label_content=ft.Text("1",color=ft.colors.BLACK)
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER,color=ft.colors.BLACK),
                    selected_icon_content=ft.Icon(ft.icons.BOOKMARK,color=ft.colors.BLACK),
                    label_content=ft.Text("2",color=ft.colors.BLACK)
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER,color=ft.colors.BLACK),
                    selected_icon_content=ft.Icon(ft.icons.BOOKMARK,color=ft.colors.BLACK),
                    label_content=ft.Text("3",color=ft.colors.BLACK),
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER,color=ft.colors.BLACK),
                    selected_icon_content=ft.Icon(ft.icons.BOOKMARK,color=ft.colors.BLACK),
                    label_content=ft.Text("4",color=ft.colors.BLACK),
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER,color=ft.colors.BLACK),
                    selected_icon_content=ft.Icon(ft.icons.BOOKMARK,color=ft.colors.BLACK),
                    label_content=ft.Text("5",color=ft.colors.BLACK),
                )]

                for i in range(Nivel):

                    formatsubmenus.append(listofsubmenus[i])


                raiz.window_width = 1000
                raiz.controls.pop()
                raiz.bgcolor = colores[1]

                rail = ft.NavigationRail(
                    selected_index=0,
                    label_type=ft.NavigationRailLabelType.ALL,
                    min_width=100,
                    min_extended_width=400,
                    group_alignment=-0.9,
                    bgcolor=colores[1],
                    destinations=formatsubmenus,                   
                    on_change=lambda e:Selector(e.control.selected_index),
                    
                )
     
                raiz.add(ft.Row(
                        [
                            rail,
                            ft.VerticalDivider(width=1),
                        ],
                        expand=True,
                    )
                )

        ft.app(target=main)

    def Español(e):    

        def main(raizes: ft.Page):

            # seteo de la pagina
            raizes.window_prevent_close = True
            raizes.window_height = 700
            raizes.window_width = 500
            raizes.window_bgcolor = colores2[0]
            raizes.bgcolor = ft.colors.TRANSPARENT
            raizes.window_title_bar_hidden = True
            raizes.window_frameless = True
            raizes.window_resizable = False
            raizes.padding = 10
            # -------------------------------------
            def OFF(e):
                global cual    
                raizes.window_destroy()
                cual = 2



                
            apagado_boton = ft.IconButton(ft.icons.EXIT_TO_APP_ROUNDED,on_click=OFF, icon_size=35,)

            def logear(e):
                z =  login(User.value,Password.value)
                if z:
                    Menu()
                else:
                    dlg = ft.AlertDialog(
                    title=ft.Text("Usuario Incorrecto"), on_dismiss=lambda e: print("Dialog dismissed!")
                    )
                    def open_dlg(e):
                        raizes.dialog = dlg
                        dlg.open = True
                        raizes.update()
                    open_dlg(e)

            def EsEn(e):
                global cual
                raizes.window_destroy()
                cual = 0


                
            # -------------------------------------
            #----------------Appbar---------------------
                
            nombre = ft.Container(content=Text(
                "Axys", color=colores[9],), bgcolor=colores[3], width=200, height=40, border_radius=ft.border_radius.all(10))
            nombre.alignment = ft.alignment.center

            def theme(e:ControlEvent) -> None:
                    if raizes.theme_mode == ft.ThemeMode.LIGHT:
                        raizes.theme_mode = ft.ThemeMode.DARK
                    else:
                        raizes.theme_mode = ft.ThemeMode.LIGHT

                    raizes.update()

            raizes.appbar = ft.AppBar(
                title=nombre,
                center_title=True,
                bgcolor=colores2[8],
                actions=[
                    ft.IconButton(ft.icons.LANGUAGE,on_click=EsEn, icon_size=35,bgcolor=ft.colors.AMBER_200),
                    apagado_boton,
                ]

            )


            # ------------CONTENEDOR------------
            def validate(e: ControlEvent) -> None:
                if all([User.value, Password.value]):
                    Button.disabled = False
                else:
                    Button.disabled = True

                raizes.update()
            

            User: TextField = TextField(label="User", text_align=ft.TextAlign.LEFT, width= 200)
            Password: TextField = TextField(label="Password", text_align=ft.TextAlign.LEFT, width= 200, password = True, can_reveal_password=True)
            Button: ElevatedButton = ElevatedButton(text="Sign Up",on_click=logear)
            
            User.on_change = validate
            Password.on_change = validate
            

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

            contenedor_login = ft.Container(content=Filas_login, height=623, width=500, bgcolor=colores[3], border_radius=ft.border_radius.all(10), padding=ft.padding.only(top=70))

            raizes.add(contenedor_login)
            # __________________________________________________________________________
            def Menu():
                raizes.window_width = 1000
                raizes.controls.pop()
                raizes.theme_mode = ft.ThemeMode.LIGHT


                rail = ft.NavigationRail(
                    selected_index=0,
                    label_type=ft.NavigationRailLabelType.ALL,
                    min_width=100,
                    min_extended_width=400,
                    group_alignment=-0.9,
                    destinations=[
                        ft.NavigationRailDestination(
                            icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.PEOPLE, label="First"
                        ),
                        ft.NavigationRailDestination(
                            icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                            selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                            label="Second",
                        ),
                        ft.NavigationRailDestination(
                            icon=ft.icons.SETTINGS_OUTLINED,
                            selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                            label_content=ft.Text("Settings"),
                        ),
                    ],
                    on_change=lambda e: print("Selected destination:", e.control.selected_index),
                )
                raizes.add(ft.Row(
                        [
                            rail,
                            ft.VerticalDivider(width=1),
                            ft.Column([ ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True),
                        ],
                        expand=True,
                    )
                )
        ft.app(target=main)

Controlador = Maestro()
while True:
    if cual == 0:
        Controlador.Ingles()
    if cual == 1:
        Controlador.Español()
    if cual == 2:
        break