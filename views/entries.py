import flet as ft
from objects import appWidth,appHeight,ElevatedButton

def EntriesContent():
    content = ft.Container(width=appWidth,height=appHeight,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ElevatedButton("Return Home",lambda _:_.page.go("/home")),
                        ElevatedButton("Select",None),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ]
        )
    )
    return content