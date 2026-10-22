from entidades import Categoria
from servicios.servicio_base import ServicioBase


class CategoriaServicio(ServicioBase[Categoria]):
    _nombre_entidad = "categoría"

    # ---------- auxiliar ----------
    def existe_nombre(self, nombre: str, excluir_id: int | None = None) -> bool:
        """True si ya hay una categoría activa con ese nombre (sin distinguir
        mayúsculas). excluir_id sirve al editar, para no chocar consigo misma."""
        buscado = nombre.strip().lower()
        return any(
            c.nombre.lower() == buscado and c.id != excluir_id
            for c in self.listar_activos()
        )

    # ---------- HU-CAT-02 ----------
    def crear(self, nombre: str, descripcion: str) -> Categoria:
        # TODO:
        # 1. Si self.existe_nombre(nombre) -> DuplicadoError.
        # 2. Crear Categoria(nombre, descripcion) (el setter valida vacíos).
        # 3. self._agregar(categoria) y devolverla (la consola muestra el id).
        raise NotImplementedError("CategoriaServicio.crear")

    # ---------- HU-CAT-03 ----------
    def editar(
        self,
        categoria_id: int,
        nombre: str | None = None,
        descripcion: str | None = None,
    ) -> Categoria:
        # TODO:
        # 1. categoria = self.buscar_por_id(categoria_id) (lanza si no existe).
        # 2. None = "no cambiar" (el usuario apretó Enter).
        # 3. Si cambia el nombre: validar con existe_nombre(nombre, excluir_id=categoria_id).
        # 4. Asignar con los setters y devolver la categoría.
        # Tip: validar todo ANTES de asignar, para no dejarla a medio editar.
        raise NotImplementedError("CategoriaServicio.editar")

    # ---------- HU-CAT-04 ----------
    def eliminar(self, categoria_id: int) -> None:
        # TODO:
        # 1. Buscar por id.
        # 2. activos = categoria.contar_productos_activos(); si > 0 ->
        #    OperacionNoPermitidaError(f"La categoría tiene {activos} productos activos").
        # 3. categoria.eliminar() (baja lógica).
        raise NotImplementedError("CategoriaServicio.eliminar")
