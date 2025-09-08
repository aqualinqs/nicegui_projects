from turtle import color
from nicegui import ui

def render():
   # big container
    with ui.element("div").style("background-image: url(/assets/cover.jpg)").classes("h-screen w-screen flex flex-col bg-cover bg-center justify-center items-center"):
        # navbar
        with ui.element("nav").classes("flex flex-row justify-between items-center w-full fixed left-0 top-0 px-20 py-10"):
            # logo
            ui.image("assets\logo2.png").classes("w-5 px-10 py-10 h-5")
            #ui.label("LOGO").classes("text-white font-bold text-2xl")

            # navlinks  
            with ui.row():
                navlinks = [
                {"title": "Home", "path": "/"}, 
                {"title": "Menu", "path": "/"},
                {"title": "About", "path": "/"},
                {"title": "Gallery", "path": "/"},
                {"title": "Contact", "path": "/"},
                ]
                for item in navlinks:
                    ui.link(item["title"], item["path"]).classes("no-underline uppercase text-orange font-bold")

            # socials
            with ui.row().classes("text-white"):
                ui.html('<i class="fa-brands fa-facebook-f"></i>')
                ui.html('<i class="fa-brands fa-instagram"></i>')
                ui.html('<i class="fa-brands fa-x-twitter"></i>')
        
        # text
        with ui.element("div").classes('text-white font-bold text-center bg-black/70 h-full w-full flex flex-col items-center justify-center'): 
            ui.label("Welcome to").classes("text-5xl")
            ui.html("<h1>Akua's Eatry</h1>").classes("text-7xl uppercase text-orange")
            ui.button("Choose from Menu ➡", color="orange-800").classes("")
            