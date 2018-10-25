# Alfheim Project
#### A Control Panel for Ragnarok Online private servers

* [API documentation](https://app.swaggerhub.com/apis-docs/alfheimproject/alfheimprojectAPI/1.0.0)
* [Discord](https://discord.gg/hbXgkxV)

[![Build Status](https://travis-ci.org/kubixservice/ragnarok.svg?branch=master)](https://travis-ci.org/kubixservice/ragnarok)

## Requirements
* Python (3.5+)
* MySQL

## Installation (Linux/Windows)
* cd **<projectdir>/alfheimproject/conf/**
* Rename the file _**secrets.example.json**_ to _**secrets.example.json**_
* Rename the file _**config.example.json**_ to _**config.example.json**_
* Rename the file _**donations.example.json**_ to _**donations.example.json**_
* Setup your secrets.json file
* Setup your config.json file
* Setup your donations.json file
* Run **python manage.py migrate**
* Run **python manage.py runserver HOST:PORT** to enable website
* Have fun!