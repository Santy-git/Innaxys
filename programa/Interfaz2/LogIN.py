# _______________________________________V1_______________________________________

# from flet import *

# LogIN = Container(
#     Container(
#         Stack([
#             Container(
#                 border_radius = 11,
#                 rotate=Rotate(0.98*3.14), #Grados
#                 widht=360,
#                 height=560,
#                 bgcolor='#22ffffff',
#             ),
#             Container(
#                 Container(
#                     Column([
#                         Container(
#                             Image(
#                                 src='axys.png',
#                                 widht=50,
#                             ),padding=padding.only(150,20)
#                         ),
#                         Text(
#                             'Sign in',
#                             widht=360,
#                             size=30,
#                             weight='w900',
#                             text_align='center',
#                         ),
#                         Text(
#                             "Please login to use the plataform",
#                             widht=360,
#                             text_align='center',

#                         ),
#                         Container(
#                             TextField(
#                                 widht=280,
#                                 height=40,
#                                 hint_text='Username',
#                                 borde='underline',
#                                 prefix_icon = icons.EMAIL,
#                                 border_radius=11,

#                             ),padding=padding.only(25,20)
#                         ),
#                         # Container
#                     ]),
#                 ),
#                 width=360,
#                 height=560,
#                 bgcolor='#22ffffff'
#                 border_radius=11,

#             ),
#         ]),
#         width=360,
#         height=560,
#     ),
#     width=360,
#     height=740,
#     gradient=LinearGradient(['#333399','#ff00cc'])
# ),

# def main(page:Page):
#     page.window_max_width=580
#     page.window_max_height=740
#     page.padding = 0
#     page.add(LogIN)

# app(target=main)

# _______________________________________V1_______________________________________


# _______________________________________V2_______________________________________

from flet import *

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
                        Container(
                            TextField(
                                width=290,
                                height=60,
                                label='Username',
                                border='underline',
                                color='#303030',
                                prefix_icon = icons.PERSON,
                            ),padding=padding.only(25,20),
                        ),
                        Container(
                            TextField(
                                width=280,
                                height=60,
                                label='Password',
                                border='underline',
                                color='#303030',
                                prefix_icon= icons.LOCK,
                            ),padding=padding.only(25,20),
                        ),
                        Container(
                            TextButton(
                                'I forgot my password: ',
                            ),padding=padding.only(90),
                        ),
                        Container(
                            ElevatedButton(
                                content=Text(
                                    'SIGN IN',
                                    color='white',
                                    weight='w500'
                                ),width=280,bgcolor='black',
                            ),padding=padding.only(40,10)
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

def main(page:Page):
    # page.window_full_screen= True
    page.window_max_width=580
    page.window_max_height=740
    page.padding=0
    page.window_frameless = True
    page.add(body)

app(target=main)

# _______________________________________V2_______________________________________