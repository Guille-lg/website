import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import html

SOCIALS = [
    {
        'name': 'LinkedIn',
        'icon-name': 'skill-icons:linkedin',
        'url': 'https://www.linkedin.com/in/guillermolopezgomez/'

    },
    {
        'name': 'GitHub',
        'icon-name': 'simple-icons:github',
        'url': 'https://github.com/Guille-lg'
    },
    {
        'name': 'Gmail',
        'icon-name': 'logos:google-gmail',
        'url': 'mailto:guillerlogo@gmail.com?subject=Hello%20from%20your%20website!'
    }
]


class main_layout:
    @staticmethod
    def get_divider():
        return dmc.Divider(
            color='blue',
            w='90%',
            m='auto',
        )

    @staticmethod
    def __get_greetings_section():

        title = dmc.Title(
            'BUILDING STORIES FROM DATA',
            variant='gradient',
            size='10vh',
            weight=500,
            mt='10vh',
        )

        data_science_button = dmc.Button(
            'What is Data Science?',
            className='button',
            variant='gradient',
            size='xl',
        )

        about_me_button = dmc.Button(
            'About me',
            className='button',
            id='about-me-button',
            variant='outline',
            size='xl',
            ml='2rem',
        )

        button_container = dmc.Center(
            children=[
                data_science_button,
                about_me_button
            ],
            mt='5vh',
            style={
                'justify-content': 'start',
            }
           
        )

        greetings_container = dmc.Container(
            children=[
                title,
                button_container
            ],
            maw='100%',


        )

        image = dmc.Image(
            src='/assets/images/ds.png',
            w='10vh',
            h='10vh',
        )

        body_container = dmc.Container(
            children=[
                greetings_container,
                image
            ],
            maw='100%',
            h='90vh',
            style={
                'display': 'flex',
                'flex-direction': 'row',
                'justify-content': 'space-between',
                'background-image': 'url(/assets/images/gradient_background.jpg)',
                'background-size': 'cover',
                'background-position': 'center',
            }

        )

        return body_container

    @staticmethod
    def __get_about_me_section():
        title = dmc.Title(
            'Who am I?',
            variant='gradient',
            size='7vh',
            weight=500,
        )

        subtitle = dmc.Title(
            'Hey there! I\'m Guillermo',
            variant='gradient',
            size='5vh',
            weight=500,
            order=3,
        )

        text = dmc.Text(
            'I\'m a college student based in Madrid, currently pursuing a double  degree in Computer Science and Business Administration at UCM. I\'m passionate about data science and its applications to business, and I\'m always looking for new challenges to learn and grow. I\'m always ready to make a positive impact and contribute to exciting projects, so let\'s connect and explore the possibilities together!',
            color='blue',
            mt='2rem',
        )

        cv_button = dmc.Button(
            'Want to know more?, check my CV!',
            variant='gradient',
            id='secondary-cv-button',
            className='button',
            size='lg',
            radius='md',
            mt='2rem',
            w='fit-content',
        )

        button_container = dmc.Container(
            [cv_button],
            mr=0,
            ml='auto',
        )

        text_container = dmc.Container(
            children=[
                subtitle,
                text,
                button_container
            ],
            p='2rem',
            m=0,
            w='50%',
            style={
                'display': 'flex',
                'flex-direction': 'column',
                'justify-content': 'center',
                'box-shadow': 'rgba(0, 0, 0, 0.35) 0px 5px 10px',
                'border-radius': '0.5rem',
            }
        )

        about_me_container = dmc.Container(
            children=[
                title,
                text_container, 
               
            ],
            maw='100%',
            p='2rem',
            h='50vh',
            style={
                'display': 'flex',
                'flex-direction': 'row',
                'justify-content': 'center',
                'align-items': 'center',
                'gap': '10vh',
            }
        )

        return about_me_container

    @staticmethod
    def get_social_cards():
        card_list = []

        for social in SOCIALS:
            icon = DashIconify(
                icon=social['icon-name'],
                width=40,
                height=40,
            )

            name = dmc.Text(
                social['name'],
                color='black',
                weight=500,
                size='lg',
                mt='2vh',
            )

            card = html.A(
                href=social['url'],
                className='social-card',
                children=[
                    dmc.Card(
                        children=[
                            icon,
                            name
                        ],
                        className='social-card-container',
                        shadow='sm',
                        radius='md',
                        p='1.5rem',
                        display='flex',
                        style={
                            'transition': '0.3s',
                            'cursor': 'pointer',
                            'box-shadow': 'rgba(0, 0, 0, 0.35) 0px 5px 10px',
                            'flex-direction': 'column',
                            'justify-content': 'center',
                            'align-items': 'center',
                        },
                    )
                ],
                style={
                    'transition': '0.3s',
                    'text-decoration': 'none',
                    'color': 'black',
                }
            )
            card_list.append(card)

        return card_list

    @staticmethod
    def get_socials_section():
        card_list = main_layout.get_social_cards()

        card_container = dmc.Group(
            children=card_list,
            spacing='xl',
            position='apart',
            grow=True,
        )

        socials_title = dmc.Title(
            'Find me on ...',
            variant='gradient',
            size='7vh',
            weight=500,
            mb='5vh',
            ta='center',
        )

        socials_container = dmc.Container(
            children=[
                socials_title,
                card_container
            ],
            display='flex',
            w='80%',
            style={
                'flex-direction': 'column',
                'justify-content': 'center',
            }
        )

        section_container = dmc.Container(
            children=[
                socials_container
            ],
            maw='100%',
            h='fit-content',
            p='5vh',
            style={
                'display': 'flex',
                'justify-content': 'center',
                'align-items': 'center',
            }
        )

        return section_container

    def get_main_layout():

        container = dmc.Container(
            children=[
                main_layout.__get_greetings_section(),
                main_layout.get_divider(),
                main_layout.__get_about_me_section(),
                main_layout.get_divider(),
                main_layout.get_socials_section()
            ],
            maw='100%',
            p=0,
        )

        return container
