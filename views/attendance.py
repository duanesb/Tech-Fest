import flet as ft
from objects import appWidth,appHeight,ElevatedButton,TextField
import sqlite3
from datetime import datetime, timedelta


def AttendanceContent():
    content = ft.Container(width=appWidth,height=appHeight,
        content= ft.Column(
            controls=[
                ft.Text(f"Attendance {datetime.now().strftime("%Y-%m-%d")}",color="black",size=30,weight=ft.FontWeight.BOLD, width=appWidth, text_align=ft.TextAlign.CENTER)
            ],
        )
    )
    return content