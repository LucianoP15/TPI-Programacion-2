from enum import Enum


class FormaPago(Enum):
    """Formas de pago aceptadas en un pedido."""

    TARJETA = "Tarjeta"
    TRANSFERENCIA = "Transferencia"
    EFECTIVO = "Efectivo"
