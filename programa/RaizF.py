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
'#f6f6f6',
'#e7e7e7',
'#d1d1d1',
'#b0b0b0',
'#888888',
'#6d6d6d',
'#5d5d5d',
'#4f4f4f',
'#454545',
'#3d3d3d',
'#0f0f0f',
]


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
            bgcolor=colores[8],
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

    def Menu4(self):

        #--------------Funciones--------------
        def reg_emp_aux(dni_emp,nombre_emp,email,telefono,puesto,usuario,contraseña,nivel):
            validacion = reg_emp(dni_emp,nombre_emp,email,telefono,puesto,usuario,contraseña,nivel)
            if validacion:
                dlg = ft.AlertDialog(
                title=ft.Text("Registro completo")
                )
                def open_dlg(self):
                    self.raiz.dialog = dlg
                    dlg.open = True
                    self.raiz.update()
                open_dlg(self)
                Container_menus.clean()
                self.Menu4()

            
        #--------------Elementos-------------
        dni_emp = ft.TextField(label="Dni de Empleado",width=300)
        nombre_emp = ft.TextField(label="Nombre",width=300)
        email = ft.TextField(label="Email",width=300)
        telefono = ft.TextField(label="Telefono",width=300)
        puesto = ft.TextField(label="Puesto",width=300)
        usuario = ft.TextField(label="Usuario",width=300)
        contraseña = ft.TextField(label="Contraseña",width=300)
        nivel = ft.TextField(label="Nivel de acceso",width=300)
        registrar = ft.CupertinoButton(
            content=ft.Text("Registrar", color=ft.colors.BLACK),
            bgcolor=colores[1],
            border_radius=ft.border_radius.all(15),
            on_click=lambda _: reg_emp_aux(dni_emp.value,nombre_emp.value,email.value,telefono.value,puesto.value,usuario.value,contraseña.value,nivel.value)
            )
        #---------------como se muestran---------------------
        Container_menus.content = ft.Column (
            [dni_emp,
            nombre_emp,
            email,
            telefono,
            puesto,
            usuario,
            contraseña,
            nivel,
            registrar],
            expand= True
        )
        Container_menus.update()
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


    def Selector(self,a):
        Indices_menus = {0:self.Menu0,1:self.Menu1,2:self.Menu2,3:self.Menu3,4:self.Menu4}
        Indices_menus[a]()  

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


                            )
                        ]
                    )
                ]
            )
        )

    def ContainerIcon(self, icon_name:str, text:str, a:int):
        return Container(
            width=180, 
            height=45,
            border_radius=10,
            on_hover=lambda e: self.HighLight(e),
            on_click=lambda: self.Selector(a),
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
                        )
                        ,
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
        
    def Menu(self):
        global Container_menus
        self.raiz.clean()
        self.raiz.appbar = ft.AppBar(
        title=self.nombre,
        center_title=True,
        bgcolor=colores[8],
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



        Left_bar = ft.Container(

        width=200,
        height=580,
        content = Column(

            alignment=ft.alignment.center,
            horizontal_alignment="center",

            controls =[
                self.UserData(niveles[5]),
                ft.Divider(height=2 , color='white54'),
                self.ContainerIcon(ft.icons.SEARCH,"Search",0),
                self.ContainerIcon(ft.icons.DASHBOARD_ROUNDED,"Bashboard",1),
                self.ContainerIcon(ft.icons.BAR_CHART,"Analitics",2),
                self.ContainerIcon(ft.icons.NOTIFICATIONS,"Nofications",3),
                self.ContainerIcon(ft.icons.PIE_CHART,"Analitics",4),
                
                # Divisor
                ft.Divider(height=5, color="white54"),
                self.ContainerIcon(ft.icons.FAVORITE_ROUNDED,"Likes",5),

            ]
        ),)

        penas = Container(
            width=200,
            height=1000,
            bgcolor='black',
            border_radius=10,
            content=Left_bar
            )    
        Container_menus = ft.Container(width=1700,height=850,bgcolor=colores[3],border_radius=ft.border_radius.all(3))

        self.raiz.add(ft.Row(
                [                    
                    penas,
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




