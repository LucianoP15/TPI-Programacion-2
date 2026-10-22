from __future__ import annotations

from typing import TYPE_CHECKING

from entidades.base import Base
from entidades.validaciones import (
    validar_entero_no_negativo,
    validar_entero_positivo,
    validar_texto,
)
from excepciones import DatoInvalidoError, PrecioInvalidoError, StockInsuficienteError

if TYPE_CHECKING:
    from entidades.categoria import Categoria


class Producto(Base):
    """Producto del catálogo. Relación N..1 con Categoria."""

    def __init__(
        self,
        nombre: str,
        descripcion: str,
        precio: float,
        stock: int,
        imagen: str,
        disponible: bool,
        categoria: Categoria,
    ) -> None:
        super().__init__()
        self.__categoria: Categoria | None = None
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.imagen = imagen
        self.disponible = disponible
        self.categoria = categoria

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
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, valor: float) -> None:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise PrecioInvalidoError("El precio debe ser numérico")
        if valor < 0:
            raise PrecioInvalidoError("El precio no puede ser negativo")
        self.__precio = float(valor)

    @property
    def stock(self) -> int:
        return self.__stock

    @stock.setter
    def stock(self, valor: int) -> None:
        self.__stock = validar_entero_no_negativo(valor, "stock")

    @property
    def imagen(self) -> str:
        return self.__imagen

    @imagen.setter
    def imagen(self, valor: str) -> None:
        # La imagen es opcional (puede ser ""), solo se exige que sea texto.
        if not isinstance(valor, str):
            raise DatoInvalidoError("La imagen debe ser un texto (ruta o URL)")
        self.__imagen = valor.strip()

    @property
    def disponible(self) -> bool:
        return self.__disponible

    @disponible.setter
    def disponible(self, valor: bool) -> None:
        if not isinstance(valor, bool):
            raise DatoInvalidoError("Disponible debe ser verdadero o falso")
        self.__disponible = valor

    @property
    def categoria(self) -> Categoria:
        assert self.__categoria is not None
        return self.__categoria

    @categoria.setter
    def categoria(self, nueva: Categoria) -> None:
        """Mantiene los dos lados de la relación sincronizados."""
        if nueva is None:
            raise DatoInvalidoError("El producto debe tener una categoría")
        if self.__categoria is not None:
            self.__categoria.quitar_producto(self)
        self.__categoria = nueva
        nueva.agregar_producto(self)

    # ---------- auxiliares de stock ----------
    def tiene_stock(self, cantidad: int) -> bool:
        return cantidad <= self.__stock

    def descontar_stock(self, cantidad: int) -> None:
        validar_entero_positivo(cantidad, "cantidad")
        if cantidad > self.__stock:
            raise StockInsuficienteError(
                f"Stock insuficiente de '{self.nombre}': "
                f"pedido {cantidad}, disponible {self.__stock}"
            )
        self.__stock -= cantidad

    def reponer_stock(self, cantidad: int) -> None:
        validar_entero_positivo(cantidad, "cantidad")
        self.__stock += cantidad

    def esta_a_la_venta(self) -> bool:
        """Lo que ve el cliente: no eliminado, disponible y con stock > 0."""
        return not self.eliminado and self.__disponible and self.__stock > 0

    def __str__(self) -> str:
        # TODO: línea para el listado con id, nombre, precio, stock y
        # nombre de la categoría (HU-PROD-01). Ej:
        #   "[7] Muzzarella | $8500.00 | stock: 10 | Pizzas"
        raise NotImplementedError("Producto.__str__")
