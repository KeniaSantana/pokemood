from models.usuarioModel import UsuarioModel
from models.schemasModel import UsuarioSchema
from pydantic import ValidationError


class AuthController:

    def __init__(self):

        self.model = UsuarioModel()

    def registrar_usuario(
        self,
        nombre,
        apellido,
        correo,
        password,
        telefono
    ):

        try:

            nuevo_usuario = UsuarioSchema(
                nombre=nombre,
                apellido=apellido,
                correo=correo,
                password=password,
                telefono=telefono
            )

            success = self.model.registrar(nuevo_usuario)

            if success:

                return True, " Usuario creado correctamente"

            return False, " El correo ya existe"

        except ValidationError as e:

            errores = e.errors()

            if errores:
                return False, errores[0]["msg"]

            return False, "Datos inválidos"

        except Exception as e:

            return False, f" Error: {str(e)}"

    def login(self, correo, password):

        try:

            user = self.model.validar_login(
                correo,
                password
            )

            if user:

                return user, "Inicio correcto"

            return None, " Credenciales incorrectas"

        except Exception as e:

            return None, f"Error: {str(e)}"