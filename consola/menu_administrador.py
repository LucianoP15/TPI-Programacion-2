from consola.menu import Menu
from consola.secciones.categorias import submenu_categorias
from consola.secciones.pedidos import submenu_pedidos
from consola.secciones.productos import submenu_productos
from consola.secciones.usuarios import submenu_usuarios
from entidades import Usuario
from servicios import Servicios


class MenuAdministrador(Menu):
    """Menú completo de gestión (ADMIN)."""

    def __init__(self, usuario: Usuario, servicios: Servicios) -> None:
        super().__init__(usuario)
        self._servicios = servicios

    def mostrar(self) -> bool:
        s = self._servicios
        return self._correr_menu_principal(
            "FOOD STORE – ADMINISTRADOR",
            {
                "1": ("Categorías", lambda: submenu_categorias(s.categorias)),
                "2": ("Productos", lambda: submenu_productos(s.productos, s.categorias)),
                "3": ("Usuarios", lambda: submenu_usuarios(s.usuarios, self._usuario)),
                "4": ("Pedidos", lambda: submenu_pedidos(s.pedidos, s.usuarios, s.productos)),
            },
        )
