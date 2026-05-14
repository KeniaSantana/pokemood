from models.usuarioModel import UsuarioModel

class AuthController:
    def __init__(self):
        self.usuario_model = UsuarioModel()

    def login(self, correo, contraseña):
        return self.usuario_model.login(correo, contraseña)