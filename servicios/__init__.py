"""Servicios: un servicio por entidad + el contenedor que los agrupa."""

from dataclasses import dataclass

from servicios.categoria_servicio import CategoriaServicio
from servicios.pedido_servicio import PedidoServicio
from servicios.producto_servicio import ProductoServicio
from servicios.usuario_servicio import UsuarioServicio


@dataclass
class Servicios:
    """Agrupa los servicios para pasarlos juntos desde main() a los menús
    (así no hay variables globales)."""

    categorias: CategoriaServicio
    productos: ProductoServicio
    usuarios: UsuarioServicio
    pedidos: PedidoServicio

    @classmethod
    def crear(cls) -> "Servicios":
        categorias = CategoriaServicio()
        productos = ProductoServicio(categorias)
        usuarios = UsuarioServicio()
        pedidos = PedidoServicio(usuarios, productos)
        return cls(categorias, productos, usuarios, pedidos)


__all__ = [
    "CategoriaServicio",
    "PedidoServicio",
    "ProductoServicio",
    "Servicios",
    "UsuarioServicio",
]
