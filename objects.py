import flet as ft

global appWidth, appHeight, baseColor, fonts
appWidth = 500
appHeight = 600
baseColor = "white"
fonts = {
    "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
    "please": "/Users/duanebollig/Desktop/VSCode/12th Grade/Tech-Fest/assets/JetBrainsMono-2/fonts/ttf/JetBrainsMono-Bold.ttf"
}

class View(ft.View):
    def __init__(self,route,content):
        super().__init__(route=route)
        self.controls.append(content)
        self.bgcolor = baseColor

    def set(self,page):
        page.views.append(self)

class ElevatedButton(ft.ElevatedButton):
    def __init__(self,text,function):
        super().__init__()
        self.text = text
        self.bgcolor = "#353535"
        self.color = "white"
        self.width = appWidth*0.35
        self.height = 50
        self.style = ft.ButtonStyle(
            shape={"":ft.RoundedRectangleBorder(radius=5)},
            side=ft.BorderSide(width=2,color="#171717"),
            text_style=ft.TextStyle(size=15,weight=ft.FontWeight.BOLD))
        self.on_click=function

class TextField(ft.TextField):
    def __init__(self,label,function):
        super().__init__()
        self.label = label
        self.width = appWidth*0.7
        self.height = 50
        self.border_width = 2
        self.border_color = "#878787"
        self.color = "black"
        self.on_change=function