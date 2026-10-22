from enum import Enum


class Rol(Enum):
    """Rol del usuario. Define qué menú ve al iniciar sesión."""

    ADMIN = "Administrador"
    USUARIO = "Cliente"
