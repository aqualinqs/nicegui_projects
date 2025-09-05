from nicegui import ui

def show_home_page():
    ui.label("Welcome to the Home Page")
    with ui.row():
        ui.link("Signup", "/signup")
        ui.link("Signin", "/signin")
        ui.button("Create event", on_click=lambda: ui.open('/create_event'))
        with ui.link("", "/not_found"):
            ui.button("Don't Click")