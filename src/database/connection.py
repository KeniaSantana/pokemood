import mysql.connector

class Database:
    def get_connection(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pokemood"
        )