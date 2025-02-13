import flet as ft
from objects import appWidth,appHeight,ElevatedButton,TextField

def RegisterContent():
    content = ft.Container(width=appWidth,height=appHeight,
        content=ft.Column(
            controls=[
                ft.Text("Register Student",size=35,color="black",weight="bold",
                        width=appWidth/1.5,text_align=ft.TextAlign.CENTER),
                TextField("Name"),
                TextField("Student ID"),
                ft.Row(
                    controls=[
                        ElevatedButton("Return Home",lambda _:_.page.go("/home")),
                        ElevatedButton("Register",None),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Stack([
                    ft.Image(src="idCardEmpty.png",width=appWidth*0.8),
                    ft.Text()
                ])
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )
    return content