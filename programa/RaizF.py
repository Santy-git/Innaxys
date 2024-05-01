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
español = {1: "axys", 2: "Ingresar",
           }
idioma = español
ingles = {1: "axys", 2: "Sing in", 3: "User", 4: "Password", 5: "SIGN IN", 6: "Admin", 7: "Employees", 8: "Room booking", 9: "Park booking",
          10: "Add client",
          11: "Add element",
          12: "Add employee",
          13: "calendar",
          14: "client id",
          15: "Description",
          16: "Query",
          17: "Check in",
          18: "Check out",
          19: "Query",
          20: "Confirm",
          21: "Name",
          22: "Mail",
          23: "Upload",
          24: "Parking",
          25: "Room",
          26: "Floor",
          27: "boked parking",
          28: "Queen size bed",
          29: "Bed",
          30: "Price",
          31: "Employee id",
          32: "Phone",
          33: "Job",
          34: "Access level",
          }
codigo = 0

Meses = {'01': 31,
         '02': 29,
         '03': 31,
         '04': 30,
         '05': 31,
         '06': 30,
         '07': 31,
         '08': 31,
         '09': 30,
         '10': 31,
         '11': 30,
         '12': 31}


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
        try:
            if z[0]:
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
            self.idioma[1], color=colores[9],), bgcolor=colores[3], width=ancho*0.1, height=altura*0.05, border_radius=ft.border_radius.all(10))
        self.nombre.alignment = ft.alignment.center

        self.raiz.appbar = ft.AppBar(
            title=self.nombre,
            center_title=True,
            bgcolor=colores[8],
            actions=[
                ft.IconButton(ft.icons.LANGUAGE,
                              on_click=self.EnEs, icon_size=ancho*.03),
                ft.IconButton(ft.icons.EXIT_TO_APP_ROUNDED,
                              on_click=self.OFF, icon_size=ancho*.03),
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
            height=altura * .08,
            label='User',
            border='underline',
            color='white',
            prefix_icon=ft.icons.PERSON,)

        self.Password: TextField = TextField(
            width=ancho * .2,
            height=altura * .08,
            label='Password',
            border='underline',
            color='white',
            prefix_icon=ft.icons.LOCK,)

        self.Button: ElevatedButton = ElevatedButton(
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
                        border_radius=ancho*.005,
                        rotate=ft.Rotate(0.98*3.1),  # Degree
                        width=ancho * .2,
                        height=altura * .5,
                        bgcolor='#22ffffff'
                    ),
                    Container(
                        Container(
                            Column([
                                Text(
                                    'Sign in',
                                    width=ancho * .2,
                                    size=altura * .03,
                                    text_align='center',
                                ),
                                Text(
                                    'Please login to use the plataform',
                                    width=ancho * .2,
                                    text_align='center',

                                ),
                                Container(self.User, padding=ft.padding.symmetric(horizontal=ancho * .03)
                                          ),
                                Container(self.Password, padding=ft.padding.symmetric(horizontal=ancho * .03)
                                          ),
                                Container(self.Button, padding=ft.padding.symmetric(horizontal=ancho * .03)
                                          )
                            ])
                        ),
                        width=ancho * .2,
                        height=altura * .5,
                        bgcolor='#22ffffff',
                        border_radius=ancho*0.005,
                    )
                ]),
                alignment=ft.alignment.center,
                width=ancho * 0.3,
                height=altura * 0.6,
                bgcolor='grey900'

            ),
            width=(ancho/100)*30,
            height=(altura/100)*70,
            border_radius=ft.border_radius.all(ancho*.005),
            margin=ft.margin.symmetric(horizontal=ancho*0.33)
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

    def Consulta_aux(self, Ingreso_Res, Egreso_Res,num):
        global hres
        hres = []
        self.variable2 = Consulta(Ingreso_Res, Egreso_Res,num)
        self.disponibles()

    def res_final(self, cli, emp, fecha, desc, hres, Ing, Eng,num):
        if num != 0:
            confirmar = ft.TextButton(text="Confirmar", icon_color="#659863", on_click=lambda _: completar_actualizar(
                cli, emp, fecha, desc, hres, Ing, Eng,num))
        else:
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

    def Reservar_Aux(self, cli, emp, fecha, desc,num):
        Container_menus.clean()
        Verificar = Reservar(cli, emp, fecha, desc)
        if Verificar == 1:
            Container_menus.clean()
            Ingreso_Res = create_text_field("Ingreso (aaaa-mm-dd)")
            Egreso_Res = create_text_field("Egreso (aaaa-mm-dd)")
            consultar = ft.TextButton(text="Consultar", on_click=lambda _: self.Consulta_aux(
                Ingreso_Res.value, Egreso_Res.value,num))
            reservarboton = ft.TextButton(text="el otro boton", on_click=lambda _: self.res_final(
                cli, emp, fecha, desc, hres, Ingreso_Res.value, Egreso_Res.value,num
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
# ...............lo de arriba es la reserva subir..............

    def res_eliminar_aux(self, dni):
        info = consulta_eliminar(dni)
        registro = ft.Column(
            width=Container_menus.width - 100,
            height=Container_menus.height - 100,
            spacing=2,
            scroll=ft.ScrollMode.ALWAYS,
            on_scroll_interval=0,
        )

        for i in range(len(info)):
            self.text = ft.Text(value="codigo de reserva:"+str(info[i][0])+"   codigo del empleado: "+str(
                info[i][2])+"   fecha de reserva: "+str(info[i][3]),)
            registro.controls.append(ft.Row(controls=[self.text]))
        codigo = ft.TextField(label="codigo de reserva a modificar")
        registro.controls.append(
            ft.Row(
                controls=[codigo,
                          ft.IconButton(icon=ft.icons.DELETE,
                                        icon_size=30,
                                        width=60,
                                        height=60,
                                        on_click=lambda _: eliminar_reserva(
                                            codigo.value)
                                        )]))
        Container_menus.clean()
        Container_menus.content = registro
        Container_menus.update()

# ...............eliminar reservas arriba....................



    def dador(self,cod,info,dni):

        for j in range(len(info)):
            if str(cod) == str(info[j][0]):
                self.Reservar_Aux(dni,str(
                info[j][2]),
                datetime.now().date(),
                info[j][4],
                cod
                )

    def res_actualizar(self, dni):
        info = consulta_eliminar(dni)
        registro = ft.Column(
            width=Container_menus.width - 100,
            height=Container_menus.height - 100,
            spacing=2,
            scroll=ft.ScrollMode.ALWAYS,
            on_scroll_interval=0,
        )

        for i in range(len(info)):
            self.text = ft.Text(value="codigo de reserva:"+str(info[i][0])+"   codigo del empleado: "+str(
                info[i][2])+"   fecha de reserva: "+str(info[i][3]),)
            registro.controls.append(ft.Row(controls=[self.text]))
        codigo = ft.TextField(label="codigo de reserva a modificar")
        registro.controls.append(
            ft.Row(
                controls=[codigo,
                          ft.IconButton(icon=ft.icons.SEND,
                                        icon_size=30,
                                        width=60,
                                        height=60,
                                        on_click=lambda _:self.dador(codigo.value,info,dni)                                  
                                        )]))
        Container_menus.clean()
        Container_menus.content = registro
        Container_menus.update()
#................actualizar reserva.......................

    def Menu0(self):
        cod_cliente = create_text_field(
            "Dni de cliente")

        fecha_res = datetime.now().date()
        desc = create_text_field(
            "Descripción",
            multiline=True,
            max_length=200,
            max_lines=3)

        eliminar = ft.CupertinoButton(
            content=ft.Text("eliminar", color=ft.colors.BLACK),
            bgcolor=colores[1],
            on_click=lambda _: self.res_eliminar_aux(cod_cliente.value))

        modificar = ft.CupertinoButton(
            content=ft.Text("modificar", color=ft.colors.BLACK),
            bgcolor=colores[1],
            on_click=lambda _: self.res_actualizar(cod_cliente.value))

        subir = ft.CupertinoButton(
            content=ft.Text("subir", color=ft.colors.BLACK),
            bgcolor=colores[1],
            on_click=lambda _: self.Reservar_Aux(cod_cliente.value, z[2], fecha_res, desc.value,0))
        botones = ft.Row(controls=[eliminar, modificar, subir])
        Container_menus.content = ft.Column(
            [cod_cliente,
             desc,
             botones],
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
                       "Añadir Cliente": 2, "Añadir elementos": 3, "Añadir Empleado": 4, "Calendario": 5}
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

    def Menu5(self):
        def Calendario_menu(mes, año):

            # aca estan los elementos visuales
            cl = ft.Column(
                width=Container_menus.width-50,
                height=Container_menus.height-50,
                spacing=2,
                scroll=ft.ScrollMode.ALWAYS,
                on_scroll_interval=0,
            )

            mes_consulta = str(año)+'-'+str(mes)+'-'+'01'
            año_consulta = str(año)+'-'+str(mes)+'-'+str(Meses[mes])
            matris = calendario(mes_consulta, año_consulta)

            # listas para armar la tabla
            verificador = [[0, 0, 0]]
            for i in range(len(matris[0])):
                y = datetime.fromisoformat(matris[0][i][1])
                y = y.strftime("%d")
                x = datetime.fromisoformat(matris[0][i][2])
                x = x.strftime("%d")
                verificador.append([matris[0][i][0], y, x])

            for j in range(len(matris[1])):
                dias = [ft.Text(bgcolor=colores[4],
                                value="hab:"+str(matris[1][j][0])),]
                for o in range(Meses[mes]):
                    bandera = 0
                    for i in range(len(verificador)):
                        if o+1 >= int(verificador[i][1]) and o+1 <= int(verificador[i][2]) and int(matris[1][j][0]) == int(verificador[i][0]):
                            bandera = 1
                    if bandera == 1:
                        dias.append(ft.Container(width=20, height=20, bgcolor='red', content=ft.Text(
                            value=o+1), alignment=ft.alignment.center))
                    else:
                        dias.append(ft.Container(width=20, height=20, bgcolor='green', content=ft.Text(
                            value=o+1), alignment=ft.alignment.center))

                cl.controls.append(ft.Row(controls=dias,width=Container_menus.width -100))


            container_calendar = ft.Container(cl, border=ft.border.all(1))
            elementos.controls.append(container_calendar)
            Container_menus.update()

        self.Ingreso_Res = create_text_field("Mes (mm)")
        self.Egreso_Res = create_text_field("Año(aaaa)")
        consultar = ft.TextButton(
            text="Consultar",
            on_click=lambda _: Calendario_menu(
                self.Ingreso_Res.value,
                self.Egreso_Res.value)
        )

        input_fecha = ft.Row([self.Ingreso_Res, self.Egreso_Res, consultar])
        elementos = ft.Column([input_fecha])
        Container_menus.content = elementos
        Container_menus.alignment = ft.alignment.top_center

        Container_menus.update()
# ...................calendario.......................

# .....................modificar.......................

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
                    self.ContainerIcon(
                        ft.icons.PIE_CHART_OUTLINE, "Calendario"),
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


while True:
    if codigo == 0:
        def main(raiz: ft.Page):
            global altura
            global ancho
            ancho = 1280
            altura = 720
            raiz.window_resizable = False
            raiz.window_title_bar_hidden = True
            raiz.window_width = 1280
            raiz.window_height = 720
            raiz.window_center()
            raiz.update()
            objeto = Plantilla(raiz, idioma, español, ingles)
            objeto.ej()
            z = objeto.appbar()
            objeto.login_menu()
        ft.app(target=main)
    else:
        break
