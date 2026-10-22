from typing import ClassVar

from entidades import Base
from excepciones import EntidadNoEncontradaError


class ServicioBase[T: Base]:
    """Servicio genérico: guarda la colección y resuelve lo común a todos
    (agregar, listar activos, buscar por id). Cada servicio concreto hereda
    de acá y agrega sus reglas de negocio.

    Los servicios NUNCA usan input() ni print().
    """

    _nombre_entidad: ClassVar[str] = "elemento"

    def __init__(self) -> None:
        self._items: list[T] = []

    def _agregar(self, item: T) -> None:
        self._items.append(item)

    def listar_todos(self) -> list[T]:
        """Incluye los eliminados (útil para pruebas y auditoría)."""
        return list(self._items)

    def listar_activos(self) -> list[T]:
        return [item for item in self._items if not item.eliminado]

    def buscar_por_id(self, id_: int) -> T:
        """Devuelve la entidad activa con ese id o lanza EntidadNoEncontradaError."""
        for item in self._items:
            if item.id == id_ and not item.eliminado:
                return item
        raise EntidadNoEncontradaError(f"No existe {self._nombre_entidad} con id {id_}")
