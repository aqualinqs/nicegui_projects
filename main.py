from nicegui import ui
from pages.home import show_home_page
from pages.signin import show_signin_page
from pages.signup import show_signup_page
from pages.event import show_event_page
from pages.college import show_college_page
from pages.create_event import show_create_event_page
from pages.not_found import show_not_found_page
from components.navbar import show_navbar
from components.footer import show_footer

def page_layout(content_func, with_footer: bool = True):
    """Reusable page layout with navbar, page content, and footer."""
    def wrapper():
        show_navbar()
        content_func()
        if with_footer:
            show_footer()
    return wrapper

@ui.page("/")
def home_page():
    page_layout(show_home_page)()

@ui.page("/signin")
def signin_page():
    show_signin_page()

@ui.page("/signup")
def signup_page():
    show_signup_page()

@ui.page("/event")
def event_page():
    page_layout(show_event_page)()
  
@ui.page("/college")
def college_page():
    page_layout(show_college_page)()
    


@ui.page("/create_event")
def create_event_page():
    show_create_event_page()
    page_layout(show_create_event_page)()


@ui.page("/not_found")
def not_found_page():
    page_layout(show_not_found_page)()


ui.run(port=8000)
