
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="rehanais2cool",
        database="taskmanagerdb"
    )
