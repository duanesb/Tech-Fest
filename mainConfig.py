import qrcode
import sqlite3
import flet as ft
from objects import baseColor,appWidth,appHeight,View,fonts

from views.home import HomeContent
from views.register import RegisterContent
from views.entries import EntriesContent
from views.qrScanner import qrScannerContent
from views.attendance import AttendanceContent

# DATABASE CONFIG
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        student_id TEXT UNIQUE NOT NULL,
        qr TEXT UNIQUE NOT NULL
    )
''')
conn.commit()
conn.close()

# FLET CONFIG


def main(page: ft.Page):
    # CONFIG
    page.title = "Student ID Card"
    page.window.width = appWidth
    page.window.height = appHeight
    page.bgcolor = baseColor
    page.fonts = fonts


    # ROUTING
    def route_change(route):
        page.views.clear()
        match(page.route):
            case "/register":
                View("/register",RegisterContent()).set(page)
            case "/entries":
                View("/entries",EntriesContent()).set(page)
            case "/qrScanner":
                View("/qrScanner",qrScannerContent()).set(page)
            case "/attendance":
                View("/attendance",AttendanceContent()).set(page)
            case _:
                View("/home",HomeContent()).set(page)
        
        page.update()
    
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view)
    
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # STARTING PAGE
    page.go("/home")

ft.app(target=main,assets_dir="assets")