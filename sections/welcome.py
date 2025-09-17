from turtle import color
from nicegui import ui

def render():
    # Adding the fontawesome icons
    ui.add_head_html("<script src='https://kit.fontawesome.com/ccba89e5d4.js' crossorigin='anonymous'></script>")
   # big container
    with ui.element("div").style("background-image: url(/assets/background.jpg)").classes("h-screen w-screen flex flex-col bg-cover bg-center justify-center items-center"):
        # navbar
        with ui.element("nav").classes("flex flex-row justify-between items-center w-full fixed bg-white-200 shadow-sm font-bold left-0 top-0"):
            # logo
            ui.image("assets\logo2.png").classes("w-5 px-10 py-10 h-5 ml-20 mt-5")
            #ui.label("LOGO").classes("text-white font-bold text-2xl")

            # navlinks  
            with ui.row().classes("font-bold text-1xl"):
                navlinks = [
                {"title": "Home", "path": "/"}, 
                {"title": "Menu", "path": "/menu"},
                {"title": "About Us", "path": "/about"},
                {"title": "Gallery", "path": "/gallery"},
                {"title": "Contact", "path": "/contact"},
                ]
                for item in navlinks:
                    ui.link(item["title"], item["path"]).classes("no-underline uppercase text-orange font-bold")
            ui.button("Order Now 🍝", color="orange-800", on_click=lambda: ui.navigate.to('/menu')).classes("text-white uppercase font-bold bg-orange")

            # socials
            with ui.row().classes("text-orange font-bold gap-4 justify-center mr-15 items-center"):
                ui.html('<i class="fa-brands fa-facebook-f"></i>')
                ui.html('<i class="fa-brands fa-instagram"></i>')
                ui.html('<i class="fa-brands fa-x-twitter"></i>')
        
        # text
        with ui.element("div").classes('text-white font-bold text-center bg-black/70 h-full w-full flex flex-col items-center justify-center'): 
            ui.label("Welcome to").classes("text-5xl")
            ui.html("<h1>Akua's Eatry</h1>").classes("text-7xl uppercase text-orange mt-10 md-7")
            ui.button("Choose from Menu ➡", color="orange-800", on_click=lambda: ui.navigate.to('/menu')).classes("mt-5")
            