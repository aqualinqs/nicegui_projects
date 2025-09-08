from nicegui import ui

def show_contact_page():
    ui.label("Enquire from us today")

with ui.row().style("flex-wrap:no-wrap"):
    ui.image("assets\contactpage.jpg")
    ui.label("Cover photo")