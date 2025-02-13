import flet as ft
from objects import appWidth,appHeight,ElevatedButton,TextField
import sqlite3

def RegisterContent():
    def registerStudent(e):
        conn = sqlite3.connect("attendance.db")
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO students (name, student_id) VALUES (?, ?)", (textFieldName.value,textFieldID.value))
        textFieldName.value = ""
        textFieldID.value = ""
        cardNameText.value = "Full Name"
        cardIDText.value = "Student ID"

        e.page.update()
        conn.commit()
        conn.close()

    def setCardText(e):
        cardNameText.value = e.control.value
        e.page.update()
    
    def setCardID(e):
        cardIDText.value = e.control.value
        e.page.update()

    cardNameText = ft.Text("Full Name",size=30,weight="bold",width=200)
    cardIDText = ft.Text("Student ID",size=30,weight="bold",width=200)
    textFieldName = TextField("Name",setCardText)
    textFieldID = TextField("Student ID",setCardID)

    content = ft.Container(width=appWidth,height=appHeight,
        content=ft.Column(
            controls=[
                ft.Text("Register Student",size=35,color="black",weight="bold",
                        width=appWidth/1.5,text_align=ft.TextAlign.CENTER),
                textFieldName,
                textFieldID,
                ft.Row(
                    controls=[
                        ElevatedButton("Return Home",lambda _:_.page.go("/home")),
                        ElevatedButton("Register",lambda _: registerStudent(_)),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Stack([
                    ft.Image(src="idCardEmpty.png",width=appWidth*0.8),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                cardNameText,
                                cardIDText
                            ]
                        ),
                        left=38,
                        top=50
                    )
                ])
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )
    return content