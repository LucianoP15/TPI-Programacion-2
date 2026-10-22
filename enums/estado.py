from enum import Enum


class Estado(Enum):
    """Estados posibles de un pedido.

    Transiciones válidas (ver Pedido.TRANSICIONES_VALIDAS):
        PENDIENTE  -> CONFIRMADO | CANCELADO
        CONFIRMADO -> TERMINADO  | CANCELADO
        TERMINADO y CANCELADO son estados finales.
    """

    PENDIENTE = "Pendiente"
    CONFIRMADO = "Confirmado"
    TERMINADO = "Terminado"
    CANCELADO = "Cancelado"
