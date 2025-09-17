from nicegui import ui

def render():
    # Use a div to act as the main container for the centered content
    with ui.element("div").classes('w-full h-screen bg-gray-900 flex flex-wrap items-center justify-center p-8 lg:p-16'):      
        # Right side for text content
        with ui.column().classes('w-full lg:w-1/2 flex flex-col justify-center items-center lg:items-start text-center lg:text-left p-4'):
            # Main heading
            ui.label('Authentic Flavors, Unforgettable Experience!').classes('text-4xl sm:text-4xl lg:text-4xl font-extrabold text-white uppercase leading-tight mb-4')

            # Sub-heading
            ui.label('Freshly prepared, mouthwatering dishes made with love. Explore our menu and taste the difference!').classes('text-lg sm:text-xl text-gray-400 mb-8 max-w-xl')

            # "Order Now" button
            ui.button('Order Now', on_click=lambda: ui.navigate.to('/menu')).classes("text-white font-bold bg-orange font-bold py-3 px-8 rounded-full shadow-lg hover:bg-gray transition-colors duration-300 transform hover:scale-105")
        # Left side for the image
        with ui.column().classes('w-full lg:w-1/2 flex items-center justify-center p-4'):
            # Image component
            ui.image("assets\gallery3.jpg").classes('w-full h-1/4 max-w-sm md:max-w-md lg:max-w-lg rounded-2xl shadow-xl')
