from nicegui import ui

ui.add_head_html('<script src="https://kit.fontawesome.com/ccba89e5d4.js" crossorigin="anonymous"></script>') 

def show_footer():
    with ui.element("div").classes("w-full bg-orange items-center justify-center px-10 py-5"):
        with ui.row().classes("items-center justify-center text-4xl font-bold mb-4"):
            ui.label("Akua's").classes("text-white")
            ui.label("Eatries").classes("text-purple-400")

        with ui.row().classes("items-center justify-center text-white mb-8"):
            ui.input(placeholder="Enter your mail").props("outlined").classes("bg-orange w-64")
            ui.button("Subscribe").props("color=orange-7").classes("px-20 py-4")

        ui.html("<hr>").classes("mt-16")

        with ui.element("div").classes("flex flex-row justify-between text-white px-4 py-8"):
            with ui.row():
                ui.label("English")
                ui.label("French")
                ui.label("Twi")

            with ui.row().classes("gap-4 justify-center text-4xl"):
                ui.html('<a href="https://facebookcom" target="blank"><i class="fa-brands fa-facebook"></i></a>')
                ui.html('<a href="https://instagram.com" target="blank"><i class="fa-brands fa-instagram"></i></a>')
                ui.html('<a href="https://twitter.com" target="blank"><i class="fa-brands fa-twitter"></i></a>')

