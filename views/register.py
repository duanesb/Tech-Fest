import flet as ft
from objects import appWidth,appHeight,ElevatedButton,TextField
import sqlite3
import qrcode
from PIL import Image
import numpy as np
import os

def RegisterContent():
    def registerStudent(e):
        # CREATE FOLDER FOR STUDENT
        os.makedirs("assets/pl")
        # GENERATE QR CODE
        imagePath = f"assets/QRs/{textFieldID.value}.png"
        qr = qrcode.make(f"{textFieldName.value}\n{textFieldID.value}")
        qr.save(imagePath)
        
        image = np.array(Image.open(imagePath).convert("RGBA"))

        # Define white color in RGBA
        white = np.array([255, 255, 255, 255])

        # Create a mask where white pixels are detected (consider near-white pixels too)
        white_mask = (image[:, :, :3] > [240, 240, 240]).all(axis=2)  # Detects near-white pixels

        # Make white pixels transparent
        image[white_mask] = [255, 255, 255, 0]  # White with 0 alpha (fully transparent)

        # Remove black pixels (turn them into white)
        black_mask = (image[:, :, :3] == [0, 0, 0]).all(axis=2)  # Detects black pixels
        image[black_mask, :3] = [255, 255, 255]  # Change RGB to white
        image[black_mask, 3] = image[black_mask, 3]  # Keep alpha unchanged

        # Convert back to an image and save
        output_image = Image.fromarray(image)
        output_path = imagePath.replace(".png", ".png")
        output_image.save(output_path)

        # TRANSFORM IMAGE
        
        # STORE IN DATABASE
        conn = sqlite3.connect("attendance.db")
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO students (name, student_id, qr) VALUES (?, ?, ?)", (textFieldName.value,textFieldID.value, f"assets/QRs/{textFieldID.value}.png"))
        textFieldName.value = ""
        textFieldID.value = ""
        cardNameText.value = "Full Name"
        cardIDText.value = "Student ID"

        e.page.update()
        conn.commit()
        conn.close()

    def setCardText(e):
        cardNameText.value = e.control.value
        if(len(cardNameText.value) > 10):
            cardNameText.size = 295/len(cardNameText.value)
            print(cardNameText.size)
        else:
            cardNameText.size = 30
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