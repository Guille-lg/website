# dash
from dash import callback, callback_context, no_update, ALL
from dash.dependencies import Input, Output, State

# local packages
from src.layout_manager import layout_manager
import src.utils as utils
import src.database as db

lm = layout_manager()


@callback(
    Output('main-container', 'children', allow_duplicate=True),
    Input('home-button', 'n_clicks'),
    prevent_initial_call=True
)
def home_button_callback(n_clicks):
    """Callback for the home button. It loads the home page."""
    return no_update if n_clicks is None else lm.get_layout('home')


@callback(
    Output('main-container', 'children', allow_duplicate=True),
    Output('cv-button', 'n_clicks'),
    Input('cv-button', 'n_clicks'),
    prevent_initial_call=True
)
def cv_button_callback(n_clicks):
    """Callback for the cv button. It loads the cv page."""
    if lm.current_page == 'cv':
        return no_update, None
    
    if n_clicks != None:
        return lm.get_layout('cv'), None
    else:
        return no_update, None


@callback(
    Output('main-container', 'children', allow_duplicate=True),
    Output('about-me-button', 'n_clicks'),
    Input('about-me-button', 'n_clicks'),
    prevent_initial_call=True
)
def cv_button_callback(n_clicks):
    """Callback for the about me button. It loads the cv page."""
    return no_update if n_clicks is None else lm.get_layout('cv'), None

@callback(
    Output('main-container', 'children', allow_duplicate=True),
    Output('contact-button', 'n_clicks'),
    Input('contact-button', 'n_clicks'),
    prevent_initial_call=True
)
def cv_button_callback(n_clicks):
    """Callback for the contact button. It loads the contact page."""
    return no_update if n_clicks is None else lm.get_layout('contact'), None


@callback(
    Output('main-container', 'children', allow_duplicate=True),
    Output('projects-button', 'n_clicks'),
    Input('projects-button', 'n_clicks'),
    prevent_initial_call=True
)
def projects_button_callback(n_clicks):
    """Callback for the projects button. It loads the projects page."""
    return no_update if n_clicks is None else lm.get_layout('projects'), None

@callback(
    Output('cv-timeline', 'active'),
    Input('cv-accordion', 'value'),
    prevent_initial_call=True
)
def cv_timeline_callback(value):
    """Callback for the cv timeline. It loads the corresponding section."""
    sections = {
        'Who Am I?': 0,
        'Education': 1,
        'Experience': 2,
        'Extra-Curricular Activities': 3,
        'Courses': 4,
        'Languages': 5
    }

    return 0 if value is None else sections[value]

@callback(
    Output('main-container', 'children', allow_duplicate=True),
    Output('name-input', 'error'),
    Output('email-input', 'error'),
    Output('message-input', 'error'),
    Output('submit-button', 'n_clicks'),
    Input('submit-button', 'n_clicks'),
    State('name-input', 'value'),
    State('email-input', 'value'),
    State('message-input', 'value'),
    prevent_initial_call=True
)
def submit_button_callback(n_clicks, name, email, message):
    """
    Callback for the submit button. It updates the database with new information. For further information, please
    refer to the documentation.
    """

    main_layout = no_update
    name_error = None
    email_error = None
    message_error = None


    if n_clicks is None:
        return main_layout, name_error, email_error, message_error, None
    
    else:
        # communicate with the database
        if not utils.check_email_adress(email):
            email_error = 'Please enter a valid email address'
        if name == '':
            name_error = 'Please enter a name'
        if message == '':
            message_error = 'Please enter a message'
        
        if name_error == None and email_error == None and message_error == None:
            main_layout = lm.get_layout('contact_sent')
            db.database.insert_one(name, email, message)

        return main_layout, name_error, email_error, message_error, None


@callback(
    Output('main-container', 'children', allow_duplicate=True),
    Input({'type': 'project-button', 'project': ALL}, 'n_clicks'),
    prevent_initial_call=True
)
def project_button_callback(n_clicks):
    """Callback for the project buttons. It loads the corresponding project."""
    return no_update
