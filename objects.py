import flet as ft

global appWidth, appHeight, baseColor
appWidth = 500
appHeight = 600
baseColor = "white"

class View(ft.View):
    def __init__(self,route,content):
        super().__init__(route=route)
        self.controls.append(content)
        self.bgcolor = baseColor

    def set(self,page):
        page.views.append(self)

class ElevatedButton(ft.ElevatedButton):
    def __init__(self,text,function,width,height,textSize):
        super().__init__()
        self.text = text
        self.bgcolor = "#353535"
        self.color = "white"
        self.width = 175
        self.height = 50
        self.style = ft.ButtonStyle(
            shape={"":ft.RoundedRectangleBorder(radius=5)},
            side=ft.BorderSide(width=5,color="#171717"),
            text_style=ft.TextStyle(size=15,weight=ft.FontWeight.BOLD))
        self.on_click=function