import flet as ft

class View(ft.View):
    def __init__(self,route,content):
        super().__init__(route=route)
        self.controls.append(content)
    def set(self,page):
        page.views.append(self)

def main(page: ft.Page):
    # CONFIG
    page.title = "Student ID Card"
    page.window.width = 500
    page.window.height = 500

    # ROUTING
    def route_change(route):
        page.views.clear()
        match(page.route):
            case _:
                pass
    
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view)

ft.app(main)