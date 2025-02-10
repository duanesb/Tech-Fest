import sqlite3
import pandas as pd

def export_attendance():
    conn = sqlite3.connect("attendance.db")
    df = pd.read_sql_query("SELECT * FROM attendance", conn)
    df.to_csv("attendance_records.csv", index=False)
    conn.close()
    print("Attendance exported as CSV!")

export_attendance()
