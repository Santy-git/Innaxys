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


# ....................diccionario idioma..............................

# ....................diccionario idioma..............................

# Funcionas que nos ayudan a modificar muchos objetos del flet

# los label
global idioma
global español
global ingles
global codigo
español = {3: "hola"}
idioma = español
ingles = {3: "hello"}
codigo = 0


def create_text_field(label_text, **kwargs):
    return ft.TextField(
        label=label_text,
        label_style={
            'color': ft.colors.BLACK,
            'font_size': 16,
        },
        border_radius=20,
        width=ancho*.3,
        **kwargs
    )


niveles = {5: "Administrador", 3: "Empleado"}
creardb()
# ....................................


class Plantilla:
    def __init__(self, raiz, idioma, español, ingles):
        self.raiz = raiz
        self.idioma = idioma
        self.español = español
        self.ingles = ingles
# ..................................................

    def ej(self):
        self.raiz.bgcolor = '#4a624e'
        self.raiz.update()

    def OFF(self, e):
        global codigo
        self.raiz.window_destroy()
        codigo = 1

    def EnEs(self, e):
        global codigo
        global idioma
        self.raiz.window_destroy()
        if self.idioma == self.español:
            idioma = self.ingles
        else:
            idioma = self.español
        print(idioma)
        codigo = 0

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
            self.idioma[3], color=colores[9],), bgcolor=colores[3], width=ancho*0.10, height=altura*0.05, border_radius=ft.border_radius.all(10))
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
        global Nivel
        global z
        # z = (True, '5', '0')
        # Nivel = 5
        # self.Menu()
        # esto es lo que saca el login sacar lo de arriba y eliminar el if
        # if z[2] == 3:

        self.User: TextField = TextField(
            width=ancho * .2,
            height=altura * .1,
            label='User',
            border='underline',
            color='white',
            prefix_icon=ft.icons.PERSON,)

        self.Password: TextField = TextField(
            width=ancho * .2,
            height=altura * .1,
            label='Password',
            border='underline',
            color='white',
            prefix_icon=ft.icons.LOCK,)

        Button: ElevatedButton = ElevatedButton(
            content=Text(
                'SIGN IN',
                color='white',
                weight='w500',
            ), width=ancho * .2,
            bgcolor='black',
            on_click=self.logear)

        self.contenedor_login = ft.Container(
            Container(
                Stack([
                    Container(
                        border_radius=11,
                        rotate=ft.Rotate(0.98*3.1),  # Degree
                        width=ancho * .45,
                        height=altura * .8,
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
                                    width=ancho * .25,
                                    size=altura * .05,
                                    weight='w900',
                                    text_align='center',
                                ),
                                Text(
                                    'Please login to use the plataform',
                                    width=ancho * .25,
                                    text_align='center',

                                ),
                                Container(self.User, padding=ft.padding.only(ancho * .04, altura * .03)
                                          ),
                                Container(self.Password, padding=ft.padding.only(ancho * .04, altura * .03),
                                          ),
                                Container(Button, padding=ft.padding.only(ancho * .04, altura * .03)
                                          )
                            ])
                        ),
                        width=ancho * .45,
                        height=altura * .8,
                        bgcolor='#22ffffff',
                        border_radius=11,
                    )
                ]),
                padding=ancho * .09,
                width=ancho * .45,
                height=altura * .8,
                bgcolor='grey900'

            ),
            width=ancho * .45,
            height=altura * 1.1,
            gradient=ft.LinearGradient(['white30', 'white10']),
            border_radius=ft.border_radius.all(30),
            margin=ft.margin.symmetric(horizontal=(ancho*0.37)),

        )

        self.raiz.add(self.contenedor_login)

# ...................................Menus............................

# ...................................Menus............................

    def pedidos(self, var):
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
        self.contador.value = (
            "Habitaciones: ", totalH, "total de espacios: ", totalesp, "costo total: ", costo)
        self.contador.update()
        self.disponibles()

    def disponibles(self):
        global images

        def valor(a):
            indice = a
            infoH = ft.Row([
                ft.Container(width=50, height=50, bgcolor='#A3CD91',
                             border_radius=ft.border_radius.all(6),
                             margin=ft.margin.all(10),
                             alignment=ft.alignment.center,
                             content=ft.Text(value=self.variable2[a][0], color='#000000')),

                ft.Text(value="Piso: "+str(self.variable2[a][1]))
            ])
            infoH2 = ft.Row([
                ft.Text(value="Camas Individuales: " +
                        str(self.variable2[a][2])),

            ])
            infoH4 = ft.Row([
                ft.Text(value="Camas Matrimoniales: " +
                        str(self.variable2[a][3])),

            ])

            infoH3 = ft.Row([
                ft.Text(value="Costo: "+str(self.variable2[a][4])),
                ft.TextButton(
                    text="+", on_click=lambda _: self.pedidos(indice))
            ])
            contener = ft.Container(width=60, height=60,
                                    border_radius=ft.border_radius.all(3), bgcolor=colores[9],
                                    content=ft.Column([infoH, infoH2, infoH4, infoH3]))
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

    def Consulta_aux(self, Ingreso_Res, Egreso_Res):
        global hres
        hres = []
        self.variable2 = Consulta(Ingreso_Res, Egreso_Res)
        self.disponibles()

    def res_final(self, cli, emp, fecha, desc, hres, Ing, Eng):

        confirmar = ft.TextButton(text="Confirmar", icon_color="#659863", on_click=lambda _: completar(
            cli, emp, fecha, desc, hres, Ing, Eng))
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
        texto = "Numero de habitacion: " + \
            str(a)+" camas matrimoniales:"+str(c) + \
            " camas individuales:"+str(d)+" Costo:"+str(e)
        Container_menus.content = ft.Container(content=ft.Row([ft.Text(
            value=texto), confirmar]), bgcolor='#3B6639', width=ancho*0.56, height=altura*0.1, border_radius=ft.border_radius.all(3))
        Container_menus.update()

    def Reservar_Aux(self, cli, emp, fecha, desc):
        Container_menus.clean()
        Verificar = Reservar(cli, emp, fecha, desc)
        if Verificar == 1:
            Container_menus.clean()
            Ingreso_Res = create_text_field("Ingreso (aaaa-mm-dd)")
            Egreso_Res = create_text_field("Egreso (aaaa-mm-dd)")
            consultar = ft.TextButton(text="Consultar", on_click=lambda _: self.Consulta_aux(
                Ingreso_Res.value, Egreso_Res.value))
            reservarboton = ft.TextButton(text="el otro boton", on_click=lambda _: self.res_final(
                cli, emp, fecha, desc, hres, Ingreso_Res.value, Egreso_Res.value
            ))
            self.Departamentos = ft.Container(
                width=830, height=500, bgcolor=colores[2], margin=10)
            self.contador = ft.Text(value="")
            a = ft.Row([Ingreso_Res, Egreso_Res])
            b = ft.Row([consultar, reservarboton, self.contador])
            c = ft.Row([self.Departamentos])
            Container_menus.content = ft.Column([a, b, c])
            Container_menus.alignment = ft.alignment.top_center

            Container_menus.update()
        if Verificar == 2:
            # aca poner que el cliente no existe
            pass

    def Menu0(self):
        cod_cliente = create_text_field(
            "Dni de cliente")

        fecha_res = datetime.now().date()
        desc = create_text_field(
            "Descripción",
            multiline=True,
            max_length=200,
            max_lines=3)

        subir = ft.CupertinoButton(
            content=ft.Text("Next", color=ft.colors.BLACK),
            bgcolor=colores[1],
            on_click=lambda _: self.Reservar_Aux(cod_cliente.value, z[2], fecha_res, desc.value))

        Container_menus.content = ft.Column(
            [cod_cliente,
             desc,
             subir],
            expand=True,
        )
        Container_menus.alignment = ft.alignment.center
        Container_menus.update()
# ................................habitacion.......................

    def pedidosCoch(self, var):
        hres.append(self.variable2[var])
        images.controls.pop(var)
        images.update()
        self.variable2.pop(var)
        self.disponiblesCoch()

    def disponiblesCoch(self):
        global images

        def valor(a):
            indice = a
            infoH = ft.Row([
                ft.Text(value=self.variable2[a][0]),
                ft.Text(value=self.variable2[a][1])
            ])
            contener = ft.Container(width=60, height=60, bgcolor=colores[9], content=ft.Column(
                [infoH, ft.TextButton(text="+", on_click=lambda _: self.pedidosCoch(indice))]))
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

    def ConsultaCoch_aux(self, Ingreso_Res, Egreso_Res):
        global hres
        hres = []
        self.variable2 = ConsultaCoch(Ingreso_Res, Egreso_Res)
        self.disponiblesCoch()

    def resCoch_final(self, cli, emp, fecha, desc, hres, Ing, Eng):
        confirmar = ft.TextButton(text="Confirmar", icon_color="#659863", on_click=lambda _: completarCoch(
            cli, emp, fecha, desc, hres, Ing, Eng))
        Container_menus.clean()
        a = []
        for i in range(len(hres)):
            a.append(hres[i][0])

        texto = "Numeros de las habitaciones: "+str(a)
        Container_menus.content = ft.Container(content=ft.Row([ft.Text(
            value=texto), confirmar]), bgcolor='#3B6639', width=ancho*0.56, height=altura*0.1, border_radius=ft.border_radius.all(3))
        Container_menus.update()

        confirmar = ft.TextButton(text="Confirmar", on_click=lambda _: completarCoch(
            cli, emp, fecha, desc, hres, Ing, Eng))
        Container_menus.clean()
        Container_menus.update()

    def ReservarCoch_Aux(self, cli, emp, fecha, desc):
        Container_menus.clean()
        Verificar = ReservarCoch(cli, emp, fecha, desc)

        if Verificar == 1:
            Container_menus.clean()
            Ingreso_Res = create_text_field("Ingreso (aaaa-mm-dd)")
            Egreso_Res = create_text_field("Ingreso (aaaa-mm-dd)")
            consultar = ft.TextButton(text="Consultar", on_click=lambda _: self.ConsultaCoch_aux(
                Ingreso_Res.value, Egreso_Res.value))
            reservarboton = ft.TextButton(text="el otro boton", on_click=lambda _: self.resCoch_final(
                cli, emp, fecha, desc, hres, Ingreso_Res.value, Egreso_Res.value
            ))
            self.Departamentos = ft.Container(
                width=830, height=500, bgcolor=colores[2], margin=10)
            contador = ft.Text(value="")
            a = ft.Row([Ingreso_Res, Egreso_Res])
            b = ft.Row([consultar, reservarboton, contador])
            c = ft.Row([self.Departamentos])
            Container_menus.content = ft.Column([a, b, c])
            Container_menus.alignment = ft.alignment.top_center

            Container_menus.update()
        if Verificar == 2:
            pass

    def Menu1(self):
        cod_cliente = create_text_field("Dni de cliente")
        fecha_res = datetime.now().date()
        desc = create_text_field(
            "Descripcion", multiline=True, max_length=200, max_lines=3)
        subir = ft.CupertinoButton(
            content=ft.Text("Subir", color=ft.colors.BLACK),
            bgcolor=colores[1],
            border_radius=ft.border_radius.all(15),
            on_click=lambda _: self.ReservarCoch_Aux(cod_cliente.value, z[2], fecha_res, desc.value))

        Container_menus.content = ft.Column(
            [cod_cliente,
             desc,
             subir],
            expand=True
        )
        Container_menus.alignment = ft.alignment.center
        Container_menus.update()
# ................................cochera.......................

    def Cli_Aux(self, a, b, c, d):
        Verificar = Cli_add(a, b, c, d)
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
        cod_cliente = create_text_field("Dni de cliente")
        nom_cli = create_text_field("Nombre")
        email_cli = create_text_field("Email")
        desc_cli = create_text_field(
            "Descripcion", multiline=True, max_length=200, max_lines=3)
        subir_cli = ft.CupertinoButton(
            content=ft.Text("Subir", color=ft.colors.BLACK),
            bgcolor=colores[1],
            border_radius=ft.border_radius.all(15),
            on_click=lambda _: self.Cli_Aux(cod_cliente.value, nom_cli.value, email_cli.value, desc_cli.value))

        Container_menus.content = ft.Column(
            [cod_cliente,
             nom_cli,
             email_cli,
             desc_cli,
             subir_cli],
            expand=True
        )
        Container_menus.alignment = ft.alignment.center
        Container_menus.update()
# ......................cliente...............

    def Menu3(self):
        cocherav = ft.CupertinoButton(
            text="cochera", on_click=lambda _: self.cochera(), bgcolor=colores[5])
        habitacionv = ft.CupertinoButton(
            text="habitacion", on_click=lambda _: self.habitacion(), bgcolor=colores[5])
        Container_menus.content = ft.Row([cocherav, habitacionv])
        Container_menus.padding = ft.padding.symmetric(horizontal=ancho*0.18)
        Container_menus.update()

    def crear_coch(self, a):
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
        piso_coch = create_text_field("Piso")
        subir_coch = ft.CupertinoButton(
            content=ft.Text("Subir", color=ft.colors.BLACK),
            bgcolor=colores[1],
            border_radius=ft.border_radius.all(15),
            on_click=lambda _: self.crear_coch(piso_coch.value))
        Container_menus.content = ft.Column(
            [piso_coch, subir_coch
             ],
            expand=True
        )
        Container_menus.update()

    def crear_habitacion(self, a, b, c, d):
        validacion = crear_hab(a, b, c, d)
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
        piso = create_text_field("Piso")
        camamatr = create_text_field("camas matrimoniales")
        camaind = create_text_field("camas individuales")
        costo = create_text_field("Costo")
        subir_cli = ft.CupertinoButton(
            content=ft.Text("Subir", color=ft.colors.BLACK),
            bgcolor=colores[1],
            border_radius=ft.border_radius.all(15),
            on_click=lambda _: self.crear_habitacion(piso.value, camamatr.value, camaind.value, costo.value))
        Container_menus.content = ft.Column(
            [piso,
             camamatr,
             camaind,
             costo,
             subir_cli],
            expand=True
        )
        Container_menus.update()
# ....................elementos........................

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
        dni_emp = create_text_field("Dni del empleado")
        nombre_emp = create_text_field("Nombre")
        email = create_text_field("Email")
        telefono = create_text_field("Telefono")
        puesto = create_text_field("Puesto")
        usuario = create_text_field("Usuario")
        contraseña = create_text_field("Contraseña")
        nivel = create_text_field("Nivel de acceso")
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
                       "Añadir Cliente": 2, "Añadir elementos": 3, "Añadir Empleado": 4, "nose": 5}
        Indices_menus = {0: self.Menu0, 1: self.Menu1,
                         2: self.Menu2, 3: self.Menu3, 4: self.Menu4, 5: self.Menu5}
        Indices_menus[diccionario[a]]()

    def UserData(self, name: str):
        # Fila exclusiva para la informacion del usuario

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
# ....................empleado.........................

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
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    ft.icons.BOOKMARK_BORDER, color=ft.colors.BLACK),
                selected_icon_content=ft.Icon(
                    ft.icons.BOOKMARK, color=ft.colors.BLACK),
                label_content=ft.Text("6", color=ft.colors.BLACK)
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
                    self.ContainerIcon(ft.icons.PIE_CHART_OUTLINE, "nose")

                ]
            ),)

        penas = Container(
            width=200,
            height=1000,
            bgcolor='black',
            border_radius=3,
            content=Left_bar
        )
        Container_menus = ft.Container(
            width=ancho - penas.width,
            height=850,
            bgcolor=colores[3],
            border_radius=ft.border_radius.all(3)
        )

        print(f"El ancho tendría que ser de {ancho - penas.width}")
        self.raiz.add(ft.Row(
            [
                penas,
                ft.Container(
                    Container_menus,
                    width=ancho,
                    height=850,
                )
            ],
            expand=True,
        )
        )

# ...................calendario.......................
    def Menu5(self):
        def Calendario_menu(ing, eng):
            a = ing.replace("-", "")
            e = eng.replace("-", "")
            matris = calendario()
            for i in range(len(matris)):
                y = matris[i][1].replace("-", "")
                x = matris[i][2].replace("-", "")
                if int(x) > int(a) and int(y) < int(e):
                    print(matris[i], "ocupado")

                else:

                    print(matris[i], "desocupado")

        self.Ingreso_Res = create_text_field("Ingreso (aaaa-mm-dd)")
        self.Egreso_Res = create_text_field("Egreso (aaaa-mm-dd)")
        consultar = ft.TextButton(
            text="Consultar",
            on_click=lambda _: Calendario_menu(
                self.Ingreso_Res.value,
                self.Egreso_Res.value)
        )
        Container_menus.content = ft.Row(
            [self.Ingreso_Res, self.Egreso_Res, consultar],
        )
        Container_menus.alignment = ft.alignment.top_center

        Container_menus.update()


while True:
    if codigo == 0:
        def main(raiz: ft.Page):
            global altura
            global ancho
            altura = raiz.window_height
            ancho = raiz.window_width
            print(altura, ancho)
            raiz.window_resizable = False
            raiz.window_full_screen = True
            raiz.update()
            objeto = Plantilla(raiz, idioma, español, ingles)
            objeto.ej()
            z = objeto.appbar()
            objeto.login_menu()
        ft.app(target=main)
    else:
        break
