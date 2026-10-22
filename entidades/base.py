from abc import ABC, abstractmethod
from datetime import datetime
from typing import ClassVar


class Base(ABC):
    """Superclase abstracta de todas las entidades.

    Decisión (justificar en el informe): se usa UN contador compartido por
    todas las entidades, así ningún objeto del sistema repite id y __eq__
    por id es seguro aunque se comparen objetos de clases distintas.
    """

    _contador_id: ClassVar[int] = 0

    def __init__(self) -> None:
        Base._contador_id += 1
        self.__id: int = Base._contador_id
        self.__eliminado: bool = False
        self.__creado_en: datetime = datetime.now()

    @property
    def id(self) -> int:
        return self.__id

    @property
    def eliminado(self) -> bool:
        return self.__eliminado

    @property
    def creado_en(self) -> datetime:
        return self.__creado_en

    def eliminar(self) -> None:
        """Baja lógica: el objeto sigue en la colección pero marcado."""
        self.__eliminado = True

    def __eq__(self, otro: object) -> bool:
        return isinstance(otro, Base) and self.id == otro.id

    def __hash__(self) -> int:
        return hash(self.id)

    @abstractmethod
    def __str__(self) -> str:
        """Abstracto: obliga a cada entidad a definir su línea para los listados
        (y además hace que Base no se pueda instanciar)."""
        ...
