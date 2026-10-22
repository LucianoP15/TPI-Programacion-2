from consola.menu import Menu
from consola.menu_administrador import MenuAdministrador
from consola.menu_cliente import MenuCliente
from entidades import Usuario
from enums import Rol
from servicios import Servicios


def crear_menu(usuario: Usuario, servicios: Servicios) -> Menu:
    """ÚNICO lugar del programa donde se pregunta por el rol.
    Agregar un rol nuevo = agregar una subclase de Menu y una línea acá."""
    if usuario.rol == Rol.ADMIN:
        return MenuAdministrador(usuario, servicios)
    return MenuCliente(usuario, servicios.categorias, servicios.productos, servicios.pedidos)
