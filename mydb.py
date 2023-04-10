# setting up mysql

import mysql.connector

data_base = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '@prettyflacko2k2',

)

# prepare a cursor object
cursor_object = data_base.cursor()

# create the database .
cursor_object.execute("CREATE DATABASE Flackodatabase")

