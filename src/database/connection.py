import mysql.connector
from config.db_config import DB_CONFIG

class Database:
    def get_connection(self):
        try:
            connection = mysql.connector.connect(**DB_CONFIG)
            return connection
        except mysql.connector.Error as err:
            print(f"Error de conexión a la base de datos: {err}")
            return None