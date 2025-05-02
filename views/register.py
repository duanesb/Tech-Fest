import flet as ft
from objects import appWidth,appHeight,ElevatedButton,TextField
import sqlite3
import qrcode
from PIL import Image
import numpy as np
import os
fontSize = 25

def RegisterContent():
    def registerStudent(e):
        # CREATE FOLDER FOR STUDENT
        # os.makedirs("assets/")
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
        max_width = 200  # Width of the container
        max_lines = 2
        base_font_size = 20 / 0.61
        min_font_size = 10

        cardNameText.value = e.control.value
<<<<<<< HEAD
        cardNameText.max_lines = max_lines  # Allow up to 2 lines
        cardNameText.no_wrap = False  # Allow text wrapping

        text_length = len(e.control.value)
        estimated_single_line_width = (0.61 * base_font_size) * text_length

    # Two lines means double the width available (kind of)
        if estimated_single_line_width > max_width * max_lines:
        # Too wide even for 2 lines: shrink text
            scale_factor = (max_width * max_lines) / estimated_single_line_width
            new_font_size = base_font_size * scale_factor
            cardNameText.size = max(new_font_size, min_font_size)  # Don't shrink too much
        else:
            cardNameText.size = base_font_size
=======
        if(len(cardNameText.value) > 20):
            # print(len(cardNameText.value) % 20)
            cardNameText.size = fontSize - 0.61*(len(cardNameText.value) % 20)
        else:
            cardNameText.size = fontSize
        # print((0.61*cardNameText.size)*len(cardNameText.value))
>>>>>>> 82d8feb2d0e1a4578d35969321907b9a4001278d

        e.page.update()


    
    def setCardID(e):
        cardIDText.value = e.control.value
        e.page.update()

    cardNameText = ft.Text("Full Name",size=20/0.61,weight="bold",bgcolor="black", font_family="please", overflow=ft.TextOverflow.CLIP)
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
                                    height=94,
                                    bgcolor="red",
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