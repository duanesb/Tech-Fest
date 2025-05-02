import flet as ft
from objects import appWidth,appHeight,ElevatedButton

def HomeContent():
    content = ft.Container(padding=0,width=appWidth,height=appHeight,
        content=ft.Column(
            controls=[
                ft.Text("Student ID Card Management",size=40,color="black",weight="bold",
                        width=appWidth/1.5,text_align=ft.TextAlign.CENTER),
                ft.Row(
                    controls=[
                        ElevatedButton("Register Student",lambda _:_.page.go("/register")),
                        ElevatedButton("View Entries",lambda _:_.page.go("/entries")),
                        ElevatedButton("Scan QRs",lambda _:_.page.go("/qrScanner")),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    wrap=True
                ),
                ft.Image(src="idCardEmpty.png",width=appWidth*0.8),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        ),
        margin=ft.margin.only(top=25)
    )
    return content