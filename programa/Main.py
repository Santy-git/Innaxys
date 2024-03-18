import flet as f
from flet import TextField, Checkbox, ElevateButton, Text, Row, Column
from flet_core.control_event import ControlEvent

# new

#El None solo se usa porque solo corremos esta funcion en el codigo
def main(page: f.Page) -> None:
    page.title = "INNAXYS"
    page.vertical_aligment = f.MainAxisAligment.Center
    # Crear una manera de cambiar de modo :)
    page.theme_mode = f.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False

    #Setup

    User: TextField = TextField(label="User", text_align=f.TextAlign.LEFT, WHITH= 200)
    Password: TextField = TextField(label="Password", text_align=f.TextAlign.LEFT, WHITH= 200, password = True)
    checkbox: Checkbox = Checkbox(label="I agree to stuff",value = False)
    Button: ElevateButton = ElevateButton(text="Sign Up")

    def validate(e: ControlEvent) -> None:
        if all([User.value,Password.value,checkbox.value]):
            Button.disabled = False
        else:
            Button.disabled = True

        page.update()

    def sudmit(e: ControlEvent) -> None:
        print("User:",User.value)
        print("User:",User.value)

        page.clean()
        page.add(
            Row(
                controls=[Text(value=f'Welcome: {User.value}',size = 20)],
                aligment=f.MainAxisAligment.CENTER
            )
        )
    checkbox.on_change = validate
    User.on_change = validate
    Password.on_change = validate
    Button.on_change = sudmit
    

    #Render bonito de la pagina skeree
    page.add(
        Row(
            controls=[
                Column(
                    [User,
                     Password,
                     checkbox,
                     Button]
                )
            ],
            aligment = f.MainAxisAligment.CENTER
        )
    )

    if __name__ == '__main__':
        f.app(target=main)