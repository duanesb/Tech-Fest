import flet as ft
from objects import appWidth,appHeight,ElevatedButton,TextField
import sqlite3

def AttendanceContent():
    content = ft.Container(width=appWidth,height=appHeight,
        content= ft.Column(
            controls=[
                ft.Text("attendance")
            ]
        )
    )
    return content