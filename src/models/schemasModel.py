from pydantic import BaseModel, EmailStr, Field

class UsuarioSchema(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50)
    apellido: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)
    telefono: str = Field(..., pattern=r'^\d{10}$')