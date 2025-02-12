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