from entidades import Producto
from servicios.categoria_servicio import CategoriaServicio
from servicios.servicio_base import ServicioBase


class ProductoServicio(ServicioBase[Producto]):
    _nombre_entidad = "producto"

    def __init__(self, categoria_servicio: CategoriaServicio) -> None:
        super().__init__()
        self._categoria_servicio = categoria_servicio

    # ---------- auxiliar ----------
    def listar_por_categoria(self, categoria_id: int) -> list[Producto]:
        """Opcional de HU-PROD-01: productos activos de una categoría."""
        return [p for p in self.listar_activos() if p.categoria.id == categoria_id]

    # ---------- HU-PROD-01 (vista cliente) ----------
    def listar_disponibles(self) -> list[Producto]:
        # TODO: devolver solo los productos que el cliente puede ver
        # (usar producto.esta_a_la_venta()).
        raise NotImplementedError("ProductoServicio.listar_disponibles")

    # ---------- HU-PROD-02 ----------
    def crear(
        self,
        nombre: str,
        descripcion: str,
        precio: float,
        stock: int,
        imagen: str,
        disponible: bool,
        categoria_id: int,
    ) -> Producto:
        # TODO:
        # 1. categoria = self._categoria_servicio.buscar_por_id(categoria_id)
        #    (lanza si no existe o está eliminada).
        # 2. Crear el Producto (los setters validan precio/stock/nombre y
        #    el setter de categoria ya lo agrega a la categoría).
        # 3. self._agregar(producto) y devolverlo.
        raise NotImplementedError("ProductoServicio.crear")

    # ---------- HU-PROD-03 ----------
    def editar(
        self,
        producto_id: int,
        nombre: str | None = None,
        descripcion: str | None = None,
        precio: float | None = None,
        stock: int | None = None,
        imagen: str | None = None,
        disponible: bool | None = None,
        categoria_id: int | None = None,
    ) -> Producto:
        # TODO:
        # 1. producto = self.buscar_por_id(producto_id).
        # 2. Cada parámetro en None = no cambiar.
        # 3. Si viene categoria_id: buscar la categoría nueva con el servicio.
        # 4. Asignar con los setters (validan solos) y devolver el producto.
        raise NotImplementedError("ProductoServicio.editar")

    # ---------- HU-PROD-04 ----------
    def eliminar(self, producto_id: int) -> None:
        # TODO: buscar por id y producto.eliminar().
        # No se toca la lista de la categoría: contar_productos_activos()
        # ya ignora los eliminados, y los pedidos viejos lo siguen mostrando.
        raise NotImplementedError("ProductoServicio.eliminar")
