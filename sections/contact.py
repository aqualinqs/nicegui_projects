from nicegui import ui

# This function will create the contact page content
def render():
    # === Main Page Container ===
    with ui.element("div").classes("w-full h-full flex flex-row bg-gray-900 font-sans m-0 items-center"):
        
        # === Contact Content Section ===
        # This row contains both the left content and the right content
        with ui.element("div").classes("w-full max-w-6xl mx-auto py-12 px-4 gap-12"):
            
            # Left Column: Text Content
            with ui.column().classes("w-full md:w-1/2"):
                with ui.row().classes("items-center mb-4"):
                    ui.icon("location_on").classes("text-[#ff006e]")
                    ui.label("CONTACT US").classes("text-3xl font-bold text-white")
                
                ui.label("Pellentesque rutrum at sapien at sollicitudin. Nam quis orci at orci fermentum mollis maximus at justo. Duis elit felis, congue egestas tristique quis, dictum vitae massa. Suspendisse at justo enim.").classes("text-sm text-gray-500 mb-6")

                with ui.column().classes("space-y-4 text-sm text-white"):
                    with ui.row().classes("items-center space-x-2"):
                        ui.icon("location_on").classes("text-gray-500")
                        with ui.column():
                            ui.label("APPLE STORE SOHO").classes("font-bold")
                            ui.label("103 PRINCE ST. NEW YORK, NY 10012, UNITED STATES")
                            ui.label("+1 212-226-3126")
                    
                    with ui.row().classes("items-center space-x-2"):
                        ui.icon("mail_outline").classes("text-gray-500")
                        ui.label("hello@imevent.com").classes("text-[#ff006e]")
            
            # Right Column: This single column will contain the form AND the image grid
        with ui.element("div").classes("w-full md:w-1/2 gap-8 flex flex-row m-0"):
                # === Image Grid Section ===
            with ui.element('div').classes('w-full mt-8'):
                    with ui.element().classes("w-full items-center"):
                        ui.label("Social Media").classes("text-[#ff006e] font-bold text-sm mb-2")
                        ui.label("Follow Us & Stay Connected").classes("text-2xl font-bold text-white mb-2")
                        ui.label("Get the latest updates, special offers, and mouthwatering food photos!").classes("text-sm text-gray-500 mb-6")
                    
                    with ui.grid(columns='2').classes('w-full gap-2'):
                        ui.image("https://cdn.pixabay.com/photo/2016/02/10/13/35/hotel-1191718_1280.jpg").classes("w-20 h-20 rounded-lg")
                        ui.image("https://cdn.pixabay.com/photo/2016/11/29/05/08/adult-1869620_1280.jpg").classes("w-20 h-20 rounded-lg")
                        ui.image("https://cdn.pixabay.com/photo/2018/01/15/21/50/concert-3084876_1280.jpg").classes("w-20 h-20 rounded-lg")
                        ui.image("https://cdn.pixabay.com/photo/2018/05/10/11/34/concert-3387324_1280.jpg").classes("w-20 h-20 rounded-lg")


            # === Contact Form ===
            with ui.column().classes("w-full bg-gray-100 p-8 rounded-lg shadow-md"):
                    ui.label("Tell Us What You Need").classes("text-2xl font-bold mb-4")
                    ui.label("Quisquam sint blanditiis ex eos esse et quo voluptatem ea. Aut iste et et fuga aut rerum vel. Qui sunt et non qui. Cum et quas est aut et.").classes("text-sm text-gray-500 mb-6")


                    ui.label('Enter your details here ⬇').classes('text-3xl font-bold text-gray-800')
                    with ui.row().classes("w-full gap-4"):
                        ui.input(placeholder="First Name").classes('w-1/2').props("outlined")
                        ui.input(placeholder="Last Name").classes('w-1/2').props("outlined")
                    
                    with ui.row().classes("w-full gap-4"):
                        ui.input(placeholder="Company").classes('w-1/2').props("outlined")
                        ui.input(placeholder="Phone Number").classes('w-1/2').props("outlined")
                    
                    ui.input(placeholder="Email Address").classes("w-full").props("outlined")
                    
                    ui.label("Type of Inquiry").classes("font-semibold text-gray-700 mt-4")
                    with ui.row().classes('items-center space-x-4'):
                        ui.select(options=['Booking', 'General', "Wedding", "Corporate", "Others"], value='General').props('outlined dense')
                    
                    ui.input(placeholder="Message").classes("w-full h-32").props("type=textarea outlined")
                    
                    with ui.checkbox("I'd like to receive exclusive offers and updates.").classes("text-sm text-gray-500"):
                        pass # Checkbox content
                    
                    ui.button("Submit", on_click=lambda: ui.notify('Message Sent!')).classes("w-full py-3 text-white font-semibold rounded-lg shadow-md").props("color=black")


# from nicegui import ui
# #from components.navbar import show_navbar


# def render():
#     #show_navbar()
#     # === Main Content Container ===
#     with ui.column().classes("w-full items-center"):

#         # === Page Header ===
#         with ui.element('div').classes('w-full bg-gray-100 py-8 text-center'):
#             # ui.label("CONTACTS").classes("text-4xl font-bold text-gray-800 mb-2")
#             # ui.label("Home > Contact Us").classes("text-sm text-gray-500")
#         # === Contact Section: Info and Map ===
#             with ui.row().classes("w-full max-w-6xl mx-auto my-12 items-start justify-center p-4"):
#                 # Contact Information Column
#                 with ui.column().classes("w-full md:w-1/2 lg:w-1/2 p-4"):
#                     with ui.row().classes("items-center mb-4"):
#                         ui.icon("location_on").classes("text-purple-600")
#                         ui.label("CONTACT US / lorem ipsum").classes("text-xl font-bold text-gray-800")
                
#                 ui.label("Pellentesque rutrum at sapien at sollicitudin. Nam quis orci at orci fermentum mollis maximus at justo. Duis elit felis, congue egestas tristique quis, dictum vitae massa. Suspendisse at justo enim.").classes("text-sm text-gray-600 mb-4")

#                 with ui.column().classes("space-y-2 text-sm text-gray-600"):
#                     ui.label("APPLE STORE SOHO").classes("font-bold")
#                     ui.label("103 PRINCE ST. NEW YORK, NY 10012, UNITED STATES")
#                     ui.label("+1 212-226-3126")
#                     ui.label("hello@imevent.com").classes("text-purple-600")

#             # Google Maps Placeholder
#             with ui.element('div').classes("w-full md:w-1/2 lg:w-1/2 h-96 p-4"):
#                 # Placeholder for the map, as embedding a live map is not direct
#                 with ui.element('div').classes('w-full h-full bg-gray-300 flex items-center justify-center rounded-lg'):
#                     ui.label("Google Maps placeholder").classes("text-gray-500 italic")

#         # === Contact Form Section ===
#         with ui.element('div').classes("w-full bg-red-800 py-16 flex justify-center"):
#             with ui.column().classes("w-full max-w-2xl px-4 space-y-4"):
#                 ui.input(placeholder="Type Your Name...").classes('w-full').props('outlined rounded bg-white')
#                 ui.input(placeholder="Type Your Email...").classes('w-full').props('outlined rounded bg-white')
#                 ui.input(placeholder="Type Your Message...").classes('w-full h-32').props('type=textarea outlined rounded bg-white')
#                 ui.button("SEND MESSAGE", on_click=lambda: ui.notify('Message Sent!')).classes("w-48 mx-auto font-bold rounded-full").props("color=black")
