import flet as ft
from objects import appWidth, appHeight, ElevatedButton, TextField
import sqlite3
from datetime import datetime

def AttendanceContent():
    # Get today's date in YYYY-MM-DD
    today = datetime.now().strftime("%Y-%m-%d")

    # Fetch today's attendance records
    conn = sqlite3.connect("storage.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT student_id, name, timestamp FROM attendance WHERE timestamp LIKE ? ORDER BY timestamp",
        (f"{today}%",)
    )
    records = cursor.fetchall()
    conn.close()

    # Build DataTable rows
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

    # Create the table
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Student ID", weight=ft.FontWeight.BOLD,color="black")),
            ft.DataColumn(ft.Text("Name", weight=ft.FontWeight.BOLD,color="black")),
            ft.DataColumn(ft.Text("Time", weight=ft.FontWeight.BOLD,color="black")),
        ],
        rows=rows,
        border=ft.border.all(1, ft.colors.BLACK)
    )

    # Build the container
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
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ]
        )
    )
    return content
