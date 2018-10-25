# Alfheim Project

Build status: 
[![Build Status](https://travis-ci.org/kubixservice/ragnarok.svg?branch=master)](https://travis-ci.org/kubixservice/ragnarok)


# Table of Contents
* [What is Alfheim Project?](#what-is-alfheim-project)
* [Helpful Links](#helpful-links)
* [Prerequisites](#prerequisites)
* [How do I get started?](#how-do-i-get-started)
* [Todos](#todos)
* [Contributors](#contributors)


## What is Alfheim Project?
Alfheim Project is a Control Panel for a robust Massively Multiplayer Online Role Playing Game (MMORPG) Ragnarok Online. Written in Python. The project supports two biggest open-source Ragnarok Online emulators:
* [Hercules](https://github.com/HerculesWS/Hercules)
* [rAthena](https://github.com/rathena/rathena)

## Helpful Links
* [Discord Server](https://discord.gg/hbXgkxV)
* [API documentation](https://app.swaggerhub.com/apis/alfheimproject/alfheimprojectAPI/1.0.0)
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)

## Todos
* Multilanguage support
* Web vending database endpoint
* Web itemdb/mobdb endpoint


## Prerequisites
Before installing Alfheim Project, you will need to install certain tools and applications. This differs between the varying Operating Systems available, so the following list is broken down into Windows and Unix (incl. Linux) prerequisites.

#### Windows
* [Python 3.6+](https://www.python.org/downloads/)
* [MySQL server](https://dev.mysql.com/downloads/windows/)
* [MySQL client](https://dev.mysql.com/downloads/workbench/) (not required, you can use cmd or other shell)
* [GIT](https://git-scm.com/download/win)

#### Unix/Linux/BSD (names of packages may require specific version numbers on certain distributions) current links are for Ubuntu.
* [Python 3.6+](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04)
* [MySQL server](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-16-04)
* [GIT](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-16-04)
* libmysqlclient (``mysql-devel``)
* In additional you may need (``python3-dev``) package

## How do I get started?
This section is a very brief set of installation instructions. For more concise guides relevant to your Operation System, please refer to the Wiki (``not completed section!``).
#### Windows
* Install the prerequisites.
* Clone `Alfheim Project` repository (see [GitHub](https://github.com/kubixservice/ragnarok)) using a git client, into a new folder.
* Configure `MySQL` server if not already installed
* Complete [this](#configure-alfheim-project) section

#### Unix
* Install the prerequisites.
* Clone `Alfheim Project` repository (see [GitHub](https://github.com/kubixservice/ragnarok)) using a git client, into a new folder.
* Configure `MySQL` server if not already installed
* Install additional prerequisites if needed (``sudo apt-get install python3-dev``, ``sudo apt-get install libmysqlclient-dev libmysqld-dev`` for ``Ubuntu``)
* Complete [this](#configure-alfheim-project) section

##### Configure Alfheim Project
* Run ``cd path/to/project``
* Run ``travis.sh``
* Open and configure ``alfheimproject/conf/config.json``
* Open and configure ``alfheimproject/conf/secrets.json``
* Open and configure ``alfheimproject/conf/donations.json``
* Run ``python3 manage.py verify_setup`` and follow instructions
* Run ``python3 manage.py migrate``
* Run ``python3 manage.py runserver HOST:PORT``

If you're having problems with starting Alfheim Project, the first thing you should do is check what's happening on your consoles. More often that not, all support issues can be solved simply by looking at the error messages given.
## Contributors
* [kubix](https://github.com/kubixservice)
* [outofgamut](https://github.com/outofgamut)
* [Arnoldicus](https://github.com/Arnoldicus)
