# dash
from dash import Dash, html, dcc
import dash_mantine_components as dmc

# utils
from dotenv import load_dotenv; load_dotenv()

# local packages
from src.layout_manager import layout_manager 
from src.ui import header
from src import callbacks

app = Dash(
    __name__,
    external_stylesheets=['styles.css'],
    suppress_callback_exceptions=True,
    title='Guillermo López Gómez',
    update_title='Loading...',
    prevent_initial_callbacks=True
)

lm = layout_manager()

app.layout = dmc.NotificationsProvider(
    children=[
        dcc.Store(id='store'),
        header.get_header(),
        html.Div(
            [
                lm.get_layout('home')
            ],
            className='main-container',
            id='main-container',
        )
    ],
    position='top-center',
    autoClose=False,
)

if __name__ == '__main__':
    app.run_server(debug=True)