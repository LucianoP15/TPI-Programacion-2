from __future__ import annotations

from typing import TYPE_CHECKING

from entidades.base import Base
from entidades.validaciones import validar_texto

if TYPE_CHECKING:
    from entidades.producto import Producto


class Categoria(Base):
    """Categoría del catálogo. Agregación 1..N con Producto:
    los productos existen por sí mismos, la categoría solo los agrupa."""

    def __init__(self, nombre: str, descripcion: str) -> None:
        super().__init__()
        self.nombre = nombre
        self.descripcion = descripcion
        self.__productos: list[Producto] = []

    # ---------- properties ----------
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        self.__nombre = validar_texto(valor, "nombre")

    @property
    def descripcion(self) -> str:
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, valor: str) -> None:
        self.__descripcion = validar_texto(valor, "descripción")

    @property
    def productos(self) -> tuple[Producto, ...]:
        """Copia inmutable: desde afuera no se puede modificar la lista."""
        return tuple(self.__productos)

    # ---------- auxiliares de la agregación ----------
    def agregar_producto(self, producto: Producto) -> None:
        """Lo llama Producto al asignarse esta categoría."""
        if producto not in self.__productos:
            self.__productos.append(producto)

    def quitar_producto(self, producto: Producto) -> None:
        """Lo llama Producto al cambiarse de categoría."""
        if producto in self.__productos:
            self.__productos.remove(producto)

    def contar_productos_activos(self) -> int:
        """Cantidad de productos no eliminados (regla: no se elimina una
        categoría con productos activos)."""
        return sum(1 for p in self.__productos if not p.eliminado)

    def __str__(self) -> str:
        # TODO: devolver una línea para el listado, por ejemplo:
        #   "[3] Pizzas - Pizzas a la piedra"
        # (id, nombre y descripción, según HU-CAT-01)
        raise NotImplementedError("Categoria.__str__")
