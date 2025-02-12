import flet as ft
from objects import appWidth,appHeight

def HomeContent():
    content = ft.Container(padding=0,width=appWidth,height=appHeight,
        content=ft.Column(
            controls=[
                ft.Text("Student ID Card Management",size=40,color="black",weight="bold",
                        width=appWidth/1.5,text_align=ft.TextAlign.CENTER)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        margin=ft.margin.only(top=20)
    )
    return content