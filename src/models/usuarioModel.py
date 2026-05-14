from database.connection import Database

class UsuarioModel:
    def __init__(self):
        self.db = Database()

    def login(self, correo, contraseña):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM usuario WHERE correo=%s AND contraseña=%s"
        values = (correo, contraseña)

        cursor.execute(query, values)
        usuario = cursor.fetchone()

        cursor.close()
        conn.close()

        return usuario