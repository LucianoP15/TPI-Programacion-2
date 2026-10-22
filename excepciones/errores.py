"""Excepciones propias de Food Store. Todas heredan de FoodStoreError,
así la consola puede capturarlas juntas con un solo `except FoodStoreError`."""


class FoodStoreError(Exception):
    """Excepción base de todos los errores de negocio del sistema."""


class EntidadNoEncontradaError(FoodStoreError):
    """Id inexistente o entidad dada de baja (eliminado = True)."""


class DatoInvalidoError(FoodStoreError):
    """Texto vacío, formato incorrecto, número fuera de rango, etc."""


class PrecioInvalidoError(DatoInvalidoError):
    """Precio negativo."""


class StockInsuficienteError(FoodStoreError):
    """La cantidad pedida supera el stock disponible del producto."""


class DuplicadoError(FoodStoreError):
    """Mail de usuario o nombre de categoría repetido."""


class OperacionNoPermitidaError(FoodStoreError):
    """Transición de estado inválida, categoría con productos activos,
    administrador que intenta eliminarse a sí mismo, etc."""


class CredencialesInvalidasError(FoodStoreError):
    """Mail inexistente, usuario eliminado o contraseña incorrecta.
    El mensaje es siempre el mismo para no revelar qué dato falló."""

    def __init__(self, mensaje: str = "Mail o contraseña incorrectos") -> None:
        super().__init__(mensaje)
