# Alfheim Project
#### Control Panel for Ragnarok Online private servers

API Documentation: 

## Requirements
* Python (3.5+)
* MySQL

## Installation (Linux/Windows)
* Create file _**secrets.json**_ at _**alfheimproject/conf**_
##### Paste these lines to your secrets.json
```json
{
  "secret_key": "my_key",  // Generate random key (sha512 preferred)
  "db_engine": "mysql",  // Your DB engine (since herc and rA doesn't support postgres and etc, left mysql here)
  "db_host": "localhost",
  "db_username": "root",
  "db_password": "password",
  "db_database": "database",
  "db_port": 3306,
  "table_prefix": "cp_",
  "smtp": { // smtp settings required if you want to have email confirmation when users register their accounts
    "email_host": "smtp.gmail.com",
    "email_host_user": "your_email@gmail.com",
    "email_port": 465,
    "email_use_ssl": true,
    "email_host_password": "yourpassword"
  }
}
```
* Setup your secrets.json file
* Setup your config.json file
* Run **python manage.py makemigrations**
* Run **python manage.py runserver HOST:PORT** to enable website
