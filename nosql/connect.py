import psycopg2
from psycopg2 import Error
def connect():
    try:
        connection = psycopg2.connect(user="admin",
                                    password="csc@123A",
                                    host="localhost",
                                    port="5555",
                                    database="DNS Center")
        
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    return connection.cursor()

connect()
