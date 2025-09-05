from nicegui import ui

ui.add_head_html('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">') 

def show_footer():
    with ui.element("div").classes("w-full bg-blue-800 items-center justify-center px-10 py-5"):
        with ui.row().classes("items-center justify-center text-4xl font-bold mb-4"):
            ui.label("Event").classes("text-white")
            ui.label("Hive").classes("text-purple-400")

        with ui.row().classes("items-center justify-center text-white mb-8"):
            ui.input(placeholder="Enter your mail").props("outlined").classes("bg-white w-64")
            ui.button("Subscribe").props("color=deep-purple-7").classes("px-20 py-4")

        ui.html("<hr>").classes("mt-16")

        with ui.element("div").classes("flex flex-row justify-between text-white px-4 py-8"):
            with ui.row():
                ui.label("English")
                ui.label("French")
                ui.label("Twi")

            with ui.row().classes("text-white text-4xl"):
                ui.html('<i class="fa-brands fa-facebook"></i>')
                ui.html('<i class="fa-brands fa-instagram"></i>')
                ui.html('<i class="fa-brands fa-twitter"></i>')

            with ui.row():
                ui.label("Non Copyrighted &copy 2025 Upload by dr. crack studio")

