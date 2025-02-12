import flet as ft

global appWidth, appHeight
appWidth = 500
appHeight = 600

class View(ft.View):
    def __init__(self,route,content):
        super().__init__(route=route)
        self.controls.append(content)
    def set(self,page):
        page.views.append(self)