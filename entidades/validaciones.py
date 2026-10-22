"""Funciones auxiliares de validación que usan los setters de las entidades.
Lanzan DatoInvalidoError (o una subclase) si el valor no es válido."""

from excepciones import DatoInvalidoError


def validar_texto(valor: str, campo: str) -> str:
    """Devuelve el texto sin espacios al inicio/fin. Falla si queda vacío."""
    if not isinstance(valor, str) or not valor.strip():
        raise DatoInvalidoError(f"El campo '{campo}' no puede estar vacío")
    return valor.strip()


def validar_no_negativo(valor: float, campo: str) -> float:
    """Valor numérico >= 0."""
    if isinstance(valor, bool) or not isinstance(valor, (int, float)):
        raise DatoInvalidoError(f"El campo '{campo}' debe ser numérico")
    if valor < 0:
        raise DatoInvalidoError(f"El campo '{campo}' no puede ser negativo")
    return valor


def validar_entero_no_negativo(valor: int, campo: str) -> int:
    """Entero >= 0 (por ejemplo, stock)."""
    if isinstance(valor, bool) or not isinstance(valor, int):
        raise DatoInvalidoError(f"El campo '{campo}' debe ser un número entero")
    if valor < 0:
        raise DatoInvalidoError(f"El campo '{campo}' no puede ser negativo")
    return valor


def validar_entero_positivo(valor: int, campo: str) -> int:
    """Entero > 0 (por ejemplo, cantidad de un detalle)."""
    if isinstance(valor, bool) or not isinstance(valor, int):
        raise DatoInvalidoError(f"El campo '{campo}' debe ser un número entero")
    if valor <= 0:
        raise DatoInvalidoError(f"El campo '{campo}' debe ser mayor a 0")
    return valor


def validar_formato_mail(mail: str) -> str:
    """Formato básico: no vacío, contiene '@' y '.'. Devuelve el mail en minúsculas."""
    mail = validar_texto(mail, "mail").lower()
    if "@" not in mail or "." not in mail:
        raise DatoInvalidoError("El mail debe contener '@' y '.'")
    return mail
