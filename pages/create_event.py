from nicegui import ui

def show_create_event_page():
    ui.label("This is the Create Event page")

with ui.row().style("flex-wrap:no-wrap"):
    ui.image("assets\eventHome2.PNG")
    ui.label("Cover photo")
    # add css styling
    ui.element("div").style(
        "height:200px; width: 200px; background-color: red")
