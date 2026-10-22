from __future__ import annotations

from typing import TYPE_CHECKING

from entidades.base import Base
from entidades.validaciones import validar_entero_positivo

if TYPE_CHECKING:
    from entidades.producto import Producto


class DetallePedido(Base):
    """Línea de un pedido. Composición: SOLO Pedido crea DetallePedido
    (desde Pedido.agregar_detalle); el detalle nace y muere con su pedido.

    El precio unitario se copia del producto al crear el detalle, así el
    subtotal no cambia si después se edita el precio del producto.
    """

    def __init__(self, cantidad: int, producto: Producto) -> None:
        super().__init__()
        self.__producto: Producto = producto
        self.__precio_unitario: float = producto.precio
        self.cantidad = cantidad  # el setter valida y calcula el subtotal

    @property
    def producto(self) -> Producto:
        return self.__producto

    @property
    def precio_unitario(self) -> float:
        return self.__precio_unitario

    @property
    def cantidad(self) -> int:
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, valor: int) -> None:
        """Valida > 0 y recalcula el subtotal. El control de stock lo hace
        Pedido.agregar_detalle (porque depende del total pedido)."""
        self.__cantidad = validar_entero_positivo(valor, "cantidad")
        self.__subtotal: float = self.__cantidad * self.__precio_unitario

    @property
    def subtotal(self) -> float:
        return self.__subtotal

    def __str__(self) -> str:
        # TODO: línea con producto, cantidad, precio unitario y subtotal. Ej:
        #   "Muzzarella x2 ($8500.00 c/u) = $17000.00"
        raise NotImplementedError("DetallePedido.__str__")
