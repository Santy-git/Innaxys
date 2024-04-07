# Librerias de python

import flet
from flet import * 
from functools import partial
import time

# Librerias de python


# ______________________________________Manejo de usuarios ______________________________________

x = int(input("Nivel de usuario: \n1_Administrador\n2_Empleado\n3_Cliente\n"))

niveles = (("CS", "Camilo Sanchez", "Administrador"),("JL", "Josefina Lopez", "Empleada"),("JS", "Jose Sanchez", "Cliente"))

# ______________________________________Manejo de usuarios ______________________________________



# Sidebar Clase
class ModernNavBar(UserControl):
    def __init__(self):
        super().__init__()

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
                    self.UserData(niveles[x-1][0],niveles[x-1][1], niveles[x-1][2])
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