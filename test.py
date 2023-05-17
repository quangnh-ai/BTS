from sqlalchemy import create_engine
import pymysql

connection = pymysql.connect(
    host="localhost",
    user="user",
    password="password",
    db="BTS"
)

cursor = connection.cc