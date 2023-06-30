# Dash imports
import dash_mantine_components as dmc
from dash_iconify import DashIconify

PROJECT_LIST = {
    'WeRepair': {
        'institution' : 'Complutense University of Madrid (UCM)',
        'description' : 'A web application that allows users to request and offer repair services. This webapp received the highest grade in the subject "Web Development".',
        'chips' : ['PHP', 'MySQL', 'HTML', 'CSS', 'JavaScript', 'jQuery', 'Bootstrap', 'Git', 'GitHub', 'Scrum', 'Agile'],
        'available' : False,
    },
    'SDG Labelling App':{
        'institution' : 'United Nations Development Programme (UNDP)',
        'description' : 'A web application that allows users to label paragraphs for the Sustainable Development Goals (SDGs).',
        'chips' : ['Python','Machine Learning', 'Natural Language Processing', 'Flask', 'GitFlow', 'GitHub', 'Data Visualization'],
        'available' : False,
    },

    'Prediction of death in Covid-19 patients' : {
        'institution' : 'Complutense University of Madrid (UCM)',
        'description' : 'My final degree project. A machine learning model that predicts the death of Covid-19 patients.',
        'chips' : ['Python', 'Machine Learning', 'Embeddings', 'SQL', 'Data Visualization', 'Statistics'],
        'available' : False,
    }
    
}

class project_list_layout:

    def __get_chips(chip_list):
        chips = []

        for chip in chip_list:
            aux = dmc.Badge(
                str(chip).upper(),
                variant='dot',
                color='indigo',
                size='md',
            )
            chips.append(aux)
        
        chip_group = dmc.Group(
            children=chips,
            spacing='xs',
            w='70%',
            style={
                'display': 'flex',
                'align-items': 'center',
                'justify-content': 'center',
            }
        )

        return chip_group

    def __get_project_card(item_name):


        title = dmc.Title(
            item_name,
            variant='gradient',
            size='2rem',
            weight=500,
            ta='center',
        )

        desc = dmc.Text(
            PROJECT_LIST[item_name]['description'],
            color='blue',
            weight=500,
            ta='center',
        )

        chips = project_list_layout.__get_chips(PROJECT_LIST[item_name]['chips'])

        button = dmc.Button

        if PROJECT_LIST[item_name]['available']:
            button = dmc.Button(
                'See more',
                variant='gradient',
                size='lg',
                className='button',
                id={'type': 'project-button', 'project': item_name},
                mt='1rem',
            )
        else:
            button = dmc.Button(
                'Comming soon!',
                variant='gradient',
                size='lg',
                className='button',
                disabled=True,
                mt='1rem',
            )

        text_container = dmc.Container(
            children=[
                title,
                desc,
                chips,
                button,
            ],
            style={
                'display': 'flex',
                'flex-direction': 'column',
                'gap': '1rem',
                'align-items': 'center',
                'justify-content': 'center',
            }
        )

        project_container = dmc.Container(
            children=[
                text_container,
            ],
            maw='100%',
            p='2rem',
            mb='5vh',
            style={
                'display': 'flex',
                'flex-direction': 'row',
                'box-shadow': 'rgba(0, 0, 0, 0.35) 0px 5px 10px',
                'border-radius': '0.5rem',  
                'align-items': 'center',  
                'justify-content': 'space-between',
                'gap': '10vh',
            }

        )

        return project_container
        


    def get_project_list_layout():

        title = dmc.Title(
            'Welcome to my projects page!',
            size='3rem',
            variant='gradient',
            weight=500,
            ta='center',
            mt='5vh',
            mb='2vh',
        )

        subtitle = dmc.Text(
            'Here you can find a list of my projects. Click on any of them to see more details.',
            ta='center',
        )

        project_list = []

        for item in PROJECT_LIST:
            project_list.append(project_list_layout.__get_project_card(item))
        
        project_list_container = dmc.Container(
            children=project_list,
            maw='100%',
            mt='5vh',
        )

        body = dmc.Container(
            children=[
                title,
                subtitle,
                project_list_container,
            ],
        )

        return body
