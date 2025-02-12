import flet as ft
from objects import appWidth,appHeight,ElevatedButton

def HomeContent():
    content = ft.Container(padding=0,width=appWidth,height=appHeight,
        content=ft.Column(
            controls=[
                ft.Text("Student ID Card Management",size=40,color="black",weight="bold",
                        width=appWidth/1.5,text_align=ft.TextAlign.CENTER),
                ft.Divider(10,leading_indent=50,trailing_indent=50,thickness=5),
                ElevatedButton("Register Student",None),
                ElevatedButton("View Entries",None),
                ft.Image(src="idCard.png",width=appWidth*0.75)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        margin=ft.margin.only(top=20)
    )
    return content