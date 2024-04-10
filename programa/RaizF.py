#....................Librerias....................
from crearBase import * 
import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column ,Container, Stack
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

niveles = {5:"Administrador"}

#....................................

class Plantilla:
    def __init__(self,raiz):
        self.raiz = raiz

#..................................................       
    def ej(self):
        self.raiz.bgcolor = '#8AA597'
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
        z =  [self.User.value,self.Password.value]
        z = login(z[0],z[1])
        print(z)
        try:
            if z[0]:
                print("hola")
                Nivel = int(z[1])
                self.Menu()
                #Menu0()

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
        self.nombre = ft.Container(content=Text(
            "Axys", color=colores[9],), bgcolor=colores[3], width=200, height=40, border_radius=ft.border_radius.all(10))
        self.nombre.alignment = ft.alignment.center

        self.raiz.appbar = ft.AppBar(
            title=self.nombre,
            center_title=True,
            bgcolor=colores2[8],
            actions=[
                ft.IconButton(ft.icons.LANGUAGE,on_click=self.EnEs,icon_size=35),
                ft.IconButton(ft.icons.EXIT_TO_APP_ROUNDED,on_click=self.OFF, icon_size=35,),
            ]

        )
        self.raiz.update()

    def login_menu(self):

        self.User : TextField = TextField(
            width=290,
            height=60,
            label='User',
            border='underline',
            color='#303030',
            prefix_icon = ft.icons.PERSON,)
        
        self.Password : TextField = TextField(
            width=280,
            height=60,
            label='Password',
            border='underline',
            color='#303030',
            prefix_icon= ft.icons.LOCK,)
        
        Button : ElevatedButton=ElevatedButton(
            content=Text(
                'SIGN IN',
                color='white',
                weight='w500',       
            ),width=280,
            bgcolor='black',
            on_click=self.logear)
        
        self.contenedor_login = ft.Container(
                Container(
                    Stack([
                        Container(
                            border_radius=11,
                            rotate=ft.Rotate(0.98*3.14), #Degree
                            width=360,
                            height=560,
                            bgcolor='#22ffffff'
                        ),
                        Container(
                            Container(
                                Column([
                                    Container(
                                        ft.Image(
                                            src='axys.png',
                                            width=50,
                                        ),padding=ft.padding.only(150,20),
                                    ),
                                    Text(
                                        'Sign in',
                                        width=360,
                                        size=30,
                                        weight='w900',
                                        text_align='center',
                                    ),
                                    Text(
                                        'Please login to use the plataform',
                                        width=360,
                                        text_align='center',

                                    ),
                                    Container(self.User,padding=ft.padding.only(25,20)
                                        ),
                                    Container(self.Password,padding=ft.padding.only(25,20),
                                    ),
                                    Container(Button,padding=ft.padding.only(40,10)
                                    )
                                ])
                            ),
                            width=360,
                            height=560,
                            bgcolor='#22ffffff',
                            border_radius=11,
                        )
                    ]),
                    padding=110,
                    width=360,
                    height=560 
                ),  
                width=580,
                height=740,
                gradient=ft.LinearGradient(['white30','white10']),
                border_radius=ft.border_radius.all(10),
                margin=ft.margin.symmetric(horizontal=650,vertical=100)


            )

        self.raiz.add(self.contenedor_login)



#...................................Menus............................


    def Selector(self,a):
        Indices_menus = {0:self.Menu0,1:self.Menu1,2:self.Menu2,3:self.Menu3,4:self.Menu4}
        Indices_menus[a]()  








    def HighLight(self,e):
        if e.data == "true":
            e.control.bgcolor= "white10"
            e.control.update()

            # Ahora lo que hago aparte de cambiar el color de fondo, el texto

            # Control del contenido por indice del IconButton y el texto
            e.control.content.controls[0].icon_color = "white"
            e.control.content.controls[1].icon_color = "white"
            e.control.content.update()


        else:
            e.control.bgcolor= None
            e.control.update()

            # Ahora lo que hago aparte de cambiar el color de fondo, el texto

            # Control del contenido por indice del IconButton y el texto
            e.control.content.controls[0].icon_color = "white54"
            e.control.content.controls[1].icon_color = "white54"
            e.control.content.update()


    def UserData(self,name:str):
        # Fila esclusiva para la informacion del usuario

        return Container(
            content=Row(
                controls=[
                    Container(
                        width=42,
                        border_radius = 8,
                        height=42,
                        bgcolor='bluegrey900',
                        alignment=ft.alignment.center,
                        content=Text(
                            value=Nivel,
                            size=20,
                            weight='bold',
                            
                        ),
                    ),
                    Column(
                        spacing=1,
                        controls=[
                            Text(
                                value=name,
                                size=11,
                                weight='bold',
                                # Detalles para la animacion
                                opacity=1,
                                animate_opacity=200, #Velocidad de animacion

                            )
                        ]
                    )
                ]
            )
        )


    def ContainerIcon(self, icon_name:str, text:str):
        return Container(
            width=180, 
            height=45,
            border_radius=10,
            on_hover=lambda e: self.HighLight(e),
            content=Row(
                controls=[
                    ft.IconButton(
                        icon=icon_name,
                        icon_size=18,
                        icon_color='white54',
                        style=ft.ButtonStyle(
                            shape={
                                "": ft.RoundedRectangleBorder(radius=7),
                            },
                            overlay_color={"":"transparent"}

                        ),
                    ),
                    Text(
                        value=text,
                        color="white54",
                        size=11,
                        opacity=1,
                        animate_opacity=200,
                    )
                ]
            ),

        )


    def build(self):
        
        self.Left_bar = ft.Container(

        width=200,
        height=580,
        content = Column(

            alignment=ft.alignment.center,
            horizontal_alignment="center",

            controls =[
                # Los iconos del SideBar aca

                # Nivel y informacion del usuario(3 Niveles , Administrador ,empleado, cliente)
                
                self.UserData(niveles[Nivel]),

                # Boton para redimensionar 

                Container(
                    width= 24,
                    height=24,
                    bgcolor= "bluegrey800",
                    border_radius= 8
                    # Func es la animacion para minimizar y maximizar
                ),

                # Divisor
                ft.Divider(height=2 , color='white54'),
                self.ContainerIcon(ft.icons.SEARCH,"Search"),
                self.ContainerIcon(ft.icons.DASHBOARD_ROUNDED,"Bashboard"),
                self.ContainerIcon(ft.icons.BAR_CHART,"Analitics"),
                self.ContainerIcon(ft.icons.NOTIFICATIONS,"Nofications"),
                self.ContainerIcon(ft.icons.PIE_CHART,"Analitics"),
                
                # Divisor
                ft.Divider(height=5, color="white54"),
                self.ContainerIcon(ft.icons.FAVORITE_ROUNDED,"Likes"),

            ]
        ),)

        return Container(
            width=200,
            height=1000,
            bgcolor='black',
            border_radius=10,
            content=self.Left_bar
            )



    def Menu(self):
        global Container_menus
        self.raiz.clean()
        self.raiz.appbar = ft.AppBar(
        title=self.nombre,
        center_title=True,
        bgcolor=colores2[8],
        actions=[
            ft.IconButton(ft.icons.EXIT_TO_APP_ROUNDED,on_click=self.OFF, icon_size=35,),
        ])
        formatsubmenus=[]
        formatsubmenusAux=[
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
            formatsubmenus.append(formatsubmenusAux[i])


        rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=400,
            group_alignment=-0.9,
            bgcolor=colores[1],
            destinations=formatsubmenus,                   
            on_change=lambda e:self.Selector(e.control.selected_index),
            
        )
        Container_menus = ft.Container(width=1700,height=850,bgcolor=colores[3],border_radius=ft.border_radius.all(3))

        self.raiz.add(ft.Row(
                [                    
                    rail,
                    ft.VerticalDivider(width=1),
                    Container_menus
                ],
                expand=True,
            )
        )

def main(raiz: ft.Page):
    global altura 
    global ancho
    altura = raiz.height
    ancho = raiz.width
    raiz.window_prevent_close = True 
    raiz.bgcolor = ft.colors.BLUE_GREY_100
    raiz.window_frameless = True
    raiz.window_resizable = False
    raiz.window_full_screen = True
    raiz.update()
    objeto = Plantilla(raiz)
    objeto.ej()
    z = objeto.appbar()
    objeto.login_menu()


ft.app(target=main)




'''