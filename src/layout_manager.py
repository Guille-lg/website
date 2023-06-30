from src.ui.layouts import main_layout as ml
from src.ui.layouts import cv_layout as cvl
from src.ui.layouts import contact_layout as cl
from src.ui.layouts import project_list_layout as pll

class layout_manager:
    """Class that manages the different layouts of the app."""
    pages = {
        'home': ml.main_layout.get_main_layout(),
        'cv': cvl.cv_layout.get_cv_layout(),
        'contact' : cl.contact_layout.get_contact_layout(),
        'contact_sent' : cl.contact_layout.get_contact_layout_sent(),
        'projects' : pll.project_list_layout.get_project_list_layout(),
    }

    current_page = ''

    def __init__(self) -> None:
        self.current_page = 'home'   

    def get_layout(self,page):
        self.current_page = page
        return layout_manager.pages[page]


