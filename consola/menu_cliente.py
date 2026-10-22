from consola.menu import Menu
from consola.secciones.categorias import listar_categorias
from entidades import Usuario
from servicios import CategoriaServicio, PedidoServicio, ProductoServicio


class MenuCliente(Menu):
    """Menú de solo consulta (USUARIO). No ofrece NINGUNA opción que modifique datos."""

    def __init__(
        self,
        usuario: Usuario,
        categoria_servicio: CategoriaServicio,
        producto_servicio: ProductoServicio,
        pedido_servicio: PedidoServicio,
    ) -> None:
        super().__init__(usuario)
        self._categorias = categoria_servicio
        self._productos = producto_servicio
        self._pedidos = pedido_servicio

    def mostrar(self) -> bool:
        return self._correr_menu_principal(
            "FOOD STORE – CLIENTE",
            {
                "1": ("Ver categorías", lambda: listar_categorias(self._categorias)),
                "2": ("Ver productos disponibles", self._ver_productos_disponibles),
                "3": ("Mis pedidos", self._mis_pedidos),
                "4": ("Mis datos", self._mis_datos),
            },
        )

    # ---------- HU-PROD-01 (vista cliente) ----------
    def _ver_productos_disponibles(self) -> None:
        # TODO: mostrar_lista(self._productos.listar_disponibles(),
        #                     "No hay productos disponibles")
        raise NotImplementedError("MenuCliente._ver_productos_disponibles")

    # ---------- HU-PED-05 ----------
    def _mis_pedidos(self) -> None:
        # TODO:
        # 1. Listar self._pedidos.listar_de_usuario(self._usuario).
        #    Si no hay -> informar y volver.
        # 2. Preguntar si quiere ver el detalle de alguno (leer_si_no).
        # 3. Pedir id y usar buscar_de_usuario(id, self._usuario)
        #    (si es de otro usuario lanza EntidadNoEncontradaError).
        # 4. Mostrar cada detalle (producto, cantidad, subtotal) y el total.
        raise NotImplementedError("MenuCliente._mis_pedidos")

    # ---------- HU-USR-05 ----------
    def _mis_datos(self) -> None:
        # TODO: imprimir nombre, apellido, mail, celular y rol de self._usuario.
        # NUNCA la contraseña (igual no hay forma de leerla).
        raise NotImplementedError("MenuCliente._mis_datos")
