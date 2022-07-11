import csv

d1 = {
    "schedule": {
        "slots": [
            {
                "time": 480,
                "duration": 60,
                "sessions": [
                    {
                        "id": "EVHW39",
                        "title": "Registration @ Ground Foyer",
                        "duration": 60,
                        "abstract": "Please show up on time for registration and bring your E-ticket along with the order code in order for a speedy registration.\r\nWe'll require you to present a form of ID document (ex: passport) to verify your identity.\r\n\r\nDon't be late :)",
                        "day": "2022-07-13",
                        "time": 480,
                        "endTime": 540,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "registration-ground-foyer",
                        "type": "registration",
                        "speakers": [],
                        "start": "2022-07-13T08:00:00+01:00",
                        "end": "2022-07-13T09:00:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 540,
                "duration": 30,
                "sessions": [
                    {
                        "id": "UMU8GH",
                        "title": "Opening Session [in-person & remote]",
                        "duration": 30,
                        "abstract": "Opening Session Opening Session Opening Session Opening Session Opening Session Opening Session Opening Session Opening Session Opening Session Opening Session Opening Session Opening Session Opening Session Opening Session Opening Session Opening Session Opening Session Opening Session Opening Session Opening Session Opening Session Opening Session Opening Session Opening Session",
                        "day": "2022-07-13",
                        "time": 540,
                        "endTime": 570,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "opening-session-in-person-remote",
                        "type": "opening-session",
                        "speakers": [],
                        "start": "2022-07-13T09:00:00+01:00",
                        "end": "2022-07-13T09:15:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 570,
                "duration": 45,
                "sessions": [
                    {
                        "id": "KG3M3F",
                        "title": "Python's role in unlocking the secrets of the Universe with the James Webb Space Telescope",
                        "duration": 45,
                        "abstract": "The James Webb Space Telescope is a groundbreaking infrared observatory resulting from an international collaboration between NASA, the European Space Agency, and the Canadian Space Agency. It was successfully launched on Christmas Day 2021 from Europe's spaceport in Kourou, French Guiana, and is currently orbiting the L2 point 1.5 million km from Earth.\r\n\r\nWebb was designed to address some of the biggest questions in astronomy and astrophysics, including identifying the first stars in the Universe, observing the first galaxies, revealing the initial stages of star and planet formation, and probing the composition of exoplanet atmospheres.\r\n\r\nBut how do we go from the raw data collected by Webb to science-ready data products delivered to astronomers and astrophysicists around the world? How do we embed our understanding of the telescope and its instruments into this process? How did we prepare and test this?\r\n\r\nFrom instrument simulators to the ambitious Webb Calibration Pipeline, the software suites that support these tasks are written in Python. In this talk I will give an overview of Webb, the crucial role of Python in Webb's development and data processing, and I will show and discuss the first publicly released images from this revolutionary telescope.",
                        "day": "2022-07-13",
                        "time": 570,
                        "endTime": 615,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "python-s-role-in-unlocking-the-secrets-of-the-universe-with-the-james-webb-space-telescope",
                        "type": "keynote",
                        "speakers": [
                            {
                                "code": "EKYUCH",
                                "name": "Dr. Patrick Kavanagh",
                                "biography": "Dr. Patrick Kavanagh is an astrophysicist and software developer based at the Dublin Institute for Advanced Studies (DIAS). He is an expert in high-energy studies of supernova remnants, superbubbles and the hot interstellar medium.\r\n\r\nSince moving to DIAS he has worked on the development of calibration and software tools for the Mid-Infrared Instrument (MIRI) on Webb. MIRI is an international project comprising a consortium of European partner institutes, including DIAS, the European Space Agency, and partners in the US.\r\n\r\nHe works on many aspects of MIRI including the calibration of the MIRI Medium Resolution Spectrometer, development of the MIRI simulator, MIRI commissioning activities and analysis tools, and will support MIRI commissioning at the Webb Mission Operations Center at the Space Telescope Science Institute in Baltimore.",
                                "avatar": None,
                                "slug": "dr-patrick-kavanagh",
                                "affiliation": "Dublin Institute for Advanced Studies (DIAS)",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-13T09:30:00+01:00",
                        "end": "2022-07-13T10:15:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 615,
                "title": "Coffee Break",
                "duration": 30,
                "type": "break"
            },
            {
                "time": 645,
                "duration": 45,
                "sessions": [
                    {
                        "id": "3XNT9R",
                        "title": "LocalStack: Turbocharging dev loops and team collaboration for cloud applications",
                        "duration": 45,
                        "abstract": "With the staggering dominance of public cloud providers, dev teams across the globe are increasingly focusing time and energy on optimizing their cloud development and deployment flows. The traditional deploy-and-test cycles against public clouds can become slow and tedious, where developers are often facing several minutes of idle times between deployments that need to be frequently triggered during testing & debugging.\r\n\r\nIn this session, we provide a hands-on introduction to LocalStack (39k+ Github stars), a fully functional local AWS cloud stack. With LocalStack, applications can be developed entirely on your local machine, reducing dev&test cycles from minutes to seconds.\r\n\r\nThe session covers interactive live coding to showcase common scenarios and use cases, different settings for local debugging of Lambdas and containerized apps (e.g., ECS/EKS), as well as some advanced new features that can radically improve productivity and team collaboration patterns.\r\nWe will also glance over the large ecosystem of tools that LocalStack natively integrates with - from IaC frameworks like Terraform or Pulumi, to application frameworks like Serverless or Architect, to a whole suite of tools provided by AWS itself (CDK, SAM, Copilot, Chalice, etc).\r\n\r\nWe'll wrap up the session with a deep dive into some of the Python internals of LocalStack, which reveals some interesting architectural patterns and hidden gems!",
                        "day": "2022-07-13",
                        "time": 645,
                        "endTime": 690,
                        "audience": "intermediate",
                        "rooms": [
                            "Wicklow Hall 1"
                        ],
                        "slug": "localstack-turbocharging-dev-loops-and-team-collaboration-for-cloud-applications",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "DP8DBG",
                                "name": "Waldemar Hummer",
                                "biography": "Waldemar is co-founder and CTO of LocalStack, where he and his team are building the world-leading platform for local cloud development, based on the hugely popular open source framework with 39k+ stars on Github. Prior to founding LocalStack, Waldemar has held several engineering and management roles at startups as well as large international companies, including Atlassian (Sydney), IBM (New York), and more recently as Head of Engineering at Zurich Insurance. Waldemar is originally from Austria and holds a PhD in Computer Science from TU Vienna, where his research focused on software engineering and reliability in large-scale distributed systems.",
                                "avatar": "https://program.europython.eu/media/avatars/profile_head_3P9wr6I.png",
                                "slug": "waldemar-hummer",
                                "affiliation": "LocalStack",
                                "homepage": "https://localstack.cloud",
                                "twitter": "@_localstack"
                            }
                        ],
                        "start": "2022-07-13T10:45:00+01:00",
                        "end": "2022-07-13T11:30:00+01:00"
                    },
                    {
                        "id": "83QRQG",
                        "title": "An Introduction to Apache TVM",
                        "duration": 45,
                        "abstract": "Apache TVM is an open source machine learning compiler framework for CPUs, GPUs, and machine learning accelerators. It aims to enable machine learning engineers to optimize and run computations efficiently on any hardware backend.\r\n\r\nThis talk will present an introduction to Apache TVM using its Python API, and demonstrated using examples of deep learning models being execute in CPUs and Microcontrollers.",
                        "day": "2022-07-13",
                        "time": 645,
                        "endTime": 690,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 2"
                        ],
                        "slug": "an-introduction-to-apache-tvm",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "8ZHWHC",
                                "name": "Leandro Nunes",
                                "biography": "I'm a software engineer, currently working on compilation tools for machine learning workloads and contributing to the Apache TVM Compiler Stack as a PMC member and committer. In the academic background, I hold a M.S. degree in Microelectronics and a B.S. degree in Computer Science.",
                                "avatar": None,
                                "slug": "leandro-nunes",
                                "affiliation": "Arm",
                                "homepage": None,
                                "twitter": "@leandron"
                            }
                        ],
                        "start": "2022-07-13T10:45:00+01:00",
                        "end": "2022-07-13T11:30:00+01:00"
                    },
                    {
                        "id": "8SJSVS",
                        "title": "The Design of Everyday APIs",
                        "duration": 30,
                        "abstract": "What makes a good API for a library? Or more importantly, what makes it bad? This talk will discuss the principles of what goes into user-centered design, and how best to apply those principles when writing a Python library for fellow developers.",
                        "day": "2022-07-13",
                        "time": 645,
                        "endTime": 675,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey B"
                        ],
                        "slug": "the-design-of-everyday-apis",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "K7PLZQ",
                                "name": "Lynn Root",
                                "biography": "Lynn Root is a Staff Engineer at Spotify and resident FOSS evangelist. She is a seasoned speaker on building and maintaining distributed systems, and maintains Spotify’s audio processing framework. Lynn is a global leader of diversity in the Python community, the Chair of the PyLadies global council, and the former Vice Chair of the Python Software Foundation Board of Directors.",
                                "avatar": "https://program.europython.eu/media/avatars/lynn_root_spb_sq_FiY8tmR.jpg",
                                "slug": "lynn-root",
                                "affiliation": "Spotify",
                                "homepage": "https://roguelynn.com",
                                "twitter": "@roguelynn"
                            }
                        ],
                        "start": "2022-07-13T10:45:00+01:00",
                        "end": "2022-07-13T11:15:00+01:00"
                    },
                    {
                        "id": "CJYTER",
                        "title": "Making Python better one error message at a time",
                        "duration": 45,
                        "abstract": "Error reporting has been an area that sadly has not improved a lot recently in the Python interpreter and users have been battling with very obscure runtime errors and puzzling syntax error messages that range from very generic (just “syntax error: invalid syntax”) to directly misleading (the error displayed for unclosed parentheses). This situation has frustrated users for a long time and has forced everyone into learning “what the interpreter really wants to say” or “where the error really could be”. This problem is especially acquitted for first-time learners of the language as they can lose a lot of time trying to decipher what the error messages they just got mean and where the problem may be.",
                        "day": "2022-07-13",
                        "time": 645,
                        "endTime": 690,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "making-python-better-one-error-message-at-a-time",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "NLHSWB",
                                "name": "Pablo Galindo Salgado",
                                "biography": "Pablo Galindo Salgado works in the Python Infrastructure team at the Software Infrastructure department at Bloomberg L.P. He is a CPython core developer and a Theoretical Physicist specializing in general relativity and black hole physics. He is currently serving on the Python Steering Council and he is the release manager for Python 3.10 and 3.11. He has also a cat but he does not code.",
                                "avatar": "https://program.europython.eu/media/avatars/9AwOpo3r_400x400_1_UTovywe.jpg",
                                "slug": "pablo-galindo-salgado",
                                "affiliation": "Bloomberg LP / CPython core team",
                                "homepage": None,
                                "twitter": "pyblogsal"
                            }
                        ],
                        "start": "2022-07-13T10:45:00+01:00",
                        "end": "2022-07-13T11:30:00+01:00"
                    },
                    {
                        "id": "S9ANCN",
                        "title": "Elephants, ibises and a more Pythonic way to work with databases",
                        "duration": 45,
                        "abstract": "In this talk, I will be sharing about Ibis, a software package that provides a more Pythonic way of interacting with multiple database engines. In my own adventures living in Zimbabwe, I’ve always encountered ibises (the bird versions) perched on top of elephants. If you’ve never seen an elephant in real life I can confirm that they are huge, complex creatures. The image of a small bird sitting on top of a large elephant serves as a metaphor for how ibis (the package) provides a less complex, more performant way for Pythonistas to interact with multiple big data engines. \r\n\r\nI'll use the metaphor of elephants and ibises to show how this package can make a data workflow more Pythonic. The Zen of Python lets us know that simple is better than complex. The bigger and more complex your data, the more of an argument there is to use Ibis. Raw SQL can be quite difficult to maintain when your queries are very complex. For Python programmers, Ibis offers a way to write SQL in Python that allows for unit-testing, composability, and abstraction over specific query engines (e.g.BigQuery)! You can carry out joins, filters, and other operations on your data in a familiar, Pandas-like syntax. Overall, using Ibis simplifies your workflows, makes you more productive, and keeps your code readable.",
                        "day": "2022-07-13",
                        "time": 645,
                        "endTime": 690,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 1"
                        ],
                        "slug": "elephants-ibises-and-a-more-pythonic-way-to-work-with-databases",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "7NWTAL",
                                "name": "Marlene Mhangami",
                                "biography": "Marlene is a Zimbabwean software engineer, explorer, and speaker based in the city of Harare. She is an advocate for using science and technology for social good and increasing diversity in these fields. She is a director and vice-chair for the Python Software Foundation and is currently working as a Developer Advocate at Voltron Data. In 2017, she co-founded ZimboPy, a non-profit organization that gives Zimbabwean young women access to resources in the field of technology. She is also the previous chair of PyCon Africa and is an advocate for women in tech on the continent.",
                                "avatar": "https://program.europython.eu/media/avatars/Screenshot_2022-06-13_at_10.23.18_b4fqgxG.png",
                                "slug": "marlene-mhangami",
                                "affiliation": "Voltron Data",
                                "homepage": "marlenemhangami.com",
                                "twitter": "@marlene_zw"
                            }
                        ],
                        "start": "2022-07-13T10:45:00+01:00",
                        "end": "2022-07-13T11:30:00+01:00"
                    },
                    {
                        "id": "YC7KJU",
                        "title": "Code coverage through unit tests running in sub-processes/threads: Locally and automated on GitHub",
                        "duration": 45,
                        "abstract": "Unit testing and code coverage are two essential aspects of an open-source codebase. These unit tests often run in spawned sub-processes or threads as sub-processes or multi-threading allow them to run parallelly. They also make it easier to stop the tests midway if the process is taking too much time (probabilistic tests).\r\n\r\nHowever, running unit tests in a sub-process creates a problem in the local repository as well as in the remote repository. As the documentation of `coverage.py` says — *“Measuring coverage in those sub-processes can be tricky because you have to modify the code spawning the process to invoke coverage.py.”*",
                        "day": "2022-07-13",
                        "time": 645,
                        "endTime": 690,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey A"
                        ],
                        "slug": "code-coverage-through-unit-tests-running-in-sub-processes-threads-locally-and-automated-on-github",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "T8FLGG",
                                "name": "Saransh Chopra",
                                "biography": "I am Saransh, a sophomore at the University of Delhi, pursuing a major in Information Technology and Mathematics. In daylight, I work towards my academic skills and professional commitments, and by night, I develop and maintain open-source research software written in Python, which I believe are the key to collaborative and reproducible research. Currently, I develop PyBaMM, BattBot, liionpack, and my contributions range from DeepXDE to Colour. I also like to experiment with Python a lot in the form of projects, which are all available on my GitHub!",
                                "avatar": "https://program.europython.eu/media/avatars/PyCon_Squared_5BJkaJz.jpg",
                                "slug": "saransh-chopra",
                                "affiliation": "University of Delhi",
                                "homepage": "http://cic.du.ac.in/",
                                "twitter": "@saranshchopra7"
                            }
                        ],
                        "start": "2022-07-13T10:45:00+01:00",
                        "end": "2022-07-13T11:30:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 695,
                "duration": 30,
                "sessions": [
                    {
                        "id": "DYDA3H",
                        "title": "Python & Visual Studio Code - Revolutionizing the way you do data science",
                        "duration": 30,
                        "abstract": "Visual Studio Code along with GitHub, Codespaces, and Azure Machine Learning have been investing substantially into tools and platforms to make the lives of Python data scientists easier, and we want to share why VS Code is now the #1 tool for Python Data Scientists according to the 2021 Python Software Foundation Developer Survey, and how you can leverage VS Code to take your data science productivity to the next level.\r\n\r\nThis talk will walk through several common Python data science scenarios, showcasing all the productive tooling VS Code has to offer along the way. As a sneak peek, we will be demoing a best in class Jupyter Notebooks experience with VS Code Notebooks, a revolutionary new data cleaning / preparation experience with Data Wrangler in VS Code, collaboration features with GitHub and Codespaces, Azure Machine Learning for deployment, and more!",
                        "day": "2022-07-13",
                        "time": 695,
                        "endTime": 725,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey A"
                        ],
                        "slug": "python-visual-studio-code-revolutionizing-the-way-you-do-data-science",
                        "type": "sponsored-talk",
                        "speakers": [
                            {
                                "code": "LLPY8M",
                                "name": "Jeffrey Mew",
                                "biography": "Jeffrey Mew is a Product Manager at Microsoft working on Python Data Science and AI tooling in VS Code. Specifically, he focuses on making the lives of Data Scientists easier across our ecosystem. Jeffrey holds his Bachelor’s Degree in Computer Engineering from the University of Waterloo. He is a lover of dogs and Python (the language, still unsure about the snake).",
                                "avatar": "https://program.europython.eu/media/avatars/IMG_2250_7yWSbHF.jpeg",
                                "slug": "jeffrey-mew",
                                "affiliation": "Micorosft",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-13T11:35:00+01:00",
                        "end": "2022-07-13T12:05:00+01:00"
                    },
                    {
                        "id": "G7MNXY",
                        "title": "From pip to poetry - Python (many) ways of packaging and publishing",
                        "duration": 30,
                        "abstract": "Ever had issues to manage your python packages and environment? Do you know how to create and share a package to the community? It can be challenging if you've never done it, but it also doesn't have to be hard. There is always a better tool to fit our needs.\r\n\r\nIn this presentation, I'd like to discuss how Python's package managers appeared and evolved with time. Discussing pip, pipenv, and poetry, presenting each of their weak and strong points. Also intend to present how to package and publish a simple code with each one of them, and suggest which package manager should you choose, whether you are just starting with python, or feel like there is something bothering and never knew you could solve it easily and painless.",
                        "day": "2022-07-13",
                        "time": 695,
                        "endTime": 725,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey B"
                        ],
                        "slug": "from-pip-to-poetry-python-many-ways-of-packaging-and-publishing",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "PK8LSS",
                                "name": "Vinícius Gubiani Ferreira",
                                "biography": "Love to code, to read other people's code, and to help others achieve what they want with code. Be it directly or by guiding them to find out for themselves.",
                                "avatar": "https://program.europython.eu/media/avatars/profile_xKpnCpq.jpeg",
                                "slug": "vinicius-gubiani-ferreira",
                                "affiliation": "Azion Technologies",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-13T11:35:00+01:00",
                        "end": "2022-07-13T12:05:00+01:00"
                    },
                    {
                        "id": "KMCFKN",
                        "title": "Data Warehouses Meet Data Lakes",
                        "duration": 30,
                        "abstract": "Many organizations have migrated their data warehouses to datalake solutions in recent years.\r\nWith the convergence of the data warehouse and the data lake, a new data management paradigm has emerged that combines the best of 2 approaches: the botton-up of big data and the top-down of a classic data warehouse.",
                        "day": "2022-07-13",
                        "time": 695,
                        "endTime": 725,
                        "audience": "advanced",
                        "rooms": [
                            "Liffey Hall 1"
                        ],
                        "slug": "data-warehouses-meet-data-lakes",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "8MDEKJ",
                                "name": "Mauro",
                                "biography": "Mauro Pelucchi is a senior data scientist and big data engineer \r\nresponsible for the design of the \"Real-Time Labour Market Information System on Skill Requirements\" for CEDEFOP.\r\n\r\nHe currently works as Head of Global Data Science @ EMSI Burning-Glass with the goal to develop innovative models, methods and deployments of labour market data and other data to meet customer requirements and prototype new potential solutions. His main tasks are related to advanced machine learning modelling, labour market analyses, and the design of big data pipelines to process large datasets of online job vacancies.\r\nIn collaboration with the University of Milano-Bicocca, he took part in many research projects related to the labour market intelligence systems.\r\nHe collaborates with the University of Milano-Bicocca as a lecturer at the Master Business Intelligence and Big Data Analytics and with the University of Bergamo as a lecturer in Computer Engineering.",
                                "avatar": "https://program.europython.eu/media/avatars/BGT_Mauro_Pelucchi__LARGE_UV7Pfua.jpg",
                                "slug": "mauro",
                                "affiliation": "I am the Head of Global Data Science @ EMSI Burning-Glass.",
                                "homepage": "www.mauropelucchi.com",
                                "twitter": "@mauropelucchi"
                            }
                        ],
                        "start": "2022-07-13T11:35:00+01:00",
                        "end": "2022-07-13T12:05:00+01:00"
                    },
                    {
                        "id": "MADLNQ",
                        "title": "Python Packaging Automation — Auto-Publish to PyPI via Pull Requests",
                        "duration": 30,
                        "abstract": "A huge source of friction in software is publishing new releases. Somebody has to manually review commits and write a change-log, add a version number, and publish to PyPI. We will cover a better way: an automated process in which new versions are automatically published by merging pull requests.",
                        "day": "2022-07-13",
                        "time": 695,
                        "endTime": 725,
                        "audience": "beginner",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "python-packaging-automation-auto-publish-to-pypi-via-pull-requests",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "P9YEAF",
                                "name": "Justin Mayer",
                                "biography": "Justin Mayer is a serial entrepreneur, investor, and advocate for data portability and privacy. His latest project is [Fortressa.com](https://fortressa.com), which replaces expensive SaaS data silos with self-hosted open-source applications. He also maintains the [Pelican static site generator](https://github.com/getpelican/pelican) as well as a number of other projects for Python, Django, and the Fish shell.\r\n\r\nJustin speaks Japanese and Italian, graduated with honors from the University of California, Berkeley, and received his M.B.A. from the Wharton School of Business.\r\n\r\nHe writes about security and privacy at [justinmayer.com](https://justinmayer.com) and via [@JMayer on Twitter](https://twitter.com/jmayer).",
                                "avatar": "https://program.europython.eu/media/avatars/jm_c7gpVSI.jpg",
                                "slug": "justin-mayer",
                                "affiliation": "Fortressa.com",
                                "homepage": "https://justinmayer.com",
                                "twitter": "@JMayer"
                            }
                        ],
                        "start": "2022-07-13T11:35:00+01:00",
                        "end": "2022-07-13T12:05:00+01:00"
                    },
                    {
                        "id": "STQEKX",
                        "title": "Using python to predict Asset price reversals.",
                        "duration": 30,
                        "abstract": "Using Pandas, Python and Plotly to locate potential trend reversals in Stocks, Crypto or any OHLC feed.  Learn how to locate Fibonacci retrace levels and predict price reversal zones for the lowest risk entry to a trade.",
                        "day": "2022-07-13",
                        "time": 695,
                        "endTime": 725,
                        "audience": "intermediate",
                        "rooms": [
                            "Wicklow Hall 1"
                        ],
                        "slug": "using-python-to-predict-asset-price-reversals",
                        "type": "sponsored-talk",
                        "speakers": [
                            {
                                "code": "K379P3",
                                "name": "Niall O'Connor",
                                "biography": "Niall started coding on a sord m5 in 1984, love coding.  Started playing music in 1986, love performing. Started working in a bank in 2012, love trading.  Started gardening in 2017, love gardening.  Started noticing cycles in the markets, similar to the gardening and the seasons.  Started investigating supply chains and trends.  Realized coding and markets and gardening all related.  Discovered harmonic and fibonacci based patterns in the trends, just like music.  Realized my entire life was one gigantic intertwined blob of stuff.  Realized everyone else life is more or less the same.  Chilled out and condensed it all into a 30 minute talk.",
                                "avatar": None,
                                "slug": "niall-o-connor",
                                "affiliation": "Bank Of America",
                                "homepage": "nialloconnor.info",
                                "twitter": "@ZechsMarquie"
                            }
                        ],
                        "start": "2022-07-13T11:35:00+01:00",
                        "end": "2022-07-13T12:05:00+01:00"
                    },
                    {
                        "id": "ZYAD7Z",
                        "title": "The beginner’s data science project checklist",
                        "duration": 30,
                        "abstract": "In this talk, I will give you tips and practical advice on what steps to follow and how to plan your data science project to avoid making the most common mistakes during its development.\r\n\r\nDespite my limited experience delivering data science projects, I have learned how to avoid certain mistakes. In this talk I will teach you how to prevent them and save you lots of headaches.",
                        "day": "2022-07-13",
                        "time": 695,
                        "endTime": 725,
                        "audience": "beginner",
                        "rooms": [
                            "Liffey Hall 2"
                        ],
                        "slug": "the-beginners-data-science-project-checklist",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "XZLFAA",
                                "name": "Sara Iris Garcia",
                                "biography": "Business Intelligence analyst at NHS and machine learning enthusiast. Sara is active in the Python community and efforts in empowering women in tech by leading and organizing events focused on increasing the visibility of women in stem careers.",
                                "avatar": "https://program.europython.eu/media/avatars/20200525_121756_wfAB0TP.jpg",
                                "slug": "sara-iris-garcia",
                                "affiliation": "NHS",
                                "homepage": "https://montjoile.medium.com/",
                                "twitter": "@montjoile"
                            }
                        ],
                        "start": "2022-07-13T11:35:00+01:00",
                        "end": "2022-07-13T12:05:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 730,
                "duration": 45,
                "sessions": [
                    {
                        "id": "8KEVYF",
                        "title": "The intricate art of making your (internal) clients happy - the story from a Python-centered Infra team",
                        "duration": 45,
                        "abstract": "If you have ever worked on an internal company project, you may feel it deep in your bones.\r\nLet’s say that you discovered a need for a generic technological component in your organization’s tech stack. You identified stakeholders, gathered requirements, and started agile iterations on providing it. Then comes a day when you can show the MVP to your internal client! Yet… the client has lost his interest: maybe right now he says that he has already come up with his own temporary solution and he has no intention to switch to another one?  Building internal products differs from commercial ones - there is no flow of cash and your clients are fully transparent.\r\n\r\nIn this talk, I would like to share with you my experience and tips connected with developing such internal tools and standards. All of this from the perspective of a member of the Machine Learning Infra team that is delivering its solutions to a rapidly growing ML department in a company whose product is used by 300 million unique users per month.\r\n\r\nBut let’s be specific! I will talk about:\r\n\r\n- Common pitfalls and try to dig up the reasons for why they happen when developing internal solutions\r\n- How one can approach delivering tools (spoiler: pilot programs, guilds, and more!)\r\n- Learnings from introducing such approaches (what worked, what didn’t) in our case",
                        "day": "2022-07-13",
                        "time": 730,
                        "endTime": 775,
                        "audience": "intermediate",
                        "rooms": [
                            "Wicklow Hall 1"
                        ],
                        "slug": "the-intricate-art-of-making-your-internal-clients-happy-the-story-from-a-python-centered-infra-team",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "FSUDFU",
                                "name": "Paulina Winkowska",
                                "biography": "Paulina fell in love with Python and Machine Learning back in her university years and right now she continues her adventure as Machine Learning Engineer at Brainly. Based in Kraków, Poland, she spends her free time learning ice skating and inline skating.",
                                "avatar": "https://program.europython.eu/media/avatars/Zrzut_ekranu_2022-03-24_o_13.52.28_Cropped_1_alDGEnP.png",
                                "slug": "paulina-winkowska",
                                "affiliation": "Brainly",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-13T12:10:00+01:00",
                        "end": "2022-07-13T12:40:00+01:00"
                    },
                    {
                        "id": "9LFFBL",
                        "title": "Czech Drought Monitoring system – a journey from manual work to global drought monitoring and machine learning, powered by Python",
                        "duration": 30,
                        "abstract": "This talk aims to encourage beginner developers not to underestimate the skills and benefits they can bring to various non-IT environments. I joined a team focused on drought research at the Czech Academy of Science in 2016 with a fresh degree in Geoinformatics and minimal experience with coding. Thanks to this very little initial knowledge, we were able to build a robust system providing drought monitoring and forecast for Czechia and also the whole of central Europe. We were able to fight through text files, user inputs, and geodata of all sorts and say goodbye to manual processing thanks to Python and its geospatial and data processing libraries. On the technical side, the presentation should introduce some of the handy geospatial and data processing tools to get your hands on any task, from producing colorful maps to analyzing time trends in satellite imagery. It should also be a guide on identifying needs and building the most necessary data manipulation processes from scratch.",
                        "day": "2022-07-13",
                        "time": 730,
                        "endTime": 760,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey B"
                        ],
                        "slug": "czech-drought-monitoring-system-a-journey-from-manual-work-to-global-drought-monitoring-and-machine-learning-powered-by-python",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "HGRDTS",
                                "name": "Monika Bláhová",
                                "biography": "I am Monika Bláhová, currently based at Global Change Research Institute, CAS in Brno, Czech Republic as a GIS data analyst and first-year Ph.D. student. My background is cartography and geoinformatics, and my first experience with coding is from 2013 with JavaScript. Since then, I have walked a long way through learning Python, lecturing PyLadies courses, working as an IT administrator, and finally landing in a big scientific team focusing on climate change’s impact on the agroecosystems at the Czech Academy of Science.",
                                "avatar": None,
                                "slug": "monika-blahova",
                                "affiliation": "Global Chnage Research Institute, CAS",
                                "homepage": "https://www.czechglobe.cz/en/",
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-13T12:10:00+01:00",
                        "end": "2022-07-13T12:40:00+01:00"
                    },
                    {
                        "id": "E7CX9K",
                        "title": "CPython bugs & risky features",
                        "duration": 45,
                        "abstract": "In this talk we will look into a few bug cases or doubtful features in CPython some of which are still present (and known to bugs.python.org) and may impose a security risk for admins or organizations.",
                        "day": "2022-07-13",
                        "time": 730,
                        "endTime": 775,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "cpython-bugs-risky-features",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "KL7QNZ",
                                "name": "disconnect3d",
                                "biography": "Disconnect3d is a security engineer at Trail of Bits where he hunt for security bugs in different kinds of software using both manual code analysis and various tools like static analyzers, fuzzers and others. He specializes in low level aspects and likes to understand how things works under the hood. On his free time, Disconnect3d plays CTF security competitions with justCatTheFish team and plays DoTA2 moba game.",
                                "avatar": "https://program.europython.eu/media/avatars/cropped_5gRT9IF.jpg",
                                "slug": "disconnect3d",
                                "affiliation": "Trail of Bits",
                                "homepage": "https://disconnect3d.pl/",
                                "twitter": "@disconnect3d_pl"
                            }
                        ],
                        "start": "2022-07-13T12:10:00+01:00",
                        "end": "2022-07-13T12:55:00+01:00"
                    },
                    {
                        "id": "N3HJ87",
                        "title": "Taking charge of your race conditions",
                        "duration": 45,
                        "abstract": "Are you working with threads, processes, or more generally “workers”? And do you have blocks of code that must not be called concurrently? Maybe you didn't even realise it until your system experienced a bug you could not reproduce until the stars aligned. Then you surely know that hope is not the answer to a robust system, we must be prepared to face worst-case scenarios.\r\n\r\nThis talk will first briefly present race conditions, a staple in concurrent computing. We will then compare implicit and explicit concurrency management in your core logic, that is whether you delegate or craft protective logic yourself. Next comes testing, the real crux of the talk, where we will demonstrate how to manufacture a race condition. Finally we will explore how to solve such problems with the built-in tools the Python standard library offers.",
                        "day": "2022-07-13",
                        "time": 730,
                        "endTime": 775,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey A"
                        ],
                        "slug": "taking-charge-of-your-race-conditions",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "MHFQEH",
                                "name": "Borjan Tchakaloff",
                                "biography": "Borjan has been fully focusing his attention on software engineering with Python for the last four years. Prior to that, he was neck deep in the Android world where he was a maintainer of an Android distribution for a phone manufacturer for a few years.\r\nPython came into play there as a nice automation language from applying missing Linux kernel patches to bench testing operating system builds.",
                                "avatar": None,
                                "slug": "borjan-tchakaloff",
                                "affiliation": "AgOS",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-13T12:10:00+01:00",
                        "end": "2022-07-13T12:40:00+01:00"
                    },
                    {
                        "id": "NUF3K9",
                        "title": "Applying machine learning capabilities to wearable IoT devices for boxing technique management",
                        "duration": 30,
                        "abstract": "IoT devices are increasing in power and capabilities, now allowing developers to deploy machine learning models on the device. This talk will analyse a boxing training session with motion sensors onboard multiple IoT devices using TinyML: a TensorFlow-based framework. Ultimately, these machine-learning powered IoT devices provide feedback to boxers on their technique.",
                        "day": "2022-07-13",
                        "time": 730,
                        "endTime": 760,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 2"
                        ],
                        "slug": "applying-machine-learning-capabilities-to-wearable-iot-devices-for-boxing-technique-management",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "DEZCB8",
                                "name": "Anthony I. Joseph",
                                "biography": "Anthony is an Australian software engineer and mathematician. As a UTS MBT graduate, Anthony is the technology co-founder of a property and cycling-tech startup and enjoys teaching and learning coding with the Australian startup scene.",
                                "avatar": "https://program.europython.eu/media/avatars/Image_from_iOS_XuOClu6.jpg",
                                "slug": "anthony-i-joseph",
                                "affiliation": "Bike Party",
                                "homepage": "https://bikeparty.com.au",
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-13T12:10:00+01:00",
                        "end": "2022-07-13T12:40:00+01:00"
                    },
                    {
                        "id": "QQJFSS",
                        "title": "On the benefits of using workflows: insights from two software tools in the context of computational neuroscience",
                        "duration": 45,
                        "abstract": "The Blue Brain Project strives to simulate the whole mouse brain. The amount of data and code this implies is astoundingly high, and it requires the development of software tools that have both a strict and clear structure and that are resilient to errors that will manifest when developing complex code. Workflows are a straightforward way to maintain structure in toolchains that grow increasingly complex. Workflow management packages such as Luigi bring functionality to run different tasks in parallel, keep track of completed tasks and improve the reproducibility. This poster will present two Blue Brain Project software tools, the e-model-packages software and BluePyEModel, focusing on the creation and distribution of in-silico neuron cells. The e-model-packages software collects cells from an in-silico brain circuit and arranges them in individual ‘neuron packages’ to be distributed to the public through the Blue Brain online portals. The cells packages it creates are designed to be easily run with the open source EModelRunner package. The BluePyEModel software creates and optimizes in-silico neurons and is able to reproduce features from real neuronal experiment recordings. Under the hood, it uses the open source BluePyEfe and eFel packages to extract the electrophysiological features from experimental cells, and the open source BluePyOpt simulator to optimize and validate the parameters of the in-silico neurons.",
                        "day": "2022-07-13",
                        "time": 730,
                        "endTime": 775,
                        "audience": "",
                        "rooms": [
                            "Forum"
                        ],
                        "slug": "on-the-benefits-of-using-workflows-insights-from-two-software-tools-in-the-context-of-computational-neuroscience",
                        "type": "poster",
                        "speakers": [
                            {
                                "code": "YDZC9Z",
                                "name": "Aurélien Jaquier",
                                "biography": "Hi, my name is Aurélien Jaquier, from Switzerland, I am 27 and I currently work for the Blue Brain Project as a Scientific Software Developer. I have a Master of Science MSc in Physics from the EPFL (Ecole Polytechnique Fédérale de Lausanne), with a master thesis centered on dwarf galaxy simulation.\r\nI love sciences and coding, and have been blessed with a job where I can help fundamental brain research with my coding skills. I develop and maintain different software in the context of neuron cell simulation and electrophysiological parameter optimization, such as EModelRunner, BluePyOpt or eFel.\r\nFeel free to talk to me in english, french or japanese.",
                                "avatar": "https://program.europython.eu/media/avatars/photo_DyCk2BJ.jpg",
                                "slug": "aurelien-jaquier",
                                "affiliation": "Blue Brain Project",
                                "homepage": "https://www.epfl.ch/research/domains/bluebrain/",
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-13T12:10:00+01:00",
                        "end": "2022-07-13T12:55:00+01:00"
                    },
                    {
                        "id": "YYQBM3",
                        "title": "Choosing the right database for your next project - Looking at options beyond PostgreSQL and MySQL",
                        "duration": 30,
                        "abstract": "In the last few years, lots of new database engines have been developed, making the selection process even more challenging than it was before, if you want to maintain an edge.\r\n\r\nThe talk will give an overview of what to consider in different situations.",
                        "day": "2022-07-13",
                        "time": 730,
                        "endTime": 760,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 1"
                        ],
                        "slug": "choosing-the-right-database-for-your-next-project-looking-at-options-beyond-postgresql-and-mysql",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "QYTJB9",
                                "name": "Marc-Andre Lemburg",
                                "biography": "Marc-Andre is the CEO and founder of eGenix.com, a Python-focused project and consulting company based in Germany, specializing in the data, finance and database space. He has a degree in mathematics from the University of Düsseldorf.\r\n\r\nHis work with and for Python started in 1994. He is a Python Core Developer, designed and implemented the Unicode support in Python, and author of the mx Extensions, e.g. mxTools, mxDateTime and mxODBC, which are now distributed and maintained through eGenix.com.\r\n\r\nMarc-Andre is a EuroPython Society (EPS) Fellow, a Python Software Foundation (PSF) founding Fellow and co-founded a local Python meeting in Düsseldorf (PyDDF). He served on the board of the PSF and EPS for many terms and loves to contribute to the growth of Python where ever he can.\r\n\r\nMore information is available on https://malemburg.com/",
                                "avatar": "https://program.europython.eu/media/avatars/mal-business-2-170x170_VPXpWrX.jpg",
                                "slug": "marc-andre-lemburg",
                                "affiliation": "eGenix.com Software, Skills and Service GmbH",
                                "homepage": "https://egenix.com/",
                                "twitter": "@malemburg"
                            }
                        ],
                        "start": "2022-07-13T12:10:00+01:00",
                        "end": "2022-07-13T12:40:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 780,
                "title": "Lunch Break",
                "duration": 60,
                "type": "break"
            },
            {
                "time": 840,
                "duration": 30,
                "sessions": [
                    {
                        "id": "DSCHNK",
                        "title": "Managing the code quality of your project. Leave the past behind: Focus on new code.",
                        "duration": 30,
                        "abstract": "If you try to use Pylint or Flake8 on a legacy project, the results are usually truly overwhelming. There might be thousands of warnings, hundreds of errors and maybe even no unit tests. \r\nThe usual emotional response to this is distress, exasperation... even despair. And then the question comes: *Where do I start?*\r\n\r\nDuring this talk we will see why it’s better to set old code aside and focus first on the new code you’re writing. We’ll show some possible approaches and tools that can help you keep the focus and deliver new code with a high level of quality.",
                        "day": "2022-07-13",
                        "time": 840,
                        "endTime": 870,
                        "audience": "intermediate",
                        "rooms": [
                            "Wicklow Hall 1"
                        ],
                        "slug": "managing-the-code-quality-of-your-project-leave-the-past-behind-focus-on-new-code",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "QQNWRG",
                                "name": "Andrea Guarino",
                                "biography": "Developer at SonarSource, working on SonarQube Python analyzer.\r\nPassionate about programming languages, soulslike video games and astrophotography.",
                                "avatar": "https://program.europython.eu/media/avatars/andrea-guarino_09DVeT1.jpeg",
                                "slug": "andrea-guarino",
                                "affiliation": "SonarSource",
                                "homepage": "https://sonarsource.com/",
                                "twitter": "@andre_mnon"
                            }
                        ],
                        "start": "2022-07-13T14:00:00+01:00",
                        "end": "2022-07-13T14:30:00+01:00"
                    },
                    {
                        "id": "HLYETC",
                        "title": "I have to Confess, I still Love Pandas",
                        "duration": 30,
                        "abstract": "Pandas is the first Python library that I learned to use. It is used by data scientists to manage, transform and inspect data. As more and more open-source tools appear, it seems the spotlight has shifted and I would love to shine some light on this tool that all should know.",
                        "day": "2022-07-13",
                        "time": 840,
                        "endTime": 870,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 1"
                        ],
                        "slug": "i-have-to-confess-i-still-love-pandas",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "8EGVC9",
                                "name": "Cheuk Ting Ho",
                                "biography": "Before working in Developer Relations, Cheuk has been a Data Scientist in various companies which demands high numerical and programmatical skills, especially in Python. To follow her passion for the tech community, now Cheuk is the Developer Relations Lead at TerminusDB - an open-source graph database. Cheuk maintains its Python client and engages with its user community daily.\r\n\r\nBesides her work, Cheuk enjoys talking about Python on personal streaming platforms and podcasts. Cheuk has also been a speaker at Universities and various conferences. Besides speaking at conferences, Cheuk also organises events for developers. Conferences that Cheuk has organized include EuroPython (which she is a board member of), PyData Global and Pyjamas Conf. Believing in Tech Diversity and Inclusion, Cheuk constantly organizes workshops and mentored sprints for minority groups. In 2021, Cheuk has become a Python Software Foundation fellow.",
                                "avatar": "https://program.europython.eu/media/avatars/Cheuk_Ting_Ho_myGoldi.JPG",
                                "slug": "cheuk-ting-ho",
                                "affiliation": "TerminusDB",
                                "homepage": "https://cheuk.dev/",
                                "twitter": "@cheukting_ho"
                            }
                        ],
                        "start": "2022-07-13T14:00:00+01:00",
                        "end": "2022-07-13T14:30:00+01:00"
                    },
                    {
                        "id": "L7PFLV",
                        "title": "Protocols in Python: Why You Need Them",
                        "duration": 30,
                        "abstract": "Protocols have been around since Python 3.8. So what are they, and how can they help you write better code? And how are they different from Abstract Base Classes? In this talk I will introduce you to both concepts (ABCs and Protocols), and show you by example how they can make your life easier, and your code cleaner.",
                        "day": "2022-07-13",
                        "time": 840,
                        "endTime": 870,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey B"
                        ],
                        "slug": "protocols-in-python-why-you-need-them",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "CSV3TP",
                                "name": "Rogier van der Geer",
                                "biography": "Before joining GoDataDriven, Rogier obtained a PhD in particle physics. Rogier gained hands-on experience with handling enormous quantities of data and processing, or 'charming,' them into a manageable format before performing complicated analyses. After his PhD he exchanged physical science for data science at GoDataDriven, where he is now putting his skills to use on more business-driven problems. He likes applying data science to anything; be it his daily commute, improving his photography skills or the contents of his lunch box.",
                                "avatar": "https://program.europython.eu/media/avatars/Screenshot_2022-03-16_at_14.59.51_7NEnkCC.png",
                                "slug": "rogier-van-der-geer",
                                "affiliation": "GoDataDriven",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-13T14:00:00+01:00",
                        "end": "2022-07-13T14:30:00+01:00"
                    },
                    {
                        "id": "LTMDS9",
                        "title": "The Geometry of the Universe",
                        "duration": 45,
                        "abstract": "A place to come and talk about the geometry of the universe.\r\n\r\nSagittarius A* and where is the Sun?\r\n\r\ngamma ray bursts\r\n\r\ngravitational waves.\r\n\r\nWhat will James Webb see?\r\n\r\nHow to test different models?\r\n\r\nPython, matplotlib, scipy, astropy\r\n\r\nunits and constants.   Hubble and c\r\n\r\nBut maybe Hubble's not constant?",
                        "day": "2022-07-13",
                        "time": 840,
                        "endTime": 885,
                        "audience": "",
                        "rooms": [
                            "Forum"
                        ],
                        "slug": "the-geometry-of-the-universe",
                        "type": "poster",
                        "speakers": [
                            {
                                "code": "SVGULC",
                                "name": "John Gill",
                                "biography": "I grew up in Yorkshire, UK and always had an interest in space.\r\n\r\nI was lucky enough to be taught by Colin Rourke, when studying mathematics at Warwick some 40 years ago.\r\n\r\nAfter graduating I worked with computers for all my career, using python and linux almost exclusively since 2000.\r\n\r\nThis included a period of many years living and working in Dublin, when I first discovered the python world.\r\n\r\nMy interest in space-time has been rekindled by Colin Rourke's work, after many years of assuming astronomy only had minor details to work out.\r\n\r\nI am now semi-retired, teaching skiing in the winter and do some python mentoring as well.\r\n\r\nI write code to help me explore the universe.",
                                "avatar": None,
                                "slug": "john-gill",
                                "affiliation": "Retired part time ski instructor studying the universe at home",
                                "homepage": "https://github.com/swfiua/gotu",
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-13T14:00:00+01:00",
                        "end": "2022-07-13T15:00:00+01:00"
                    },
                    {
                        "id": "NVKPEJ",
                        "title": "How to craft awesome Machine Learning demos with Python",
                        "duration": 30,
                        "abstract": "Building interactive Machine Learning demos is now easier than ever. With Open Source libraries such as Gradio and Streamlit, you can use Python to craft demos, and use Spaces to share them with the rest of the ML ecosystem as well as non-ML people.  Learning to create graphic interfaces for models is extremely useful for sharing with other people interesting in them. All of this leverages free, open-source tools that anyone can use.",
                        "day": "2022-07-13",
                        "time": 840,
                        "endTime": 870,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 2"
                        ],
                        "slug": "how-to-craft-awesome-machine-learning-demos-with-python",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "BGUJLS",
                                "name": "Omar Sanseviero",
                                "biography": "Omar Sanseviero is a Machine Learning Engineer working at Hugging Face in the Open Source team democratizing the usage of Machine Learning. Previously, Omar worked as a Software Engineer at Google in the teams of Assistant and TensorFlow Graphics. Omar is passionate about education and co-founded AI Learners, a Spanish-speaking community of people that want to learn about AI and its different applications.",
                                "avatar": None,
                                "slug": "omar-sanseviero",
                                "affiliation": "Hugging Face",
                                "homepage": None,
                                "twitter": "@osanseviero"
                            }
                        ],
                        "start": "2022-07-13T14:00:00+01:00",
                        "end": "2022-07-13T14:30:00+01:00"
                    },
                    {
                        "id": "Q3FPVG",
                        "title": "Raise better errors with Exception Groups",
                        "duration": 30,
                        "abstract": "New to python 3.11, Exception Groups help you raise and handle errors more robustly than ever before - you will delve deep into the current gaps in python's exception handling mechanisms, and get to know Error Groups, and a new python keyword except*, that can be used to overcome those issues and to write cleaner code.",
                        "day": "2022-07-13",
                        "time": 840,
                        "endTime": 870,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey A"
                        ],
                        "slug": "raise-better-errors-with-exception-groups",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "VM3NZN",
                                "name": "Or Chen",
                                "biography": "I've been writing Python every day for 5 years, excited about Deep Learning, VR Gaming, and my dog Chika",
                                "avatar": "https://program.europython.eu/media/avatars/1634304370356_45bm3T9.jpg",
                                "slug": "or-chen",
                                "affiliation": "Orca Security",
                                "homepage": "orca.security",
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-13T14:00:00+01:00",
                        "end": "2022-07-13T14:30:00+01:00"
                    },
                    {
                        "id": "X3CQ77",
                        "title": "CPython Developer Panel",
                        "duration": 60,
                        "abstract": "Come meet the folks who make the Python programming language!\r\n\r\nA panel discussion of core Python developers will take place on Wednesday at 2pm. Hear what's on their mind, what they're working on and what the future holds for Python.\r\n\r\nWith Pablo Galindo Salgado, Steve Dower, Batuhan Taskaya, Ken Jin, Irit Katriel and Dr.Mark \"HotPy\" Shannon. Chaired by the esteemed Łukasz \"Any color you like so long as it's black\" Langa.",
                        "day": "2022-07-13",
                        "time": 840,
                        "endTime": 900,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "cpython-developer-panel",
                        "type": "panel",
                        "speakers": [
                            {
                                "code": "YFCVFV",
                                "name": "Łukasz Langa",
                                "biography": "CPython Developer in Residence, Python 3.8 and 3.9 release manager, creator of Black, pianist, dad.\r\n\r\nEqually interested in music and software engineering, as a classically-trained pianist and a long-time contributor to the Python programming language. Loves to build software for musical instruments. Makes music under the [RPLKTR](https://rplktr.com/) moniker.",
                                "avatar": "https://program.europython.eu/media/avatars/%C5%81ukasz_Langa_Portret_2021.10_Prawy_profil_VNI4Aj1.jpeg",
                                "slug": "lukasz-langa",
                                "affiliation": "Python Software Foundation",
                                "homepage": "https://lukasz.langa.pl/",
                                "twitter": "@llanga"
                            },
                            {
                                "code": "NLHSWB",
                                "name": "Pablo Galindo Salgado",
                                "biography": "Pablo Galindo Salgado works in the Python Infrastructure team at the Software Infrastructure department at Bloomberg L.P. He is a CPython core developer and a Theoretical Physicist specializing in general relativity and black hole physics. He is currently serving on the Python Steering Council and he is the release manager for Python 3.10 and 3.11. He has also a cat but he does not code.",
                                "avatar": "https://program.europython.eu/media/avatars/9AwOpo3r_400x400_1_UTovywe.jpg",
                                "slug": "pablo-galindo-salgado",
                                "affiliation": "Bloomberg LP / CPython core team",
                                "homepage": None,
                                "twitter": "pyblogsal"
                            },
                            {
                                "code": "LUY39H",
                                "name": "Mark Shannon",
                                "biography": "I've been using Python since 2005.\r\nI have an extensive background in compilers, virtual machines and static analysis for dynamic languages, specifically Python.\r\nAfter a long interlude working on static analysis tools, I have returned to performance work over the last couple of years.\r\n\r\nI am currently working as technical lead with the \"Faster CPython\" team funded by Microsoft.",
                                "avatar": "https://program.europython.eu/media/avatars/IMG_20191130_122850_3mkOJrs.jpg",
                                "slug": "mark-shannon",
                                "affiliation": "HotPy Ltd",
                                "homepage": None,
                                "twitter": None
                            },
                            {
                                "code": "PMWVSA",
                                "name": "Steve Dower",
                                "biography": "Steve is an engineer who tells people about Python and then gives them excuses to use it and great tools to use it with. He is a core developer and Windows expert for CPython, a member of the Python Security Response Team, and works at Microsoft as a roaming Python expert, making sure Python users are well supported across all their platforms.",
                                "avatar": "https://program.europython.eu/media/avatars/Headshot_Python_2q9HWBk.jpg",
                                "slug": "steve-dower",
                                "affiliation": "Microsoft",
                                "homepage": "https://stevedower.id.au",
                                "twitter": "zooba"
                            },
                            {
                                "code": "LPMUJ3",
                                "name": "Irit Katriel",
                                "biography": "Irit Katriel is a CPython core developer. Her contributions include the implementation of Exception Groups and except* in Python 3.11 and optimisations in exception handling and jump opcodes. She works on the Python Performance team at Microsoft.",
                                "avatar": "https://program.europython.eu/media/avatars/irit_FboTPgh.jpg",
                                "slug": "irit-katriel",
                                "affiliation": "Microsoft",
                                "homepage": None,
                                "twitter": None
                            },
                            {
                                "code": "PBSYRY",
                                "name": "Batuhan Taskaya",
                                "biography": "Batuhan Taskaya is a Python enthusiast who loves to work on the open-source ecosystem surrounding Python. Besides CPython, he regularly contributes/maintains various other projects like fsspec, refactor, black, parso, reiz, teyit and more! Currently employed at Features & Labels, building developer tools for the modern data stack.",
                                "avatar": None,
                                "slug": "batuhan-taskaya",
                                "affiliation": None,
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-13T14:00:00+01:00",
                        "end": "2022-07-13T15:00:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 875,
                "duration": 30,
                "sessions": [
                    {
                        "id": "7DJJMK",
                        "title": "PySnooper: Never use print for debugging again",
                        "duration": 30,
                        "abstract": "I had an idea for a debugging solution for Python that doesn't require complicated configuration like PyCharm. I released PySnooper as a cute little open-source project that does that, and to my surprise, it became a huge hit overnight, hitting the top of Hacker News, r/python and GitHub trending.\r\nIn this talk I'll go into:\r\n\r\n* How PySnooper can help you debug your code.\r\n* How you can write your own debugging / code intelligence tools.\r\n* How to make your open-source project go viral.\r\n* How to use PuDB, another debugging solution, to find bugs in your code.",
                        "day": "2022-07-13",
                        "time": 875,
                        "endTime": 905,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey A"
                        ],
                        "slug": "pysnooper-never-use-print-for-debugging-again",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "RJ7N8Z",
                                "name": "Ram Rachum",
                                "biography": "Ram Rachum is a software developer specializing in Python, and a Fellow of the Python Software Foundation.\r\n\r\nWhen he's not writing his biography in the third person, Ram is doing Python infrastructure work for clients, giving Python training to teams that would like to deepen their Python skills, and organizing the bi-monthly PyWeb-IL conference.",
                                "avatar": "https://www.gravatar.com/avatar/d24c45635a5171615a7cdb936f36daad",
                                "slug": "ram-rachum",
                                "affiliation": "Independent",
                                "homepage": "https://ram.rachum.com/",
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-13T14:35:00+01:00",
                        "end": "2022-07-13T15:05:00+01:00"
                    },
                    {
                        "id": "AKJCWL",
                        "title": "Dance with shadows: stubs, patch and mock",
                        "duration": 30,
                        "abstract": "To ensure quality, automated testing is a must. But sometimes is impossible or very expensive to use real environments. In this case, you can isolate some parts of a system and use fake simulated objects.",
                        "day": "2022-07-13",
                        "time": 875,
                        "endTime": 905,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 2"
                        ],
                        "slug": "dance-with-shadows-stubs-patch-and-mock",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "CLQCZS",
                                "name": "María Andrea Vignau",
                                "biography": "I gave many talks in spanish and two in english. I come from Argentina and gave five talks on PyCon Argentina, gave a talk in Europython https://youtu.be/s7110IaMEOs, a charla at PyCon Charlas 2019, and this year in PyCon España and other for Basis Technology on extending forensic software using python (https://youtu.be/ocuFZ8RA1p8). I was also organizer in 9 events in my city, Resistencia Chaco, collaborator in many others, including mentoring at PyCon Charlas 2022.",
                                "avatar": "https://program.europython.eu/media/avatars/me_-_saco_btsKqZy.jpg",
                                "slug": "maria-andrea-vignau",
                                "affiliation": "Shiphero LLC",
                                "homepage": "https://mavignau.gitlab.io/",
                                "twitter": "mavignau"
                            }
                        ],
                        "start": "2022-07-13T14:35:00+01:00",
                        "end": "2022-07-13T15:05:00+01:00"
                    },
                    {
                        "id": "BL9NGV",
                        "title": "Protocols - Static duck typing for decoupled code",
                        "duration": 30,
                        "abstract": "Python introduces Protocols to support static duck typing, where static type checkers (mypy) and other tools can verify code correctness prior to runtime.\r\n\r\nThis was added in order to circumvent explicitly inheriting from ABCs (Abstract base classes) which is \"unpythonic and unlike what one would normally do in idiomatic dynamically typed Python code\" - according to PEP 544.\r\n\r\nWe will explore the different use cases for Protocols and how to use them correctly.",
                        "day": "2022-07-13",
                        "time": 875,
                        "endTime": 905,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey B"
                        ],
                        "slug": "protocols-static-duck-typing-for-decoupled-code",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "V7BWTA",
                                "name": "Ran Zvi",
                                "biography": "I'm a software engineer currently living in USA. I enjoy learning new languages and learning about them.",
                                "avatar": "https://program.europython.eu/media/avatars/image1_eD11cms.jpeg",
                                "slug": "ran-zvi",
                                "affiliation": "BlueVine",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-13T14:35:00+01:00",
                        "end": "2022-07-13T15:05:00+01:00"
                    },
                    {
                        "id": "DZZ8X9",
                        "title": "Classifying LEGO Bricks with Machine Learning",
                        "duration": 30,
                        "abstract": "There are over 70 000 different Lego bricks and they appear in almost 200 different colors. Even the most hardcore AFOLs (Adult Fan of Lego) don’t know all of them. Let alone be able to recognize them. So I got curious whether it’s possible to create an application that can recognize the particular brick using only its photo.",
                        "day": "2022-07-13",
                        "time": 875,
                        "endTime": 905,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 1"
                        ],
                        "slug": "classifying-lego-bricks-with-machine-learning",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "8DK3QT",
                                "name": "Piotr Rybak",
                                "biography": "Piotr Rybak is a Machine Learning Researcher with experience in industry and academia. In his work, he mainly focuses on Natural Language Understanding but once in a while, he likes to dive into other topics. In his free time, he's a big fan of board games, Lego bricks, and boulder climbing.",
                                "avatar": "https://program.europython.eu/media/avatars/photo_saoAk1U.jpg",
                                "slug": "piotr-rybak",
                                "affiliation": "Wrocław University of Science and Technology",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-13T14:35:00+01:00",
                        "end": "2022-07-13T15:05:00+01:00"
                    },
                    {
                        "id": "P3EYQE",
                        "title": "Event-driven microservices with Python and Apache Kafka",
                        "duration": 30,
                        "abstract": "Implementing complex systems with microservices can be a great decision, but if we’re not careful we can end up with a distributed monolith. Let’s see how to avoid that by building lightweight, loosely coupled microservices using Python, Flask, and Apache Kafka.",
                        "day": "2022-07-13",
                        "time": 875,
                        "endTime": 905,
                        "audience": "intermediate",
                        "rooms": [
                            "Wicklow Hall 1"
                        ],
                        "slug": "event-driven-microservices-with-python-and-apache-kafka",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "FHJBQF",
                                "name": "Dave Klein",
                                "biography": "After 28 years as a developer, architect, project manager (recovered), author, trainer, conference organizer, and homeschooling dad, Dave Klein landed his dream job as a developer advocate at Confluent. Dave is marveling in and eager to help others explore the amazing world of event streaming with Apache Kafka.",
                                "avatar": "https://program.europython.eu/media/avatars/daveklein_ogDny9Q.jpg",
                                "slug": "dave-klein",
                                "affiliation": "Confluent",
                                "homepage": "developer.confluent.io",
                                "twitter": "@daveklein"
                            }
                        ],
                        "start": "2022-07-13T14:35:00+01:00",
                        "end": "2022-07-13T15:05:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 905,
                "title": "Coffee Break",
                "duration": 25,
                "type": "break"
            },
            {
                "time": 930,
                "duration": 30,
                "sessions": [
                    {
                        "id": "E73V8G",
                        "title": "Automate the Boring Stuff with Slackbot(ver.2)",
                        "duration": 30,
                        "abstract": "Today, there are many tasks to repeat in the company/community.\r\nIn addition, we often use chat such as Slack for daily communication.\r\nSo, I created a chatbot([PyCon JP Bot](https://github.com/pyconjp/pyconjpbot)) to automate various boring tasks related to holding PyCon JP.\r\n\r\nIn this talk, I will first explain how to create a chatbot using [Bolt for Python](https://slack.dev/bolt-python/concepts).\r\nI will tell you how to registers bot's integration on Slack and how to create a simple bot in Python that responds to specific keywords.",
                        "day": "2022-07-13",
                        "time": 930,
                        "endTime": 960,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey B"
                        ],
                        "slug": "automate-the-boring-stuff-with-slackbot-ver-2",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "3TLEGG",
                                "name": "Takanori Suzuki",
                                "biography": "Takanori([@takanory](https://twitter.com/takanory)) is a Vice Chairperson of [PyCon JP Association](https://www.pycon.jp/).\r\nHe is also a Director of [BeProud Inc.](https://www.beproud.jp/careers/en/), and his title is \"Python Climber\".\r\nTakanori held PyCon JP 2014 to 2016 as the Chairperson.\r\nCurrently he teaches Python to beginners as a lecturer at [Python Boot Camp](https://pycamp.pycon.jp/) all over Japan.\r\nIn addition, he published several [Python books](https://www.amazon.co.jp/%E9%88%B4%E6%9C%A8%E3%81%9F%E3%81%8B%E3%81%AE%E3%82%8A/e/B00W95A036/).\r\nTananori plays trumpet, climbs boulder, loves Lego, ferrets and beer.",
                                "avatar": "https://program.europython.eu/media/avatars/sokidan1002x1002_QLUmEpL.jpg",
                                "slug": "takanori-suzuki",
                                "affiliation": "PyCon JP Association",
                                "homepage": None,
                                "twitter": "takanory"
                            }
                        ],
                        "start": "2022-07-13T15:30:00+01:00",
                        "end": "2022-07-13T16:00:00+01:00"
                    },
                    {
                        "id": "NZJDKC",
                        "title": "My journey using Docker as a development tool",
                        "duration": 30,
                        "abstract": "I have been programming in Python for 5 years and almost from day one I've been using Docker with Python. Docker is now a widely used tool across the industry, due to its flexibility. It can be used as a tool to help deploy your code in production, say using Kubernetes. It can also be used as a tool to help develop code locally, with tools such as docker-compose.\r\n\r\nIt has taken me some time to discover various features and best practices when using Docker. Especially when it comes to using it for local development.\r\n\r\nIn this talk, I would like to go over a journey I have taken with Docker whilst working with it over several years. Starting from a single build step with a full-fat image, going over multi-stage Docker images. Showing you how you can use the same Dockerfile for development and production.",
                        "day": "2022-07-13",
                        "time": 930,
                        "endTime": 960,
                        "audience": "intermediate",
                        "rooms": [
                            "Wicklow Hall 1"
                        ],
                        "slug": "my-journey-using-docker-as-a-development-tool",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "HLJHD3",
                                "name": "Haseeb Majid",
                                "biography": "I am software engineer with around 5 years of professional experience. I am currently working for ZOE, a start-up in the healthcare space. Most of my experience is writing backend web services, using Python. I also extensive experience with Docker, Git and Linux.",
                                "avatar": "https://program.europython.eu/media/avatars/photo_5337101068850544252_y_1_iRZhyzu.jpg",
                                "slug": "haseeb-majid",
                                "affiliation": "ZOE",
                                "homepage": "http://haseebmajid.dev",
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-13T15:30:00+01:00",
                        "end": "2022-07-13T16:00:00+01:00"
                    },
                    {
                        "id": "TF9Z8Q",
                        "title": "HPy: a better C API for Python",
                        "duration": 30,
                        "abstract": "The official Python C API is specific to the current implementation of CPython. It has served us well and forms the basis upon which our entire extension ecosystem rests. \r\nHowever, it exposes a lot of internal details which makes it hard to implement it for other Python implementations (e.g. PyPy, GraalPython, Jython, IronPython, etc.), and \r\nprevents major evolutions of CPython itself, such as using a GC instead of refcounting, or removing the GIL.\r\n\r\nThis is where HPy comes in. It's a new C API designed from the ground up according to the following goals:\r\n* running much faster on alternate implementations, and at native speed on CPython\r\n* making it possible to compile a single binary which runs unmodified on all supported Python implementations and versions\r\n* being simpler and more manageable than the Python/C API\r\n* providing an improved debugging experience.\r\n\r\nWe'll discuss its current status and show how existing extensions can be gradually ported to it.",
                        "day": "2022-07-13",
                        "time": 930,
                        "endTime": 960,
                        "audience": "advanced",
                        "rooms": [
                            "Liffey A"
                        ],
                        "slug": "hpy-a-better-c-api-for-python",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "T8FUFL",
                                "name": "Ronan Lamy",
                                "biography": "I'm a freelance software developer and open-source consultant. I'm a cofounder of HPy and I've been a PyPy core developer since 2012.",
                                "avatar": "https://www.gravatar.com/avatar/a8f4ba9cf0d41e36ee03ae2c487b170c",
                                "slug": "ronan-lamy",
                                "affiliation": "Self-employed",
                                "homepage": None,
                                "twitter": "@ronanlamy"
                            }
                        ],
                        "start": "2022-07-13T15:30:00+01:00",
                        "end": "2022-07-13T16:00:00+01:00"
                    },
                    {
                        "id": "VFEVKR",
                        "title": "Making AI Happen at Your Company",
                        "duration": 30,
                        "abstract": "All one needs is strategy, skill and resources to make digitalization and AI happen. So why is everything taking so long? Shouldn’t you all be finished yesterday already? An honest talk about how to address the complexity of making AI happen in enterprises.",
                        "day": "2022-07-13",
                        "time": 930,
                        "endTime": 960,
                        "audience": "beginner",
                        "rooms": [
                            "Liffey Hall 1"
                        ],
                        "slug": "making-ai-happen-at-your-company",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "8F38DV",
                                "name": "Alexander CS Hendorf",
                                "biography": None,
                                "avatar": "https://program.europython.eu/media/avatars/hendorf-2020_square_1LJOKAe.jpg",
                                "slug": "alexander-cs-hendorf",
                                "affiliation": None,
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-13T15:30:00+01:00",
                        "end": "2022-07-13T16:00:00+01:00"
                    },
                    {
                        "id": "ZK7MVG",
                        "title": "Property-based testing the Python way",
                        "duration": 30,
                        "abstract": "What if I told you you could write simpler tests but still get better results ? \r\n\r\nWhat if I told you can automatically generate your test data ?\r\n\r\nThis may sound difficult to your traditional testing approach but can be easily done with property-based testing. \r\n\r\nProperty-based testing allows a range of inputs to be tested on a given aspect of a software property, abstracting away the details.\r\n\r\nIn the world of Python you can accomplish this with Hypothesis, the Python library used for property-based testing. \r\n\r\nHypothesis helps you design cleaner and clever test suites.",
                        "day": "2022-07-13",
                        "time": 930,
                        "endTime": 960,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 2"
                        ],
                        "slug": "property-based-testing-the-python-way",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "TEJVNB",
                                "name": "Emma Saroyan",
                                "biography": "Emma is a developer advocate at Alpaca. She enjoys sharing her knowledge and learning from fellow developers.",
                                "avatar": "https://program.europython.eu/media/avatars/photo_bU7CgTE.jpg",
                                "slug": "emma-saroyan",
                                "affiliation": "Alpaca markets",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-13T15:30:00+01:00",
                        "end": "2022-07-13T16:00:00+01:00"
                    },
                    {
                        "id": "ZV9Y8M",
                        "title": "What happens when you import a module?",
                        "duration": 30,
                        "abstract": "It's a rare program that doesn't include at least one \"import\" statement. But what actually happens when we import a module? How does Python find our file, decide whether to load it, and then keep track of it in memory? In this talk, I'll walk you through what happens when you \"import\" a module into Python, revealing the complexities of something seemingly simple that we use every day.",
                        "day": "2022-07-13",
                        "time": 930,
                        "endTime": 960,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "what-happens-when-you-import-a-module",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "VZM8L3",
                                "name": "Reuven M. Lerner",
                                "biography": "Reuven is a full-time trainer in Python and data science, teaching companies around the world via in-person, online, and recorded courses. He is the author of both \"Python Workout\" and \"Pandas Workout,\" published by Manning, and writes the free, weekly \"Better developers\" newsletter read by more than 25,000 developers around the world. He lives with his wife and children in Modi'in, Israel.",
                                "avatar": "https://program.europython.eu/media/avatars/reuven-headshot_eNVHHfd.jpg",
                                "slug": "reuven-m-lerner",
                                "affiliation": "Lerner Consulting",
                                "homepage": "https://lerner.co.il/",
                                "twitter": "reuvenmlerner"
                            }
                        ],
                        "start": "2022-07-13T15:30:00+01:00",
                        "end": "2022-07-13T16:00:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 965,
                "duration": 45,
                "sessions": [
                    {
                        "id": "39YWUH",
                        "title": "Working with Audio in Python (feat. Pedalboard)",
                        "duration": 30,
                        "abstract": "Come _hear_ about how to play with audio in only a couple lines of Python!\r\n\r\nPython can do (nearly) anything, but using Python to work with audio has always been a complicated and messy affair. In this talk, we'll be going through how digital audio works, how Python can be used to play with audio data, and how a new library - Pedalboard - can help. Pedalboard is a simple, fast, and performant library for doing common audio tasks in Python, including applying effects, using VSTs and audio plugins, and encoding/decoding various audio formats.",
                        "day": "2022-07-13",
                        "time": 965,
                        "endTime": 995,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey B"
                        ],
                        "slug": "working-with-audio-in-python-feat-pedalboard",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "XSUHP3",
                                "name": "Peter Sobot",
                                "biography": "Peter is a Staff Machine Learning Engineer at Spotify in New York, where he helps lead their Audio Intelligence Lab - an ML research lab dedicated to pushing the state of the art in audio-based machine learning. He hails from Canada (and so spells colour the _correct_ way) and when not hacking on audio software, he plays drums and bass in a handful of bands.",
                                "avatar": "https://program.europython.eu/media/avatars/2020-09-08-straightened_agoHJCQ.png",
                                "slug": "peter-sobot",
                                "affiliation": "Spotify",
                                "homepage": "https://petersobot.com",
                                "twitter": "psobot"
                            }
                        ],
                        "start": "2022-07-13T16:05:00+01:00",
                        "end": "2022-07-13T16:35:00+01:00"
                    },
                    {
                        "id": "98XE8Q",
                        "title": "When to refactor your code into generators and how",
                        "duration": 30,
                        "abstract": "Have you ever found yourself coding variations of a loop construct where fragments of the loop code were exactly the same between the variations? Or, in an attempt to factor out these common parts, you ended up with a loop construct containing a lot of conditional code for varying start, stop, or selection criteria?\r\n\r\nYou might have felt that the end result just didn't look right. Because of the duplicated parts in your code, you noticed that the code didn't conform to the DRY (_Don't Repeat Yourself_) principle. Or, after an attempt to combine the variations into a single loop, with consequently a lot of conditional code, your inner voice told you that the resulting code had become too complex and difficult to maintain.\r\n\r\nThis talk will show you a way out of this situation. It demonstrates how you can create a **generator function** that implements only the common parts of your loop construct. Subsequently you will learn how you can combine this generator function with distinct hand-crafted functions or building blocks from the standard library `itertools` module or the `more-itertools` package.\r\n\r\nAs an example, imagine you'd need to implement some varying functionality based on the Fibonacci sequence. This talk shows you how it would look like before and after you've refactored it into a **pipeline of generators**.\r\n\r\nAfter having seen this pattern, you will recognize more quickly when this kind of refactoring helps you to create more maintainable and more Pythonic code.",
                        "day": "2022-07-13",
                        "time": 965,
                        "endTime": 995,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey A"
                        ],
                        "slug": "when-to-refactor-your-code-into-generators-and-how",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "MDZNRX",
                                "name": "Jan-Hein Bührman",
                                "biography": "Jan-Hein is a software engineer who witnessed Python’s first baby steps up very close, and loves programming in Python since then. While he worked in different software development roles, he always kept an eye on its development. After he has founded a dedicated Python software unit within Ordina, the company he works for, he’s now back at the work that leaves him with a positive energy balance at the end of the day: programming in Python!",
                                "avatar": "https://program.europython.eu/media/avatars/Jan-Hein_helderder_aClbtTP.jpg",
                                "slug": "jan-hein-buhrman",
                                "affiliation": "Ordina Pythoneers",
                                "homepage": "https://www.ordina.nl/vakgebieden/python/",
                                "twitter": "@janheinb"
                            }
                        ],
                        "start": "2022-07-13T16:05:00+01:00",
                        "end": "2022-07-13T16:35:00+01:00"
                    },
                    {
                        "id": "CQ7NBC",
                        "title": "Building a Just-in-Time Python FaaS Platform with Unikraft",
                        "duration": 30,
                        "abstract": "Function-as-a-Service (FaaS) platforms are one of the key service offerings for any cloud provider. To provide strong isolation, the functions are run inside heavy-weight virtual machines (and within containers inside those for orchestration reasons). Consequently, such instances take too long to boot and so are kept on all the time, even though the functions only receive requests intermittently. The end result is that current FaaS platforms are much less efficient than they could be.\r\n\r\nWe will introduce a radically novel way to build FaaS platforms based on Python and the Unikraft Linux Foundation open source project (www.unikraft.org). Unikraft is a toolkit for building fully specialized, cloud-ready virtual machines called unikernels targeting a single application . Using Unikraft we can construct extremely specialized, Python-based unikernels that use only a few MBs to run a boot in 10s of milliseconds, allowing us to bring VMs up as a request to a function comes in, and to shut it down (or suspend it) afterwards. The result: a Python-based FaaS platform that is significantly more efficient and cheaper to operate than existing offerings.\r\n\r\nIn the talk we will provide an introduction to Unikraft, how Python is built on top of it, a full description of the FaaS platform and a short demo.",
                        "day": "2022-07-13",
                        "time": 965,
                        "endTime": 995,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 1"
                        ],
                        "slug": "building-a-just-in-time-python-faas-platform-with-unikraft",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "GXDRHH",
                                "name": "Felipe Huici",
                                "biography": "Dr. Felipe Huici is CEO and Co-Founder at Unikraft UG, a start-up dedicated to lightweight and open source virtualization technologies and significantly lowering cloud infrastructure bills. In addition, Felipe is a chief researcher at NEC Laboratories Europe in Heidelberg, Germany where his main research and interests lie in the areas of high-performance software systems, and in particular specialization, virtualization and security. He has been published in several top-tier conferences and journals such as SOSP, ASPLOS, OSDI, Eurosys, SIGCOMM, NSDI, CoNEXT, and SIGCOMM CCR. Finally, Felipe is one of the founders and maintainers of the Linux Foundation Unikraft open source project.",
                                "avatar": "https://program.europython.eu/media/avatars/felipehuici_ixalJ4j.jpeg",
                                "slug": "felipe-huici",
                                "affiliation": "Unikraft UG and NEC Laboratories Europe GmbH",
                                "homepage": "https://unikraft.io/",
                                "twitter": None
                            },
                            {
                                "code": "RRE9DV",
                                "name": "Alexander Jung",
                                "biography": "Alexander Jung is a Co-Founder and Chief Product Officer at the Lightweight Virtualization company Unikraft, focusing on leading unikernels into market and mass deployment.  He is also a PhD student at Lancaster University, where he focuses primarily on optimizations of unikernels for network-bound operations; delivering effective continuous integration and deployment of VNF-based services; as well as compile-time methods for inter-VM communication based on library Operating Systems.  Previously he has worked as the Chief Information Officer at UK-based startup Adjacent Systems, securing and delivering systems for local law-enforcement and government.",
                                "avatar": "https://program.europython.eu/media/avatars/Photo-on-12.08.21-at-15.36_shop_copy_a4H0crA.jpg",
                                "slug": "alexander-jung",
                                "affiliation": "Unikraft",
                                "homepage": None,
                                "twitter": "@nderjung"
                            }
                        ],
                        "start": "2022-07-13T16:05:00+01:00",
                        "end": "2022-07-13T16:35:00+01:00"
                    },
                    {
                        "id": "HJWZ37",
                        "title": "How much time does it take to write tests? A case study",
                        "duration": 30,
                        "abstract": "Writing automated tests takes time. As developers, we are constantly pressed by management to deliver early, which means we are tempted to skip writing some of the tests. Of course, in the long term, the time needed to write tests is paid off.\r\n\r\nBut how much of our time do we spend in order to write tests? Is it half? Is it three-quarters? This can be difficult to measure, particularly if we are using test-driven development, because in that case writing tests is integrated in the process of writing code.\r\n\r\nWhile I like test-driven development, I can only practice it when I have a good idea of what code I want to write. But sometimes my idea of how to approach the problem at hand is quite vague and I experiment a lot. In these cases, I write the code first and the tests after that. \r\n\r\nIn one such case I first finished the functionality I was developing and proclaimed it \"beta\". I then went on to write the unit tests for it. As a result, I have a clear idea how much time I spent writing documentation and main code, and how much I spent writing tests. In this talk I examine the implications of all this.",
                        "day": "2022-07-13",
                        "time": 965,
                        "endTime": 995,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 2"
                        ],
                        "slug": "how-much-time-does-it-take-to-write-tests-a-case-study",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "QRKRQL",
                                "name": "Antonis Christofides",
                                "biography": "I've been writing software for more than 30 years. I’ve written software to streamline the management of hydro/meteorological measurements; to make time series visualization and processing easy; to provide irrigation advice; and much more. I have been working with automatic meteorological stations since 1992; I’ve occasionally written programs to interface directly with meteorological loggers; I’ve dug out dusty old handwritten weather observations and keyed them in myself; I have created various web sites and web-accessible databases; I’ve administrated servers, including email and network, and high-availability databases with automatic failover. I have written the book on Django deployment (https://djangodeployment.com).\r\n\r\nIn research, I’ve worked on water-related decision making when there are conflicting objectives; on evaluation of climate models; on causation and determinism in hydrology and the climate; and more. My opinion on climate change is that there is no evidence that it is man-made.\r\n\r\nI help scientists and engineers create software. In particular, I help them bring their models to the web.",
                                "avatar": "https://www.gravatar.com/avatar/39d2ea0a36d1740e5f544076955a4b30",
                                "slug": "antonis-christofides",
                                "affiliation": "IRMASYS P.C.",
                                "homepage": "https://antonischristofides.com",
                                "twitter": "@a_christofides"
                            }
                        ],
                        "start": "2022-07-13T16:05:00+01:00",
                        "end": "2022-07-13T16:35:00+01:00"
                    },
                    {
                        "id": "HWMZZG",
                        "title": "Music and Code",
                        "duration": 45,
                        "abstract": "A playful exploration of the similarities and differences between music and code. What could coders learn from musicians, especially when it comes to learning, training and mentoring? (A personal perspective from someone who has been a professional musician, a professional teacher, and a professional coder.)",
                        "day": "2022-07-13",
                        "time": 965,
                        "endTime": 1010,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "music-and-code",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "WADEN9",
                                "name": "Nicholas H.Tollervey",
                                "biography": "A recovering former member of the Python community.\r\n\r\nMusic, philosophy, teaching, writing & computing. Just like this bio: concise, honest and full of useful information. Everything I say is false...",
                                "avatar": "https://www.gravatar.com/avatar/e8d4e155929363bd22a7852494d18c25",
                                "slug": "nicholas-h-tollervey",
                                "affiliation": "Freelancer",
                                "homepage": "https://ntoll.org/",
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-13T16:05:00+01:00",
                        "end": "2022-07-13T16:50:00+01:00"
                    },
                    {
                        "id": "VAGHFS",
                        "title": "Using Python to  manage Software Bill of Materials",
                        "duration": 30,
                        "abstract": "Software has become increasingly complex as it is constructed from a multitude of software components. In many cases the identification of these components are hidden as they are included through implicit dependencies. Without fully understanding the dependencies of your product it is not possible to understand the current vulnerability status of your software product or system.\r\nIn the past 12 months, there has been an increasing focus on the use Software Bill of Materials (SBOMs) as a key artefact to be delivered with a software product; it will be mandated for all software products in some markets later in 2022. SBOMs which were initially developed to capture the inter-dependencies between components (the focus was on capturing the different types of open source licences used within a product) but with the latest evolution, tracking of vulnerabilities within a product can now be performed.\r\n\r\nThis talk will introduce the SBOM concept and show how Python and its ecosystem can be used to create, manage and use SBOMs as part of your development pipeline.",
                        "day": "2022-07-13",
                        "time": 965,
                        "endTime": 995,
                        "audience": "beginner",
                        "rooms": [
                            "Wicklow Hall 1"
                        ],
                        "slug": "using-python-to-manage-software-bill-of-materials",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "JGAHYH",
                                "name": "Anthony Harrison",
                                "biography": "An experienced solution architect and cyber security consultant delivering and securing mission critical systems. In his spare time, teaches Python at Manchester CoderDojo and has acts as a mentor for Google Summer of Code (GSOC) projects supported by the Python Software Foundation.",
                                "avatar": None,
                                "slug": "anthony-harrison",
                                "affiliation": "Independent",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-13T16:05:00+01:00",
                        "end": "2022-07-13T16:35:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 1015,
                "duration": 45,
                "sessions": [
                    {
                        "id": "GN9FNF",
                        "title": "Dodging AI Dystopia: you can't save the world alone",
                        "duration": 45,
                        "abstract": "If real life was a superhero movie, we’d have all the ingredients needed for a hero’s rescue. So many “AI” algorithms are being applied to EU education, employment, and public safety systems that you might wonder if the TV series “Black Mirror” is fiction or a blueprint for nefarious actors. Luckily, there are codes to keep dystopia at bay, whether from the fictional Justice League or from real-life courts of justice. This talk discusses both, and is aimed at software engineers, architects, designers, testers and product/project managers who want to slow the Automation of Everything, but don’t know how.",
                        "day": "2022-07-13",
                        "time": 1015,
                        "endTime": 1060,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "dodging-ai-dystopia-you-can-t-save-the-world-alone",
                        "type": "keynote",
                        "speakers": [
                            {
                                "code": "DRUEEZ",
                                "name": "Dr. Nakeema Stefflbauer",
                                "biography": "Dr. Nakeema Stefflbauer is a digital product executive with expertise in early-stage ideation, test, and development. Her digital transformation iexperience s paired with a focus on algorithmic explainability, equity, and fairness. Dr. Stefflbauer is the founder and CEO of FrauenLoop in Berlin and, both privately and as part of the Atomico angel programme, she advises and invests in startups building innovative, sustainable tech solutions.\r\n\r\n\r\n  Dr. Stefflbauer holds MA and PhD degrees from [Harvard University](https://gsas.harvard.edu/), a BA from [Brown University](https://www.brown.edu/), and an executive MBA from the disruptive [Quantic School of Business and Technology](https://quantic.edu/). Her accomplishments includes delivery of software in the context of eLearning, enterprise resource planning (ERP), eCommerce, fintech and insurtech in the United States, Canada, and Germany.",
                                "avatar": None,
                                "slug": "dr-nakeema-stefflbauer",
                                "affiliation": "FrauenLoop",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-13T16:55:00+01:00",
                        "end": "2022-07-13T17:40:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 1065,
                "duration": 45,
                "sessions": [
                    {
                        "id": "CPYWPM",
                        "title": "Lightning Talks",
                        "duration": 45,
                        "abstract": "A lightning talk (LT) is a short presentation that must not be longer than five minutes.\r\n\r\nTo sign up for a lightning talk, you can put your name on the information board during the conference before the second coffee break. For our online participants, we will set up a separate form or Google sheet for you to put your name and topic in - similar to how we run this at the in-person conference. \r\n\r\nWe will announce the same every day both online and in person.",
                        "day": "2022-07-13",
                        "time": 1065,
                        "endTime": 1110,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "lightning-talks",
                        "type": "lightning-talks",
                        "speakers": [],
                        "start": "2022-07-13T17:45:00+01:00",
                        "end": "2022-07-13T18:30:00+01:00"
                    }
                ],
                "type": "timeslot"
            }
        ],
        "rooms": [
            "The Auditorium",
            "Wicklow Hall 1",
            "Liffey A",
            "Liffey B",
            "Liffey Hall 1",
            "Liffey Hall 2",
            "Forum"
        ]
    },
    "dayType": "Talks"
}

d2 = {
    "schedule": {
        "slots": [
            {
                "time": 540,
                "duration": 15,
                "sessions": [
                    {
                        "id": "KJAB7A",
                        "title": "Morning Announcement",
                        "duration": 15,
                        "abstract": "Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement",
                        "day": "2022-07-14",
                        "time": 540,
                        "endTime": 555,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "morning-announcement",
                        "type": "opening-session",
                        "speakers": [],
                        "start": "2022-07-14T09:00:00+01:00",
                        "end": "2022-07-14T09:15:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 555,
                "duration": 45,
                "sessions": [
                    {
                        "id": "X9URCX",
                        "title": "Killer Robots Considered Harmful",
                        "duration": 45,
                        "abstract": "Killer robots may sound like something from a movie, but in recent years weapons have been developed that can select targets and attack without any human input, and expert systems have been used to assist in military targeting.\r\n\r\nSome argue that this is a positive development, because automation can increase precision in targeting and reduce civilian casualties. However, others point out that highly automated systems do not have a good track record in complex and high-stakes real world situations, and military conflict is unlikely to be better.\r\n\r\nThis talk will outline the technological underpinnings of autonomous weapons and automated targeting systems, as well as examining the legal and ethical debate over these systems that has been happening at the UN over the past decade.",
                        "day": "2022-07-14",
                        "time": 555,
                        "endTime": 600,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "killer-robots-considered-harmful",
                        "type": "keynote",
                        "speakers": [
                            {
                                "code": "VFFGTH",
                                "name": "Laura Nolan",
                                "biography": "Affiliation: Campaign to Stop Killer Robots\r\n\r\nLaura Nolan is a software engineer who focuses on software operations and reliability. She holds degrees in Computer Science and in Ethics, and is currently completing another MA in Strategic Studies. Since 2018, Laura has been part of the Campaign to Stop Killer Robots, an umbrella organisation of NGOs that works towards a legally-binding instrument to regulate autonomous weapons.",
                                "avatar": None,
                                "slug": "laura-nolan",
                                "affiliation": "Campaign to Stop Killer Robots",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-14T09:15:00+01:00",
                        "end": "2022-07-14T10:00:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 600,
                "title": "Coffee Break",
                "duration": 30,
                "type": "break"
            },
            {
                "time": 630,
                "duration": 45,
                "sessions": [
                    {
                        "id": "BVRBYQ",
                        "title": "Predicting urban heat islands in Calgary",
                        "duration": 45,
                        "abstract": "This talk explains how geospatial Python libraries can help us understand and predict Land Surface Temperature in urban areas using historical openly available satellite images and urban morphological data. This makes data science a powerful tool to plan and design urban areas while reducing the impact of urban warming.",
                        "day": "2022-07-14",
                        "time": 630,
                        "endTime": 675,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 2"
                        ],
                        "slug": "predicting-urban-heat-islands-in-calgary",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "7CNVPN",
                                "name": "Anand S",
                                "biography": "Anand is a co-founder of Gramener, a data science company. He leads a team that automates insights from data and narrates these as visual data stories. He is recognized as one of India's top 10 data scientists, and is a regular TEDx speaker.\r\n\r\nAnand is a gold medalist at IIM Bangalore and an alumnus of IIT Madras, London Business School, IBM, Infosys, Lehman Brothers, and BCG.\r\n\r\nMore importantly, he has hand-transcribed every Calvin & Hobbes strip ever and dreams of watching every film on the IMDb Top 250.\r\n\r\nHe blogs at https://s-anand.net. His talks are at https://bit.ly/anandtalks",
                                "avatar": "https://www.gravatar.com/avatar/d6a854b850c70c0ee5f9511d845b613e",
                                "slug": "anand-s",
                                "affiliation": "Gramener",
                                "homepage": "https://s-anand.net/",
                                "twitter": "@sanand0"
                            }
                        ],
                        "start": "2022-07-14T10:30:00+01:00",
                        "end": "2022-07-14T11:15:00+01:00"
                    },
                    {
                        "id": "C9LDHB",
                        "title": "Developers Documentation: your secret weapon",
                        "duration": 45,
                        "abstract": "You can have the best product in your expertise area, but if your documentation isn’t on par with the flawless experience you want to offer to the world, success is not guaranteed. Let’s be real here: documentation is often an afterthought and rarely included in life cycle development processes. Still, documentation is the secret weapon for greater adoption, and growth that you may have not known you could achieve.\r\n\r\nIt’s time for you to step up your game and measure up to the big players. Learn about the benefits of high quality and educational documentation and the true role it plays in the developer community. You’ll also learn the principles of a solid foundation, and tips on how to use one of the most powerful developer relations’ tools.",
                        "day": "2022-07-14",
                        "time": 630,
                        "endTime": 675,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey B"
                        ],
                        "slug": "developers-documentation-your-secret-weapon",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "7RBHLZ",
                                "name": "Frédéric Harper",
                                "biography": "As the Director of Developer Relations at Mindee, Frédéric Harper helps developers merge the physical and digital worlds using the magic of machine learning coupled with the ease of APIs. Fred has shared his passion for technology on the stage at dozens of events around the world. He’s helped build successful communities at npm, Mozilla, Microsoft, DigitalOcean, and Fitbit, and is the author of the book Personal Branding for Developers at Apress. Behind this extrovert is a very passionate individual who believes in the power of communication... and cat videos.",
                                "avatar": "https://program.europython.eu/media/avatars/fred_z1RngGv.png",
                                "slug": "frederic-harper",
                                "affiliation": "Mindee",
                                "homepage": "http://mindee.com",
                                "twitter": "@fharper"
                            }
                        ],
                        "start": "2022-07-14T10:30:00+01:00",
                        "end": "2022-07-14T11:15:00+01:00"
                    },
                    {
                        "id": "F9FURV",
                        "title": "PyArrow and the future of data analytics",
                        "duration": 45,
                        "abstract": "In this talk we will introduce PyArrow and talk bout the transformation that the Arrow format is allowing in the Data Analytics world.\r\n\r\nPyArrow provides an in-memory format, a disk format, a network exchange protocol, a dataframe library and a query engine all integrated in a single library. But the Arrow ecosystem doesn't stop there and allows you to work integrating multiple different technologies. It can be a swiss army knife for data engineers and it integrates zero cost with NumPy and Pandas in many cases.",
                        "day": "2022-07-14",
                        "time": 630,
                        "endTime": 675,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 1"
                        ],
                        "slug": "pyarrow-and-the-future-of-data-analytics",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "AQNTYV",
                                "name": "Alessandro Molina",
                                "biography": "Relying on Python as his primary development language for more than 15 years, has always been interested in Python as a Development Platform.\r\n\r\nHe worked as CTO and team leader of Python teams for the past 10 years and is currently core developer of the [TurboGears2](http://turbogears.org) web framework and a contributor to the [Apache Arrow](https://arrow.apache.org/) project.\r\n\r\nAlessandro is the author of [Crafting Test-Driven Software with Python](http://www.pythontdd.com) and [Modern Python Standard Library Cookbook](https://www.pythonstandardlibrarybook.com/)\r\nand has authored many OpenSource Python projects like the [DEPOT](https://depot.readthedocs.io/en/latest/) file storage framework and the [DukPy](https://github.com/amol-/dukpy#dukpy) JavaScript interpreter for Python.\r\n\r\nAlessandro has been an [active speaker](https://pyvideo.org/speaker/alessandro-molina.html) to tens of European conferences since 2012",
                                "avatar": "https://www.gravatar.com/avatar/7d9269c9eb62ef4691264f019796fbd0",
                                "slug": "alessandro-molina",
                                "affiliation": "VoltronData",
                                "homepage": "https://voltrondata.com/",
                                "twitter": "@__amol__"
                            }
                        ],
                        "start": "2022-07-14T10:30:00+01:00",
                        "end": "2022-07-14T11:15:00+01:00"
                    },
                    {
                        "id": "VUTSHW",
                        "title": "Walk-through of Django internals",
                        "duration": 45,
                        "abstract": "⭐ The talk will cover the Django codebase internals and showcase various moving parts in the code.\r\n\r\n⭐ Talk will cover the internals of CGI, WSGI, working on runserver, views, Middleware, app loading, Django settings load, ORM, Django utilities, etc.",
                        "day": "2022-07-14",
                        "time": 630,
                        "endTime": 675,
                        "audience": "intermediate",
                        "rooms": [
                            "Wicklow Hall 1"
                        ],
                        "slug": "walk-through-of-django-internals",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "RUX9LK",
                                "name": "Hitul Mistry",
                                "biography": "[Hitul](https://www.linkedin.com/in/hitulmistry/) is the founder of [Digiqt Technolabs](https://digiqt.com). He helps companies in building Technology products, DevOps and Data Engineering. \r\n\r\nHe is experienced in the development of large-scale enterprise mission-critical and fault tolerance distributed applications in e-commerce, insurance, finance, and health care domains.",
                                "avatar": "https://program.europython.eu/media/avatars/1563792480043_ppImby8.jpeg",
                                "slug": "hitul-mistry",
                                "affiliation": "Digiqt Technolabs",
                                "homepage": "digiqt.com",
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-14T10:30:00+01:00",
                        "end": "2022-07-14T11:15:00+01:00"
                    },
                    {
                        "id": "WX9PBG",
                        "title": "Writing Faster Python 3",
                        "duration": 45,
                        "abstract": "Did you know that Python preallocates integers from -5 to 257? Reusing them 1000 times, instead of allocating memory for a bigger integer, can save you a couple milliseconds of code’s execution time. If you want to learn more about this kind of optimizations then, … well, probably this presentation is not for you :) Instead of going into such small details, I will talk about more “sane” ideas for writing faster code.\r\n\r\nAfter a brief overview of different levels of optimization and how they work in Python, I will show you simple and fast ways of measuring the execution time of your code and finally, discuss examples of how some code structures could be improved.\r\n\r\nYou will see:\r\n\r\n* The fastest way of removing duplicates from a list\r\n* How much faster your code is when you reuse the built-in functions instead of trying to reinvent the wheel\r\n* What is faster than the “for loop”\r\n* If the lookup is faster in a list or a set\r\n* When it’s better to beg for forgiveness than to ask for permission",
                        "day": "2022-07-14",
                        "time": 630,
                        "endTime": 675,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "writing-faster-python-3",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "8D7B98",
                                "name": "Sebastian Witowski",
                                "biography": "Sebastian is a Python consultant and online course creator based in Poland. He started his journey with programming as a software developer at CERN, where he fell in love with Python (and teaching). Now he is helping companies untangle their complicated architecture and build all sorts of interesting Python projects.\r\n\r\nIn his spare time, he talks about Python, best practices in programming, and productivity.",
                                "avatar": "https://program.europython.eu/media/avatars/2019-07-29_profesjonalny_fotograf_small_YUM1emC.jpg",
                                "slug": "sebastian-witowski",
                                "affiliation": "Sebastian Witowski",
                                "homepage": "https://switowski.com/",
                                "twitter": "@SebaWitowski"
                            }
                        ],
                        "start": "2022-07-14T10:30:00+01:00",
                        "end": "2022-07-14T11:15:00+01:00"
                    },
                    {
                        "id": "YBQYF3",
                        "title": "Forget Mono vs. Multi-Repo - Building Centralized Git Workflows with Python",
                        "duration": 30,
                        "abstract": "The mono vs. multi-repo is an age-old debate in the DevOpsphere, and one that can still cause flame wars.  What if I were to tell you that you don't have to choose?\r\nIn this talk we will dive into how we built a centralized Git workflow that can work with any kind of repo architecture, delivered with Python.\r\n\r\nOne of the greatest recurring pains in CI/CD is the need to reinvent the wheel and define your CI workflow for each and every repository or (micro)service, when eventually 99% of the config is the same.  What if we could hard reset this paradigm and create a single, unified workflow that is shared by all of our repos and microservices?  In this talk, we will showcase how a simple solution implemented in Python, demoed on Github as the SCM, and Github Actions for our CI, enabled us to unify this process for all of our services, and improve our CI/CD velocity by orders of magnitude.",
                        "day": "2022-07-14",
                        "time": 630,
                        "endTime": 660,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey A"
                        ],
                        "slug": "forget-mono-vs-multi-repo-building-centralized-git-workflows-with-python",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "TUCBCX",
                                "name": "Daniel Koch",
                                "biography": "VP Engineering of Jit, the Continuous Security platform for Developers. Daniel is an experienced VP Engineering, manager and tech lead with many years of industry experience at startups and global enterprise companies. Passionate about developing innovative products and leading engineering teams to deliver quality products. Skilled in architecting SaaS solutions, building high-performing teams, software security, design and development. A true cloud and automation enthusiast.",
                                "avatar": "https://program.europython.eu/media/avatars/photo_2_zzo3iwW.jpg",
                                "slug": "daniel-koch",
                                "affiliation": "Jit",
                                "homepage": "https://jit.io",
                                "twitter": "@danokoch"
                            },
                            {
                                "code": "J8TMQE",
                                "name": "",
                                "biography": None,
                                "avatar": None,
                                "slug": "",
                                "affiliation": None,
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-14T10:30:00+01:00",
                        "end": "2022-07-14T11:00:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 680,
                "duration": 30,
                "sessions": [
                    {
                        "id": "F9M9BR",
                        "title": "Maps with Django",
                        "duration": 30,
                        "abstract": "Keeping in mind the **Pythonic** principle that _“simple is better than complex”_ we'll see how to create a web **map** with the **Python** based _web framework_ **Django** using its **GeoDjango** module, storing _geographic data_ in your _local database_ on which to run _geospatial queries_.",
                        "day": "2022-07-14",
                        "time": 680,
                        "endTime": 710,
                        "audience": "intermediate",
                        "rooms": [
                            "Wicklow Hall 1"
                        ],
                        "slug": "maps-with-django",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "BGLPFA",
                                "name": "Paolo Melchiorre",
                                "biography": "I’m Paolo Melchiorre, a longtime Python backend developer who contributes to the Django project and gives talks at tech conferences.\r\n\r\nI’ve been a GNU/Linux user for over 20 years and I use and promote Free Software.\r\n\r\nI graduated in Software Engineering and I’m an alumnus of the University of Bologna, Italy.\r\n\r\nI’ve been working in the web for 15 years and now I’m the CTO of 20tab, a pythonic software company, for which I work remotely.",
                                "avatar": "https://program.europython.eu/media/avatars/1-IMG_20170423_153741-192x192_Q5gms7I.jpg",
                                "slug": "paolo-melchiorre",
                                "affiliation": "20tab",
                                "homepage": "https://www.paulox.net/",
                                "twitter": "@pauloxnet"
                            }
                        ],
                        "start": "2022-07-14T11:20:00+01:00",
                        "end": "2022-07-14T11:50:00+01:00"
                    },
                    {
                        "id": "HAKFFR",
                        "title": "How we are making Python 3.11 faster",
                        "duration": 30,
                        "abstract": "Python 3.11 is between 10% and 60% faster than Python 3.10, depending on the application. \r\nWe have achieved this in a fully portable way by making the interpreter adapt to the \r\nprogram being run, and by streamlining key data structures.\r\n\r\nIn this talk I will explain what changes we have made, and how they improve performance.",
                        "day": "2022-07-14",
                        "time": 680,
                        "endTime": 710,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "how-we-are-making-python-3-11-faster",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "LUY39H",
                                "name": "Mark Shannon",
                                "biography": "I've been using Python since 2005.\r\nI have an extensive background in compilers, virtual machines and static analysis for dynamic languages, specifically Python.\r\nAfter a long interlude working on static analysis tools, I have returned to performance work over the last couple of years.\r\n\r\nI am currently working as technical lead with the \"Faster CPython\" team funded by Microsoft.",
                                "avatar": "https://program.europython.eu/media/avatars/IMG_20191130_122850_3mkOJrs.jpg",
                                "slug": "mark-shannon",
                                "affiliation": "HotPy Ltd",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-14T11:20:00+01:00",
                        "end": "2022-07-14T11:50:00+01:00"
                    },
                    {
                        "id": "JBHNRE",
                        "title": "Creating the Next Generation of Billionaires - Part 4",
                        "duration": 30,
                        "abstract": "Our generation of young people in school (aged 5-18) have noticed the connection between Computer pRogramming, Technology, Bitcoinism Success, Climate Change and Billionaires.\r\n\r\nOn mass young people are clamouring to master the skill of Computer pRogramming. It has been dubbed the ‘4th’ R’ (computer pRogramming) along with Reading, wRiting and aRithmetic. So, governments worldwide have launched initiatives to have it taught in schools from Kindergarten to all the way to high school. And now young people are successfully mastering this skill.\r\n\r\nThis talk will describe a case study whereby Computer Programming (Python) was introduced for the first time to a group of young people and how the young people are using it to explore and understand real world problems and data such as those relating to climate change, world population growth and carbon dioxide emissions with Python visualisation libraries such as Matplotlib, Numpy and Pandas. We will talk about the joys and challenges and discoveries made by the young people. We will conclude with suggestions on how to proceed in this area.",
                        "day": "2022-07-14",
                        "time": 680,
                        "endTime": 710,
                        "audience": "beginner",
                        "rooms": [
                            "Liffey B"
                        ],
                        "slug": "creating-the-next-generation-of-billionaires-part-4",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "8QTNH7",
                                "name": "Lilian",
                                "biography": "Lilian studied Computer Science at high school and did her PhD in Computer Modelling. She went on to looking at computer applications and programming in the pharmaceutical sector before entering formal teaching for the next generation. She is currently engaged in teaching Python programming, C# and Javascript. She has given lectures in conferences both in the UK and abroad about the teaching of Computer Programming to young people. She has ran computer clubs including that of 'computer-assisted' investment for children and is a full member of the British Computer Society.\r\n\r\nLilian firmly believes that in this emergent brave new world, the Anthrpocene age, the computer (with its associated technologies) is the harbinger to transform globally man's short slavish existence to a better one - a world community defined by longer, richer and freer life experiences. She believes it is imperative that our schools empower our young children with his new knowledge, and Lilian herself did help reshape the Computer Science Department of an independent boys' school as Head of Department. She has produced for children more than 75 YouTube (online) videos on Computer Science and Programming - and has had more than 12,000 hits globally.",
                                "avatar": None,
                                "slug": "lilian",
                                "affiliation": "Oxford Education Online",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-14T11:20:00+01:00",
                        "end": "2022-07-14T11:50:00+01:00"
                    },
                    {
                        "id": "KPW7X7",
                        "title": "A Tale of two Kitchens, hyper modernizing your codebase.",
                        "duration": 30,
                        "abstract": "When starting a new python project, the “hypermodern” python ‘template’ is a popular choice. Its style is opinionated and strict, and it brings a consistent style and today's best practices. How do I bring my legacy codebase up to this standard?",
                        "day": "2022-07-14",
                        "time": 680,
                        "endTime": 710,
                        "audience": "beginner",
                        "rooms": [
                            "Liffey A"
                        ],
                        "slug": "a-tale-of-two-kitchens-hyper-modernizing-your-codebase",
                        "type": "sponsored-talk",
                        "speakers": [
                            {
                                "code": "LQ93ZB",
                                "name": "Christian Ledermann",
                                "biography": "I have been working in the Software industry for over 25ish years in 4 Countries - 🇩🇪, 🇰🇪, 🇬🇧, and 🇮🇪 - and ended up as Senior Software Engineer at Oomnitza in Galway, Ireland. The first time I saw a Python Prompt it displayed the version Number 1.5.2 🦖, professionally I used python since 2003, (Python 2.2)",
                                "avatar": "https://program.europython.eu/media/avatars/cleder_pZuh7c0.png",
                                "slug": "christian-ledermann",
                                "affiliation": "Oomnitza",
                                "homepage": "https://www.oomnitza.com/",
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-14T11:20:00+01:00",
                        "end": "2022-07-14T11:50:00+01:00"
                    },
                    {
                        "id": "ULWUP3",
                        "title": "Scaling scikit-learn: introducing new sets of computational routines",
                        "duration": 30,
                        "abstract": "For more than 10 years, scikit-learn has been bringing machine learning and data science methods to the world. Since then, the library always aimed to deliver quality implementations, focusing on a clear and accessible code-base built on top of the PyData ecosystem.\r\n\r\nThis talk aims at explaining the recent on-going work of the scikit-learn developers to boost the native performances of the library.",
                        "day": "2022-07-14",
                        "time": 680,
                        "endTime": 710,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 2"
                        ],
                        "slug": "scaling-scikit-learn-introducing-new-sets-of-computational-routines",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "P8VJPK",
                                "name": "Julien Jerphanion",
                                "biography": "I am mainly interested in computational, algorithmic and mathematical methods. I first started to contribute to open-source in 2017 and since then my contributions focused on scientific software.\r\n\r\nSince April 2021, I work at Inria as a Research Software Engineer, mainly on improving performances of scikit-learn. I became one of scikit-learn maintainers in October 2021.",
                                "avatar": "https://program.europython.eu/media/avatars/me_l3L07Kv.jpg",
                                "slug": "julien-jerphanion",
                                "affiliation": "Inria",
                                "homepage": "https://jjerphan.xyz/",
                                "twitter": "@jjerphan"
                            }
                        ],
                        "start": "2022-07-14T11:20:00+01:00",
                        "end": "2022-07-14T11:50:00+01:00"
                    },
                    {
                        "id": "XUCMH3",
                        "title": "A Network Embeddings based Recommendation Model with multi-factor consideration",
                        "duration": 30,
                        "abstract": "Recommendation systems are increasingly in demand to provide a personalized customer experience for diversified product mix offerings. Traditionally we use interaction information based on user preferences and item characteristics. This brings in collaborative filtering-driven recommendations with higher accuracy and relevance. However, such a method has certain limitations in utilizing implicit information like cross-domain specific factors that are equally important for making personalized recommendations. We propose an improvised way of using network embeddings based matrix factorization technique with multi-factors to make a match between both implicit and explicit features resulting in more accurate recommendation.",
                        "day": "2022-07-14",
                        "time": 680,
                        "endTime": 710,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 1"
                        ],
                        "slug": "a-network-embeddings-based-recommendation-model-with-multi-factor-consideration",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "JFZNJ9",
                                "name": "ABHISHEK",
                                "biography": "Abhishek is a leading Innovation Specialist and a distinguished digital transformation leader who has worked across diversified domains retail, finance, logistics and enterprise technology. He has 13+ years of strong global business transformation experience in applied data science practice with a key focus on Artificial Intelligence, Machine Learning and NLP across various sectors. Currently working at Microsoft and delivered impactful outcomes by playing pivotal role in setting up AI CoEs while working for Maersk, Visa, Fidelity Investments and Dell. His active research interest reciprocated by 6 patents (US/ Denmark), 3 trade secrets and 5 international publications in top-peer reviews journals and conferences. He holds Master’s in industrial management & Engineering from Indian Institute of Technology Kanpur with specialization in Machine Learning & Natural Language Processing.",
                                "avatar": "https://program.europython.eu/media/avatars/Abhishek_Photo_JnBJ1x1.jpg",
                                "slug": "abhishek",
                                "affiliation": "Microsoft",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-14T11:20:00+01:00",
                        "end": "2022-07-14T11:50:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 715,
                "duration": 45,
                "sessions": [
                    {
                        "id": "8YX9RG",
                        "title": "Use animated charts to present & share your findings with ipyvizzu",
                        "duration": 45,
                        "abstract": "Sharing and explaining the results of your analysis can be a lot easier and more fun when you can create an animated story of the charts containing your insights. [ipyvizzu](https://github.com/vizzuhq/ipyvizzu) - a new open-source charting tool for Jupyter & Databricks notebooks and similar platforms, enables just that with a simple Python interface. In this talk, the creator of ipyvizzu shows how their technology works and provides examples of the advantages of using animation for storytelling with data.",
                        "day": "2022-07-14",
                        "time": 715,
                        "endTime": 760,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 2"
                        ],
                        "slug": "use-animated-charts-to-present-share-your-findings-with-ipyvizzu",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "Q7VFPN",
                                "name": "Peter Vidos",
                                "biography": "Peter is the CEO & Co-Founder of [Vizzu](https://vizzuhq.com). \r\n\r\nHis primary focus is understanding how Vizzu's innovative approach to data visualization can be put to good use. Listening to people complaining about their current hurdles with building charts and presenting them is his main obsession, next to figuring out how to help data professionals utilize the power of animation in dataviz.\r\n\r\nPeter has been involved with digital product development for over 15 years. Earlier products/projects he worked on cover mobile app testing, online analytics, data visualization, decision support, e-learning, educational administration & social. Still, building a selfie teleport just for fun is what he likes to boast about when asked about previous experiences.",
                                "avatar": "https://program.europython.eu/media/avatars/Peter_Vidos_headshot3_Ak67UYJ.jpg",
                                "slug": "peter-vidos",
                                "affiliation": "Vizzu",
                                "homepage": "http://vizzuhq.com",
                                "twitter": "@petervidos"
                            }
                        ],
                        "start": "2022-07-14T11:55:00+01:00",
                        "end": "2022-07-14T12:40:00+01:00"
                    },
                    {
                        "id": "FBRMPN",
                        "title": "Sponsor Recruitment Session",
                        "duration": 30,
                        "abstract": "Many of our sponsors are looking to hire talented people and EuroPython is the perfect place to reach out to them!\r\n\r\nIn this session, our sponsors will each give a short presentation about their company and what they do with Python. You can then approach them directly at their booth to discuss more details.",
                        "day": "2022-07-14",
                        "time": 715,
                        "endTime": 745,
                        "audience": "beginner",
                        "rooms": [
                            "Liffey A"
                        ],
                        "slug": "sponsor-recruitment-session",
                        "type": "talk",
                        "speakers": [],
                        "start": "2022-07-14T11:55:00+01:00",
                        "end": "2022-07-14T12:25:00+01:00"
                    },
                    {
                        "id": "H79EHW",
                        "title": "Online voting system used for primary elections for the French Presidential, must be secure right ?",
                        "duration": 45,
                        "abstract": "Since it inception, online voting has been an apealing but controversial technology.\r\n\r\nIndeed, what seems like a modern way of making vote cheaper and more convenient is often considered by activist and reserchers as a pandora box unleashing never-ending privacy and authenticity concerns.\r\n\r\nHowever with Covid 19 shriking our public interaction, many have considered the benefits overcome the theorical issues and online voting system have skyrocketed like never before...\r\n\r\nThe Neovote voting system has been massively used in France: tenths of Universty, hundreds of private companies and, more importantly, it was chosen to organise\r\n3 of the 5 main primary elections for the French Presidential election of 2022 (Primaires de l'Écologie, Les Républicains and Primaire Populaire).\r\n\r\nNeovote claims to have the highest possible level of security, the voter being even able to access the final ballot box to do the recount by himself and ensure his own vote has been taken into account !\r\n\r\nSo challenge accepted, this talk will walk you through the Neovote voting system to understand why their claims are \"slightly\" exagerated ;-)",
                        "day": "2022-07-14",
                        "time": 715,
                        "endTime": 760,
                        "audience": "beginner",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "online-voting-system-used-for-primary-elections-for-the-french-presidential-must-be-secure-right",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "9BBUPC",
                                "name": "Emmanuel Leblond",
                                "biography": "Coming from the C/C++ embedded software world, I ended up starting a software company specialized in end-to-end encryption solution.\r\n\r\nI fall in love with Python a long time ago, fortunately programing can be polyamorous because I've met Rust in the meantime ;-)",
                                "avatar": "https://www.gravatar.com/avatar/969c58822a3243c5b51e61eaa4745807",
                                "slug": "emmanuel-leblond",
                                "affiliation": "Scille SAS",
                                "homepage": "https://scille.eu",
                                "twitter": "@touilleMan"
                            }
                        ],
                        "start": "2022-07-14T11:55:00+01:00",
                        "end": "2022-07-14T12:40:00+01:00"
                    },
                    {
                        "id": "MZS3MM",
                        "title": "EModelRunner: a Python package to run online available biological neuron model implementations",
                        "duration": 45,
                        "abstract": "The Blue Brain Project hosts several online portals from which users can download single neuron model implementations. These contain the information necessary to simulate the electrical behavior of a neuron. EModelRunner is a Python library that provides a unified interface to the users to run these downloaded models. It gives the users the ability to customize the properties of the neurons, apply various stimuli in order to observe the corresponding behavior, or activate the synapses that are present on the morphology of the neuron. This way neuroscientists can investigate the neurons in a self-contained environment and conduct digital experiments on them.",
                        "day": "2022-07-14",
                        "time": 715,
                        "endTime": 760,
                        "audience": "",
                        "rooms": [
                            "Forum"
                        ],
                        "slug": "emodelrunner-a-python-package-to-run-online-available-biological-neuron-model-implementations",
                        "type": "poster",
                        "speakers": [
                            {
                                "code": "HYZCUT",
                                "name": "Anıl Tuncel",
                                "biography": "I am a Software Engineer with working experience in multidisciplinary scientific fields such as simulation neuroscience and genomics.\r\n\r\nAt the Blue Brain Project, we are building biologically detailed digital reconstructions and simulations of the mouse brain. We are running supercomputer-based simulations for understanding the multi-level structure and function of the brain.\r\n\r\nBefore joining Blue Brain Project, I was employed by ETH Zurich to work on Roche Tumour Profiler Project. I designed data analysis pipelines and statistical methods to provide personalised treatments for cancer patients.\r\n\r\nI volunteer as a Contributing Member at the Python Software Foundation. My contributions relate to the creation or maintenance of open-source software available to the public at no charge.\r\n\r\nhttps://wiki.python.org/psf/AnilTuncel",
                                "avatar": "https://program.europython.eu/media/avatars/Goldwyn_Shooting_ETH_KP_2019_0628_tT9k0YP.jpg",
                                "slug": "anil-tuncel",
                                "affiliation": "Blue Brain Project",
                                "homepage": "https://www.epfl.ch/research/domains/bluebrain/blue-brain/people/our-people/simulation-neuroscience-division/anil-tuncel/",
                                "twitter": "@anilbey"
                            }
                        ],
                        "start": "2022-07-14T11:55:00+01:00",
                        "end": "2022-07-14T12:55:00+01:00"
                    },
                    {
                        "id": "S8XSTF",
                        "title": "ShapePipe: A modular weak-lensing processing and analysis pipeline",
                        "duration": 45,
                        "abstract": "I will the present the first public release of [ShapePipe](https://cosmostat.github.io/shapepipe/), an open-source and modular weak-lensing measurement, analysis and validation pipeline written in Python. I will begin by giving an (easy-to-follow) introduction on how and why we measure the shapes of galaxies to map the distribution of dark matter in the Universe. I will then describe the design of the software, mentioning the numerous Python packages we used, and justify the choices we made. I will conclude by discussing some of the lessons we learned along the way and how these can be applied to other scientific software development projects.",
                        "day": "2022-07-14",
                        "time": 715,
                        "endTime": 760,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 1"
                        ],
                        "slug": "shapepipe-a-modular-weak-lensing-processing-and-analysis-pipeline",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "VFV3HW",
                                "name": "Samuel FARRENS",
                                "biography": "I am a researcher at the CosmoStat lab in CEA Paris-Saclay. I work on developing software for cosmology and collaborate with a team working on biomedical imaging. You can find out more about what I do on [my website](https://sfarrens.github.io/).",
                                "avatar": "https://program.europython.eu/media/avatars/office_wave_reoyMY9.jpeg",
                                "slug": "samuel-farrens",
                                "affiliation": "CEA Paris-Saclay",
                                "homepage": "https://sfarrens.github.io/",
                                "twitter": "@Sam_Farrens"
                            }
                        ],
                        "start": "2022-07-14T11:55:00+01:00",
                        "end": "2022-07-14T12:40:00+01:00"
                    },
                    {
                        "id": "WWRGSS",
                        "title": "Async Django",
                        "duration": 45,
                        "abstract": "Python has a full set of tools for asynchronous programming - multiprocessing, multithreading, coroutines, etc. And Django uses most of them.\r\n\r\nSince Django 3, we have the ability to create fully async non-blocking Django views that could handle thousands of requests concurrently.\r\n\r\nIn this talk, we'll focus on 2 key topics:\r\n1. The motivation and the decisions behind the Django async support\r\n2. Choosing the right tools to make our views async and efficient",
                        "day": "2022-07-14",
                        "time": 715,
                        "endTime": 760,
                        "audience": "intermediate",
                        "rooms": [
                            "Wicklow Hall 1"
                        ],
                        "slug": "async-django",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "7HPWPW",
                                "name": "Ivaylo Donchev",
                                "biography": "Currently working as Technical team lead in HackSoft in Bulgaria.\r\n\r\nA programmer for ~7 years, working with Python and DJango for 6 years.\r\n\r\nSpeaker at EuroPython 2018 and PyCon Balkan 2018.",
                                "avatar": "https://program.europython.eu/media/avatars/personal_KPiB7nc.jpg",
                                "slug": "ivaylo-donchev",
                                "affiliation": "HackSoft",
                                "homepage": "https://github.com/Ivo-Donchev",
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-14T11:55:00+01:00",
                        "end": "2022-07-14T12:40:00+01:00"
                    },
                    {
                        "id": "XSRUNF",
                        "title": "Revolutionizing Education: How Python is Essential Beyond Computer Science",
                        "duration": 30,
                        "abstract": "Python has had a transformational effect on countless fields so far, but its permeation can be accelerated through the integration of Python into non-computing coursework. Currently, Python’s presence within secondary and post-secondary schools varies greatly between different institutions, but the continuity in the lack of interdisciplinary coursework is a key limiting factor in the widespread growth of computing education. This is due to a variety of factors, including stereotypes and policy issues, but the bottom line is that Python being restricted to only computing classes restricts career opportunities and misrepresents the professional world. With support from a case-study of college-level physics students exposed to scientific programming, we propose novel methods of integrating Python into traditional coursework during this talk. The overarching mission of this discussion is to demonstrate how Python literacy in non-computing coursework can ultimately help in streamlining processes and accelerating progress in various industries. Attendees will have the opportunity to hear about the exciting prospect of expanding Python beyond the confines of computer science, and will have an exclusive look at a case-study that offers insight into student benefits of integrated coursework: as concerned stakeholders, it is ultimately well-informed Python community members who must unite to make a positive impact on the education system.",
                        "day": "2022-07-14",
                        "time": 715,
                        "endTime": 745,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey B"
                        ],
                        "slug": "revolutionizing-education-how-python-is-essential-beyond-computer-science",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "9WBNHR",
                                "name": "Srivatsa Kundurthy",
                                "biography": "Srivatsa Kundurthy is a student based in the Greater New York City Area. As a Python practitioner, his projects include Open Source Intelligence tools for extracting public data and Python notebooks for explaining and simulating chaotic dynamical systems. His work in machine learning includes studying computer vision for problems in ecology and researching neural networks for predicting states of chaotic dynamical systems. Additionally, he is working with the LAION Research Group to develop and strengthen the world’s largest image-text dataset. Apart from Machine Learning Research, Srivatsa is greatly interested in technology policy and community-related issues, particularly those extending to the accessibility of programming education. On the side, Srivatsa enjoys science communication and stargazing.",
                                "avatar": "https://program.europython.eu/media/avatars/IMG-1848-Original-Original_qSILF51.jpg",
                                "slug": "srivatsa-kundurthy",
                                "affiliation": "The Academy for Mathematics, Science, and Engineering",
                                "homepage": None,
                                "twitter": "@srkundurthy"
                            }
                        ],
                        "start": "2022-07-14T11:55:00+01:00",
                        "end": "2022-07-14T12:25:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 780,
                "title": "Lunch Break",
                "duration": 60,
                "type": "break"
            },
            {
                "time": 840,
                "duration": 30,
                "sessions": [
                    {
                        "id": "3U9T9S",
                        "title": "Self-explaining APIs",
                        "duration": 60,
                        "abstract": "To mash up various APIs, data need to have a well defined meaning: imagine meshing up healthcare APIs using different units for human temperature, or financial APIs using different currencies.\r\n\r\nThis talk describes strategies and python tools to overcome these problems in large API ecosystems such as data exchanges between different countries.",
                        "day": "2022-07-14",
                        "time": 840,
                        "endTime": 900,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey A"
                        ],
                        "slug": "self-explaining-apis",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "VST3SV",
                                "name": "Roberto Polli",
                                "biography": "Roberto joined in the [Italian Digital Transformation Department](https://innovazione.gov.it/it/progetti/api/) - to create a national API Ecosystem based on internet standards.\r\n\r\nHe's a Red Hat Certified Engineer and MySQL/MongoDB certified DBA, but loves maintaining free software.\r\n\r\nA life ago he took a Math degree, and he's really proud of it.",
                                "avatar": "https://www.gravatar.com/avatar/c6c5e33601dc00f6dc863f768e8e5687",
                                "slug": "roberto-polli",
                                "affiliation": "Digital Transformation Department, Italian Government",
                                "homepage": None,
                                "twitter": "@ioggstream"
                            }
                        ],
                        "start": "2022-07-14T14:00:00+01:00",
                        "end": "2022-07-14T15:00:00+01:00"
                    },
                    {
                        "id": "8JSS8X",
                        "title": "Lessons learnt from building my own library",
                        "duration": 30,
                        "abstract": "One of the many strengths of python is PyPI, which complements and enhances the \"batteries included\" approach of the standard library. Building a library, and publishing it to PyPI has a number of challenges, pitfalls, and choices that someone has to make. In this talk, I would share my journey from v0.1.0 to v1.0.0 and all the moments that I said: \"I wish I knew this thing before\".",
                        "day": "2022-07-14",
                        "time": 840,
                        "endTime": 870,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey B"
                        ],
                        "slug": "lessons-learnt-from-building-my-own-library",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "FDHNUF",
                                "name": "Stephanos",
                                "biography": "Before becoming a software engineer, Stephanos used to be a number theorist, working on Arithmetic Geometry and Diophantine Equations. During his research, he realised his passion for coding and decided to pursue a career in it.\r\n\r\nHe is currently working as a Software Engineer at Piper, handling the infrastructure, the databases and the backend of the company.",
                                "avatar": "https://program.europython.eu/media/avatars/avatar_real_Sb142ar.jpeg",
                                "slug": "stephanos",
                                "affiliation": "Piper",
                                "homepage": "https://www.piperhq.co",
                                "twitter": "spapanik21"
                            }
                        ],
                        "start": "2022-07-14T14:00:00+01:00",
                        "end": "2022-07-14T14:30:00+01:00"
                    },
                    {
                        "id": "BLHK9U",
                        "title": "When gRPC met Python",
                        "duration": 30,
                        "abstract": "What if we can have a tool that helps us to do intelligent load balancing or What if we can do selective compression of the data and extremely fast and light weight transfer of data? Then let me introduce gRPC, the technology that helps us to do all of this and how can we integrate gRPC with Python.",
                        "day": "2022-07-14",
                        "time": 840,
                        "endTime": 870,
                        "audience": "intermediate",
                        "rooms": [
                            "Wicklow Hall 1"
                        ],
                        "slug": "when-grpc-met-python",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "WHQUTW",
                                "name": "Sanket Singh",
                                "biography": "Sanket Singh is an avid and passionate Software Engineer at Google. He has worked with organizations like LinkedIn and Harvard - Berkman Klein Centre in the past. He is curious to build products that can solve simple and complex problems but in a graceful way. \r\nSanket has always been a forefront runner for writing high-quality code. But he also understands that it is a gradual process and thus it is important to always look back every few months and refractor the code whenever possible so that it's easier to debug in case of any issues. \r\nHe has taken multiple workshops in the past to promote the same and encouraged many engineers to not neglect the power of well refactored code. \r\nHe has taught more than 15000 budding engineers and wants to create a community of people with impactful skills. He runs a YouTube channel with a 25k+ subscriber base where he shares unpopular opinions and his tech journey experiences. \r\nIn his free time, he likes to play chess and mentor budding engineers in the industry.",
                                "avatar": "https://program.europython.eu/media/avatars/9579-200o200o2-NhELdkcqcQAigZMCd47Efx_gFsCRU8.jpeg",
                                "slug": "sanket-singh",
                                "affiliation": "Google",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-14T14:00:00+01:00",
                        "end": "2022-07-14T14:30:00+01:00"
                    },
                    {
                        "id": "CFRUXG",
                        "title": "Synergize AI and Domain Expertise - Explainability Check with Python",
                        "duration": 30,
                        "abstract": "The talk focuses on establishing guidelines for Explainable AI by diving into fundamental concepts and checkpoints, before accepting AI models to make decisions. We go through explainers, types, and algorithms with a simple implementation in Python, to strengthen our understanding of \"WHY?\" the model predicts a certain value and \"HOW?\" to validate it with experiential learning of experts to bridge potential gaps",
                        "day": "2022-07-14",
                        "time": 840,
                        "endTime": 870,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 1"
                        ],
                        "slug": "synergize-ai-and-domain-expertise-explainability-check-with-python",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "CCZUDR",
                                "name": "Pranjal Biyani",
                                "biography": "Pranjal is an experienced AI Scientist building the first AI powered platform to accelerate R&D for Material Sciences across the globe. He loves opening black-box models to reveal insightful AI secrets that help decision makers adapt with the ever changing Industry needs. He also loves to teach and mentor passionate individuals aspiring to be a part of the Data Science Community, all with his favourite language, Python!",
                                "avatar": None,
                                "slug": "pranjal-biyani",
                                "affiliation": "Polymerize, Singapore",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-14T14:00:00+01:00",
                        "end": "2022-07-14T14:30:00+01:00"
                    },
                    {
                        "id": "HN3NNP",
                        "title": "Real-time browser-ready computer vision apps with Streamlit",
                        "duration": 30,
                        "abstract": "By using Streamlit and streamlit-webrtc, we can create web-based real-time computer vision apps only with ~10 or 20 additional lines of Python code.\r\n\r\nTo turn computer vision models into real-time demos, we have conventionally used OpenCV modules such as `cv2.VideoCapture` and `cv2.imshow()`. However, such apps are difficult or impossible to share with friends, run on smartphones, or integrate with modern interactive widgets and other data views and inputs.\r\n\r\nWeb-based apps don't have such problems.\r\n\r\nStreamlit provides an easy way to build web apps quickly, and `streamlit-webrtc` allows to use real-time video streams.\r\nYou can create real-time video apps with modern interactive views and inputs, and host these apps on the cloud to use from any devices with browsers.\r\n\r\nIn this talk, I will demonstrate the development process using these libraries and show a variety of examples so that we see how easy and useful they are and can make use of them in daily development and research.`streamlit-webrtc` extends Streamlit to be capable of dealing with real-time video and audio streams.\r\nWith a combination of these libraries, developers can rapidly create real-time computer vision and audio processing apps for which OpenCV has typically been used.",
                        "day": "2022-07-14",
                        "time": 840,
                        "endTime": 870,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 2"
                        ],
                        "slug": "real-time-browser-ready-computer-vision-apps-with-streamlit",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "FLSGCD",
                                "name": "Yuichiro Tachibana",
                                "biography": "Yuichiro works as a professional software developer and also loves contributing to OSS projects.\r\nAs a Pythonista, he has participated in various projects including web development, multimedia streaming, data management, computer vision, and machine learning.",
                                "avatar": "https://program.europython.eu/media/avatars/pk2649_trimmed1_800_rgd5YPt.jpg",
                                "slug": "yuichiro-tachibana",
                                "affiliation": "Freelancer",
                                "homepage": "https://www.whitphx.info/",
                                "twitter": "@whitphx"
                            }
                        ],
                        "start": "2022-07-14T14:00:00+01:00",
                        "end": "2022-07-14T14:30:00+01:00"
                    },
                    {
                        "id": "P3EV3C",
                        "title": "Diversity & Inclusion in the Python Community Panel",
                        "duration": 60,
                        "abstract": "Come meet some of the folks working on Diversity and Inclusion in the global Python Community!\r\nJoin the live panel discussion to hear about the challenges and the work they do.\r\n\r\nWith Marlene Mhangami, Nabanita Roy, Iqbal Abdullah. Chaired by Naomi Ceder.",
                        "day": "2022-07-14",
                        "time": 840,
                        "endTime": 900,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "diversity-inclusion-in-the-python-community-panel",
                        "type": "panel",
                        "speakers": [
                            {
                                "code": "NMACLQ",
                                "name": "Tereza Iofciu",
                                "biography": "Tereza Iofciu is an experienced data practitioner, having worked as a data science manager, data scientist, data engineer, and product manager. She is leading a coaching team and teaching data science and neuefische in Hamburg. She is a co-organizer of the PyLadies Hamburg group, hosting regular meetups with the community. She is also a PSF Code of Conduct and Diversity & Inclusion working groups member and has been awarded the Python Software Foundation 2021 Q1 community service award. Recently she has joined the DISC Steering Committee team.",
                                "avatar": "https://program.europython.eu/media/avatars/IMG_1246_mOIzBWp.jpg",
                                "slug": "tereza-iofciu",
                                "affiliation": "neuefische",
                                "homepage": "https://terezaif.github.io",
                                "twitter": "@terezaif"
                            },
                            {
                                "code": "7NWTAL",
                                "name": "Marlene Mhangami",
                                "biography": "Marlene is a Zimbabwean software engineer, explorer, and speaker based in the city of Harare. She is an advocate for using science and technology for social good and increasing diversity in these fields. She is a director and vice-chair for the Python Software Foundation and is currently working as a Developer Advocate at Voltron Data. In 2017, she co-founded ZimboPy, a non-profit organization that gives Zimbabwean young women access to resources in the field of technology. She is also the previous chair of PyCon Africa and is an advocate for women in tech on the continent.",
                                "avatar": "https://program.europython.eu/media/avatars/Screenshot_2022-06-13_at_10.23.18_b4fqgxG.png",
                                "slug": "marlene-mhangami",
                                "affiliation": "Voltron Data",
                                "homepage": "marlenemhangami.com",
                                "twitter": "@marlene_zw"
                            },
                            {
                                "code": "SM8RTE",
                                "name": "Naomi Ceder",
                                "biography": "Founder of Trans*Code. An elected fellow of the Python Software Foundation, Naomi is a past chair of its board of directors. She also speaks internationally about the Python community, and on inclusion and diversity in technology in general.",
                                "avatar": None,
                                "slug": "naomi-ceder",
                                "affiliation": "Trans*Code",
                                "homepage": None,
                                "twitter": None
                            },
                            {
                                "code": "QXW3WL",
                                "name": "Nabanita Roy",
                                "biography": "Data Scientist @ ACI Worldwide | Education Lead @ Women in AI Ireland | Tech-Blogger @ Medium | ❤ NLP",
                                "avatar": "https://program.europython.eu/media/avatars/1608393249873_I8mfcX7.jpg",
                                "slug": "nabanita-roy",
                                "affiliation": "ACI Worldwide",
                                "homepage": "https://medium.com/@nroy0110",
                                "twitter": None
                            },
                            {
                                "code": "ZE89HA",
                                "name": "Iqbal Abdullah",
                                "biography": "Iqbal is the CEO of [LaLoka Labs](https://lalokalabs.co/en/) and has been a Python user since 1.5.2\r\n\r\nHe is a Malaysian based in Japan and have been actively participating as a speaker as well as an organizer within the Python communities around the East Asia and South East Asia region.\r\n\r\nHe was the PyCon chairperson for PyCon APAC 2017, PyCon MY 2015 and also founded PyCon JP in 2013. He is currently active within the PSF Trademarks WG and also the PSF Diversity and Inclusion WG.\r\n\r\nYou can read his writing and thoughts about Python and the community in his [blog](https://thefortunate.blog/category/python-and-pycons.html). Feel free to connect with Iqbal on [LinkedIn](https://www.linkedin.com/in/iqbalabd/) or on [Twitter](https://twitter.com/iqbalabd)",
                                "avatar": "https://program.europython.eu/media/avatars/iqbal-sm-portrait-01-ai_52KZHYB.png",
                                "slug": "iqbal-abdullah",
                                "affiliation": "LaLoka Labs LLC",
                                "homepage": "https://lalokalabs.co/en/",
                                "twitter": "@iqbalabd"
                            }
                        ],
                        "start": "2022-07-14T14:00:00+01:00",
                        "end": "2022-07-14T15:00:00+01:00"
                    },
                    {
                        "id": "RMLCKR",
                        "title": "A Personal Brand? Surprise, you already have one!",
                        "duration": 60,
                        "abstract": "Why should you care about your personal brand? After all, it’s not like you are an actor or the lead singer for a rock band. In fact, it’s never been more important for you to think about yourself as a brand. Doing so will provide rocket fuel for your career. You’ll find better jobs and become a  “thought leader” in your industry. You’ll become known for your expertise and leadership; people will seek your advice and point of view. As a developer, there are many tools you can use to build a personal brand, and this presentation will help you learn how to get visibility, make a real impact, and achieve your goals. You don’t need to be a marketing expert or a personal branding guru— you can be yourself and get your dream job or reach the next level of your career.",
                        "day": "2022-07-14",
                        "time": 840,
                        "endTime": 900,
                        "audience": "",
                        "rooms": [
                            "Forum"
                        ],
                        "slug": "a-personal-brand-surprise-you-already-have-one",
                        "type": "poster",
                        "speakers": [
                            {
                                "code": "7RBHLZ",
                                "name": "Frédéric Harper",
                                "biography": "As the Director of Developer Relations at Mindee, Frédéric Harper helps developers merge the physical and digital worlds using the magic of machine learning coupled with the ease of APIs. Fred has shared his passion for technology on the stage at dozens of events around the world. He’s helped build successful communities at npm, Mozilla, Microsoft, DigitalOcean, and Fitbit, and is the author of the book Personal Branding for Developers at Apress. Behind this extrovert is a very passionate individual who believes in the power of communication... and cat videos.",
                                "avatar": "https://program.europython.eu/media/avatars/fred_z1RngGv.png",
                                "slug": "frederic-harper",
                                "affiliation": "Mindee",
                                "homepage": "http://mindee.com",
                                "twitter": "@fharper"
                            }
                        ],
                        "start": "2022-07-14T14:00:00+01:00",
                        "end": "2022-07-14T15:00:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 875,
                "duration": 30,
                "sessions": [
                    {
                        "id": "8D9LD8",
                        "title": "Creating great user interfaces on Jupyter Notebooks with ipywidgets",
                        "duration": 30,
                        "abstract": "Jupyter notebooks are great to quickly try new ideas and experiments, but the downside is that using code to change inputs and see the results can be inefficient and error-prone. ipywidget is a Python library that solves this problem by providing a user-friendly interface with iterative widgets. It's all in Python so we don't have to worry with any CSS or Javascript. In this talk we'll learn how ipywidgets can help us build tools in the context of Data Science.",
                        "day": "2022-07-14",
                        "time": 875,
                        "endTime": 905,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 2"
                        ],
                        "slug": "creating-great-user-interfaces-on-jupyter-notebooks-with-ipywidgets",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "TQCKYE",
                                "name": "Deborah Mesquita",
                                "biography": "I’m Déborah and I’m a data scientist who really likes to write. I have a BSc in Computer Science and I’ve been working with Data Science since 2016 when I won the Microsoft Imagine Machine Learning Award.\r\n\r\nI’m a generalist, so I can grasp new technology quickly and I can learn as much as I need to reach the goals of a project. I think this gives me an advantage in writing because it’s easier for me to “zoom out” and explain things from a broader point of view than someone who has more experience in a particular technology.",
                                "avatar": "https://program.europython.eu/media/avatars/scene01901_qomhn8m.jpeg",
                                "slug": "deborah-mesquita",
                                "affiliation": "NTT Data",
                                "homepage": "deborahmesquita.com",
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-14T14:35:00+01:00",
                        "end": "2022-07-14T15:05:00+01:00"
                    },
                    {
                        "id": "RWKPFX",
                        "title": "Open Science: Building Models LIke We Build Open-Source Software",
                        "duration": 30,
                        "abstract": "The use of transfer learning has begun a golden era in applications of Machine Learning but the development of these models “democratically” is still in the dark ages compared to best practices in Software Engineering. I describe how methods of open-source software development can allow models to be built by a distributed community of researchers.",
                        "day": "2022-07-14",
                        "time": 875,
                        "endTime": 905,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 1"
                        ],
                        "slug": "open-science-building-models-like-we-build-open-source-software",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "LKGJ7S",
                                "name": "Steven Kolawole",
                                "biography": "Steven Kolawole has his technical skillset cuts across Data Science and Software Engineering, with a bias for ML Research these days. His research interests focus on resource-efficient machine learning in terms of computational resources and low-resource/limited labeled data.\r\n\r\nHe is and has been heavily involved in varieties of ML subfields including ML Engineering, Software Engineering, Data Engineering, Data Science/Analytics, and Cloud Computing.\r\n\r\nSteven is also big on knowledge sharing via community mentorship and collective growth, open-source development, meetups facilitation, speakership, technical writing, research, and he gets kicks from helping tech muggles find their feet.",
                                "avatar": "https://program.europython.eu/media/avatars/08.42_1Rtwig6.jpeg",
                                "slug": "steven-kolawole",
                                "affiliation": "ML Collective",
                                "homepage": None,
                                "twitter": "@steveddev"
                            }
                        ],
                        "start": "2022-07-14T14:35:00+01:00",
                        "end": "2022-07-14T15:05:00+01:00"
                    },
                    {
                        "id": "SE83WQ",
                        "title": "Lint All the Things!",
                        "duration": 30,
                        "abstract": "Code that’s uniform is easier to read, write, and debug, but writing down your standards and conventions in a README that no one reads isn’t enough. The explosion of CI and linter tools allow you to no only document your standards and conventions, but make sure people actually adhere to them.",
                        "day": "2022-07-14",
                        "time": 875,
                        "endTime": 905,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey B"
                        ],
                        "slug": "lint-all-the-things",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "GLYM3N",
                                "name": "Luke Lee",
                                "biography": "I've been developing software professionally for almost 20 years. During that time, I've written device drivers for SSDs, desktop GUIs, and web applications. Now I'm working for Octopus Energy trying to save the world from Climate Change. In addition to writing software, I enjoy writing, teaching yoga, cycling, and chasing my Corgi.",
                                "avatar": "https://program.europython.eu/media/avatars/IMG_8325_45G8ZsD.jpg",
                                "slug": "luke-lee",
                                "affiliation": "Octopus Energy",
                                "homepage": "http://www.lukelee.me",
                                "twitter": "durden20"
                            }
                        ],
                        "start": "2022-07-14T14:35:00+01:00",
                        "end": "2022-07-14T15:05:00+01:00"
                    },
                    {
                        "id": "SHXRMJ",
                        "title": "How I wrote a Python client for HTTP/3 proxies",
                        "duration": 30,
                        "abstract": "[MASQUE](https://tools.ietf.org/id/draft-schinazi-masque-01.html) (Multiplexed Application Substrate over QUIC Encryption) is a draft of a new protocol that allows running proxy or VPN services indistinguishable from HTTPS servers. Akamai built a managed proxy service based on the MASQUE protocol [to provide egress proxy](https://www.akamai.com/blog/cloud/powering-and-protecting-online-privacy-icloud-private-relay) for iCloud Private Relay.\r\n \r\nWhile working on the proxy at Akamai, I wrote a Python client for testing the proxy service. The MASQUE protocol can tunnel traffic through HTTP/3 or HTTP/2, but common Python libraries only support HTTP/1.1. The tunneled traffic can use any protocol on top of TCP or UDP, including all HTTP versions, so MASQUE can be proxied through MASQUE for onion routing.\r\n\r\nIn this talk, I will show that the MASQUE proxy design is simple and yet client implementations are complex. To put everything into context, I will recap how HTTP proxies operate and how HTTP versions differ. I will highlight lessons learned from designing a low-level HTTP client using Python asyncio.",
                        "day": "2022-07-14",
                        "time": 875,
                        "endTime": 905,
                        "audience": "beginner",
                        "rooms": [
                            "Wicklow Hall 1"
                        ],
                        "slug": "how-i-wrote-a-python-client-for-http-3-proxies",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "CNVAFW",
                                "name": "Miloslav Pojman",
                                "biography": "I build data pipelines for change safety and performance monitoring in Akamai. Our Protocol optimization team implements and deploys standards for the future Internet.\r\n\r\nPreviously, I worked for Seznam.cz, where I moved from complex business applications to big data processing.\r\n\r\nI have a software engineering degree from Czech technical university in Prague, but I started to write webs a long time before studying it.",
                                "avatar": "https://program.europython.eu/media/avatars/Miloslav_Pojman_Qfkhusm.jpg",
                                "slug": "miloslav-pojman",
                                "affiliation": "Akamai Technologies",
                                "homepage": "https://pojman.cz",
                                "twitter": "@MiloslavPojman"
                            }
                        ],
                        "start": "2022-07-14T14:35:00+01:00",
                        "end": "2022-07-14T15:05:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 905,
                "title": "Coffee Break",
                "duration": 25,
                "type": "break"
            },
            {
                "time": 930,
                "duration": 30,
                "sessions": [
                    {
                        "id": "3HCYQ9",
                        "title": "Managing complex data science experiment configurations with Hydra",
                        "duration": 30,
                        "abstract": "Data science experiments have a lot of moving parts. Datasets, models, hyperparameters all have multiple knobs and dials. This means that keeping track of the exact parameter values can be tedious or error prone.\r\n\r\nThankfully you're not the only ones facing this problem and solutions are becoming available. One of them is Hydra from Meta AI Research. Hydra is an open-source application framework, which helps you handle complex configurations in an easy and elegant way. Experiments written with Hydra are traceable and reproducible with minimal boilerplate code.\r\n\r\nIn my talk I will go over the main features of Hydra and the OmegaConf configuration system it is based on. I will show examples of elegant code written with Hydra and talk about ways to integrate it with other open-source tools such as MLFlow.",
                        "day": "2022-07-14",
                        "time": 930,
                        "endTime": 960,
                        "audience": "advanced",
                        "rooms": [
                            "Liffey Hall 1"
                        ],
                        "slug": "managing-complex-data-science-experiment-configurations-with-hydra",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "RMHTBJ",
                                "name": "Michal Karzynski",
                                "biography": "Michal Karzynski currently works as a software architect and data scientist for Intel, specializing in applying neural network models to the domain of sound processing.\r\nHe is a chairman of the Operators Special Interest Group, part of the Open Neural Network Exchange (ONNX) standardization committee. He also runs the consulting company Atarnia.com and writes a blog, which can be found at http://michal.karzynski.pl",
                                "avatar": "https://program.europython.eu/media/avatars/michal.karzynski_8sqgZB4.jpg",
                                "slug": "michal-karzynski",
                                "affiliation": "Intel",
                                "homepage": "https://michal.karzynski.pl/",
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-14T15:30:00+01:00",
                        "end": "2022-07-14T16:00:00+01:00"
                    },
                    {
                        "id": "7FNTEJ",
                        "title": "Memory Problems, Did Collector Forgot to Clean the Garbage?",
                        "duration": 30,
                        "abstract": "Memory Problems are the worst nightmare of every developer whose code is serving large files in a production environment. If you ever faced issues of memory leaking in application or if frequent unexpected Out of Memory Exception is raising your anxiety levels, then this talk is for you. This talk aims to summarize the common Memory issues in Python. It is overwhelming to see them even when logic in code is properly optimized. However it is more scary that some of these errors are hard to find and harder to fix.",
                        "day": "2022-07-14",
                        "time": 930,
                        "endTime": 960,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey B"
                        ],
                        "slug": "memory-problems-did-collector-forgot-to-clean-the-garbage",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "3HJ87E",
                                "name": "Pratibha Jagnere",
                                "biography": "Pratibha is an enthusiast Pythoniasta, passionate for coding and books. Through her PyCon talks, she love to explore and share new things she learn in Python.",
                                "avatar": "https://program.europython.eu/media/avatars/profile_image_vgEgAJs.png",
                                "slug": "pratibha-jagnere",
                                "affiliation": "Google Cloud",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-14T15:30:00+01:00",
                        "end": "2022-07-14T16:00:00+01:00"
                    },
                    {
                        "id": "JWUZ7E",
                        "title": "Common Python Mistakes with Kubernetes, How They Can Cause Vulnerabilities and How to Solve Them!",
                        "duration": 30,
                        "abstract": "In this session, we will have a look at common mistakes in Python, that can cause serious code vulnerabilities, specifically for Kubernetes deployments of the code. We will subsequently have a look at what those vulnerabilities actually can result in and how your containerized application can get “hacked” as a result. We will also discuss how developer and security teams struggle to talk in a common language to prevent and mitigate these vulnerabilities. Lastly, we will see how you can prevent and mitigate these vulnerabilities in real-life.",
                        "day": "2022-07-14",
                        "time": 930,
                        "endTime": 960,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 2"
                        ],
                        "slug": "common-python-mistakes-with-kubernetes-how-they-can-cause-vulnerabilities-and-how-to-solve-them",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "B897VT",
                                "name": "Flo Pachinger",
                                "biography": "Flo is a Developer Advocate at Cisco focusing on IoT, machine learning and network programmability. With a software and networking background he has been working since a couple of years on many IoT, ML and network automation projects. He is the most passionate about connecting things and getting information out of data in any way possible. In his current role, he is working on awesome showcases with Cisco and Open-Source technologies and providing learning content to the developer community.",
                                "avatar": "https://program.europython.eu/media/avatars/me-new_On0NZxn.jpg",
                                "slug": "flo-pachinger",
                                "affiliation": "Cisco",
                                "homepage": "https://www.cisco.com/",
                                "twitter": "@flopachinger"
                            }
                        ],
                        "start": "2022-07-14T15:30:00+01:00",
                        "end": "2022-07-14T16:00:00+01:00"
                    },
                    {
                        "id": "LCNBCC",
                        "title": "Debugging asynchronous programs in Python",
                        "duration": 30,
                        "abstract": "Recently the interest in asynchronous programming has grown dramatically.\r\n Unfortunately, asynchronous programs do not always have reproducible behavior. Even when they are run with the same inputs, their results can be radically different.\r\n\tIn this talk I'll show you different approaches on how to debug asynchronous programs in Python.",
                        "day": "2022-07-14",
                        "time": 930,
                        "endTime": 960,
                        "audience": "advanced",
                        "rooms": [
                            "Liffey A"
                        ],
                        "slug": "debugging-asynchronous-programs-in-python",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "E9QEAS",
                                "name": "Andrii Soldatenko",
                                "biography": "Hi there! I’m Pythonista from Ukraine, I'm working remotely as a Senior Software Engineer at Astronomer. Also I'm a speaker at many PyCons and meetups around the globe. In my free time I’m crossFit and gymnastic amateur.",
                                "avatar": "https://www.gravatar.com/avatar/ef0c06e2a6d8c2da5dd07ebbdf20f451",
                                "slug": "andrii-soldatenko",
                                "affiliation": "Astronomer",
                                "homepage": None,
                                "twitter": "a_soldatenko"
                            }
                        ],
                        "start": "2022-07-14T15:30:00+01:00",
                        "end": "2022-07-14T16:00:00+01:00"
                    },
                    {
                        "id": "NF9HFT",
                        "title": "Scalpel: The Python Static Analysis Framework",
                        "duration": 30,
                        "abstract": "As the most popular programming language nowadays, it has been pointed out that Python static code analysis has not yet received enough attention from the research and OSS community.  For instance, to the best of our knowledge, there is no general static analysis framework proposed to facilitate the implementation of dedicated Python static analyzers (e.g., compared to the Java Soot/WALA framework). \r\n\r\nEasy to use and fast to prototyping, what makes Python stand out is bringing challenges to static analysis tasks. To fill this gap, we design and implement [Scalpel](https://github.com/SMAT-Lab/Scalpel) (A Python Static Analysis Framework) and make it publicly available as an open-source project. The Scalpel framework has already integrated a number of fundamental static analysis functions (e.g., call graph constructions, control-flow graph constructions, alias analysis, etc.) that are ready to be reused by developers to implement client applications focusing on statically resolving dedicated Python problems such as detecting bugs or fixing vulnerabilities. In addition, documentation and the user guide are provided for users. \r\n\r\nThe objective of the Scalpel framework is to (1) improve Python software quality and (2) support addressing  research challenges (e.g. API studies) in software engineering research;",
                        "day": "2022-07-14",
                        "time": 930,
                        "endTime": 960,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "scalpel-the-python-static-analysis-framework",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "RBJNZT",
                                "name": "Jiawei Wang",
                                "biography": "Jiawei Wang is a Ph.D. student at Monash University supervised by [Dr. Li Li](https://lilicoding.github.io/) and [Dr. Xiaoning Du](https://xiaoningdu.github.io/) and a member of [SMart software Analysis and Trustworthy computing Lab](https://smat-lab.github.io/). He works on static analysis for Python Programs and has published four top conference papers in the domain of software engineering research with a focus on Python code quality issues among open source projects.   \r\n\r\nCurrently, he works on the Scalpel project, aiming to provide fundamental tools to address problems in the Python eco-system such as dependency issues, bug detection for machine learning applications.",
                                "avatar": None,
                                "slug": "jiawei-wang",
                                "affiliation": "Monash University",
                                "homepage": "https://scholar.google.com.au/citations?user=jxAaupQAAAAJ",
                                "twitter": "https://twitter.com/JiaweiW02966288"
                            },
                            {
                                "code": "ARKDPR",
                                "name": "Li Li",
                                "biography": None,
                                "avatar": None,
                                "slug": "li-li",
                                "affiliation": None,
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-14T15:30:00+01:00",
                        "end": "2022-07-14T16:00:00+01:00"
                    },
                    {
                        "id": "WFJ7XP",
                        "title": "Robyn: An async web framework written in Rust",
                        "duration": 30,
                        "abstract": "Python web frameworks, like FastAPI, Flask, Quartz, Tornado, and Twisted, are important for writing high-performance web applications and for their contributions to the web ecosystem. However, even they posit some bottlenecks either due to their synchronous nature or due to the usage of python runtime. Most of them don’t have the ability to speed themselves due to their dependence on *SGIs. This is where Robyn comes in. Robyn tries to achieve near-native Rust throughput along with the benefit of writing code in Python. In this talk, we will learn more about Robyn. From what is Robyn to the development in Robyn.",
                        "day": "2022-07-14",
                        "time": 930,
                        "endTime": 960,
                        "audience": "advanced",
                        "rooms": [
                            "Wicklow Hall 1"
                        ],
                        "slug": "robyn-an-async-web-framework-written-in-rust",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "ZPQUMD",
                                "name": "Sanskar Jethi",
                                "biography": "Sanskar is a Software Engineer at Bloomberg, London during the day and a FOSS maintainer during the night. He is the author and maintainer of Robyn, which is one of the faster web frameworks in the Python ecosystem.\r\n\r\nSanskar loves attending, speaking and organising conferences and has been an active part of various Open Source and Python conferences.",
                                "avatar": "https://www.gravatar.com/avatar/50fa521c70e497435ccce40ab0feb1cb",
                                "slug": "sanskar-jethi",
                                "affiliation": "Bloomberg, London",
                                "homepage": None,
                                "twitter": "@sansyrox"
                            }
                        ],
                        "start": "2022-07-14T15:30:00+01:00",
                        "end": "2022-07-14T16:00:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 965,
                "duration": 30,
                "sessions": [
                    {
                        "id": "9VWGLC",
                        "title": "Simple data validation and setting management with Pydantic",
                        "duration": 30,
                        "abstract": "When processing data, validating its structure and its type is critical. Bad record types or changes in structure can often result in processing errors or worst in wrong data output. Yet, solving this problem cleanly and efficiently can be challenging. It often results in complicated code logic and increases complexity; consequently decreasing code readability. Pydantic is an efficient and elegant answer to these challenges\r\n\r\nWe expect you'll leave this talk with a good understanding of:\r\n\r\n- Existing challenges in data validation\r\n- What Pydantic Models, Validators, and Convertors are\r\n- How to leverage Pydantic in your day to day (using real-life examples)\r\n- [Bonnus] How to use Code Generation to create Pydantic Models from any data sources",
                        "day": "2022-07-14",
                        "time": 965,
                        "endTime": 995,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 1"
                        ],
                        "slug": "simple-data-validation-and-setting-management-with-pydantic",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "7UGD3J",
                                "name": "Teddy Crepineau",
                                "biography": "Teddy is a Software Engineer at Collate (the software company building OpenMetadata, a metadata catalog). He is currently working on the ingestion part, more specifically on everything related to data profiling and quality tests.\r\n\r\nTeddy has been working in the data field for 5 years in Analytics, Business Intelligence, and Engineering teams. He previously worked on building a data platform infrastructure, an ELT overlay framework and data pipelines. He loves contributing to open source projects in his downtime and studying software engineering and Python fundamentals.",
                                "avatar": "https://www.gravatar.com/avatar/1f84f1792847e674df72aea18d4e4f43",
                                "slug": "teddy-crepineau",
                                "affiliation": "Collate",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-14T16:05:00+01:00",
                        "end": "2022-07-14T16:35:00+01:00"
                    },
                    {
                        "id": "BNJPUH",
                        "title": "Automate cleaning code in few easy steps!",
                        "duration": 30,
                        "abstract": "How annoying is it to find out that everything went to hell on the pipeline because you forgot to run the formatters? \r\n\r\nDon’t waste precious time and learn how it is possible to automate these little things, but most importantly understand why it is important to have them in your code!",
                        "day": "2022-07-14",
                        "time": 965,
                        "endTime": 995,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "automate-cleaning-code-in-few-easy-steps",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "LJNU97",
                                "name": "Ester",
                                "biography": "I'm a Python Developer living in London who is passionate about clean code and architecture. \r\nI try to give my contribution to the development of [PyCon Italia](pycon.it), [Strawberry GraphQL](strawberry.rocks) and [Poetry](python-poetry.org) Package Manager.",
                                "avatar": "https://program.europython.eu/media/avatars/CleanShot_2022-03-28_at_11.03.022x_xZYrlYU.png",
                                "slug": "ester",
                                "affiliation": "Made.com",
                                "homepage": "made.com",
                                "twitter": "esterbeltrami"
                            }
                        ],
                        "start": "2022-07-14T16:05:00+01:00",
                        "end": "2022-07-14T16:35:00+01:00"
                    },
                    {
                        "id": "JJQSXA",
                        "title": "Let's talk about JWT",
                        "duration": 30,
                        "abstract": "JSON Web Tokens, or JWTs for short, are all over the web. They can be used to track bits of information about a user in a very compact way and can be used in APIs for authorization purposes. Join me and learn what JWTs are, what problems it solves, how you can use JWTs, and how to be safer when using JWTs on your applications.",
                        "day": "2022-07-14",
                        "time": 965,
                        "endTime": 995,
                        "audience": "intermediate",
                        "rooms": [
                            "Wicklow Hall 1"
                        ],
                        "slug": "let-s-talk-about-jwt",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "JX8YLX",
                                "name": "Jessica Temporal",
                                "biography": "Jessica Temporal is Senior Developer Advocate at Okta for Auth0. [Pizza de Dados](http://pizzadedados.com/en/) co-founder and co-host, Pizza is the first and most beloved Brazilian podcast about data science. Jessica is also part of the instructors team in Data Bootcamp and LinkedIn Learning. She is part of PyLadies Brazil, the Brazilian network that promotes and empowers women in technology. Creator of [GitFichas](https://gitfichas.com/en), a git study cards collection available in English and Portuguse. She was born in warm weather and keeps herself warm in the cold Brazilian south with sweaters she knits herself.",
                                "avatar": "https://program.europython.eu/media/avatars/profile-jt_kncvxT2.png",
                                "slug": "jessica-temporal",
                                "affiliation": "Okta",
                                "homepage": "https://jtemporal.com",
                                "twitter": "@jesstemporal"
                            }
                        ],
                        "start": "2022-07-14T16:05:00+01:00",
                        "end": "2022-07-14T16:35:00+01:00"
                    },
                    {
                        "id": "NL8HRY",
                        "title": "Build-A-Database with Python",
                        "duration": 30,
                        "abstract": "Databases are beautiful beasts built with several layers of abstractions that we rarely have to know or even care about, now it's time to break them open and discuss the different components that maketh a database and how one would go about building one if they wanted. This would be based on my learnings when I went about building my own Toy Database in Python",
                        "day": "2022-07-14",
                        "time": 965,
                        "endTime": 995,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey A"
                        ],
                        "slug": "build-a-database-with-python",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "RTG9TS",
                                "name": "Sangarshanan",
                                "biography": "My name is Sangarshanan and I am a Software Engineer. I love making stuff that helps and amuses me in equal measure and standing upside down while holding a banana. When I'm bored you can find me making absurdist memes, yet another Spotify playlist or staring straight into the void",
                                "avatar": "https://program.europython.eu/media/avatars/my_pic_AtjHUk4.jpeg",
                                "slug": "sangarshanan",
                                "affiliation": "Blinkit",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-14T16:05:00+01:00",
                        "end": "2022-07-14T16:35:00+01:00"
                    },
                    {
                        "id": "QMZDVX",
                        "title": "Is the news media polarized? Or are we being conditioned to think it is?",
                        "duration": 30,
                        "abstract": "In this talk, we aim to find if polarization is induced in a neural\r\nnetwork by feeding it newspaper articles with manufactured sentiments according to the\r\nAllsides Media Bias chart for the level of faith people on various aisles of the political\r\nspectrum. This project consists of a set of experiments on similar data-sets from news\r\nagencies across the various subsets in the ”media-bias” chart. News Media perceived bias\r\nis common across consumers that belong to various political affiliations. While anecdotal\r\nevidence of this exists and there exist annotated datasets that aim to annotate the ”spin”\r\na news agency puts on certain events and entities, whether this is a widespread problem\r\nand whether it can be detected by the neural network topically or temporally is a problem that needs to be explored. The news media bias analysis is modelled as a Natural\r\nLanguage Processing sentiment analysis task and a fake news binary classification task to\r\ndeduce the level of polarization in a neural network by feeding it headlines embedded using\r\npre-trained sentiment models from news publications across the political spectrum. When\r\nit came to fake news vulnerability, news from all kinds of perceived politically affiliated\r\nnews media holds up well against a fake news dataset with a very good accuracy. None of\r\nthe accuracies dropped below 95%. This is a significant result that sort of debunks the AllSlides categorization",
                        "day": "2022-07-14",
                        "time": 965,
                        "endTime": 995,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 2"
                        ],
                        "slug": "is-the-news-media-polarized-or-are-we-being-conditioned-to-think-it-is",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "HKHYS9",
                                "name": "Aroma Rodrigues",
                                "biography": "Aroma Rodrigues is a master's student at UMass Amherst. She believes that Automation is the path to Inclusion. In 2016, a teammate of her \"Shoes for the Visually Impaired\" project presented it at the FOSSASIA. She reads, writes and enjoys walking to explore places. She presently works in a financial services firm and believes that solving problems that she has would solve problems for a large chunk of the world. An ML enthusiast she has about 20+ Coursera Certifications with the respective project work to support her learning in that field. She presented a talk on “De-mystifying Terms and Conditions using NLP” at PyCon 2018 and a talk called “Propaganda Detection in Fake News using Natural Language Processing” at PyCon ZA 2019 in Johannesburg. She spoke on detecting gender roles based biases in school textbooks at PyOhio 2020.",
                                "avatar": "https://program.europython.eu/media/avatars/IMG20180523181017_xqVcRmM.jpg",
                                "slug": "aroma-rodrigues",
                                "affiliation": "University of Massachusetts, Amherst",
                                "homepage": "https://www.linkedin.com/in/aromarodrigues/",
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-14T16:05:00+01:00",
                        "end": "2022-07-14T16:35:00+01:00"
                    },
                    {
                        "id": "ZSCTME",
                        "title": "Correlating messy data with \"correlate\"",
                        "duration": 30,
                        "abstract": "An introduction to the **correlate** Python library.  You tell **correlate** about two datasets that should map to each other, and it determines the best matches for you.  The novel scoring algorithm at the heart of **correlate** means it copes exceedingly well with messy real-world data.  **correlate** supports fuzzy matching, weighted matching, and ordering.",
                        "day": "2022-07-14",
                        "time": 965,
                        "endTime": 995,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey B"
                        ],
                        "slug": "correlating-messy-data-with-correlate",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "9DMGRT",
                                "name": "Larry Hastings",
                                "biography": "Larry is a 200 foot assault robot manufactured by Yoyodyne Propulsion Systems, a major US defense contractor.  He is suitable for heavy assault against heavily armored stationary targets, like laying siege to a walled city, or protecting supply lines during forward maneuvers.",
                                "avatar": "https://program.europython.eu/media/avatars/pycon.profile.pic_2Ohe0DM.png",
                                "slug": "larry-hastings",
                                "affiliation": "CPython",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-14T16:05:00+01:00",
                        "end": "2022-07-14T16:35:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 1000,
                "duration": 45,
                "sessions": [
                    {
                        "id": "LCCECR",
                        "title": "Lightning Talks",
                        "duration": 45,
                        "abstract": "A lightning talk (LT) is a short presentation that must not be longer than five minutes.\r\n\r\nTo sign up for a lightning talk, you can put your name on the information board during the conference before the second coffee break. For our online participants, we will set up a separate form or Google sheet for you to put your name and topic in - similar to how we run this at the in-person conference. \r\n\r\nWe will announce the same every day both online and in person.",
                        "day": "2022-07-14",
                        "time": 1000,
                        "endTime": 1045,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "lightning-talks",
                        "type": "lightning-talks",
                        "speakers": [],
                        "start": "2022-07-14T16:40:00+01:00",
                        "end": "2022-07-14T17:25:00+01:00"
                    }
                ],
                "type": "timeslot"
            }
        ],
        "rooms": [
            "The Auditorium",
            "Wicklow Hall 1",
            "Liffey A",
            "Liffey B",
            "Liffey Hall 1",
            "Liffey Hall 2",
            "Forum"
        ]
    },
    "dayType": "Talks"
}

d3 = {
    "schedule": {
        "slots": [
            {
                "time": 540,
                "duration": 15,
                "sessions": [
                    {
                        "id": "8LXW7T",
                        "title": "Morning Announcement",
                        "duration": 15,
                        "abstract": "Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement Morning Announcement",
                        "day": "2022-07-15",
                        "time": 540,
                        "endTime": 555,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "morning-announcement",
                        "type": "opening-session",
                        "speakers": [],
                        "start": "2022-07-15T09:00:00+01:00",
                        "end": "2022-07-15T09:15:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 555,
                "duration": 45,
                "sessions": [
                    {
                        "id": "CEPSYS",
                        "title": "Multithreaded Python without the GIL",
                        "duration": 45,
                        "abstract": "CPython’s “Global Interpreter Lock”, or “GIL”, prevents multiple threads from executing Python code in parallel. The GIL was added to Python in 1992 together with the original support for threads in order to protect access to the interpreter’s shared state.\r\n\r\nPython supports a number of ways to enable parallelism within the constraints of the GIL, but they come with significant limitations. Imagine if you could avoid the startup time of joblib workers, the multiprocess instability of PyTorch’s DataLoaders, and the overhead of pickling data for inter-process communication.\r\n\r\nThe “nogil” project aims to remove the GIL from CPython to make multithreaded Python programs more efficient, while maintaining backward compatibility and single-threaded performance. It exists as a fork, but the eventual goal is to contribute these changes upstream.\r\n\r\nThis talk will cover the changes to Python to let it run efficiently without the GIL and what these changes mean for Python programmers and extension authors.",
                        "day": "2022-07-15",
                        "time": 555,
                        "endTime": 600,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "multithreaded-python-without-the-gil",
                        "type": "keynote",
                        "speakers": [
                            {
                                "code": "DMWLH3",
                                "name": "Sam Gross",
                                "biography": "Sam Gross is a software engineer at Meta AI. He is a co-author of PyTorch, an open-source Python machine learning framework. He holds M.Eng. and B.S. degrees in computer science from the Massachusetts Institute of Technology.\r\n\r\n\r\n  Since moving to DIAS he has worked on the development of calibration and\r\n  software tools for the Mid-Infrared Instrument (MIRI) on Webb. MIRI is an\r\n  international project comprising a consortium of European partner institutes,\r\n  including DIAS, the European Space Agency, and partners in the US.\r\n\r\n\r\n  He works on many aspects of MIRI including the calibration of the MIRI Medium\r\n  Resolution Spectrometer, development of the MIRI simulator, MIRI commissioning\r\n  activities and analysis tools, and will support MIRI commissioning at the Webb\r\n  Mission Operations Center at the Space Telescope Science Institute in\r\n  Baltimore.",
                                "avatar": None,
                                "slug": "sam-gross",
                                "affiliation": "Meta AI",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-15T09:15:00+01:00",
                        "end": "2022-07-15T10:00:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 600,
                "title": "Coffee Break",
                "duration": 30,
                "type": "break"
            },
            {
                "time": 630,
                "duration": 45,
                "sessions": [
                    {
                        "id": "8JDRVD",
                        "title": "Writing secure code in Python",
                        "duration": 45,
                        "abstract": "The talk will analyze a series of vulnerabilities that given some common mistakes might end up damaging your Python programs (with lots of exemples!). At the end, a precaution and audit method will be presented.",
                        "day": "2022-07-15",
                        "time": 630,
                        "endTime": 675,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey B"
                        ],
                        "slug": "writing-secure-code-in-python",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "SA3X9R",
                                "name": "Yan Orestes",
                                "biography": "Yan is a Brazilian Python developer, speaker, privacy freak and security enthusiast. He's worked as a teacher and takes education as a true passion in his life. Whenever he finds time, Yan ends up writing blog posts and essays and talking in conferences everywhere, following what he believes is most important in the world - sharing knowledge.",
                                "avatar": "https://program.europython.eu/media/avatars/me_8cDiqA7.jpeg",
                                "slug": "yan-orestes",
                                "affiliation": "Lean Tech",
                                "homepage": "https://esquer.dev",
                                "twitter": "@yyyyyyyan_"
                            }
                        ],
                        "start": "2022-07-15T10:30:00+01:00",
                        "end": "2022-07-15T11:00:00+01:00"
                    },
                    {
                        "id": "9QM8ZM",
                        "title": "What transitioning from male to female taught me about leadership",
                        "duration": 45,
                        "abstract": "Not many leaders transition in their mid thirties but I did and it gave me a unique perspective on courage, humility, diversity and inclusion in the context of leadership. In this talk I will tell the story of my transition and along the way you will learn how you can become a better leader.",
                        "day": "2022-07-15",
                        "time": 630,
                        "endTime": 675,
                        "audience": "beginner",
                        "rooms": [
                            "Wicklow Hall 1"
                        ],
                        "slug": "what-transitioning-from-male-to-female-taught-me-about-leadership",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "9SYDFX",
                                "name": "Ivett Ördög",
                                "biography": "Ivett Ördög is the founder and facilitator of Lean Poker events. She is also an Engineering Manager at Contentful, and she has been a frequent speaker at software conferences around Europe. Her passion for short feedback loops drove her to create Lean Poker, a workshop where developers have the opportunity to experiment with continuous delivery in a safe environment. Ivett is the creator and host of the Cup of Code YouTube channel inspiring the next generation of developers to broaden their knowledge.",
                                "avatar": "https://program.europython.eu/media/avatars/DSC_2275_VN94PyO.jpg",
                                "slug": "ivett-ordog",
                                "affiliation": "Lean Poker",
                                "homepage": "http://leanpoker.org",
                                "twitter": "@ivettordog"
                            }
                        ],
                        "start": "2022-07-15T10:30:00+01:00",
                        "end": "2022-07-15T11:15:00+01:00"
                    },
                    {
                        "id": "CPNE9S",
                        "title": "AI for Content Moderation at PayPal",
                        "duration": 45,
                        "abstract": "Online platforms have a hard time combating hate, hate speech, explicit content and other NSFW material. Most of the solutions are rule based keyword approaches which are brittle and can be bypassed easily. At PayPal, we have a wide range of user generated content and there is a great need to automatically identify and flag hate, explicit and other typologies, to improve user experience and adhere to regulatory policies. In this talk we showcase how AI can help us identify such content with great precision.",
                        "day": "2022-07-15",
                        "time": 630,
                        "endTime": 675,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 1"
                        ],
                        "slug": "ai-for-content-moderation-at-paypal",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "J98AEX",
                                "name": "Raghotham Sripadraj",
                                "biography": "Raghotham is an AI Architect at PayPal and leads AI teams for the Customer Success Platform. He comes with rich background in building AI platforms and teams for startups and large enterprises. Drawing on his deep love for data science and neural networks and his passion for teaching, Raghotham has conducted workshops across the world and given talks at a number of data science conferences. Apart from getting his hands dirty with data, he loves traveling, Pink Floyd, and masala dosas.",
                                "avatar": "https://program.europython.eu/media/avatars/2022-04-03_22.40.18_BPxR1BI.jpg",
                                "slug": "raghotham-sripadraj",
                                "affiliation": "PayPal Inc",
                                "homepage": "https://raghothams.in",
                                "twitter": "@raghothams"
                            },
                            {
                                "code": "XENQTK",
                                "name": "Ryan Roggenkemper",
                                "biography": "Ryan is an NLP Engineer at PayPal, primarily working on text content moderation for the Customer Success Platform. He is fairly new to the field of NLP, with just over 1 year of experience, but has a great passion for all things statistics and data science. This is his first conference appearance (but hopefully not his last!), and he is very excited to present and learn! He's also very enthusiastic about ice cream. Probably too enthusiastic...",
                                "avatar": None,
                                "slug": "ryan-roggenkemper",
                                "affiliation": "PayPal",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-15T10:30:00+01:00",
                        "end": "2022-07-15T11:15:00+01:00"
                    },
                    {
                        "id": "FZQGFP",
                        "title": "How to embed a Python interpreter in an iOS app",
                        "duration": 45,
                        "abstract": "Come see how you can make a native mobile app that embeds Python 3.10 to allow users to script app behavior. It's allowed by Apple but is currently underutilized by the app makers. Add superpowers to your iPhone app with Python!\r\n\r\nNative mobile applications have many advantages over mobile websites or apps made with cross-platform toolkits. They will use less battery, allow for richer graphics, more consistent UI behavior, and enable more functionality through device-specific APIs. Wouldn't it be great to have access to all this from Python?\r\n\r\nIn this talk, we'll marry a native iOS app written in Swift with an embedded Python 3.10 interpreter to allow users to customize what the application is doing. We'll go through the entire process of:\r\n\r\n- embedding Python from source;\r\n- building it into the Swift mobile app in Xcode;\r\n- adding a few pre-compiled third-party libraries like numpy and Pillow to broaden the scope of what the user can do;\r\n- running the resulting app on an iPhone 13;\r\n- modifying the app behavior at runtime thanks to our new Python superpowers!\r\n\r\nKnowledge of Swift is not required for attendees of this talk. However, it will be needed later if you're willing to embed Python in an iPhone app. Embedding Python doesn't really let you make an app without knowing Swift. Don't fret though! It's pretty easy to get a hang of Swift when you're fluent in Python.",
                        "day": "2022-07-15",
                        "time": 630,
                        "endTime": 675,
                        "audience": "advanced",
                        "rooms": [
                            "Liffey A"
                        ],
                        "slug": "how-to-embed-a-python-interpreter-in-an-ios-app",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "YFCVFV",
                                "name": "Łukasz Langa",
                                "biography": "CPython Developer in Residence, Python 3.8 and 3.9 release manager, creator of Black, pianist, dad.\r\n\r\nEqually interested in music and software engineering, as a classically-trained pianist and a long-time contributor to the Python programming language. Loves to build software for musical instruments. Makes music under the [RPLKTR](https://rplktr.com/) moniker.",
                                "avatar": "https://program.europython.eu/media/avatars/%C5%81ukasz_Langa_Portret_2021.10_Prawy_profil_VNI4Aj1.jpeg",
                                "slug": "lukasz-langa",
                                "affiliation": "Python Software Foundation",
                                "homepage": "https://lukasz.langa.pl/",
                                "twitter": "@llanga"
                            }
                        ],
                        "start": "2022-07-15T10:30:00+01:00",
                        "end": "2022-07-15T11:15:00+01:00"
                    },
                    {
                        "id": "USWAD9",
                        "title": "`typing.Protocol`: type hints as Guido intended",
                        "duration": 45,
                        "abstract": "If your type-hinted Python code is Java flavored, you're probably underusing `typing.Protocol`. Python is literally built on structural typing, a.k.a. duck typing. It's how `__special__` methods work. Type hints were introduced in Python 3.5 without support for duck typing, but it was added in Python 3.8 and we should all be using `typing.Protocol` to have our code statically checked **and** Pythonic.",
                        "day": "2022-07-15",
                        "time": 630,
                        "endTime": 675,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "typing-protocol-type-hints-as-guido-intended",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "AX8V78",
                                "name": "Luciano Ramalho",
                                "biography": "Luciano Ramalho is the author of Fluent Python, published in 9 languages. He is a Principal Consultant at Thoughtworks and a Fellow of the Python Software Foundation.",
                                "avatar": "https://program.europython.eu/media/avatars/LucianoRamalho2016-500x.jpg",
                                "slug": "luciano-ramalho",
                                "affiliation": "Thoughtworks",
                                "homepage": "https://www.thoughtworks.com/en-br/profiles/l/luciano-ramalho",
                                "twitter": "@ramalhoorg"
                            }
                        ],
                        "start": "2022-07-15T10:30:00+01:00",
                        "end": "2022-07-15T11:15:00+01:00"
                    },
                    {
                        "id": "YMAR7H",
                        "title": "Jupyter - Under the Hood",
                        "duration": 45,
                        "abstract": "Jupyter Notebooks at their core are just JSON documents that contain all your code, markdown styles and outputs. Yet when you run a notebook, there's a lot that's happening under the hood - from starting a session with the notebook server, to launching an IPython kernel, and a rich Web UI communicating with the notebook server and the IPython kernel using Jupyter's REST APIs and ZMQ websockets. We will explore the Jupyter ecosystem (Jupyter, JupyterLab, JupyterHub) and see how this system comes together.",
                        "day": "2022-07-15",
                        "time": 630,
                        "endTime": 675,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 2"
                        ],
                        "slug": "jupyter-under-the-hood",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "7VMLGN",
                                "name": "Dhanshree Arora",
                                "biography": "Hi I am Dhanshree, \r\nI have been developing with Python for over 3 years now. I enjoy working with computers. I work with machine learning, backend development, cloud and infrastructure.",
                                "avatar": "https://program.europython.eu/media/avatars/image_QQzHuxX.png",
                                "slug": "dhanshree-arora",
                                "affiliation": "ML Consultant",
                                "homepage": None,
                                "twitter": "@dhanshree_arora"
                            }
                        ],
                        "start": "2022-07-15T10:30:00+01:00",
                        "end": "2022-07-15T11:15:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 680,
                "duration": 30,
                "sessions": [
                    {
                        "id": "87XUMG",
                        "title": "Why is it slow? Strategies for solving performance problems",
                        "duration": 30,
                        "abstract": "You have a performance problem, and you don't know what to do. All you know is that one of your endpoints is very slow; and perhaps it only affects a certain user. How do you figure out why it's slow, and what can you do to catch performance problems before they hurt users in production? This talk will step through several scenarios involving typical performance problems and how to diagnose them.",
                        "day": "2022-07-15",
                        "time": 680,
                        "endTime": 710,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey A"
                        ],
                        "slug": "why-is-it-slow-strategies-for-solving-performance-problems",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "9JJFPM",
                                "name": "Caleb Hattingh",
                                "biography": "TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD",
                                "avatar": "https://program.europython.eu/media/avatars/sqfortekmojitwitch_VVdyZFb.jpg",
                                "slug": "caleb-hattingh",
                                "affiliation": "Kapiche Pty Ltd",
                                "homepage": "tekmoji.com",
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-15T11:20:00+01:00",
                        "end": "2022-07-15T11:50:00+01:00"
                    },
                    {
                        "id": "CJNVSR",
                        "title": "Mercury - Build & Share Data Apps from Jupyter Notebook",
                        "duration": 30,
                        "abstract": "Have you ever wished to magically transform your notebook into a web app and share it with non-coders? The [Mercury](https://github.com/mljar/mercury) is a new open-source framework for converting Jupyter Notebook to a web app.",
                        "day": "2022-07-15",
                        "time": 680,
                        "endTime": 710,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 2"
                        ],
                        "slug": "mercury-build-share-data-apps-from-jupyter-notebook",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "JWK7RV",
                                "name": "Piotr Płoński",
                                "biography": "Software engineer with a passion for creating Data Science tools. Working on Mercury (framework for converting notebooks to web apps) and MLJAR AutoML (Automatic Machine Learning for Tabular Data).",
                                "avatar": "https://program.europython.eu/media/avatars/pplonski_smile_Mz6QCW4.jpeg",
                                "slug": "piotr-plonski",
                                "affiliation": "MLJAR Sp. z o.o.",
                                "homepage": "https://mljar.com",
                                "twitter": "MLJARofficial"
                            }
                        ],
                        "start": "2022-07-15T11:20:00+01:00",
                        "end": "2022-07-15T11:50:00+01:00"
                    },
                    {
                        "id": "GRG9SC",
                        "title": "Tales of Python Security",
                        "duration": 30,
                        "abstract": "Security vulnerabilities receive huge publicity but also significant secrecy. In this session, we will walk through some of the biggest issues of the last few years from the perspective of a member of the Python Security Response Team. You'll learn how we work to protect all CPython users, how you can help, and how you can help protect yourself from malicious attackers.",
                        "day": "2022-07-15",
                        "time": 680,
                        "endTime": 710,
                        "audience": "beginner",
                        "rooms": [
                            "Liffey B"
                        ],
                        "slug": "tales-of-python-security",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "PMWVSA",
                                "name": "Steve Dower",
                                "biography": "Steve is an engineer who tells people about Python and then gives them excuses to use it and great tools to use it with. He is a core developer and Windows expert for CPython, a member of the Python Security Response Team, and works at Microsoft as a roaming Python expert, making sure Python users are well supported across all their platforms.",
                                "avatar": "https://program.europython.eu/media/avatars/Headshot_Python_2q9HWBk.jpg",
                                "slug": "steve-dower",
                                "affiliation": "Microsoft",
                                "homepage": "https://stevedower.id.au",
                                "twitter": "zooba"
                            }
                        ],
                        "start": "2022-07-15T11:20:00+01:00",
                        "end": "2022-07-15T11:50:00+01:00"
                    },
                    {
                        "id": "S78FW7",
                        "title": "When Models Query Models",
                        "duration": 30,
                        "abstract": "The design of large-scale engineering systems, including but not limited to aerospace, particle accelerators, nuclear power plants, is carried out by a wide range of numerical models such as CAD files, finite-element models, and machine learning surrogate models to name a few.  In order to provide a uniform modelling interface, we encapsulate numerical models in notebooks. A notebook is controlling model creation, execution, and query of results. Numerical solvers are embedded into Docker containers and provide an isolated and reproducible environment exposing a language-agnostic REST API. A model registry enables efficient queries of models. The overall system is represented as a collection of models that exchange data. Then, the design optimization involves execution of a dependency tree of models to study the impact of a parameter change and perform its optimization. In this contribution, we present a model query mechanism allowing notebook models to query one another. The model dependencies are represented with a graph with suitable processing algorithms. In order to ensure that only affected models are executed we derive and cache a model resolution order. The presented modelling framework relies on open source-technologies (packages: pydantic, Fast API, Jupyter, papermill, scrapbook, containers: Docker and Openshift as well as databases: MongoDB and Redis) and the talk will focus on good practices and design decisions encountered in the process.",
                        "day": "2022-07-15",
                        "time": 680,
                        "endTime": 710,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 1"
                        ],
                        "slug": "when-models-query-models",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "SBZRSP",
                                "name": "Michal Maciejewski",
                                "biography": "Enthusiastic, hard-working software engineer with contagious energy and passion for working on interdisciplinary projects. Focused on delivering high-quality products in a timely manner. Servant leader always eager to learn from and with team members while instilling the ownership, autonomy, and sense of responsibility. \r\n\r\nOver ten years of experience as a software developer for modelling and analysis of complex systems.  Passionate about model-based system engineering solutions improving existing analysis workflows while ensuring reproducibility. Currently, the lead developer of an MLOps framework to support the design of superconducting accelerator magnets. Formerly, a technical lead for an agile team of experts and scientists creating signal monitoring framework for the Large Hadron Collider.",
                                "avatar": None,
                                "slug": "michal-maciejewski",
                                "affiliation": "ETH Zurich",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-15T11:20:00+01:00",
                        "end": "2022-07-15T11:50:00+01:00"
                    },
                    {
                        "id": "YJYBHC",
                        "title": "Super Search with OpenSearch and Python",
                        "duration": 30,
                        "abstract": "OpenSearch is an open source and free document database with search and aggregation superpowers, based on Elasticsearch. This session covers how to use OpenSearch to perform both simple and advanced searches on semi-structured data such as a product database.",
                        "day": "2022-07-15",
                        "time": 680,
                        "endTime": 710,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "super-search-with-opensearch-and-python",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "ZLLVEH",
                                "name": "Laysa Uchoa",
                                "biography": "Laysa is a developer working towards a more diverse and fun Python community by organizing Pyladies Munich Chapter. Her passion for sharing knowledge and OSS has led her to work as developer advocate for Aiven. She help users understand databases and do cool things with them. Besides Python, she like cyberpunk movies, tea, and human languages.",
                                "avatar": "https://program.europython.eu/media/avatars/DSC_0672_1_wcU720A.jpg",
                                "slug": "laysa-uchoa",
                                "affiliation": "Aiven",
                                "homepage": None,
                                "twitter": "laysauchoa"
                            }
                        ],
                        "start": "2022-07-15T11:20:00+01:00",
                        "end": "2022-07-15T11:50:00+01:00"
                    },
                    {
                        "id": "ZGSULC",
                        "title": "Best practices to open source a product and creating a community around it",
                        "duration": 30,
                        "abstract": "In certain areas of the industry open source has become mainstream, whether it be a small part of a product, a “community edition of a product”, or creating a whole business around an open source product. One could assume the only thing required to do so is to make the source code of the project publicly accessible, possibly by putting it on a platform such as GitLab or GitHub, and one couldn’t be more wrong.\r\n\r\nIn this talk we explore those aspects such as the licence and the governance of the project and the impact they can have. Then we talk about common mistakes teams make which create an environment where outsiders don’t necessarily feel welcomed to the project. First impressions matter and it’s important that new contributors and users stay once they encounter the project.",
                        "day": "2022-07-15",
                        "time": 680,
                        "endTime": 710,
                        "audience": "beginner",
                        "rooms": [
                            "Wicklow Hall 1"
                        ],
                        "slug": "best-practices-to-open-source-a-product-and-creating-a-community-around-it",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "HGSWKF",
                                "name": "Adrin Jalali",
                                "biography": "I'm a computer scientist / bioinformatician who has turned to be a core developer of `scikit-learn` and `fairlearn`, and work as a Machine Learning Engineer at Hugging Face. I'm also an organizer of PyData Berlin.\r\n\r\nThese days I mostly focus on aspects of machine learning and tools which help with creating more ethical and fair decision making systems. This trend has influenced me to work on `fairlearn`, and to work on aspects of `scikit-learn` which would help tools such as `fairlearn` to work more fluently with the package; and at Hugging Face, my focus is to enable the community of these libraries to be able to share their models more easily and be more open about their work.",
                                "avatar": "https://program.europython.eu/media/avatars/Farb3SW3229-w-small_mpaHfiN.png",
                                "slug": "adrin-jalali",
                                "affiliation": "HuggingFace",
                                "homepage": "adrin.info",
                                "twitter": "@adrinjalali"
                            }
                        ],
                        "start": "2022-07-15T11:20:00+01:00",
                        "end": "2022-07-15T11:50:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 715,
                "duration": 45,
                "sessions": [
                    {
                        "id": "GFGSGN",
                        "title": "Leading & growing software teams",
                        "duration": 45,
                        "abstract": "Software development is a team game.\r\n\r\nAs you progress through your career, you might end up in a leadership role, taking care of  your own team, or even of multiple teams.\r\n\r\nAs a team lead, it’s up to you to establish a good working rhythm, set the right expectations, communicate up and down the chain of command and effectively help your team grow in both technical and non-technical terms.\r\n\r\nAs a team lead, you want to enable your team to reach its full potential.\r\n\r\nThe main goal of this talk is to provide pragmatic real-life examples, about how to achieve those things.",
                        "day": "2022-07-15",
                        "time": 715,
                        "endTime": 760,
                        "audience": "beginner",
                        "rooms": [
                            "Wicklow Hall 1"
                        ],
                        "slug": "leading-growing-software-teams",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "GLMZDC",
                                "name": "Radoslav Georgiev",
                                "biography": "Generalist. A multi-disciplinary problem solver & a technical team lead.\r\n\r\nCurrently leading & growing teams at HackSoft.\r\n\r\nA programmer from ~10 years, studied Computer Science in the Faculty of Mathematics and Informatics, Sofia University.\r\n\r\nFounder and CEO of HackSoft (Sofia based software company with main focus in Python, Django and Scala) and HackBulgaria (Programming courses, based in Sofia / Bulgaria with main focus of getting the students ready for their first job - either as an intern or a junior developer. Mainly focused in Python and Java)\r\n\r\nAlso doing a lot of teaching - Functional Programming classes (Racket / Haskell) @Faculty of Mathematics and Informatics , Programming with Python and Django @HackBulgaria.\r\n\r\nGitHub - https://github.com/RadoRado/",
                                "avatar": "https://program.europython.eu/media/avatars/Radoslav_HackSoft_team_AiYbuH9.jpg",
                                "slug": "radoslav-georgiev",
                                "affiliation": "HackSoft",
                                "homepage": "https://www.hacksoft.io/",
                                "twitter": "@Rado_g"
                            }
                        ],
                        "start": "2022-07-15T11:55:00+01:00",
                        "end": "2022-07-15T12:40:00+01:00"
                    },
                    {
                        "id": "HE98XH",
                        "title": "Machine Translation engines evaluation framework",
                        "duration": 30,
                        "abstract": "As an engineers in a ML R&D department of large healthcare enterprise company we were presented with the task to evaluate several Machine Translation engines and choose the one best suited for our corporate needs. To do that we created extendable Python-based framework that allowed us to easily plug-in different Machine Translation engines and compare them across large variety of test datasets with a unified set of quality metrics. Our goal from the start was to create universal MT evaluation framework, that will be useful not only for healthcare domain, but to a wider community as well.\r\n\r\nAt this talk we will present our evaluation framework an will do a walk-through of its capabilities. We also cover how it can be extended to new MT engines, new test datasets and new language pairs. We will also present our evaluation results for several state-of-the-art machine translation engines, both open-source and cloud-based.\r\n\r\nAll the source code of our framework will be published in open-source by the time of the talk.",
                        "day": "2022-07-15",
                        "time": 715,
                        "endTime": 745,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 1"
                        ],
                        "slug": "machine-translation-engines-evaluation-framework",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "GYFSQB",
                                "name": "Anton Masalovich",
                                "biography": "Machine learning scientist and engineering manager with 15+ years of experience mostly focused on Natural Language Processing, Machine Translation and Document Recognition.\r\nEx-ABBYY, ex-Microsoft, currently working in a machine learning R&D department of a  large healthcare organization. Have a lot of experience of transforming state-of-the-art ML ideas to actual product features.",
                                "avatar": None,
                                "slug": "anton-masalovich",
                                "affiliation": "Optum",
                                "homepage": None,
                                "twitter": None
                            },
                            {
                                "code": "LZRDNM",
                                "name": "Sahil Manchanda",
                                "biography": None,
                                "avatar": None,
                                "slug": "sahil-manchanda",
                                "affiliation": "Optum",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-15T11:55:00+01:00",
                        "end": "2022-07-15T12:25:00+01:00"
                    },
                    {
                        "id": "LLC3KD",
                        "title": "Game Development with CircuitPython",
                        "duration": 45,
                        "abstract": "With a large selection of handheld devices running CircuitPython, it's natural to want to make games for them. But where to start? What are the options available for the hardware, the libraries and other resources? And how do you use all of that? This talk aims to give a gentle introduction for everyone.",
                        "day": "2022-07-15",
                        "time": 715,
                        "endTime": 760,
                        "audience": "beginner",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "game-development-with-circuitpython",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "CSLXTY",
                                "name": "Radomir Dopieralski",
                                "biography": "A Python programmer by day, an electronics hobbyist by night. Building spider robots, hand-held game consoles, ergonomic keyboards and all kinds of gadgets. Very much into CircuitPython.",
                                "avatar": "https://program.europython.eu/media/avatars/gogles-big_OCjYWs4.jpg",
                                "slug": "radomir-dopieralski",
                                "affiliation": "RedHat",
                                "homepage": "dopieralski.pl",
                                "twitter": "deshipu"
                            }
                        ],
                        "start": "2022-07-15T11:55:00+01:00",
                        "end": "2022-07-15T12:40:00+01:00"
                    },
                    {
                        "id": "MBJUKF",
                        "title": "Work in Progress: Implementing PEP 458 to Secure PyPI downloads",
                        "duration": 30,
                        "abstract": "[PEP 458](https://peps.python.org/pep-0458/) uses cryptographic signing on PyPI to protect Python packages against attackers. In this talk we will share our lessons learned from the ongoing implementation work in PyPI/Warehouse with the Python community. How does PEP 458 work and what is TUF? What protection can it offer now and what does it enable in the future? And how am I affected as a Python developer and as a user?",
                        "day": "2022-07-15",
                        "time": 715,
                        "endTime": 745,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey B"
                        ],
                        "slug": "work-in-progress-implementing-pep-458-to-secure-pypi-downloads",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "ANZZRH",
                                "name": "Kairo de Araujo",
                                "biography": "I am an Open Source Software Engineer at VMware Inc, a staff member of the VMware Open Source Program Office (OSPO), working on the Security Supply Chain team.\r\nCurrently, I am focused on PyPI.org, Python-TUF, and some contributions to Tern Tools.\r\nAs a Software Engineer, I have contributed to Open Source and writing software since 2013.\r\nI am a former system engineer; however, I use these technologies daily. I have long experience in Infrastructures such as Networking, Cloud, Virtualization, Storage Area Networks, and Storage Disks.\r\nI have worked for IBM, ING, and Forescout in the past.",
                                "avatar": "https://program.europython.eu/media/avatars/Kairo_de_Araujo_y22uEvQ.jpg",
                                "slug": "kairo-de-araujo",
                                "affiliation": "VMware",
                                "homepage": "http://kairo.dev",
                                "twitter": "@kairoaraujo"
                            },
                            {
                                "code": "H3JGWN",
                                "name": "Lukas Pühringer",
                                "biography": "Lukas Pühringer is a research scholar and software developer at the NYU Center for Cyber Security (CCS), where he leads the development of The Update Framework (TUF), and has been co-maintaining several of Prof. Justin Cappos’ software projects, most notably the supply chain security framework in-toto. Lukas also supervises students and gives talks about TUF and in-toto.",
                                "avatar": None,
                                "slug": "lukas-puhringer",
                                "affiliation": "NYU",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-15T11:55:00+01:00",
                        "end": "2022-07-15T12:25:00+01:00"
                    },
                    {
                        "id": "MMWYWZ",
                        "title": "Applications of Python in Computational Chemistry and Material Design",
                        "duration": 45,
                        "abstract": "Computational chemistry is the branch of chemistry that studies chemical systems through simulation and involves HPC architecture and software packages. Python has become an integral part of computational modelling of materials in recent years, with development of packages such as the Atomic Simulation Environment (ASE) which is a set of modules for manipulating, running and visualising atomic simulation. Furthermore, ASE integrates seamlessly with many electronic structure software packages, used for calculating the energy and properties of systems based on some level of theory, e.g Density Functional Theory (DFT). Moreover, the combination with other Python packages that integrate with ASE provide an ecosystem for atomic simulations. Packages such as CatLearn, a machine-learning approach used for calculating energies needed for reactions, along with Phonopy and FHI-vibes, both are for studying lattice dynamics of materials, to name a few, provide a comprehensive toolkit for the computational study of materials and chemical systems\r\n\r\nIn our research, such approaches are essential to further our understanding of materials and chemical processes, and of particular interest are materials for green and sustainable processes, such as catalysts used to produce fossil fuel alternatives. In this regard, as Python software becomes increasingly popular for the simulation and study of materials, it also provides the tools and methods needed for tackling some of the challenges of today",
                        "day": "2022-07-15",
                        "time": 715,
                        "endTime": 760,
                        "audience": "",
                        "rooms": [
                            "Forum"
                        ],
                        "slug": "applications-of-python-in-computational-chemistry-and-material-design",
                        "type": "poster",
                        "speakers": [
                            {
                                "code": "9W9CWW",
                                "name": "Owain Beynon",
                                "biography": "PhD Student in Computational Chemistry at Cardiff University. \r\nResearch interests: software development, material science, catalysis, solid state physics.",
                                "avatar": None,
                                "slug": "owain-beynon",
                                "affiliation": "Cardiff University",
                                "homepage": "https://www.cardiff.ac.uk/",
                                "twitter": "@owainbeynon"
                            }
                        ],
                        "start": "2022-07-15T11:55:00+01:00",
                        "end": "2022-07-15T12:55:00+01:00"
                    },
                    {
                        "id": "PQADBJ",
                        "title": "Unfolding the paper windmills",
                        "duration": 30,
                        "abstract": "Research is done on the shoulders of giants. Luckily and unluckily, those giants spoke paper-English and documented their achievements kind of publicly so we could advance the science. \r\n\r\nIn this talk, we will dissect the structure of a paper, looking for the essential points that will help us understand it and implement it. Following we will get our hands dirty and implement the paper using Python. \r\nIn particular, we will dive into the seminal paper \"Attention is all you need\" and implement a transformer using JAX.\r\n\r\nThe key takeaways from this talk are:\r\n - Demystify academic reading.\r\n - Understand the Transformer architecture.\r\n - An introduction to the JAX ecosystem.",
                        "day": "2022-07-15",
                        "time": 715,
                        "endTime": 745,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 2"
                        ],
                        "slug": "unfolding-the-paper-windmills",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "7T3KC8",
                                "name": "Mai Giménez",
                                "biography": "Mai Giménez is a research engineer working at Deepmind. She holds a PhD in natural language processing, and her main research interest is in language and the sociotechnical impacts of these models in the real world.\r\nShe's a former board member of the Spanish Python Association, helped organise several PyConES conferences and is a proud member of the Pyladies.",
                                "avatar": "https://program.europython.eu/media/avatars/image_iYEZORj.png",
                                "slug": "mai-gimenez",
                                "affiliation": "Deepmind",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-15T11:55:00+01:00",
                        "end": "2022-07-15T12:25:00+01:00"
                    },
                    {
                        "id": "TE7K7D",
                        "title": "Clean Architectures in Python",
                        "duration": 45,
                        "abstract": "A brief talk that introduces software developers to the idea of \"clean architecture\" and discusses how to reduce coupling between parts of a software system through well-known strategies such as abstraction and inversion of control.",
                        "day": "2022-07-15",
                        "time": 715,
                        "endTime": 760,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey A"
                        ],
                        "slug": "clean-architectures-in-python",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "7BS3PU",
                                "name": "Leonardo Giordani",
                                "biography": "Born in 1977 together with Star Wars, bash, Apple ][, Dire Straits, The Silmarillion, and many other great things.\r\n\r\nI started coding in April 1987 on a Sinclair ZX Spectrum. I then moved to MS-DOS PCs and in 1996 I started using Linux and became interested in operating system internals. I love software architectures, algorithms, mathematics and cryptography.\r\n\r\nI’m mainly interested in open source software. I like both the theoretical and practical aspects of computer science.\r\n\r\nI am currently working as a contractor DevOps and Python developer while I design a DevOps bootcamp that I will run in London from October 2022.\r\n\r\nFrom 2013 I blog some technical thoughts at http://thedigitalcatonline.com.\r\n\r\nIn 2018 I published the free book “Clean Architectures in Python” http://bit.ly/getpycabook",
                                "avatar": "https://program.europython.eu/media/avatars/Avatar400x400_cuVmtE6.jpg",
                                "slug": "leonardo-giordani",
                                "affiliation": "The Digital Cat Services",
                                "homepage": "https://www.thedigitalcatonline.com/",
                                "twitter": "@tw_lgiordani"
                            }
                        ],
                        "start": "2022-07-15T11:55:00+01:00",
                        "end": "2022-07-15T12:40:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 780,
                "title": "Lunch Break",
                "duration": 60,
                "type": "break"
            },
            {
                "time": 840,
                "duration": 30,
                "sessions": [
                    {
                        "id": "8RH3BC",
                        "title": "Saving Lives with Predictive Geo - AI",
                        "duration": 30,
                        "abstract": "Leveraging geospatial Python libraries to understand and predict High-risk houses during cyclone-induced floods in urban areas considering historical openly available satellite images and urban morphological data.\r\n\r\nAssigning a flood risk score to each individual house near the coastal regions is a challenge. Also, as the land characteristics vary based on different geographical locations, prepare for emergencies on demand.    ​\r\n\r\n​",
                        "day": "2022-07-15",
                        "time": 840,
                        "endTime": 870,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 2"
                        ],
                        "slug": "saving-lives-with-predictive-geo-ai",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "33UKLN",
                                "name": "Sumedh Ghatage",
                                "biography": "Sumedh Ghatage is an Associate Lead Data Scientist (Geospatial) at Gramener. He has worked on various smart city initiatives including sectors such as environmental resource management, location intelligence, and disaster management projects.\r\n\r\nHe drives a community called “Geospatial Awareness Hub” which helps enable Education, Employment, and Business to foster the growth and awareness of the Geospatial Industry",
                                "avatar": "https://program.europython.eu/media/avatars/profile-pic_T1gCApf.png",
                                "slug": "sumedh-ghatage",
                                "affiliation": "Gramener",
                                "homepage": "https://gramener.com/",
                                "twitter": "@GhatageSumedh"
                            }
                        ],
                        "start": "2022-07-15T14:00:00+01:00",
                        "end": "2022-07-15T14:30:00+01:00"
                    },
                    {
                        "id": "9EH9PG",
                        "title": "Packaging security with Nix",
                        "duration": 30,
                        "abstract": "Managing securely dependencies is becoming an increasing concern of the industry. Here, we showcase how Nix, a functional-oriented package manager, can get us very far and close class of vulnerabilities that PyPI / pip had in the past, e.g. rogue PyPI packages that steals personal data.",
                        "day": "2022-07-15",
                        "time": 840,
                        "endTime": 870,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey A"
                        ],
                        "slug": "packaging-security-with-nix",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "ADBNZ8",
                                "name": "Ryan Lahfa",
                                "biography": "FOSS developer, Nix expert, software engineering expert with a love for formal methods and mathematics.",
                                "avatar": None,
                                "slug": "ryan-lahfa",
                                "affiliation": "French Ministry of Justice / École normale supérieure d'Ulm",
                                "homepage": "https://ryan.lahfa.xyz/about-me.html",
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-15T14:00:00+01:00",
                        "end": "2022-07-15T14:30:00+01:00"
                    },
                    {
                        "id": "QJDCYS",
                        "title": "Dr. Jekyll & Mr. Hyde - transition from developer to manager without going crazy or becoming evil",
                        "duration": 30,
                        "abstract": "In the career of many developers, there comes the point of deciding \"what next?\". The typical two choices are- to stay on the technical path and pursue the way of a software architect or take a leap of faith and jump to a people management role. In my talk, I'll show you the pros, cons, and challenges of pursuing the latter.",
                        "day": "2022-07-15",
                        "time": 840,
                        "endTime": 870,
                        "audience": "beginner",
                        "rooms": [
                            "Wicklow Hall 1"
                        ],
                        "slug": "dr-jekyll-mr-hyde-transition-from-developer-to-manager-without-going-crazy-or-becoming-evil",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "8B79FL",
                                "name": "Jakub Paczkowski",
                                "biography": "Python development enthusiast for the last 11 years, currently working as Director of Engineering at SpotOn. I love clean and straightforward solutions, focused on usability and robustness. I am privately a motorcycling enthusiast in summer and squash lover in winter.",
                                "avatar": "https://program.europython.eu/media/avatars/T02G0JQBC-UUTHKAS8N-5842edf034ff-512_JnL4JO5.jpeg",
                                "slug": "jakub-paczkowski",
                                "affiliation": "SpotOn",
                                "homepage": "https://www.spoton.com/",
                                "twitter": "jpaczkowski"
                            }
                        ],
                        "start": "2022-07-15T14:00:00+01:00",
                        "end": "2022-07-15T14:30:00+01:00"
                    },
                    {
                        "id": "QYRKGA",
                        "title": "Education Panel",
                        "duration": 60,
                        "abstract": "Teaching Python: a panel discussion with perspectives from teachers, academics, makers and enthusiasts. Why is Python appealing in education? What tools and resources work well? What can the Python community do to help teachers & policy makers? Join us for an engaging and insightful discussion with a fascinating panel of experts, Dr Keith Quille, Kelly Schuster-Paredes, Chris Reina and Sarah-Jayne Carey.",
                        "day": "2022-07-15",
                        "time": 840,
                        "endTime": 900,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "education-panel",
                        "type": "panel",
                        "speakers": [
                            {
                                "code": "JSBMWD",
                                "name": "Chris Reina",
                                "biography": "Chris Reina has been involved in education since 2002, technology since 1981 and Making since 1971. (You do the maths). He is CCO (Chief Cardboard Officer) of MakerMeet.ie - who deliver Maker-led, project-based S.T.E.A.M. workshops nationwide to primary, secondary, third-level and other institutions.\r\nHe feels passionately that education is the most important thing in the world and that teaching using Maker skills is the most rewarding job there is.\r\nChris loves cats, kayaking, kite-flying, steampunk, pedantic semantics and knowing the meanings of ligatures, aglets, gallibanders and lexiphanic.",
                                "avatar": "https://program.europython.eu/media/avatars/MakerMeetIE_LOGO_M_cheCwbb.png",
                                "slug": "chris-reina",
                                "affiliation": "MakerMeet IE",
                                "homepage": "https://www.makermeet.ie/",
                                "twitter": "@makermeetie  |  @chrisreina"
                            },
                            {
                                "code": "WKRLRJ",
                                "name": "Kelly Schuster - Paredes",
                                "biography": "Kelly Schuster-Paredes is the co-host of the Teaching Python Podcast, a mom, world traveler, and teacher.  Kelly has a Masters in Curriculum, Instruction, and Technology from Nova Southeastern University. She has taught in the UK, Peru, and the USA. Kelly specializes in curriculum design, educational coaching, and curriculum development. She got started with integrating technology in the classroom in 2003, dabbled with app design in File Maker, HTML, Robotics, and now spends most of her time learning more Python. She teaches Python and Computer Science to sixth, seventh and eighth grade students at Pine Crest School in Fort Lauderdale, Florida.",
                                "avatar": "https://program.europython.eu/media/avatars/IMG_3994_utfoOyN.jpeg",
                                "slug": "kelly-schuster-paredes",
                                "affiliation": None,
                                "homepage": None,
                                "twitter": None
                            },
                            {
                                "code": "UAHSLS",
                                "name": "Aimée Fagan",
                                "biography": "Dublin-born, now London-based, Aimée works as Head of Partnerships for the Micro:bit Educational Foundation, a nonprofit with a mission to 'inspire every child to create their best digital future'. The Foundation is behind the tiny-but-mighty BBC micro:bit device, a programmable microcontroller designed for education and loved the world over. Aimée works with a wide range of partners across Europe, Middle East and Africa to ensure students and teachers have the resources and support they need to get hands on with physical computing and block- or text-based programming.",
                                "avatar": "https://program.europython.eu/media/avatars/aimee_linkedin_gzMtlft.jpeg",
                                "slug": "aimee-fagan",
                                "affiliation": "Micro:bit Educational Foundation",
                                "homepage": None,
                                "twitter": "@aimseroo"
                            },
                            {
                                "code": "DUNTUQ",
                                "name": "Keith Quille",
                                "biography": "I am a Senior Lecturer of computing in the School of Enterprise Computing and Digital Transformation in TU Dublin. My primary area of research is in Computer Science Education (with an emphasis on inclusion) which spans third, second and primary level’s. The main focus of my research at third level (including my PhD) was the early identification of students who were at risk of failing or dropping out of Computer Science (using machine learning techniques), as well as interventions to try and reduce attrition rates. My research also focuses on gender and inclusion, with an aim to reduce stereotypes and promote the Computer Science discipline across all levels of education. I am the co-chair of the ACM ITiCSE conference for 2022. My primary area of teaching is in Software Development, (CS1 and CS2: C#, Java and Python) and Applied Machine Learning with Artificial Intelligence. To complement my Computer Science Education research at third level, I have also been significantly involved at primary and second level Computer Science Education, from Governmental level with commissioned research, to co-authoring the leaving certificate book, to formal and informal teacher professional development, to leading a large scale national, primary and second level Computer Science outreach and research programme (http://CSinc.ie). I am also a member of the EU Commission expert group on AI and data in education and training.",
                                "avatar": "https://program.europython.eu/media/avatars/KeithQuille_Lhqkjlv.jpg",
                                "slug": "keith-quille",
                                "affiliation": None,
                                "homepage": None,
                                "twitter": None
                            },
                            {
                                "code": "MYEWSN",
                                "name": "Sarah-Jayne Carey",
                                "biography": None,
                                "avatar": None,
                                "slug": "sarah-jayne-carey",
                                "affiliation": None,
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-15T14:00:00+01:00",
                        "end": "2022-07-15T15:00:00+01:00"
                    },
                    {
                        "id": "SGP3PM",
                        "title": "Rapid prototyping in BBC News with Python and AWS",
                        "duration": 30,
                        "abstract": "BBC News Labs is an innovation team within BBC R&D, working with journalists and production teams to build prototypes to demonstrate and trial new ideas for ways to help journalists or bring new experiences to audiences.\r\n\r\nWorking in short project cycles, it's important for us to be able to quickly build processing pipelines connected to BBC services, test and iterate on ideas and demonstrate working prototypes. We make use of modern cloud technologies to accelerate delivery and reduce friction.\r\n\r\nIn this talk I will share our ways of working, our ideation and research methods, and the tools we use to be able to build, deploy and iterate quickly, the BBC's cloud deployment platform, and our use of serverless AWS services such as Lambda, Step Functions and Serverless Postgres.",
                        "day": "2022-07-15",
                        "time": 840,
                        "endTime": 870,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey B"
                        ],
                        "slug": "rapid-prototyping-in-bbc-news-with-python-and-aws",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "EWRKHR",
                                "name": "Ben Nuttall",
                                "biography": "Ben is a senior software engineer in BBC News Labs, an innovation team in BBC R&D. Ben was previously community manager at Raspberry Pi.",
                                "avatar": "https://program.europython.eu/media/avatars/bennuttall-redhat_m2sZ9q2.jpg",
                                "slug": "ben-nuttall",
                                "affiliation": "BBC News Labs",
                                "homepage": "https://bbcnewslabs.co.uk/",
                                "twitter": "@ben_nuttall"
                            }
                        ],
                        "start": "2022-07-15T14:00:00+01:00",
                        "end": "2022-07-15T14:30:00+01:00"
                    },
                    {
                        "id": "VXJK3Z",
                        "title": "Packaging Python in 2022",
                        "duration": 30,
                        "abstract": "Packaging in Python is one place where the common adage \"There should be one and preferably only one obvious way to do it\" doesn't seem to apply. There are a lot of choices to make when publishing python code. What is absolutely essential and what is optional?",
                        "day": "2022-07-15",
                        "time": 840,
                        "endTime": 870,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 1"
                        ],
                        "slug": "packaging-python-in-2022",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "8YFYD9",
                                "name": "Jeremiah Paige",
                                "biography": "I am a long time Python developer of almost a decade. For most of that time I have used the language to drive systems programs in and on top of C. Python is a diverse and quickly growing community and I love to contribute to it even as I try to keep up. I currently help ActiveState deliver secure, pre-build python projects to enterprise customers and individual developers.",
                                "avatar": "https://program.europython.eu/media/avatars/FB_IMG_1479148712979_7HSytv7.jpg",
                                "slug": "jeremiah-paige",
                                "affiliation": "ActiveState",
                                "homepage": None,
                                "twitter": "@ucodery"
                            }
                        ],
                        "start": "2022-07-15T14:00:00+01:00",
                        "end": "2022-07-15T14:30:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 875,
                "duration": 30,
                "sessions": [
                    {
                        "id": "9PQZKF",
                        "title": "Write Docs Devs Love: Ten Tricks To Level Up Your Tech Writing",
                        "duration": 30,
                        "abstract": "Tutorials, blog posts, and product docs help developers learn. From our favorite tutorials to bad product docs we all consume technical writing. But what makes for good technical writing? In this talk I’ll share 10 tips and tricks to improve your technical writing skills to help your readers succeed",
                        "day": "2022-07-15",
                        "time": 875,
                        "endTime": 905,
                        "audience": "beginner",
                        "rooms": [
                            "Wicklow Hall 1"
                        ],
                        "slug": "write-docs-devs-love-ten-tricks-to-level-up-your-tech-writing",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "SN9SZQ",
                                "name": "Mason Egger",
                                "biography": "Mason is currently a Developer Advocate at Gretel. Prior to his work at Gretel, he was a Developer Advocate at DigitalOcean. Prior to this he was an SRE helping build and maintain a highly available hybrid multicloud PaaS. He is an avid programmer, speaker, educator, and writer. He is an organizer of PyTexas and actively contributes to open source projects. In his spare time he enjoys reading, camping, kayaking, and exploring new places.",
                                "avatar": "https://program.europython.eu/media/avatars/attachment_6_Dicge7M.jpeg",
                                "slug": "mason-egger",
                                "affiliation": "Gretel",
                                "homepage": "https://mason.dev",
                                "twitter": "@masonegger"
                            }
                        ],
                        "start": "2022-07-15T14:35:00+01:00",
                        "end": "2022-07-15T15:05:00+01:00"
                    },
                    {
                        "id": "BADDYW",
                        "title": "Secure Python ML: Automated Security Best Practices in Machine Learning",
                        "duration": 30,
                        "abstract": "In this talk we introduce the conceptual and practical topics around MLSecOps that data science practitioners will be able to adopt, implement and/or advocate for. We will also provide an intuition on key security challenges that arise in production machine learning systems as well as best practices and frameworks that can be adopted to help mitigate security risks in ML models, ML pipelines and ML services.",
                        "day": "2022-07-15",
                        "time": 875,
                        "endTime": 905,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey B"
                        ],
                        "slug": "secure-python-ml-automated-security-best-practices-in-machine-learning",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "EQMGKH",
                                "name": "Alejandro Saucedo",
                                "biography": "Alejandro is the Chief Scientist at the Institute for Ethical AI & Machine Learning, where he contributes to policy and industry standards on the responsible design, development and operation of AI, including the fields of explainability, GPU acceleration, privacy preserving ML and other key machine learning research areas. Alejandro Saucedo is also Director of Engineering at Seldon Technologies, where he leads teams of machine learning engineers focused on the scalability and extensibility of machine learning deployment and monitoring products. With over 10 years of software development experience, Alejandro has held technical leadership positions across hyper-growth scale-ups and has a strong track record building cross-functional teams of software engineers. He is currently appointed as governing council Member-at-Large at the Association for Computing Machinery, and is currently the Chairperson of the GPU Acceleration Kompute Committee at the Linux Foundation.\r\n\r\nLInkedin: https://linkedin.com/in/axsaucedo\r\nTwitter: https://twitter.com/axsaucedo\r\nGithub: https://github.com/axsaucedo\r\nWebsite: https://ethical.institute/",
                                "avatar": "https://program.europython.eu/media/avatars/aletechuk-high-res_m9IQ6Nl.png",
                                "slug": "alejandro-saucedo",
                                "affiliation": "The Institute for Ethical AI & Machine Learning",
                                "homepage": "https://ethical.institute/",
                                "twitter": "axsaucedo"
                            }
                        ],
                        "start": "2022-07-15T14:35:00+01:00",
                        "end": "2022-07-15T15:05:00+01:00"
                    },
                    {
                        "id": "GAVCZ8",
                        "title": "Try Something Different: Explore MicroPython! (a rough guide for newcomers)",
                        "duration": 30,
                        "abstract": "MicroPython - a reimplementation of Python for microcontrollers - is nine years old. How can you find your way in a jungle of tiny chips, circuits, and jumper wires? In this session, we will run through a brief introduction to the world of MicroPython. Beyond the basics, we will explore the projects, tools, and the  community that helped your intrepid speaker to get started as a newcomer.",
                        "day": "2022-07-15",
                        "time": 875,
                        "endTime": 905,
                        "audience": "beginner",
                        "rooms": [
                            "Liffey Hall 2"
                        ],
                        "slug": "try-something-different-explore-micropython-a-rough-guide-for-newcomers",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "HYCU7H",
                                "name": "Andy Piper",
                                "biography": "Developer Advocate. API tinkerer. Friendly DEV.to moderator & community helper. IoT hacker (Eclipse IoT / MQTT). Perpetual student. LEGO fan. Prefer they/them pronouns.",
                                "avatar": "https://www.gravatar.com/avatar/1526dcb784188b422544c6344ef223c2",
                                "slug": "andy-piper",
                                "affiliation": "Twitter",
                                "homepage": "https://andypiper.me",
                                "twitter": "@andypiper"
                            }
                        ],
                        "start": "2022-07-15T14:35:00+01:00",
                        "end": "2022-07-15T15:05:00+01:00"
                    },
                    {
                        "id": "PAXMHN",
                        "title": "Native Packaging of GUI Apps on Windows and macOS",
                        "duration": 30,
                        "abstract": "Distributing Python GUI applications to end users is a challenge: will they need to install Python? If so, which version? If not, how do they install the application? From a random ZIP file? How native does the process feel? Will their system trust your code? For a fluid experience, it needs to be signed and (on macOS) notarized beforehand.\r\n\r\nWelcome to [`pup`](https://pypi.org/project/pup/), the tool that the [Mu Editor](https://codewith.mu/) development team has created to package and distribute it in platform-native formats to Windows and macOS users around the world.\r\n\r\nIn this session I will show how `pup` can be used to package GUI Applications for distribution: natively on Windows and macOS, and in early stages of development for distribution-agnostic Linux artifacts. In short, if it's `pip`-installable it is `pup`-packageable!\r\n\r\nI will then describe the way `pup` works (and how it differs from comparable tools) leading on to a call-for-action moment, where I'll share its current state of development, what's good, what's bad, and where I'd like it to be headed to.\r\n\r\nI'll wrap up the talk with a set of future-looking thoughts that `pup` has helped identify not only on the specifics of CPython's distribution, but also on the Python ecosystem as whole.",
                        "day": "2022-07-15",
                        "time": 875,
                        "endTime": 905,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 1"
                        ],
                        "slug": "native-packaging-of-gui-apps-on-windows-and-macos",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "SS7TTG",
                                "name": "Tiago Montes",
                                "biography": "Freelance Consultant and Trainer with lots of experience on back-end development and architecture, relational and spatial databases, networks, infrastructure, automation, and more.\r\n\r\nMember of the Mu Editor development team.\r\n\r\nWhat matters is learning, having fun, and being and making others happy! :-)",
                                "avatar": "https://program.europython.eu/media/avatars/tiago.montes_cgAAO1f.png",
                                "slug": "tiago-montes",
                                "affiliation": "Independent",
                                "homepage": "https://tmont.es/",
                                "twitter": "@setnomt"
                            }
                        ],
                        "start": "2022-07-15T14:35:00+01:00",
                        "end": "2022-07-15T15:05:00+01:00"
                    },
                    {
                        "id": "TXFX77",
                        "title": "Automated Refactoring Large Python Codebases",
                        "duration": 30,
                        "abstract": "Like many companies with multi-million-line Python codebases, Carta has struggled to adopt best practices like Black formatting and type annotation. The extra work needed to do the right thing competes with the almost overwhelming need for new development, and unclear code ownership and lack of insight into the size and scope of type problems add to the burden. We’ve greatly mitigated these problems by building an automated refactoring pipeline that applies Black formatting and backfills missing types via incremental Github pull requests. Our refactor applications use LibCST and MonkeyType to modify the Python syntax tree and use GitPython/PyGithub to create and manage pull requests. It divides changes into small, easily reviewed pull requests and assigns appropriate code owners to review them. After creating and merging more than 3,000 pull requests, we have fully converted our large codebase to Black format and have added type annotations to more than 50,000 functions. In this talk, you’ll learn to use LibCST to build automated refactoring tools that fix general Python code quality issues at scale and how to use GitPython/PyGithub to automate the code review process.",
                        "day": "2022-07-15",
                        "time": 875,
                        "endTime": 905,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey A"
                        ],
                        "slug": "automated-refactoring-large-python-codebases",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "7DHKEF",
                                "name": "Jimmy Lai",
                                "biography": "Jimmy Lai is a Software Engineer in Instagram and Carta Infrastructure. He love Python and like to share his love in tech talks. His recent interest is automated refactoring and his prior sharing topics include profiling, optimization, asyncio and type annotations.",
                                "avatar": "https://www.gravatar.com/avatar/c7a34d0a6215dd653bfd8b952f3d7cf6",
                                "slug": "jimmy-lai",
                                "affiliation": "Instagram and Carta",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-15T14:35:00+01:00",
                        "end": "2022-07-15T15:05:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 905,
                "title": "Coffee Break",
                "duration": 25,
                "type": "break"
            },
            {
                "time": 930,
                "duration": 30,
                "sessions": [
                    {
                        "id": "3ZGCQR",
                        "title": "Python for Arts, Humanities and Social Sciences",
                        "duration": 30,
                        "abstract": "Computational methods particularly those involving data analytics are now taking root in various humanities disciplines. However, students and researchers working in these disciplines lack the necessary programming proficiency and coding experience . The need then arises to make Python-based computational methods accessible – we present case-studies of how to do this via various Python modules being taught at College of Business in Technological University Dublin and by means of walkthrough of an interdisciplinary social good project called InEire. It comes down to complementing existing quantitative and qualitative methods with methods based on analysis of various types of data specific to the social science problem being solved. We essentially go through the process of building curiosity-driven exploration in social science students via a theoretically driven research question rather than the Python technique itself, and then focusing on the various steps involved in solving that question; and finally boiling it down to a concrete Python-based data analytics methodology. This project-based teaching methodology helped us develop Python skills in newbies eventually leading to a Python-based data analytic skills in students of disciplines other than Computer Science.",
                        "day": "2022-07-15",
                        "time": 930,
                        "endTime": 960,
                        "audience": "beginner",
                        "rooms": [
                            "Liffey A"
                        ],
                        "slug": "python-for-arts-humanities-and-social-sciences",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "7CNJVE",
                                "name": "Arjumand Younus",
                                "biography": "Dr Arjumand Younus is a Research Scientist in Afiniti AI, and a part-time lecturer in Technological University Dublin. Before this appointment, Arjumand has contributed to SFI funded projects during her different post-doctoral positions at CONSUS-UCD and INSIGHT-UCD. She is also serving in the capacity of co-director for Women in Research Ireland which is a volunteer-run registered charity working for better representation of women and under-represented groups in academia.\r\n\r\nArjumand received a joint PhD in Computer Science from National University of Ireland Galway (Ireland) and University of Milano-Bicocca (Italy), MS degree in Computer Science from Korea Advanced Institute of Science and Technology (South Korea), and BS in Computer Science from the University of Karachi (Pakistan). Her research focuses on Machine Learning, Natural Language Processing, and Data Science for Social Good. Arjumand is passionate about the value of artificial intelligence technology to make society better, and at the moment is involved as an academic partner in various AI for Social Good projects.",
                                "avatar": "https://program.europython.eu/media/avatars/headshot_arjumandyounus_KdYrxO6.jpg",
                                "slug": "arjumand-younus",
                                "affiliation": "Afiniti AI",
                                "homepage": "https://arjumandyounus.github.io/",
                                "twitter": "ArjumandYounus"
                            },
                            {
                                "code": "AY9Z73",
                                "name": "Dr. Muhammad Atif Qureshi",
                                "biography": None,
                                "avatar": None,
                                "slug": "dr-muhammad-atif-qureshi",
                                "affiliation": None,
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-15T15:30:00+01:00",
                        "end": "2022-07-15T16:00:00+01:00"
                    },
                    {
                        "id": "7UYS9V",
                        "title": "Demystifying Python’s Internals: Diving into CPython by implementing a pipe operator",
                        "duration": 30,
                        "abstract": "Diving into the CPython source code can feel daunting. Whether you want to start contributing or just want to get a better understanding of Python by exploring its source code, it’s often difficult to know where to start or what you’re missing.\r\n\r\nIn my talk, I will show you around the CPython source code by implementing a new operator, a pipe operator. While doing so, I will discuss core parts of the internals, such as Python’s grammar, its syntax trees, and the underlying logic that will perform the operation. By the end, you will have a good idea of the moving parts involved in core language features.\r\n\r\nI will also take you through the steps necessary to make it all work. I’ll show you how I obtained a copy of the source code, regenerated the parser and token files, and how I compiled my modified version of CPython. I will also write and run tests to help me implement my changes. This should give you a mental framework that helps you while diving into more comprehensive resources, like the excellent [Python Developer’s Guide](https://devguide.python.org/).\r\n\r\nMy talk is aimed at everyone who wants to explore CPython’s internals. You don’t have to be an expert in Python, although some affinity with Python helps with understanding the internals. I will also use C to implement some of the operator logic, but knowledge of C is by no means required. In short, if you’re interested in diving into the CPython source code, this talk is for you.",
                        "day": "2022-07-15",
                        "time": 930,
                        "endTime": 960,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "demystifying-pythons-internals-diving-into-cpython-by-implementing-a-pipe-operator",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "UPWXFZ",
                                "name": "Sebastiaan Zeeff",
                                "biography": "Sebastiaan is a Software Engineer for the Ordina Pythoneers and a Fellow of the Python Software Foundation. He has a passion for teaching Python and writing clean code. Sebastiaan is also active in the Python community, as an owner of Python Discord, open-source contributor, Python educator, and FinAid team lead for EuroPython. As a public speaker, he makes frequent appearances at Python conferences, including various regional PyCons, EuroPython, FOSDEM, and Pyjamas Conf. Sebastiaan lives in The Netherlands.",
                                "avatar": "https://program.europython.eu/media/avatars/photo_cropped_mqQp3VS.jpg",
                                "slug": "sebastiaan-zeeff",
                                "affiliation": "Ordina Pythoneers",
                                "homepage": "https://sebastiaanzeeff.nl",
                                "twitter": "@SebastiaanZeeff"
                            }
                        ],
                        "start": "2022-07-15T15:30:00+01:00",
                        "end": "2022-07-15T16:00:00+01:00"
                    },
                    {
                        "id": "BZL7YY",
                        "title": "How a popular MMORPG made me a better developer",
                        "duration": 30,
                        "abstract": "Have you heard of the critically acclaimed MMORPG Final Fantasy XIV?\r\n\r\nAs an active player since 2015, I've used my \"problem-solving programmer brain\" to analyze my experiences in the world of Eorzea and apply them into important software lessons. From finding solutions to a housing crisis, to tracking cheaters, to networking with the president of Square Enix and applying the principles of (Y)MINASWAN, there's a lot to be learned through triumphs and failures as an MMO gamer. I will also talk about my experiences in the software community as a neurodivergent developer, and how gaming helped me break down barriers.",
                        "day": "2022-07-15",
                        "time": 930,
                        "endTime": 960,
                        "audience": "intermediate",
                        "rooms": [
                            "Wicklow Hall 1"
                        ],
                        "slug": "how-a-popular-mmorpg-made-me-a-better-developer",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "3CVRJD",
                                "name": "Valerie Shoskes",
                                "biography": "A lifelong gamer, cat mom, and abstract thinker who discovered software development by writing scripts with python in her college years and never looked back. She lives in Cleveland, Ohio, with her friends and three cats. She brings her perspective of neurodivergence in coding with her six years of professional development.",
                                "avatar": "https://program.europython.eu/media/avatars/60753290_234917830798883_1901400361449553920_n_wNXvY1e.jpg",
                                "slug": "valerie-shoskes",
                                "affiliation": "Bendyworks",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-15T15:30:00+01:00",
                        "end": "2022-07-15T16:00:00+01:00"
                    },
                    {
                        "id": "JBTGFL",
                        "title": "Build your own Playlist Recommender System with Python using your GDPR Data",
                        "duration": 30,
                        "abstract": "In my talk, we explore our usage data requested according to GDPR and leverage it - together with Spotify’s Web API - to build a personalized playlist recommender system with Python.\r\n\r\nIn 2018, the General Data Protection Regulation (GDPR) became effective in the EU. It sometimes causes data scientists great headaches. But from a consumer and Pythonista point of view this can also be interesting data for exploration. It is very useful for building personalization technology, in particular recommender systems. And there are almost endless ways to use Python for it.\r\nSo, let’s request and use our own data to build a playlist recommender system which infers our music taste from our streaming history and uses it to retrieve songs from our favorites in a new way. We will call it “Your Rediscover Past”, a personalized playlist based on your streaming history and saved songs.",
                        "day": "2022-07-15",
                        "time": 930,
                        "endTime": 960,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 1"
                        ],
                        "slug": "build-your-own-playlist-recommender-system-with-python-using-your-gdpr-data",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "G8LVXX",
                                "name": "Marcel Kurovski",
                                "biography": "Senior Data Scientist and Innovation Lead at inovex\r\nHost of Recsperts - Recommender Systems Experts, the Podcast Show with industry and academia experts in Recommender Systems\r\nBuilding Recommenders and Personalization Solutions with Python for various industries since 5+ years\r\nCreator and Instructor of Python RecSys Training",
                                "avatar": "https://program.europython.eu/media/avatars/gh_avatar_94Jm1CM.png",
                                "slug": "marcel-kurovski",
                                "affiliation": "inovex GmbH",
                                "homepage": "https://www.recsperts.com/",
                                "twitter": "@LivesInAnalogia"
                            }
                        ],
                        "start": "2022-07-15T15:30:00+01:00",
                        "end": "2022-07-15T16:00:00+01:00"
                    },
                    {
                        "id": "TDUFJ9",
                        "title": "From circuit board design to finished product: the hobbyist’s guide to hardware manufacturing",
                        "duration": 30,
                        "abstract": "Ever wondered how hardware is made, or curious about making your own? \r\n\r\nWe share our experiences manufacturing a programmable gamepad for use in IoT/MicroPython workshops. \r\n\r\nWe will cover the entire production process, including:\r\n\r\n- Designing the PCB (Printed Circuit Board)\r\n- Choosing microcontroller and parts\r\n- Finding, ordering and assembling components\r\n- Pulling together firmware, drivers and software\r\n\r\nMistakes were indeed made along the way. Let's turn them into valuable lessons!",
                        "day": "2022-07-15",
                        "time": 930,
                        "endTime": 960,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey Hall 2"
                        ],
                        "slug": "from-circuit-board-design-to-finished-product-the-hobbyists-guide-to-hardware-manufacturing",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "HBPEU7",
                                "name": "Sebastian Roll",
                                "biography": "Sebastian is a consultant, speaker and workshop organizer.\r\n\r\nHe has ten years of experience spanning Oil & Gas, Industrial IT and IoT. His main areas of interest include consulting practices, IoT and Python.",
                                "avatar": "https://program.europython.eu/media/avatars/Sebastian_Roll_lxEMZjv.jpg",
                                "slug": "sebastian-roll",
                                "affiliation": "Retraze",
                                "homepage": None,
                                "twitter": None
                            }
                        ],
                        "start": "2022-07-15T15:30:00+01:00",
                        "end": "2022-07-15T16:00:00+01:00"
                    },
                    {
                        "id": "WVFUYA",
                        "title": "Handling Errors the Graceful Way in Python",
                        "duration": 30,
                        "abstract": "Things rarely go as planned, especially in the world of programming. Errors are the bane of a programmer’s existence. You write an awesome piece of code, are ready to execute it and build a powerful machine learning model, and then poof. Python throws up an unexpected error, ending your hope of quick code execution.",
                        "day": "2022-07-15",
                        "time": 930,
                        "endTime": 960,
                        "audience": "intermediate",
                        "rooms": [
                            "Liffey B"
                        ],
                        "slug": "handling-errors-the-graceful-way-in-python",
                        "type": "talk",
                        "speakers": [
                            {
                                "code": "ND3VKT",
                                "name": "Riya Bansal",
                                "biography": "Riya Bansal is an enthusiastic and passionate Software Engineer at Microsoft with 3 years of experience with enterprise volume licensing products and Microservice technologies. Riya has a lot of experience working with Data Lakes as well. She has worked from small-sized Startups to large MNCs and gained a lot of experience over the years.\r\nShe is a big Pythonista and really interested in writing Python considering the best practices. Apart from that, Riya has also led an amazing Python Community which is a volunteer-driven organization of amazing Pythonistas, enthusiasts, entrepreneurs, researchers, students, and many more with a primary interest in Python.\r\nShe has also been awarded the Google Women Tech makers Scholarship for her leadership skills and impact on the community of women in tech as well.  She has mentored over 10000+ students in the past.",
                                "avatar": "https://program.europython.eu/media/avatars/Me_0z8yiRT.JPG",
                                "slug": "riya-bansal",
                                "affiliation": "Microsoft",
                                "homepage": None,
                                "twitter": "riyabansal1998"
                            }
                        ],
                        "start": "2022-07-15T15:30:00+01:00",
                        "end": "2022-07-15T16:00:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 965,
                "duration": 45,
                "sessions": [
                    {
                        "id": "QPDML3",
                        "title": "Lightning Talks",
                        "duration": 45,
                        "abstract": "A lightning talk (LT) is a short presentation that must not be longer than five minutes.\r\n\r\nTo sign up for a lightning talk, you can put your name on the information board during the conference before the second coffee break. For our online participants, we will set up a separate form or Google sheet for you to put your name and topic in - similar to how we run this at the in-person conference. \r\n\r\nWe will announce the same every day both online and in person.",
                        "day": "2022-07-15",
                        "time": 965,
                        "endTime": 1010,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "lightning-talks",
                        "type": "lightning-talks",
                        "speakers": [],
                        "start": "2022-07-15T16:05:00+01:00",
                        "end": "2022-07-15T16:50:00+01:00"
                    }
                ],
                "type": "timeslot"
            },
            {
                "time": 1015,
                "duration": 30,
                "sessions": [
                    {
                        "id": "7C9GUJ",
                        "title": "Closing Session",
                        "duration": 30,
                        "abstract": "Closing Session Closing Session Closing Session Closing Session Closing Session Closing Session Closing Session Closing Session Closing Session\r\nClosing Session Closing Session Closing Session Closing Session Closing Session Closing Session Closing Session Closing Session Closing Session\r\nClosing Session Closing Session Closing Session Closing Session Closing Session Closing Session Closing Session Closing Session Closing Session",
                        "day": "2022-07-15",
                        "time": 1015,
                        "endTime": 1045,
                        "audience": "intermediate",
                        "rooms": [
                            "The Auditorium"
                        ],
                        "slug": "closing-session",
                        "type": "",
                        "speakers": [],
                        "start": "2022-07-15T16:55:00+01:00",
                        "end": "2022-07-15T17:25:00+01:00"
                    }
                ],
                "type": "timeslot"
            }
        ],
        "rooms": [
            "The Auditorium",
            "Wicklow Hall 1",
            "Liffey A",
            "Liffey B",
            "Liffey Hall 1",
            "Liffey Hall 2",
            "Forum"
        ]
    },
    "dayType": "Talks"
}

def short_schedule(d1):
  return [[{"title": sess['slug'], "start": sess['start'], "room": sess['rooms'][0]} for sess in sessions] for sessions in [s['sessions'] for s in d1["schedule"]["slots"] if 'sessions' in s]]

def write_csv(csv_file, day_sched):
  with open(csv_file, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for sched in day_sched:
      spamwriter.writerow([":".join(sched[0]["start"].split("T")[1].split(":")[:2])] + [s["title"] + f" [{s['room']}]" for s in sched])

write_csv("07-13.csv", short_schedule(d1))
write_csv("07-14.csv", short_schedule(d2))
write_csv("07-15.csv", short_schedule(d3))
