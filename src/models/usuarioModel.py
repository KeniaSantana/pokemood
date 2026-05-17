import bcrypt
from database.connection import Database


class UsuarioModel:

    def __init__(self):
        self.db = Database()

    def registrar(self, usuario_data):

        conn = None
        cursor = None

        try:

            conn = self.db.get_connection()

            if conn is None:
                return False

            cursor = conn.cursor(dictionary=True)


            cursor.execute(
                "SELECT id FROM usuarios WHERE correo = %s",
                (usuario_data.email,)
            )

            if cursor.fetchone():
                print("El correo ya existe")
                return False

            # Encriptar contraseña
            hashed_pw = bcrypt.hashpw(
                usuario_data.password.encode("utf-8"),
                bcrypt.gensalt()
            )

            # Insertar usuario
            cursor.execute(
                """
                INSERT INTO usuarios
                (nombre, apellido, correo, password, telefono)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    usuario_data.nombre,
                    usuario_data.apellido,
                    usuario_data.email,
                    hashed_pw.decode("utf-8"),
                    usuario_data.telefono
                )
            )

            conn.commit()

            print(" Usuario registrado")
            return True

        except Exception as e:

            print(f"Error al registrar: {e}")
            return False

        finally:

            if cursor:
                cursor.close()

            if conn:
                conn.close()

    def validar_login(self, correo, password):

        conn = None
        cursor = None

        try:

            conn = self.db.get_connection()

            if conn is None:
                return None

            cursor = conn.cursor(dictionary=True)

            cursor.execute(
                "SELECT * FROM usuarios WHERE correo = %s",
                (correo,)
            )

            user = cursor.fetchone()

            if not user:
                return None

            if bcrypt.checkpw(
                password.encode("utf-8"),
                user["password"].encode("utf-8")
            ):

                print(" Login correcto")
                return user

            return None

        except Exception as err:

            print(f" Error en login: {err}")
            return None

        finally:

            if cursor:
                cursor.close()

            if conn:
                conn.close()

    def login(self, correo, password):
        return self.validar_login(correo, password)