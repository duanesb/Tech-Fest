import flet as ft
from objects import appWidth, appHeight, ElevatedButton, TextField
import sqlite3
from datetime import datetime
import pandas as pd

def AttendanceContent():
    today = datetime.now().strftime("%Y-%m-%d")

    # GET DAILY RESULTS
    conn = sqlite3.connect("storage.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT student_id, name, timestamp FROM attendance WHERE timestamp LIKE ? ORDER BY timestamp",
        (f"{today}%",)
    )
    records = cursor.fetchall()
    conn.close()

    # TABLE
    rows = []
    for student_id, name, timestamp in records:
        # Show only the time portion HH:MM:SS
        time_str = timestamp.split(' ')[1]  
        rows.append(
            ft.DataRow(cells=[
                ft.DataCell(ft.Text(student_id,color="black")),
                ft.DataCell(ft.Text(name,color="black")),
                ft.DataCell(ft.Text(time_str,color="black")),
            ])
        )
    
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Student ID", weight=ft.FontWeight.BOLD,color="black")),
            ft.DataColumn(ft.Text("Name", weight=ft.FontWeight.BOLD,color="black")),
            ft.DataColumn(ft.Text("Time", weight=ft.FontWeight.BOLD,color="black")),
        ],
        rows=rows,
        border=ft.border.all(1, ft.colors.BLACK)
    )

    def exportDatabase():
        conn = sqlite3.connect("storage.db")
        test = pd.read_sql_query("SELECT * FROM attendance WHERE ")
        print(records)


    content = ft.Container(
        width=appWidth,
        height=appHeight,
        padding=10,
        content=ft.Column(
            controls=[
                ft.Text(f"Attendance {today}", color="black", size=30, weight=ft.FontWeight.BOLD, width=appWidth, text_align=ft.TextAlign.CENTER),
                ft.Divider(),
                table,
                ft.Row(
                    controls=[
                        ElevatedButton("Return Home", lambda e: e.page.go("/home")),
                        ElevatedButton("Export as CSV", exportDatabase())
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ]
        )
    )
    return content
