import flet
from flet import * 
from functools import partial
import time

x = int(input("Nivel de usuario: \n1_Administrador\n2_Empleado\n3_Cliente\n"))

# Esto hay que conectarlo con la base de datos
niveles = (("CS", "Camilo Sanchez", "Administrador"),("JL", "Josefina Lopez", "Empleada"),("JS", "Jose Sanchez", "Cliente"))

# ___________________________________________________________Sidebar Class___________________________________________________________


class ModernNavBar(UserControl):
    def __init__(self, func ):
        self.func = func
        super().__init__()

    # Destacamos la columna en la que pasamos por encima
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


    def UserData(self, initials:str, name:str, descripcion:str):
        # Fila esclusiva para la informacion del usuario

        return Container(
            content=Row(
                controls=[
                    Container(
                        width=42,
                        border_radius = 8,
                        height=42,
                        bgcolor='bluegrey900',
                        alignment=alignment.center,
                        content=Text(
                            value=initials,
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

                            ),
                            Text(
                                value=descripcion,
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

    # Filas del sidebar (Fila y iconos)

    def ContainerIcon(self, icon_name:str, text:str):
        return Container(
            width=180, 
            height=45,
            border_radius=10,
            on_hover=lambda e: self.HighLight(e),
            content=Row(
                controls=[
                    IconButton(
                        icon=icon_name,
                        icon_size=18,
                        icon_color='white54',
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=7),
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
        return Container(
            # Definimos las caracteristicas del container
            width=200,
            height=580,
            padding=padding.only(top=10),
            alignment=alignment.center,
            content = Column(

                alignment=alignment.center,
                horizontal_alignment="center",

                controls =[
                    # Los iconos del SideBar aca

                    # Nivel y informacion del usuario(3 Niveles , Administrador ,empleado, cliente)
                    self.UserData(niveles[x-1][0],niveles[x-1][1], niveles[x-1][2]),


                    # Boton para redimensionar 

                    Container(
                        width= 24,
                        height=24,
                        bgcolor= "bluegrey800",
                        border_radius= 8,
                        on_click=partial(self.func),
                        # Func es la animacion para minimizar y maximizar
                    ),

                    # Divisor
                    Divider(height=2 , color='transparent'),
                    self.ContainerIcon(icons.SEARCH,"Search"),
                    self.ContainerIcon(icons.DASHBOARD_ROUNDED,"Bashboard"),
                    self.ContainerIcon(icons.BAR_CHART,"Analitics"),
                    self.ContainerIcon(icons.NOTIFICATIONS,"Nofications"),
                    self.ContainerIcon(icons.PIE_CHART,"Analitics"),
                    
                    # Divisor
                    Divider(height=5, color="white54"),
                    self.ContainerIcon(icons.FAVORITE_ROUNDED,"Likes"),

                ]
            ),
        )

# ___________________________________________________________Sidebar Class___________________________________________________________

# ___________________________________________________________LogIn Class___________________________________________________________

# class UserLogIn():
#     def __init__(self):
#         super().__init__()

#     def HighLight(self,e):
#         if e.data == "true":
#             e.control.bgcolor= "white10"
#             e.control.update()

#             # Ahora lo que hago aparte de cambiar el color de fondo, el texto

#             # Control del contenido por indice del IconButton y el texto
#             e.control.content.controls[0].icon_color = "white"
#             e.control.content.controls[1].icon_color = "white"
#             e.control.content.update()


#         else:
#             e.control.bgcolor= None
#             e.control.update()

#             # Ahora lo que hago aparte de cambiar el color de fondo, el texto

#             # Control del contenido por indice del IconButton y el texto
#             e.control.content.controls[0].icon_color = "white54"
#             e.control.content.controls[1].icon_color = "white54"
#             e.control.content.update()


#     # Filas del sidebar (Fila y iconos)

#     def TextLog(self, icon_name:str, text:str):
#         return Container(
#             width=180, 
#             height=45,
#             border_radius=10,
#             on_hover=lambda e: self.HighLight(e),
#             content=Row(
#                 controls=[
#                     Icon(
#                         icon=icon_name,
#                         icon_size=18,
#                         icon_color='white54',
#                     ),
#                     TextField(
#                         value=text,
#                         color="white54",
#                         size=11,
#                         opacity=1,
#                         animate_opacity=200,
#                     )
#                 ]
#             ),

#         )

#     def build(self):
#         return Container(
#             width=200,
#             height=580,
#             padding=padding.only(top=10),
#             alignment=alignment.center,
#             content = Column(

#                 alignment=alignment.center,
#                 horizontal_alignment="center",

#                 controls =[
#                     # Los iconos del SideBar aca

#                     # Nivel y informacion del usuario(3 Niveles , Administrador ,empleado, cliente)
#                     self.UserData(niveles[x-1][0],niveles[x-1][1], niveles[x-1][2]),


#                     # Boton para redimensionar 

#                     Container(
#                         width= 24,
#                         height=24,
#                         bgcolor= "bluegrey800",
#                         border_radius= 8,
#                         on_click=partial(self.func),
#                         # Func es la animacion para minimizar y maximizar
#                     ),

#                     # Divisor
#                     Divider(height=2 , color='transparent'),
#                     self.TextLog(icons.PERSON,"User"),
#                     self.TextLog(icons.LOCK,"Password"),

#                     # Divisor
#                     Divider(height=5, color="white54"),

#                 ]
#             ),
#         )


# ___________________________________________________________LogIn Class___________________________________________________________


# ___________________________________________________________VENTANA PRINCIPAL___________________________________________________________

# Ventana principal
def main(page: Page):
    # Titulo 
    page.title = "Innaxys"

    # Centralizado
    page.window_height = 700
    page.window_width = 500
    page.horizontal_alignment='center'
    page.vertical_alignment='center'


    # Animated sidebar
    def AnimatedSidebar(e):
        # Pasos para animar el sidebar

        #page.controls[0] es la clase a la que llamamos,  y en base a las caracteristicas del ancho de la clase
        # vamos a modificar esto 
        if page.controls[0].width != 62:
            #

            #Iteracion a traves de las filas 

            # Se reduce la opacidad de el titulo del texto
            for item in(
                page.controls[0]
                # Ingresamos a content(Contenido) del contenedor
                .content.controls[0]
                # Ingresamos a las filas de content(Contenedor) 
                .content.controls[0]

                # Otra layer aca(!)
                .content.controls[1]

                # : Indica la lista entera de controles
                .controls[:]
            ):
                item.opacity = (
                    0 #  Cada item ahora se refiere a los Text() control in the sidebar
                )
                item.update()

            # Reduccion de la opacidad del sidebar de los items del menu
            for items in page.controls[0].content.controls[0].content.controls[3:]:
                if isinstance(items, Container):
                    items.content.controls[1].opacity = 0
                    items.content.update()

            time.sleep(0.2)

            # Maximizamos la ventana
            page.controls[0].width = 62
            page.controls[0].update()

            time.sleep(0.2)


        else:
                page.controls[0].width = 200
                page.controls[0].update()
                for item in(
                    page.controls[0]
                    .content.controls[0]
                    .content.controls[0]
                    .content.controls[1]
                    .controls[:]
                ):
                    item.opacity = 1 
                    item.update()

                for items in page.controls[0].content.controls[0].content.controls[3:]:
                    if isinstance(items, Container):
                        items.content.controls[1].opacity = 1
                        items.content.update()


    # Agregamos la clase a la pagina

    # Agregando a la pagina principal el LogIN
    # page.add(
    #     Container(
    #         width=500,
    #         height=700,
    #         bgcolor='black',
    #         border_radius=25,
    #         alignment=alignment.center,
    #         padding=10,
    #         content=UserLogIn(),
    #     )
    # )

    # Clausula que denomina si la contra esta bien

    # if clave y usuario True:
    # page.clean()
    page.add(
        Container(
            width=200,
            height=500,
            bgcolor='black',
            border_radius=10,
            animate= animation.Animation(500,'decelerate'), #Animacion del SideBar
            alignment=alignment.center,
            padding=10,
            content=ModernNavBar(AnimatedSidebar)
        )
    )

# ___________________________________________________________VENTANA PRINCIPAL___________________________________________________________


#Ejecucion.
flet.app(target=main)