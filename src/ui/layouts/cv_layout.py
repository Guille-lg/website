# dash
import dash_mantine_components as dmc

# constants
TIMELINE_ITEMS = [
    'Who Am I?',
    'Education',
    'Experience',
    'Extra-Curricular Activities',
    'Courses',
    'Languages'
]


CV_SECTIONS = [
    {
        'title': 'Education',
        'items': [{
            'title': 'Double Bachelor\'s in Computer Science and Business Administration',
            'institution': 'Complutense University of Madrid',
            'institution_url': 'https://www.ucm.es/',
            'date': '2019 - 2024',
            'description': [
                'Proficient in programming languages, such as Python, R, Java, C++, or JavaScript, among others.',
                'Knowledge of database systems and querying languages such as SQL, Oracle, MongoDB, ',
                'Knowledge of project management methodologies and practices such as Agile and Scrum.',
                'Ability to design and develop web applications and software solutions'
                ]
        },
            {
            'title': 'Business Analytics and Big Data Program',
            'institution': 'Innovation Studies Center (CEI)',
            'institution_url': 'https://cei.es/',
            'date': '2023',
            'description': [
                'Familiarity with machine learning algorithms and techniques, including supervised and unsupervised learning.',
                'Experience with data visualization and storytelling using tools like PowerBI or Tableau',
                'Understanding of big data technologies and frameworks like Hadoop or Spark.',
                'Experience with data mining and exploratory data analysis.',
                'Understanding of natural language processing (NLP) and text mining techniques.',
                ]
        }
        ]
    },
    {
        'title': 'Experience',
        'items': [
            {
                'title': 'Data Science Support',
                'institution': 'United Nations Data Futures Platform',
                'institution_url': 'https://data.undp.org/',
                'date': '2023',
                'description': [
                    'Responsible for developing and implementing data-driven solutions for complex development challenges, utilizing machine learning, data augmentation, statistical analysis, and other advanced techniques.',
                    'Designed and developed a web application for data labeling, which was subsequently used to train a machine learning model, creating high-quality data that improved model performance.',
                    'Applied web scraping and data analysis techniques to gather information from multiple sources and generate useful datasets for training different models.',

                
                ]
            },
            {
                'title': 'Computer Science Tutor',
                'institution': 'Self Employed',
                'institution_url': 'N/A',
                'date': '2021 - 2023',
                'description': [
                    'Instructor of various subjects at the university and vocational training level, covering topics ranging from algorithms and data structures to databases and software architecture.',
                    'Developed customized lesson plans for each student based on their strengths and weaknesses.'
                ]
            }
        ]
    },
    {
        'title': 'Extra-Curricular Activities',
        'items': [
            {
                'title': 'Web Development',
                'institution': 'Freelance',
                'institution_url': 'N/A',
                'date': '2022 - 2023',
                'description': [
                    'Freelance web application development for a real estate agency, using React, Node.js, and MongoDB.',
                    'Volunteer web development for a non-profit organization, using UCM\'s proprietary CMS.'
                ]
            }
        ]
    },
    {
        'title': 'Courses',
        'items': [
            {
                'title': 'Data Science (120h)',
                'institution': 'CoderHouse',
                'institution_url': 'https://www.coderhouse.es/online/data-science',
                'date': '2023 - 2024',
                'description': [
                    'Online course covering the fundamentals of data science, including statistical data analysis, machine learning, and data visualization.',
                ]
            },
            {
                'title': 'Statistical Learning',
                'institution': 'Stanford University (edX)',
                'institution_url': 'https://www.edx.org/course/statistical-learning',
                'date': '2023',
                'description': [
                    'Online course covering the fundamentals of statistical machine learning, including different regressions, classification, resampling methods, tree-based methods, SVMs and more.',
                ]
            },
            {
                'title': 'Data Analytics Professional Cetificate',
                'institution': 'Google (Coursera)',
                'institution_url': 'https://www.coursera.org/professional-certificates/google-data-analytics#courses',
                'date': '2023',
                'description': [
                    'Online course covering the fundamentals of data analytics, including data cleaning, analysis, visualization and storytelling.',
                ]
            }
        ]
    },
        {
        'title': 'Languages',
        'items': [
            {
                'title': 'Spanish',
                'institution': 'Native Speaker',
                'institution_url': 'N/A',
                'date': 'N/A',
                'description': []
            },
            {
                'title': 'English',
                'institution': 'Highly Proficient',
                'institution_url': 'N/A',
                'date': 'N/A',
                'description': []
            }
        ]
    },
]


class cv_layout:

    @staticmethod
    def __get_cv_divider(type):
        if type == 'transparent':
            return dmc.Divider(
                mt='1rem',
                mb='1rem',
                color='transparent'
            )
        else:
            return dmc.Divider(
                mt='1rem',
                mb='1rem',
            )

    @staticmethod
    def __get_timeline_items():
        items = []
        for item in TIMELINE_ITEMS:
            items.append(
                dmc.TimelineItem(
                    title= dmc.Text(
                        item,
                        weight=700,
                        color='blue.9'
                    ),
                    color='blue.9',
                    mih='10vh',
                )
            )
        return items

    @staticmethod
    def __get_timeline():
        timeline = dmc.Timeline(
            id='cv-timeline',
            active=0,
            bulletSize=15,
            radius='xl',
            align='right',
            color='blue.9',
            lineWidth=2,
            children= cv_layout.__get_timeline_items(),
            h='90%'
        )
        return timeline

    def __get_title_section():
        title = dmc.Title(
            'GUILLERMO LÓPEZ',
            weight=500,
            variant='gradient',
            size='12vh',
        )

        subtitle = dmc.Title(
            'COLLEGE STUDENT',
            order=3,
            weight=500,
            variant='gradient',
            mb='5vh',
        )

        description = dmc.Text(
            'Welcome to my CV! I\'m Guillermo López Gómez, a college student based in Madrid, Spain. I\'m currently finishing a double degree in Computer Science and Business Administration at the Complutense University of Madrid. With a strong passion for machine learning and data science, I thrive in developing data-driven solutions. I also have experience in web application development and enjoy taking on new challenges. I\'m driven, adaptable, and committed to continuous learning. Let\'s connect and explore opportunities to further develop our skills together!',
            weight=400,
            w='70%',
            color='blue.9',
            mb='5vh',
            style={
                'text-align': 'justify'
            }

        )

        title_container = dmc.Container(
            children=[
                title,
                subtitle,
                description
            ],
            display='flex',
            maw='100%',
            style={
                'flex-direction': 'column',
                'align-items': 'center',
            }
        )

        return title_container

    @staticmethod
    def __get_cv_subsection(data):

        institution = dmc.Text(
            data['institution'] 
        )

        if data['institution_url'] != 'N/A':
            institution = dmc.Anchor(
                data['institution'],
                href=data['institution_url'],
            )

        description_items = []
        for subsection in data['description']:
            description_items.append(
                dmc.ListItem(
                    subsection
                )
            )
        description = None
        if len(description_items) >= 1:
            description = dmc.List(
                description_items
            )

        date = None
        if data['date'] != 'N/A':
            date = dmc.Text('(' + data['date'] + ')')


        subsection = dmc.ListItem(
            [
                dmc.Text(
                    [
                        dmc.Text(
                            data['title'] + ', ',
                            weight=700
                        ),
                        institution,
                        date
                        
                    ]
                ),
                cv_layout.__get_cv_divider('transparent'),
                description
            ]
        )

        return subsection

    def __get_section(section):
        items = []
        for item in section['items']:
            items.append(
                cv_layout.__get_cv_subsection(item)
            )
            items.append(
                cv_layout.__get_cv_divider('solid')
            )

        section = dmc.AccordionItem(
            [
                dmc.AccordionControl(
                    children=dmc.Text(
                        section['title'],
                        weight=700,
                        variant='gradient',
                        size='xl',
                    ),

                    style={
                        'transition': '0.3s'
                    }

                ),
                dmc.AccordionPanel(
                    children=dmc.List(
                        items
                    )

                ),
            ],
            value=section['title']
        )

        return section

    @staticmethod
    def get_cv_layout():
        sections = []
        for section in CV_SECTIONS:
            sections.append(
                cv_layout.__get_section(section)
            )

        cv_contents = dmc.Accordion(
            id='cv-accordion',
            children=sections,
            maw='100%',
            miw='80%',
            w='80%',
        )

        cv = dmc.Container(
            children=[
                cv_layout.__get_title_section(),
                cv_contents
            ],
            mb='5vh',
            maw='100%',
            p=0,
            style={
                'display': 'flex',
                'flex-direction': 'column',
                'align-items': 'center',
            }
        )

        body_container = dmc.Container(
            children=[
                cv,
                cv_layout.__get_timeline()
            ],
            h='fit-content',
            maw='100%',
            mih='90vh',
            style={
                'display': 'flex',
                'flex-direction': 'row',
                'align-items': 'center',
                'justify-content': 'space-between',
                'background-image': 'url(/assets/images/gradient_background.jpg)',
                'background-size': 'cover',
                'background-position': '0 0',
            }
        )

        return body_container
