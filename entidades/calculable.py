from abc import ABC, abstractmethod


class Calculable(ABC):
    """Interfaz: cualquier objeto que tenga un total calculable."""

    @abstractmethod
    def calcular_total(self) -> None:
        """Actualiza el total del objeto que implementa la interfaz."""
        ...
