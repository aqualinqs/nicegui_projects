from nicegui import ui

def show_home_page():
    ui.label("Welcome to Akua's eatries")

    with ui.element().style("flex-wrap:no-wrap"):
        ui.image("https://cdn.pixabay.com/photo/2016/02/10/13/35/hotel-1191718_1280.jpg")
        ui.label("Cover photo")

    with ui.row():
        # ui.link("Signup", "/signup")
        # ui.link("Signin", "/signin")
        ui.button("Choose from menu", on_click=lambda: ui.navigate.to('/choose_menu'))
        with ui.link("", "/not_found"):
            ui.button("Don't Click")