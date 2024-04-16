# ....................Librerias....................
from crearBase import *
import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column, Container, Stack
from flet_core.control_event import ControlEvent
from datetime import datetime
from functools import partial
import time
# .................................................

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

niveles = {5: "Administrador",3: "Empleado"}
creardb()
# ....................................


class Plantilla:
    def __init__(self, raiz):
        self.raiz = raiz

# ..................................................
    def ej(self):
        self.raiz.bgcolor = '#4a624e'
        self.raiz.update()

    def OFF(self, e):
        global cual
        self.raiz.window_destroy()
        cual = 2

    def EnEs(self, e):
        global cual
        self.raiz.window_destroy()
        cual = 1

    def logear(self, e):
        global Nivel
        global z
        z = [self.User.value, self.Password.value]
        z = login(z[0], z[1])
        print(z)
        try:
            if z[0]:
                print("hola")
                Nivel = int(z[1])
                self.Menu()
                # Menu0()

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
                ft.IconButton(ft.icons.LANGUAGE,
                              on_click=self.EnEs, icon_size=35),
                ft.IconButton(ft.icons.EXIT_TO_APP_ROUNDED,
                              on_click=self.OFF, icon_size=35,),
            ]

        )
        self.raiz.update()

    def login_menu(self):

        self.User: TextField = TextField(
            width=290,
            height=60,
            label='User',
            border='underline',
            color='white',
            prefix_icon=ft.icons.PERSON,)

        self.Password: TextField = TextField(
            width=280,
            height=60,
            label='Password',
            border='underline',
            color='white',
            prefix_icon=ft.icons.LOCK,)

        Button: ElevatedButton = ElevatedButton(
            content=Text(
                'SIGN IN',
                color='white',
                weight='w500',
            ), width=280,
            bgcolor='black',
            on_click=self.logear)

        self.contenedor_login = ft.Container(
            Container(
                Stack([
                    Container(
                        border_radius=11,
                        rotate=ft.Rotate(0.98*3.1),  # Degree
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
                                        width=100,
                                    ), padding=ft.padding.only(130, 20),
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
                                Container(self.User, padding=ft.padding.only(25, 20)
                                          ),
                                Container(self.Password, padding=ft.padding.only(25, 20),
                                          ),
                                Container(Button, padding=ft.padding.only(40, 10)
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
                height=560,
                bgcolor='grey900'

            ),
            width=580,
            height=740,
            gradient=ft.LinearGradient(['white30', 'white10']),
            border_radius=ft.border_radius.all(30),
            margin=ft.margin.symmetric(horizontal=(ancho*0.30)),

        )

        self.raiz.add(self.contenedor_login)


# ...................................Menus............................

# ...................................Menus............................

    def pedidos(self,var):
        hres.append(self.variable2[var])
        images.controls.pop(var)
        images.update()
        self.variable2.pop(var)
        totalesp = 0
        costo = 0
        
        for i in range(len(hres)):
            totalesp += hres[i][3]
            totalesp += hres[i][2]*2
            costo += hres[i][4]
        totalH = len(hres)
        self.contador.value = ("Habitaciones: ",totalH,"total de espacios: ",totalesp,"costo total: ",costo)
        self.contador.update()
        self.disponibles()

    def disponibles(self):
        global images
        def valor(a):
            indice = a                              
            infoH=ft.Row([
                ft.Container(width=50,height=50,bgcolor='#A3CD91',
                             border_radius=ft.border_radius.all(6),
                             margin=ft.margin.all(10),
                             alignment=ft.alignment.center,
                             content=ft.Text(value=self.variable2[a][0],color='#000000')),
                             
                ft.Text(value="Piso: "+str(self.variable2[a][1]))          
            ])
            infoH2 = ft.Row([
                ft.Text(value="Camas Individuales: "+str(self.variable2[a][2])),
                
            ]) 
            infoH4 = ft.Row([
                ft.Text(value="Camas Matrimoniales: "+str(self.variable2[a][3])) ,
                
            ])     
            
            infoH3 = ft.Row([     
                ft.Text(value="Costo: "+str(self.variable2[a][4])), 
                ft.TextButton(text="+",on_click=lambda _:self.pedidos(indice))
            ])                     
            contener = ft.Container(width=60,height=60,
                border_radius=ft.border_radius.all(3),bgcolor=colores[9],
                content=ft.Column([infoH,infoH2,infoH4,infoH3]))  
            return contener
        
        images = ft.GridView(
            runs_count=5,
            max_extent=300,
            child_aspect_ratio=1.0,
            spacing=20,
            run_spacing=5,
            expand=1,
        )
        
        for i in range(len(self.variable2)):
            images.controls.append(valor(i))                      
        self.Departamentos.clean()
        self.Departamentos.content = ft.Column([images])                                                                                                        
        Container_menus.update()

    def Consulta_aux(self,Ingreso_Res,Egreso_Res):
        global hres
        hres = []    
        self.variable2 = Consulta(Ingreso_Res,Egreso_Res)
        self.disponibles()

    def res_final(self,cli,emp,fecha,desc,hres,Ing,Eng):

        confirmar = ft.TextButton(text="Confirmar",icon_color="#659863",on_click=lambda _:completar(cli,emp,fecha,desc,hres,Ing,Eng))
        Container_menus.clean()   
        a = 0
        c = 0
        d = 0
        e = 0    
        for i in range(len(hres)):
            a += hres[i][0]
            c += hres[i][2]
            d += hres[i][3]
            e += hres[i][4]
        texto = "Numero de habitacion: "+str(a)+" camas matrimoniales:"+str(c)+" camas individuales:"+str(d)+" Costo:"+str(e)
        Container_menus.content = ft.Container(content=ft.Row([ft.Text(value=texto),confirmar]),bgcolor='#3B6639',width=ancho*0.56,height=altura*0.1,border_radius=ft.border_radius.all(3))
        Container_menus.update()

    def Reservar_Aux(self,cli,emp,fecha,desc):
        Container_menus.clean()
        Verificar = Reservar(cli,emp,fecha,desc)
        if Verificar == 1:
            Container_menus.clean()
            Ingreso_Res = ft.TextField(label="Ingreso (aaaa-mm-dd)")
            Egreso_Res = ft.TextField(label="Egreso (aaaa-mm-dd)")
            consultar = ft.TextButton(text="Consultar",on_click=lambda _:self.Consulta_aux(Ingreso_Res.value,Egreso_Res.value))
            reservarboton = ft.TextButton(text="el otro boton",on_click=lambda _:self.res_final(
                cli,emp,fecha,desc,hres,Ingreso_Res.value,Egreso_Res.value
            ))
            self.Departamentos = ft.Container(width=830,height=500,bgcolor=colores[2],margin=10)
            self.contador = ft.Text(value="")
            a=ft.Row([Ingreso_Res,Egreso_Res])
            b=ft.Row([consultar,reservarboton,self.contador])
            c=ft.Row([self.Departamentos])
            Container_menus.content = ft.Column([a,b,c])
            Container_menus.alignment = ft.alignment.top_center
            
            Container_menus.update()
        if Verificar == 2:
            #aca poner que el cliente no existe
            pass

    def Menu0(self):
        cod_cliente = ft.TextField(label="Dni de cliente",width=300)
        fecha_res = datetime.now().date()
        desc = ft.TextField(label="descripcion",multiline=True, width= 500, max_length=200, max_lines=3)
        subir = ft.CupertinoButton(
            content=ft.Text("Next", color=ft.colors.BLACK),
            bgcolor=colores[1],
            border_radius=ft.border_radius.all(15),
            on_click=lambda _:self.Reservar_Aux(cod_cliente.value,z[2],fecha_res,desc.value))
        
        Container_menus.content = ft.Column (
            [cod_cliente,
            desc,
            subir],
            expand= True
        )
        Container_menus.alignment = ft.alignment.center
        Container_menus.update()

    def pedidosCoch(self,var):
        hres.append(self.variable2[var])
        images.controls.pop(var)
        images.update()
        self.variable2.pop(var)
        self.disponiblesCoch()

    def disponiblesCoch(self):
        global images
        def valor(a):
            indice = a
            infoH=ft.Row([
                ft.Text(value=self.variable2[a][0]),
                ft.Text(value=self.variable2[a][1])            
            ])                         
            contener = ft.Container(width=60,height=60,bgcolor=colores[9],content=ft.Column([infoH,ft.TextButton(text="+",on_click=lambda _:self.pedidosCoch(indice))]))  
            return contener
        
        images = ft.GridView(
            runs_count=5,
            max_extent=300,
            child_aspect_ratio=1.0,
            spacing=20,
            run_spacing=5,
            expand=1,
        )
        
        for i in range(len(self.variable2)):
            images.controls.append(valor(i))                      
        self.Departamentos.clean()
        self.Departamentos.content = ft.Column([images])                                                                                                        
        Container_menus.update()
                            
    def ConsultaCoch_aux(self,Ingreso_Res,Egreso_Res):
        global hres
        hres = []
        self.variable2 = ConsultaCoch(Ingreso_Res,Egreso_Res)
        self.disponiblesCoch()

    def resCoch_final(self,cli,emp,fecha,desc,hres,Ing,Eng):
        confirmar = ft.TextButton(text="Confirmar",icon_color="#659863",on_click=lambda _:completarCoch(cli,emp,fecha,desc,hres,Ing,Eng))
        Container_menus.clean()   
        a = []   
        for i in range(len(hres)):
            a.append(hres[i][0])
            
        texto = "Numeros de las habitaciones: "+str(a)
        Container_menus.content = ft.Container(content=ft.Row([ft.Text(value=texto),confirmar]),bgcolor='#3B6639',width=ancho*0.56,height=altura*0.1,border_radius=ft.border_radius.all(3))
        Container_menus.update()
                                
        confirmar = ft.TextButton(text="Confirmar",on_click=lambda _:completarCoch(cli,emp,fecha,desc,hres,Ing,Eng))
        Container_menus.clean()
        Container_menus.update()    

    def ReservarCoch_Aux(self,cli,emp,fecha,desc):                   
        Container_menus.clean()
        Verificar = ReservarCoch(cli,emp,fecha,desc)
        

        if Verificar == 1:
            Container_menus.clean()
            Ingreso_Res = ft.TextField(label="Ingreso (aaaa-mm-dd)")
            Egreso_Res = ft.TextField(label="Egreso (aaaa-mm-dd)")
            consultar = ft.TextButton(text="Consultar",on_click=lambda _:self.ConsultaCoch_aux(Ingreso_Res.value,Egreso_Res.value))
            reservarboton = ft.TextButton(text="el otro boton",on_click=lambda _:self.resCoch_final(
                cli,emp,fecha,desc,hres,Ingreso_Res.value,Egreso_Res.value
            ))
            self.Departamentos = ft.Container(width=830,height=500,bgcolor=colores[2],margin=10)
            contador = ft.Text(value="")
            a=ft.Row([Ingreso_Res,Egreso_Res])
            b=ft.Row([consultar,reservarboton,contador])
            c=ft.Row([self.Departamentos])
            Container_menus.content = ft.Column([a,b,c])
            Container_menus.alignment = ft.alignment.top_center
            
            Container_menus.update()
        if Verificar == 2:
            pass    

    def Menu1(self):
        cod_cliente = ft.TextField(label="Dni de cliente",width=300)
        fecha_res = datetime.now().date()
        desc = ft.TextField(label="descripcion",multiline=True, width= 500, max_length=200, max_lines=3)
        subir = ft.CupertinoButton(
            content=ft.Text("Subir", color=ft.colors.BLACK),
            bgcolor=colores[1],
            border_radius=ft.border_radius.all(15),
            on_click=lambda _:self.ReservarCoch_Aux(cod_cliente.value,z[2],fecha_res,desc.value))
        
        Container_menus.content = ft.Column (
            [cod_cliente,
            desc,
            subir],
            expand= True
        )
        Container_menus.alignment = ft.alignment.center
        Container_menus.update()

    def Cli_Aux(self,a,b,c,d):
        Verificar = Cli_add(a,b,c,d)
        if Verificar:
            dlg = ft.AlertDialog(
            title=ft.Text("Datos Ingresados")
            )
            def open_dlg(self):
                self.raiz.dialog = dlg
                dlg.open = True
                self.raiz.update()
            open_dlg(self)
            Container_menus.clean()
            self.Menu2()

    def Menu2(self):
        cod_cliente = ft.TextField(label="Dni de cliente",width=300)
        nom_cli = ft.TextField(label="Nombre",width=300)
        email_cli = ft.TextField(label="Email",width=300)
        desc_cli = ft.TextField(label="descripcion",multiline=True, width= 500, max_length=200, max_lines=3)
        subir_cli = ft.CupertinoButton(
            content=ft.Text("Subir", color=ft.colors.BLACK),
            bgcolor=colores[1],
            border_radius=ft.border_radius.all(15),
            on_click=lambda _:self.Cli_Aux(cod_cliente.value,nom_cli.value,email_cli.value,desc_cli.value))
        
        Container_menus.content = ft.Column (
            [cod_cliente,
            nom_cli,
            email_cli,
            desc_cli,
            subir_cli],
            expand= True
        )
        Container_menus.alignment = ft.alignment.center
        Container_menus.update()

    def Menu3(self):
        cocherav = ft.CupertinoButton(text="cochera",width=300,on_click=lambda _:self.cochera(),bgcolor=colores[5])
        habitacionv = ft.CupertinoButton(text="habitacion",width=300,on_click=lambda _:self.habitacion(),bgcolor=colores[5])
        Container_menus.content = ft.Row([cocherav,habitacionv])
        Container_menus.padding = ft.padding.symmetric(horizontal=ancho*0.18)
        Container_menus.update()
            
    def crear_coch(self,a):
        print("crear_coch")
        validacion = crear_coch(a)
        if validacion:
            dlg = ft.AlertDialog(
            title=ft.Text("cochera registrada")
            )
            def open_dlg(self):
                self.raiz.dialog = dlg
                dlg.open = True
                self.raiz.update()
            open_dlg(self)
            Container_menus.clean()
            self.Menu3()

    def cochera(self):
        print("cochera")
        piso_coch = ft.TextField(label="piso")
        subir_coch = ft.CupertinoButton(
            content=ft.Text("Subir", color=ft.colors.BLACK),
            bgcolor=colores[1],
            border_radius=ft.border_radius.all(15),
            on_click=lambda _:self.crear_coch(piso_coch.value))
        Container_menus.content = ft.Column (
            [piso_coch,subir_coch
            ],
            expand= True
        )
        Container_menus.update()

    def crear_habitacion(self,a,b,c,d):
        validacion = crear_hab(a,b,c,d)
        if validacion:
            dlg = ft.AlertDialog(
            title=ft.Text("Habitacion registrada")
            )
            def open_dlg(self):
                self.raiz.dialog = dlg
                dlg.open = True
                self.raiz.update()
            open_dlg(self)
            Container_menus.clean()
            self.Menu3()

    def habitacion(self):
        piso = ft.TextField(label="Piso",width=300)
        camamatr = ft.TextField(label="camas matrimoniales",width=300)
        camaind = ft.TextField(label="camas individuales",width=300)
        costo = ft.TextField(label="costo",width=300)
        subir_cli = ft.CupertinoButton(
            content=ft.Text("Subir", color=ft.colors.BLACK),
            bgcolor=colores[1],
            border_radius=ft.border_radius.all(15),
            on_click=lambda _:self.crear_habitacion(piso.value,camamatr.value,camaind.value,costo.value))
        Container_menus.content = ft.Column (
            [piso,
            camamatr,
            camaind,
            costo,
            subir_cli],
            expand= True
        )
        Container_menus.update()








    
#....................................................zona de trabajo.........................................................................................    

    def Menu4(self):

        # --------------Funciones--------------
        def reg_emp_aux(dni_emp, nombre_emp, email, telefono, puesto, usuario, contraseña, nivel):
            validacion = reg_emp(dni_emp, nombre_emp, email,
                                 telefono, puesto, usuario, contraseña, nivel)
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

        # --------------Elementos-------------
        dni_emp = ft.TextField(label="Dni de Empleado",
                               width=300, border_radius=20)
        nombre_emp = ft.TextField(label="Nombre", width=300, border_radius=20)
        email = ft.TextField(label="Email", width=300, border_radius=20)
        telefono = ft.TextField(label="Telefono", width=300, border_radius=20)
        puesto = ft.TextField(label="Puesto", width=300, border_radius=20)
        usuario = ft.TextField(label="Usuario", width=300, border_radius=20)
        contraseña = ft.TextField(
            label="Contraseña", width=300, border_radius=20)
        nivel = ft.TextField(label="Nivel de acceso",
                             width=300, border_radius=20)
        registrar = ft.CupertinoButton(
            content=ft.Text("Registrar", color=ft.colors.BLACK),
            bgcolor=colores[1],
            border_radius=ft.border_radius.all(25),
            on_click=lambda _: reg_emp_aux(dni_emp.value, nombre_emp.value, email.value,
                                           telefono.value, puesto.value, usuario.value, contraseña.value, nivel.value),
            padding=ft.padding.symmetric(horizontal=120, vertical=0)
        )
        # ---------------como se muestran---------------------
        Container_menus.content = ft.Column(
            [dni_emp,
             nombre_emp,
             email,
             telefono,
             puesto,
             usuario,
             contraseña,
             nivel,
             registrar],
            expand=True
        )
        
        Container_menus.update()
# .............................................................................................................................................

    def HighLight(self, e):
        if e.data == "true":
            e.control.bgcolor = "white10"
            e.control.update()

            # Ahora lo que hago aparte de cambiar el color de fondo, el texto

            # Control del contenido por indice del IconButton y el texto
            e.control.content.controls[0].icon_color = "white"
            e.control.content.controls[1].icon_color = "white"
            e.control.content.update()

        else:
            e.control.bgcolor = None
            e.control.update()

            # Ahora lo que hago aparte de cambiar el color de fondo, el texto

            # Control del contenido por indice del IconButton y el texto
            e.control.content.controls[0].icon_color = "white54"
            e.control.content.controls[1].icon_color = "white54"
            e.control.content.update()

    def Selector(self, a):
        diccionario = {"Reservar Habitacion": 0, "Reservar Cochera": 1,
                       "Añadir Cliente": 2, "Añadir elementos": 3, "Añadir Empleado": 4, "Likes": 5}
        Indices_menus = {0: self.Menu0, 1: self.Menu1,
                         2: self.Menu2, 3: self.Menu3, 4: self.Menu4}
        Indices_menus[diccionario[a]]()

    def UserData(self, name: str):
        # Fila esclusiva para la informacion del usuario

        return Container(
            content=Row(
                controls=[
                    Container(
                        width=42,
                        border_radius=8,
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

    def ContainerIcon(self, icon_name: str, text: str):
        print("hola")
        return Container(
            width=180,
            height=45,
            border_radius=10,
            on_hover=lambda e: self.HighLight(e),
            on_click=lambda e: self.Selector(text),
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
                            overlay_color={"": "transparent"}
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
            )
        )

    def Menu(self):
        global Container_menus
        self.raiz.clean()
        self.raiz.appbar = ft.AppBar(
            title=self.nombre,
            center_title=True,
            bgcolor=colores[8],
            actions=[
                ft.IconButton(ft.icons.EXIT_TO_APP_ROUNDED,
                              on_click=self.OFF, icon_size=35,),
            ])
        formatsubmenus = []
        formatsubmenusAux = [
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    ft.icons.BOOKMARK_BORDER, color=ft.colors.BLACK),
                selected_icon_content=ft.Icon(
                    ft.icons.BOOKMARK, color=ft.colors.BLACK),
                label_content=ft.Text("1", color=ft.colors.BLACK)
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    ft.icons.BOOKMARK_BORDER, color=ft.colors.BLACK),
                selected_icon_content=ft.Icon(
                    ft.icons.BOOKMARK, color=ft.colors.BLACK),
                label_content=ft.Text("2", color=ft.colors.BLACK)
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    ft.icons.BOOKMARK_BORDER, color=ft.colors.BLACK),
                selected_icon_content=ft.Icon(
                    ft.icons.BOOKMARK, color=ft.colors.BLACK),
                label_content=ft.Text("3", color=ft.colors.BLACK),
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    ft.icons.BOOKMARK_BORDER, color=ft.colors.BLACK),
                selected_icon_content=ft.Icon(
                    ft.icons.BOOKMARK, color=ft.colors.BLACK),
                label_content=ft.Text("4", color=ft.colors.BLACK),
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    ft.icons.BOOKMARK_BORDER, color=ft.colors.BLACK),
                selected_icon_content=ft.Icon(
                    ft.icons.BOOKMARK, color=ft.colors.BLACK),
                label_content=ft.Text("5", color=ft.colors.BLACK),
            )]

        for i in range(Nivel):
            formatsubmenus.append(formatsubmenusAux[i])

        Left_bar = ft.Container(

            width=200,
            height=580,
            content=Column(

                alignment=ft.alignment.center,
                horizontal_alignment="center",

                controls=[
                    self.UserData(niveles[5]),
                    ft.Divider(height=2, color='white54'),
                    self.ContainerIcon(ft.icons.SEARCH, "Reservar Habitacion"),
                    self.ContainerIcon(
                        ft.icons.DASHBOARD_ROUNDED, "Reservar Cochera"),
                    self.ContainerIcon(ft.icons.BAR_CHART, "Añadir Cliente"),
                    self.ContainerIcon(
                        ft.icons.NOTIFICATIONS, "Añadir elementos"),
                    self.ContainerIcon(ft.icons.PIE_CHART, "Añadir Empleado"),

                ]
            ),)

        penas = Container(
            width=200,
            height=1000,
            bgcolor='black',
            border_radius=10,
            content=Left_bar
        )
        Container_menus = ft.Container(
            width=1700,
            height=850,
            bgcolor=colores[3],
            border_radius=ft.border_radius.all(3),
            padding=ft.padding.symmetric(horizontal=(ancho*0.04), vertical=(altura*0.1))
        )

        self.raiz.add(ft.Row(
            [
                penas,
                ft.VerticalDivider(width=1),
                ft.Container(
                    Container_menus,
                    width=1100,
                    height=850,
                    alignment=ft.alignment.center,
                )
            ],
            expand=True,
        )
        )


def main(raiz: ft.Page):
    global altura
    global ancho
    altura = raiz.height
    ancho = raiz.width
    raiz.window_resizable = False
    raiz.window_full_screen = True
    raiz.update()
    objeto = Plantilla(raiz)
    objeto.ej()
    z = objeto.appbar()
    objeto.login_menu()


ft.app(target=main)
