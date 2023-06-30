
import src.database as db


# Dash imports
import dash_mantine_components as dmc
from dash_iconify import DashIconify

class contact_layout:

    @staticmethod
    def __get_title():
        title = dmc.Title(
            'Would love to hear from you,\n Let\'s get in touch!',
            size='3rem',
            variant='gradient',
            weight=500,
            ta='center',
        )

        description = dmc.Text(
            "Whether you have any questions, want to propose any projects or just to say hi, I'll try my best to get back to you!",
            size='lg',
            weight=500,
            color='blue',
            ta='center',
            mt='2vh',
            mb='5vh',
        )

        title_container = dmc.Container(
            children=[
                title,
                description
            ],
            maw='100%',
            style={
                'display': 'flex',
                'flex-direction': 'column',
            }
        )

        return title_container

    @staticmethod
    def __get_form():
        name_input = dmc.TextInput(
            label='Full Name',
            id='name-input',
            icon=DashIconify(icon='lucide:text-cursor-input'),
            placeholder='John Doe',
            required=True,
            size='md',
            radius='md',
        )

        email_input = dmc.TextInput(
            label='Email',
            id='email-input',
            placeholder='john.doe@gmail.com',
            icon=DashIconify(icon='mdi-light:email'),
            required=True,
            size='md',
            radius='md',
        )


        message_input = dmc.Textarea(
            label='Your comment',
            id='message-input',
            placeholder='Write your message here ...',
            required=True, 
            size='md',
            autosize=True,
            maxRows=4,
        )

        submit_button = dmc.Button(
            'Submit',
            variant='gradient',
            className='button',
            id='submit-button',
            size='lg',
            radius='md',
            leftIcon=DashIconify(icon='fa:send'),
            style={
                'transition': 'all 0.2s ease-in-out',
            }
        )

        button_wrapper = dmc.Container(
            children=[
                submit_button
            ],
            maw='100%',
            style={
                'display': 'flex',
                'justify-content': 'flex-end',
            }
        )

        container = dmc.Container( 
            children=[
                name_input,
                email_input,
                message_input,
                button_wrapper,
            ],
            maw='100%',
            w='60%',
            m=0,
            style={
                'display': 'flex',
                'flex-direction': 'column',
                'gap': '1rem',
                'border-radius': '1rem',
                'padding': '2rem',
                'box-shadow': 'rgba(99, 99, 99, 0.3) 0px 2px 8px 0px',
            }
        )

        return container
        

    @staticmethod
    def get_contact_layout():

        body_container = dmc.Container(
            children=[
                contact_layout.__get_title(),
                contact_layout.__get_form(),
            ],
            maw='100%',
            h='90vh',
            style={
                'display': 'flex',
                'flex-direction': 'column',
                'justify-content': 'center',
                'align-items': 'center',
            }

        )

        page_container = dmc.Container(
            children=[
               body_container
            ],
            maw='100%',
        )

        return page_container
    

    @staticmethod
    def get_contact_layout_sent():

        title = dmc.Title(
            'Thank you for your message!',
            variant='gradient',
            size='7vh',
            ta='center',
            mb='5vh',
            weight=500,
        )

        subtitle = dmc.Title(
            'I will get back to you as soon as possible! :)',
            size='3vh',
            color='blue',
            ta='center',
            weight=500,
        )
        
        subtitle2= dmc.Title(
            ' If you want to send another message, please refresh the page.',
            size='3vh',
            color='blue',
            ta='center',
            weight=500,
        )

        text_container = dmc.Container(
            children=[
                title,
                subtitle,
                subtitle2,
            ],
            p='2rem',
            w='fit-content',
            style={
                'box-shadow': 'rgba(0, 0, 0, 0.35) 0px 5px 10px',
                'border-radius': '1rem',
            }
        )

        body_container = dmc.Center(
            [text_container],
            h='90vh',
            maw='100%',
        )

        return body_container

