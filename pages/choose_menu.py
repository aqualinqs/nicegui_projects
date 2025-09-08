from nicegui import ui

def show_choose_menu_page():
    ui.label("Thisis our menu")

with ui.row().style("flex-wrap:no-wrap"):
    ui.image("https://cdn.pixabay.com/photo/2016/02/10/13/35/hotel-1191718_1280.jpg")
    ui.label("Cover photo")

