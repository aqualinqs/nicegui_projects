from nicegui import ui

#define function for about section
def render():
    with ui.element("div").classes('w-full h-full bg-gray-900 flex flex-wrap items-center justify-center p-8 lg:p-16'):
         # Right side with the image
        with ui.column().classes('w-full lg:w-1/2 flex items-center justify-center p-4'):
            ui.image("assets/gallery7.jpg").classes('w-full h-auto max-w-sm md:max-w-md lg:max-w-lg rounded-2xl shadow-xl transform -rotate-6')
    #with ui.row().classes('w-full h-full bg-gray-900 flex flex-wrap items-center justify-center p-8 lg:p-16'):
       
        #with ui.column().classes('w-full lg:w-1/2 flex items-cenjustify-left p-4 relative'):
            
        # Left side for text content and chef icon
        with ui.column().classes('w-full lg:w-1/2 flex flex-col lg:items-start items-cenjustify-left p-4 relative'):
            ui.label('Who We Are').classes('text-sm text-gray-400 font-semibold uppercase tracking-widest mb-2')
            
            # Main heading
            ui.label('Passion for Great Food, Served with Love').classes('text-2xl sm:text-2xl lg:text-6xl font-extrabold text-white leading-tight mb-4')

            # Sub-heading/Body text
            ui.label("At Akua's Eatry, we bring you the finest flavors inspired by contemporary cuisine type crafted with high-quality ingredients, traditional recipes, and a passion for excellent service.").classes('text-lg sm:text-xl text-gray-400 mb-8 max-w-xl')
            ui.label("Whether you're craving signature dishes or seeking a cozy spot to enjoy with loved ones, we've got you covered. Welcome to a place where food meets passion!").classes('text-lg sm:text-xl text-gray-400 mb-8 max-w-xl')

            ui.image("assets\chef2.jpg").classes('relative w-28 h-28 max-w-sm md:max-w-md lg:max-w-lg shadow-xl right-0 gap-6 ml-60')

    # # Use a div to act as the main container for the centered content
    # with ui.element("div").classes('w-full h-screen bg-gray-900 flex flex-wrap items-center justify-center p-8 lg:p-16'):      
    #     # Right side for text content
    #     with ui.column().classes('w-full lg:w-1/2 flex flex-col justify-center items-center lg:items-start text-center lg:text-left p-4'):
    #         # Main heading
    #         ui.label('Authentic Flavors, Unforgettable Experience!').classes('text-4xl sm:text-4xl lg:text-4xl font-extrabold text-white uppercase leading-tight mb-4')

    #         # Sub-heading
    #         ui.label('Freshly prepared, mouthwatering dishes made with love. Explore our menu and taste the difference!').classes('text-lg sm:text-xl text-gray-400 mb-8 max-w-xl')

    #         # "Order Now" button
    #         ui.button('Order Now', on_click=lambda: ui.navigate.to('/menu')).classes("text-white font-bold bg-orange font-bold py-3 px-8 rounded-full shadow-lg hover:bg-gray transition-colors duration-300 transform hover:scale-105")
    #     # Left side for the image
    #     with ui.column().classes('w-full lg:w-1/2 flex items-center justify-center p-4'):
    #         # Image component
    #         ui.image("assets\gallery1.jpg").classes('w-full h-auto max-w-sm md:max-w-md lg:max-w-lg rounded-2xl shadow-xl')


# from nicegui import ui

# def render():
#     with ui.element("div").classes('w-full h-full bg-black flex flex-wrap items-center justify-center p-8 lg:p-16'):
        
#         # LEFT SIDE: overlapping/angled images + chef icon
#         with ui.column().classes('w-full lg:w-1/2 flex items-center justify-center relative p-4'):
#             # Chef hat icon (top-left)
#             ui.image("assets/chef_icon.png").classes(
#                 'absolute top-0 left-0 w-20 h-20 opacity-80'
#             )

#             # First rotated food image
#             ui.image("assets/gallery7.jpg").classes(
#                 'w-72 h-auto rounded-2xl shadow-xl transform -rotate-6 border-4 border-white mb-8'
#             )

#             # Second rotated group image (slightly offset)
#             ui.image("assets/gallery5.jpg").classes(
#                 'w-72 h-auto rounded-2xl shadow-xl transform rotate-3 border-4 border-white -mt-20 ml-16'
#             )

#         # RIGHT SIDE: about text + chef serving icon
#         with ui.column().classes('w-full lg:w-1/2 flex flex-col items-start justify-center p-4 relative'):
            
#             # Section label
#             ui.label('About us').classes(
#                 'text-sm text-red-500 font-semibold uppercase tracking-widest mb-2'
#             )

#             # Main heading
#             ui.label('Passion for Great Food,\nServed with Love').classes(
#                 'text-4xl lg:text-5xl font-extrabold text-white leading-tight mb-6'
#             )

#             # Sub-heading / description
#             ui.label(
#                 "At Akua's Eatry, we bring you the finest flavors inspired by "
#                 "local and international cuisine, crafted with high-quality "
#                 "ingredients, traditional recipes, and a passion for excellent service."
#             ).classes('text-lg text-gray-300 mb-4 max-w-xl')

#             ui.label(
#                 "Whether you're craving signature dishes or seeking a cozy spot to enjoy "
#                 "with loved ones, we've got you covered. Welcome to a place where food meets passion!"
#             ).classes('text-lg text-gray-300 mb-8 max-w-xl')

#             # Decorative chef serving icon (bottom-right)
#             ui.image("assets/chef_serving.png").classes(
#                 'absolute bottom-0 right-0 w-28 h-28 opacity-90'
#             )
