from ..models.usuarioModel import UsuarioModel
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()
        
    def registrar_usuario(self, nombre, apellido, email, password, telefono):
        try:
            nuevo_usuario = UsuarioSchema(
                nombre=nombre,
                apellido=apellido,
                email=email,
                password=password,
                telefono=telefono
            )
            success = self.model.registrar(nuevo_usuario)
            if success:
                return True, "Usuario creado correctamente"
            else:
                return False, "Error al crear usuario - El email puede existir"
        except ValidationError as e:
            return False, e.errors()[0]['msg']
        except Exception as e:
            return False, f"Error: {str(e)}"

    def login(self, email, password):
        user = self.model.validar_login(email, password)
        
        if user:
            return user, "Inicio correcto"
        else:
            return None, "Credenciales incorrectas"