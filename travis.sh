#!/bin/sh
echo "
{
  "secret_key": "",
  "db_engine": "",
  "db_host": "",
  "db_username": "",
  "db_password": "",
  "db_database": "",
  "db_port": 0,
  "table_prefix": "",
  "smtp": {
    "email_host": "",
    "email_host_user": "",
    "email_port": 0,
    "email_use_ssl": true,
    "email_host_password": ""
  }
}
" > alfheimproject/conf/secrets.json