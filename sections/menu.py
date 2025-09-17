from nicegui import ui

# Dummy data for categories
categories = [
    {
        "id": "signature",
        "title": "Signature Dishes",
        "desc": "Must-try specialties crafted with authentic flavors and premium ingredients.",
        "img": "assets/gallery1.jpg",
    },
    {
        "id": "grill",
        "title": "Grill & Kebabs",
        "desc": "Juicy, flame-grilled perfection cooked to bring out rich flavors.",
        "img": "assets/gallery2.jpg",
    },
    {
        "id": "wraps",
        "title": "Wraps & Sandwiches",
        "desc": "Quick, tasty, and packed with fresh ingredients for ultimate satisfaction.",
        "img": "assets/gallery3.jpg",
    },
]

def render():
    with ui.element("div").classes('w-full h-full bg-gray-900 flex flex-col items-center justify-center p-8 lg:p-16'):
        # Section Title
        ui.label("Our Offerings").classes("text-sm text-red-500 font-semibold uppercase tracking-widest mb-2")
        ui.label("Delicious Choices, Made Just for You").classes("text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white text-center mb-4")
        ui.label("Explore our carefully curated menu with fresh ingredients and bold flavors.").classes("text-lg text-gray-400 text-center mb-8")

        # Carousel container
        with ui.carousel().props('arrows navigation swipe').classes('w-full max-w-6xl h-auto rounded-xl shadow-lg'):
            for cat in categories:
                with ui.carousel_slide().classes('flex flex-col items-center justify-center p-6 bg-gray-800 rounded-xl'):
                    ui.image(cat["img"]).classes("w-full h-64 object-cover rounded-lg shadow-lg mb-4")
                    ui.label(cat["title"]).classes("text-xl font-bold text-white mb-2")
                    ui.label(cat["desc"]).classes("text-gray-400 text-center mb-4")
        ui.button("View Menu ↗", on_click=lambda c=cat: ui.navigate.to(f'/menu/{c["id"]}')).classes("mt-8 px-8 py-3 bg-red-600 text-white font-bold rounded-full shadow-lg hover:bg-red-700 transition-transform transform hover:scale-105 mt-20")    

        # Load More Button
        # ui.button("Load More", on_click=lambda: ui.notify("Loading more categories...")) \
        #     .classes("mt-8 px-8 py-3 bg-red-600 text-white font-bold rounded-full shadow-lg hover:bg-red-700 transition-transform transform hover:scale-105")



