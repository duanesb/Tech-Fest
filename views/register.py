import flet as ft
from objects import appWidth,appHeight,ElevatedButton,TextField
import sqlite3
import qrcode
from PIL import Image
import numpy as np
import os
import math
fontSize = 25

def RegisterContent():
    def registerStudent(e):
        # CREATE FOLDER FOR STUDENT
        # GENERATE QR CODE
        imagePath = f"assets/QRs/{textFieldID.value}.png"
        qr = qrcode.make(textFieldID.value)
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
        
        # STORE IN DATABASE
        conn = sqlite3.connect("storage.db")
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO students (name, student_id, qr) VALUES (?, ?, ?)", ((textFieldName.value).strip(),(textFieldID.value).strip(), f"assets/QRs/{textFieldID.value}.png"))        
        textFieldName.value = ""
        textFieldID.value = ""
        cardNameText.value = "Full Name"
        cardIDText.value = "Student ID"


        e.page.update()
        conn.commit()
        conn.close()

    def setCardText(e):
        cardNameText.value = e.control.value
        maxLenChar = math.floor(205/(0.61*fontSize)*2)-1
        if(len(cardNameText.value) > maxLenChar):
            cardNameText.size = fontSize - 0.61*(len(cardNameText.value) % maxLenChar)
        else:
            cardNameText.size = fontSize

        e.page.update()

    def setCardID(e):
        cardIDText.value = e.control.value
        e.page.update()

    cardNameText = ft.Text("Full Name",size=fontSize,weight="bold", font_family="please", overflow=ft.TextOverflow.CLIP)
    cardIDText = ft.Text("Student ID",size=fontSize,weight="bold",width=200)
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
                                ft.Container(
                                    width=205,
                                    height=80,
                                    content=cardNameText
                                ),
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