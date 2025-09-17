from nicegui import ui, app
from sections import about, home, welcome, menu, menu_detail, contact, gallery
#from components import navbar, footer

# Expose the assets folder to the nicegui server
app.add_static_files("/assets", "assets")

# link external icons to the head
ui.add_head_html('''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/all.min.css" 
                 integrity="sha512-2SwdPD6INVrV/lHTZbO2nodKhrnDdJK9/kg2XD1r9uGqPo1cUbujc+IYdlYdEErWNu69gVcYgdxlmVmzTWnetw==" 
                 crossorigin="anonymous" referrerpolicy="no-referrer" />

''')
ui.add_head_html('<link rel="stylesheet" href="/assets/reset.css" />')

welcome.render()
home.render()
menu.render()
menu_detail.render()
about.render()
gallery.render()
contact.render()

ui.run(port=8000)
