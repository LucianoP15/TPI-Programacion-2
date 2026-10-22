from entidades import Pedido, Usuario
from enums import Estado, FormaPago
from servicios.producto_servicio import ProductoServicio
from servicios.servicio_base import ServicioBase
from servicios.usuario_servicio import UsuarioServicio


class PedidoServicio(ServicioBase[Pedido]):
    _nombre_entidad = "pedido"

    def __init__(
        self,
        usuario_servicio: UsuarioServicio,
        producto_servicio: ProductoServicio,
    ) -> None:
        super().__init__()
        self._usuario_servicio = usuario_servicio
        self._producto_servicio = producto_servicio

    # ---------- auxiliares de stock ----------
    def _descontar_stock(self, pedido: Pedido) -> None:
        for detalle in pedido.detalles:
            detalle.producto.descontar_stock(detalle.cantidad)

    def _devolver_stock(self, pedido: Pedido) -> None:
        for detalle in pedido.detalles:
            detalle.producto.reponer_stock(detalle.cantidad)

    # ---------- HU-PED-02 ----------
    def crear(
        self,
        usuario_id: int,
        forma_pago: FormaPago,
        items: list[tuple[int, int]],
    ) -> Pedido:
        """items = lista de (producto_id, cantidad) que juntó la consola."""
        # TODO:
        # 1. Si items está vacío -> DatoInvalidoError("El pedido necesita al menos un producto").
        # 2. usuario = self._usuario_servicio.buscar_por_id(usuario_id).
        # 3. pedido = Pedido(usuario, forma_pago)  (arranca PENDIENTE, fecha de hoy).
        # 4. Por cada (producto_id, cantidad):
        #       producto = self._producto_servicio.buscar_por_id(producto_id)
        #       pedido.agregar_detalle(cantidad, producto)   <- OBLIGATORIO usarlo
        #    Si algo lanza excepción, se deja propagar: el pedido no se guardó
        #    y todavía no se tocó ningún stock (justo lo que pide la HU).
        # 5. pedido.calcular_total()   <- OBLIGATORIO (interfaz Calculable).
        # 6. self._descontar_stock(pedido), self._agregar(pedido),
        #    usuario.agregar_pedido(pedido) y devolver el pedido.
        raise NotImplementedError("PedidoServicio.crear")

    # ---------- HU-PED-03 ----------
    def cambiar_estado(self, pedido_id: int, nuevo_estado: Estado) -> Pedido:
        # TODO:
        # 1. Buscar por id.
        # 2. pedido.cambiar_estado(nuevo_estado) (valida la transición).
        # 3. Si nuevo_estado es CANCELADO -> self._devolver_stock(pedido).
        # 4. Devolver el pedido.
        raise NotImplementedError("PedidoServicio.cambiar_estado")

    def cambiar_forma_pago(self, pedido_id: int, forma_pago: FormaPago) -> Pedido:
        # TODO: buscar por id; si pedido.esta_cerrado() -> OperacionNoPermitidaError
        # (decisión de grupo, anotarla en el informe); asignar pedido.forma_pago.
        raise NotImplementedError("PedidoServicio.cambiar_forma_pago")

    # ---------- HU-PED-04 ----------
    def eliminar(self, pedido_id: int) -> None:
        # TODO:
        # 1. Buscar por id.
        # 2. Si NO está cerrado (ni TERMINADO ni CANCELADO) -> devolver stock.
        #    (Hacerlo ANTES de eliminar: pedido.detalles filtra los eliminados.)
        # 3. pedido.eliminar() (marca también los detalles).
        raise NotImplementedError("PedidoServicio.eliminar")

    # ---------- HU-PED-05 ----------
    def listar_de_usuario(self, usuario: Usuario) -> list[Pedido]:
        # TODO: pedidos activos cuyo pedido.usuario == usuario.
        raise NotImplementedError("PedidoServicio.listar_de_usuario")

    def buscar_de_usuario(self, pedido_id: int, usuario: Usuario) -> Pedido:
        # TODO: buscar por id; si el pedido es de OTRO usuario lanzar
        # EntidadNoEncontradaError igual que si no existiera (no revelar que existe).
        raise NotImplementedError("PedidoServicio.buscar_de_usuario")
