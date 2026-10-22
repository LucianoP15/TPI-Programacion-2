from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, ClassVar

from entidades.base import Base
from entidades.calculable import Calculable
from entidades.detalle_pedido import DetallePedido
from enums import Estado, FormaPago
from excepciones import DatoInvalidoError, OperacionNoPermitidaError

if TYPE_CHECKING:
    from entidades.producto import Producto
    from entidades.usuario import Usuario


class Pedido(Base, Calculable):
    """Pedido de un usuario. N..1 con Usuario, composición 1..N con DetallePedido."""

    TRANSICIONES_VALIDAS: ClassVar[dict[Estado, set[Estado]]] = {
        Estado.PENDIENTE: {Estado.CONFIRMADO, Estado.CANCELADO},
        Estado.CONFIRMADO: {Estado.TERMINADO, Estado.CANCELADO},
        Estado.TERMINADO: set(),
        Estado.CANCELADO: set(),
    }

    def __init__(self, usuario: Usuario, forma_pago: FormaPago) -> None:
        if usuario is None:
            raise OperacionNoPermitidaError("Un pedido necesita un usuario")
        if usuario.eliminado:
            raise OperacionNoPermitidaError("No se puede crear un pedido para un usuario eliminado")
        super().__init__()
        self.__usuario: Usuario = usuario
        self.__fecha: date = date.today()
        self.__estado: Estado = Estado.PENDIENTE
        self.__total: float = 0.0
        self.forma_pago = forma_pago
        self.__detalles: list[DetallePedido] = []

    # ---------- properties ----------
    @property
    def usuario(self) -> Usuario:
        return self.__usuario

    @property
    def fecha(self) -> date:
        return self.__fecha

    @property
    def estado(self) -> Estado:
        return self.__estado

    @property
    def total(self) -> float:
        return self.__total

    @property
    def forma_pago(self) -> FormaPago:
        return self.__forma_pago

    @forma_pago.setter
    def forma_pago(self, valor: FormaPago) -> None:
        if not isinstance(valor, FormaPago):
            raise DatoInvalidoError("Forma de pago inválida")
        self.__forma_pago = valor

    @property
    def detalles(self) -> tuple[DetallePedido, ...]:
        """Tupla: desde afuera no se pueden agregar ni quitar detalles."""
        return tuple(d for d in self.__detalles if not d.eliminado)

    # ---------- auxiliares ----------
    def puede_cambiar_a(self, nuevo: Estado) -> bool:
        return nuevo in self.TRANSICIONES_VALIDAS[self.__estado]

    def esta_cerrado(self) -> bool:
        """TERMINADO o CANCELADO: ya no cambia y no devuelve stock."""
        return self.__estado in (Estado.TERMINADO, Estado.CANCELADO)

    def eliminar(self) -> None:
        """Baja lógica del pedido y de todos sus detalles (composición)."""
        super().eliminar()
        for detalle in self.__detalles:
            detalle.eliminar()

    # ---------- métodos obligatorios (TODO) ----------
    def agregar_detalle(self, cantidad: int, producto: Producto) -> None:
        # TODO:
        # 1. Validar que el producto no esté eliminado ni no-disponible
        #    (si lo está -> OperacionNoPermitidaError).
        # 2. Buscar si ya hay un detalle de ese producto (buscar_detalle_por_producto).
        # 3. Calcular la cantidad total = cantidad existente + nueva y verificar
        #    con producto.tiene_stock(...). Si no alcanza -> StockInsuficienteError.
        #    OJO: acá NO se descuenta stock, eso lo hace PedidoServicio al final
        #    si todo salió bien (HU-PED-02).
        # 4. Si existía: detalle.cantidad = total (el setter recalcula subtotal).
        #    Si no existía: crear DetallePedido(cantidad, producto) y agregarlo
        #    a self.__detalles.
        # 5. Llamar a self.calcular_total().
        raise NotImplementedError("Pedido.agregar_detalle")

    def buscar_detalle_por_producto(self, producto: Producto) -> DetallePedido | None:
        # TODO: recorrer los detalles NO eliminados y devolver el que tenga
        # ese producto (comparar con ==, que compara por id). Si no hay -> None.
        raise NotImplementedError("Pedido.buscar_detalle_por_producto")

    def eliminar_detalle_por_producto(self, producto: Producto) -> None:
        # TODO: buscar el detalle; si no existe -> EntidadNoEncontradaError.
        # Si existe: detalle.eliminar() (baja lógica) y recalcular el total.
        raise NotImplementedError("Pedido.eliminar_detalle_por_producto")

    def calcular_total(self) -> None:
        # TODO (interfaz Calculable): self.__total = suma de los subtotales
        # de los detalles no eliminados.
        raise NotImplementedError("Pedido.calcular_total")

    def cambiar_estado(self, nuevo: Estado) -> None:
        # TODO: si not self.puede_cambiar_a(nuevo) -> OperacionNoPermitidaError
        # con un mensaje tipo "No se puede pasar de TERMINADO a PENDIENTE".
        # Si es válida: self.__estado = nuevo.
        # La devolución de stock al cancelar la hace PedidoServicio.
        raise NotImplementedError("Pedido.cambiar_estado")

    def __str__(self) -> str:
        # TODO: línea con id, usuario (nombre completo), estado, forma de pago,
        # total y fecha (HU-PED-01). Ej:
        #   "[15] Juan Gómez | Pendiente | Efectivo | $17000.00 | 22/10/2026"
        raise NotImplementedError("Pedido.__str__")
