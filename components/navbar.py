from nicegui import ui

ui.add_head_html('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">') 

def show_navbar():
    with ui.element("div").classes("w-full bg-deeppurple items-center justify-center px-10 py-5"):
        with ui.row().classes("items-center justify-center text-4xl font-bold mb-4"):

            with ui.row().classes("items-center justify-center text-blue mb-8") as logo:
                ui.label("Akua's Eatries").classes('text-2x1 font-bold')
            logo.on('click', lambda: ui.navigate.to("/"))


            with ui.row().classes('items-center gap-8 md:flex'):
                ui.button("Home", on_click=lambda: ui.navigate.to("/"))
                ui.button("Our Menu", on_click=lambda: ui.navigate.to("/choose_menu"))
                ui.button("Contact", on_click=lambda: ui.navigate.to("/contact"))
            
            with ui.row().classes('items-center gap-8 md:flex'):
                ui.button("Signup", on_click=lambda: ui.navigate.to("/signup"))
                ui.button("Signin", on_click=lambda: ui.navigate.to("/sigin"))



