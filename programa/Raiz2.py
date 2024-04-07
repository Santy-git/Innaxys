import flet
from flet import * 
from functools import partial
import time

x = int(input("Nivel de usuario: \n1_Administrador\n2_Empleado\n3_Cliente\n"))

# Esto hay que conectarlo con la base de datos
niveles = (("CS", "Camilo Sanchez", "Administrador"),("JL", "Josefina Lopez", "Empleada"),("JS", "Jose Sanchez", "Cliente"))

# Sidebar Class
class ModernNavBar(UserControl):
    def __init__(self):
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
                controls =[
                    # Los iconos del SideBar aca

                    # Nivel y informacion del usuario(3 Niveles , Administrador ,empleado, cliente)
                    self.UserData(niveles[x-1][0],niveles[x-1][1], niveles[x-1][2]),

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
    

# Ventana principal
def main(page: Page):
    # Titulo 
    page.title = "FleteSideBar"

    # Centralizado
    page.horizontal_alignment='center'
    page.vertical_alignment='center'

    # Agregamos la clase a la pagina
    page.add(
        Container(
            width=200,
            height=500,
            bgcolor='black',
            border_radius=10,
            animate= animation.Animation(500,'decelerate'), #Animacion del SideBar
            alignment=alignment.center,
            padding=10,
            content=ModernNavBar()
        )
    )

#Run 
if __name__ == "__main__":
    flet.app(target=main)