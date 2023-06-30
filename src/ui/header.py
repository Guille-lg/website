import dash_mantine_components as dmc
from dash_iconify import DashIconify


def get_header():
    home_button = dmc.Button(
        'Home',
        className='button',
        id='home-button',
        leftIcon=DashIconify(icon='iconamoon:home'),
        variant='outline',
        size='lg',
        color='gradient',
        ml='5vh',
    )

    cv_button = dmc.Button(
        'My CV',
        className='button',
        id='cv-button',
        variant='white',
        size='lg',
        color='gradient',
    )

    projects_button = dmc.Button(
        'My Projects',
        className='button',
        id='projects-button',
        variant='white',
        size='lg',
        color='gradient',
    )

    contact_button = dmc.Button(
        'Contact',
        className='button',
        id='contact-button',
        variant='white',
        size='lg',
        color='gradient',
    )


    button_group = dmc.Group(
        spacing='xl',
        children=[
            home_button,
            cv_button,
            projects_button,
            contact_button
        ]
    )

    title = dmc.Title(
        "Guillermo López Gómez",
        variant='gradient',
        mr='5vh',
        weight=500,
    )

    header = dmc.Header(
        [
            button_group,
            title
        ],
        height='10vh',
        display='flex',
        pos='sticky',
        style={
            'justify-content': 'space-between',
            'align-items': 'center',
        }
    )

    return header
