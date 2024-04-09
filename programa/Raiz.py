# ____________________________________________LIBRERIAS____________________________________________
from crearBase import * 
import flet as ft
from flet import *
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent
from datetime import datetime

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
#_____________________________crear bases___________________
e = 0
d = 0
creardb()
#_____________________________________________IDIOMA___________________________________________

cual = 0

class Maestro:
    def __init__(self):
        pass
    def Ingles(e):

        def main(raiz: ft.Page):
        
            # seteo de la pagina
            raiz.window_prevent_close = True
            raiz.window_height = 740
            raiz.window_width = 580
            raiz.window_bgcolor = colores2[10]
            raiz.bgcolor = ft.colors.TRANSPARENT
            raiz.window_title_bar_hidden = True
            raiz.window_frameless = True
            raiz.window_resizable = False
            raiz.padding = 10
            # ------------------------------------- 
            
            #---------------Funciones de contenedor-------------------------------       
            def OFF(e):    
                global cual    
                raiz.window_destroy()
                cual = 2
        
            def logear(e):
                global Nivel
                global z
                z =  login(User.value,Password.value)
                try:
                    if z[0]:
                        Nivel = int(z[1])
                        Menu()
                        Menu0()
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
            # ------------CONTENEDOR V2------------
    
            User : TextField = TextField(
                                            width=290,
                                            height=60,
                                            label='User',
                                            border='underline',
                                            color='#303030',
                                            prefix_icon = icons.PERSON,
                                        )
            Password : TextField = TextField(
                                            width=280,
                                            height=60,
                                            label='Password',
                                            border='underline',
                                            color='#303030',
                                            prefix_icon= icons.LOCK,
                                        )
            Button : ElevatedButton=ElevatedButton(
                                            content=Text(
                                                'SIGN IN',
                                                color='white',
                                                weight='w500',
                                                
                                            ),width=280,
                                            bgcolor='black',
                                            on_click=logear,
                                        )
                                    
    
            body = Container(
                Container(
                    Stack([
                        Container(
                            border_radius=11,
                            rotate=Rotate(0.98*3.14), #Degree
                            width=360,
                            height=560,
                            bgcolor='#22ffffff'
                        ),
                        Container(
                            Container(
                                Column([
                                    Container(
                                        Image(
                                            src='axys.png',
                                            width=50,
                                        ),padding=padding.only(150,20),
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
                                    Container(User,padding=padding.only(25,20)
                                        ),
                                    Container(Password,padding=padding.only(25,20),
                                    ),
                                    Container(
                                        TextButton(
                                            'I forgot my password: ',
                                        ),padding=padding.only(90),
                                    ),
                                    Container(Button,padding=padding.only(40,10)
                                    ),
                                    Container(
                                        Row([
                                            Text(
                                                'Don`t have an account?',
                                            ),
                                            TextButton(
                                                'Create a account',
                                            )
                                        ],spacing=-10),padding=padding.only(40),
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
                gradient=LinearGradient(['white30','white10'])
            )



            # ------------CONTENEDOR V2------------

            # ------------CONTENEDOR------------
            

            raiz.add(body)


            #_______________________________SUB MENUS______________________________________
            """
            Menu 0 generar una reserva
            menu 1 ingresar cliente
            Menu 3 crear Habitacion y cochera
            Menu 4 registro de empleado
            """



            def Menu0():

                def Reservar_Aux(cli,emp,fecha,desc):
                    Container_menus.clean()
                    print("hola")
                    Verificar = Reservar(cli,emp,fecha,desc)
                    print(Verificar)

                    if Verificar == 1:
                        def Consulta_aux(Ingreso_Res,Egreso_Res):
                            
                            variable = Consulta(Ingreso_Res,Egreso_Res)

                            def valor(z):
                                pera = ft.TextField(value=variable[z],width=300)
                                a = ft.Container(content=ft.Row(spacing=10,controls=[pera,ft.TextButton(text="+",on_click=lambda _:print(pera.value))]))
                                return a
                            images = ft.GridView(
                                height=400,
                                width=800,
                                runs_count=5,
                                max_extent=500,
                                child_aspect_ratio=1.0,
                                spacing=20,
                                run_spacing=5,
                            )

                            for i in range(len(variable)):
                                images.controls.append(valor(i))
                            Container_menus.clean()
                            Container_menus.content = ft.Column([a,b,images])
                            Container_menus.alignment = ft.alignment.top_center
                                                                           
                            Container_menus.update()


                        Container_menus.clean()
                        Ingreso_Res = ft.TextField(label="Ingreso (aaaa-mm-dd)")
                        Egreso_Res = ft.TextField(label="Egreso (aaaa-mm-dd)")
                        consultar = ft.TextButton(text="Consultar",on_click=lambda _:Consulta_aux(Ingreso_Res.value,Egreso_Res.value))
                        
                        a=ft.Row([Ingreso_Res,Egreso_Res])
                        b=ft.Row([consultar])
                        Container_menus.content = ft.Column([a,b])
                        Container_menus.alignment = ft.alignment.top_center
                        
                        Container_menus.update()


                    if Verificar == 2:
                        #aca poner que el cliente no existe
                        pass
                    
                
                            
                cod_cliente = ft.TextField(label="Dni de cliente",width=300)
                fecha_res = datetime.now().date()
                desc = ft.TextField(label="descripcion",multiline=True, width= 500, max_length=200, max_lines=3)
                subir = ft.CupertinoButton(
                    content=ft.Text("Subir", color=ft.colors.BLACK),
                    bgcolor=colores[1],
                    border_radius=ft.border_radius.all(15),
                    on_click=lambda _:Reservar_Aux(cod_cliente.value,z[0],fecha_res,desc.value))
                
                Container_menus.content = ft.Column (
                    [cod_cliente,
                    desc,
                    subir],
                    expand= True
                )
                Container_menus.alignment = ft.alignment.center
                Container_menus.update()

            def Menu1():
                #Ingresar cliente
                def Cli_Aux(a,b,c,d):
                    Verificar = Cli_add(a,b,c,d)
                    if Verificar:
                        dlg = ft.AlertDialog(
                        title=ft.Text("Datos Ingresados")
                        )
                        def open_dlg(e):
                            raiz.dialog = dlg
                            dlg.open = True
                            raiz.update()
                        open_dlg(e)
                        Container_menus.clean()
                        Menu1()

                cod_cliente = ft.TextField(label="Dni de cliente",width=300)
                nom_cli = ft.TextField(label="Nombre",width=300)
                email_cli = ft.TextField(label="Email",width=300)
                desc_cli = ft.TextField(label="descripcion",multiline=True, width= 500, max_length=200, max_lines=3)
                subir_cli = ft.CupertinoButton(
                    content=ft.Text("Subir", color=ft.colors.BLACK),
                    bgcolor=colores[1],
                    border_radius=ft.border_radius.all(15),
                    on_click=lambda _:Cli_Aux(cod_cliente.value,nom_cli.value,email_cli.value,desc_cli.value))
                
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

            def Menu2():
                pass
            def Menu3():
                def cochera():
                    def crear_coch_aux(piso):
                        validacion = crear_coch(piso)
                        if validacion:
                            dlg = ft.AlertDialog(
                            title=ft.Text("cochera registrada")
                            )
                            def open_dlg(e):
                                raiz.dialog = dlg
                                dlg.open = True
                                raiz.update()
                            open_dlg(e)
                            Container_menus.clean()
                            Menu3()
                    piso_coch = ft.TextField(label="piso")
                    subir_coch = ft.CupertinoButton(
                        content=ft.Text("Subir", color=ft.colors.BLACK),
                        bgcolor=colores[1],
                        border_radius=ft.border_radius.all(15),
                        on_click=lambda _:crear_coch_aux(piso_coch.value))
                    Container_menus.content = ft.Column (
                        [piso_coch,subir_coch
                        ],
                        expand= True
                    )
                    Container_menus.update()

                def habitacion():
                    #crear habitaciones
                    def crear_hab_aux(a,b,c,d):
                        validacion = crear_hab(a,b,c,d)
                        if validacion:
                            dlg = ft.AlertDialog(
                            title=ft.Text("Habitacion registrada")
                            )
                            def open_dlg(e):
                                raiz.dialog = dlg
                                dlg.open = True
                                raiz.update()
                            open_dlg(e)
                            Container_menus.clean()
                            Menu3()

                    piso = ft.TextField(label="Piso",width=300)
                    camamatr = ft.TextField(label="camas matrimoniales",width=300)
                    camaind = ft.TextField(label="camas individuales",width=300)
                    costo = ft.TextField(label="costo",width=300)
                    subir_cli = ft.CupertinoButton(
                        content=ft.Text("Subir", color=ft.colors.BLACK),
                        bgcolor=colores[1],
                        border_radius=ft.border_radius.all(15),
                        on_click=lambda _:crear_hab_aux(piso.value,camamatr.value,camaind.value,costo.value))
                    Container_menus.content = ft.Column (
                        [piso,
                        camamatr,
                        camaind,
                        costo,
                        subir_cli],
                        expand= True
                    )
                    Container_menus.update()
                cocherav = ft.CupertinoButton(text="cochera",width=300,on_click=lambda _:cochera(),bgcolor=colores[5])
                habitacionv = ft.CupertinoButton(text="habitacion",width=300,on_click=lambda _:habitacion(),bgcolor=colores[5])
                Container_menus.content = ft.Row([cocherav,habitacionv])
                Container_menus.alignment = ft.alignment.center
                Container_menus.update()
            
            def Menu4():
                #--------------Funciones--------------
                def reg_emp_aux(dni_emp,nombre_emp,email,telefono,puesto,usuario,contraseña,nivel):
                    validacion = reg_emp(dni_emp,nombre_emp,email,telefono,puesto,usuario,contraseña,nivel)
                    if validacion:
                        dlg = ft.AlertDialog(
                        title=ft.Text("Registro completo")
                        )
                        def open_dlg(e):
                            raiz.dialog = dlg
                            dlg.open = True
                            raiz.update()
                        open_dlg(e)
                        Container_menus.clean()
                        Menu4()

                    
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


                

            #_____________________________formatos de los sub menus_________________________
            def Selector(a):
                Indices_menus = {0:Menu0,1:Menu1,2:Menu2,3:Menu3,4:Menu4}
                Indices_menus[a]()   
            # ________________________________MENU__________________________________________
            def Menu():
                global Container_menus
                raiz.appbar = ft.AppBar(
                title=nombre,
                center_title=True,
                bgcolor=colores2[8],
                actions=[
                    ft.IconButton(ft.icons.EXIT_TO_APP_ROUNDED,on_click=OFF, icon_size=35,),
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

            #______________________Menu__________________________________
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
                Container_menus = ft.Container(width=850,height=650,bgcolor=colores[3])
     
                raiz.add(ft.Row(
                        [
                            rail,
                            ft.VerticalDivider(width=1),
                            Container_menus
                        ],
                        expand=True,
                    )
                )
                

        ft.app(target=main)

    def Español(e):    
        pass
#______________________selector de idioma__________________________________
Controlador = Maestro()
while True:
    if cual == 0:
        Controlador.Ingles()
    if cual == 1:
        Controlador.Español()
    if cual == 2:
        break