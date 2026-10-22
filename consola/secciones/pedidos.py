"""Submenú PEDIDOS (Épica 4)."""

from consola.entrada import leer_entero, leer_opcion_enum, leer_si_no
from consola.utilidades import ejecutar_submenu, mostrar_exito, mostrar_lista
from enums import Estado, FormaPago
from servicios import PedidoServicio, ProductoServicio, UsuarioServicio


def submenu_pedidos(
    servicio: PedidoServicio,
    usuario_servicio: UsuarioServicio,
    producto_servicio: ProductoServicio,
) -> None:
    ejecutar_submenu(
        "PEDIDOS",
        {
            "1": ("Listar", lambda: listar_pedidos(servicio)),
            "2": ("Crear", lambda: crear_pedido(servicio, usuario_servicio, producto_servicio)),
            "3": ("Cambiar estado", lambda: cambiar_estado_pedido(servicio)),
            "4": ("Cambiar forma de pago", lambda: cambiar_forma_pago_pedido(servicio)),
            "5": ("Eliminar", lambda: eliminar_pedido(servicio)),
            "6": ("Ver detalle de un pedido", lambda: ver_detalle_pedido(servicio)),
        },
    )


# ---------- HU-PED-01 ----------
def listar_pedidos(servicio: PedidoServicio) -> None:
    # TODO: mostrar_lista(servicio.listar_activos(), "No hay pedidos cargados")
    raise NotImplementedError("listar_pedidos")


def ver_detalle_pedido(servicio: PedidoServicio) -> None:
    # TODO (opcional): pedir id, buscar y mostrar cada detalle + el total.
    raise NotImplementedError("ver_detalle_pedido")


# ---------- HU-PED-02 ----------
def crear_pedido(
    servicio: PedidoServicio,
    usuario_servicio: UsuarioServicio,
    producto_servicio: ProductoServicio,
) -> None:
    # TODO:
    # 1. Listar usuarios activos y pedir usuario_id (validar que exista con
    #    usuario_servicio.buscar_por_id para cortar temprano).
    # 2. forma_pago = leer_opcion_enum(FormaPago, "Forma de pago: ").
    # 3. Bucle: listar productos (activos), pedir producto_id y cantidad
    #    (leer_entero(minimo=1)) y acumular en items: list[tuple[int, int]].
    #    Seguir mientras leer_si_no("¿Agregar otro producto?").
    # 4. pedido = servicio.crear(usuario_id, forma_pago, items).
    #    Si falta stock lanza StockInsuficienteError -> ejecutar_accion lo
    #    muestra y el pedido NO se crea (esto va en el video).
    # 5. mostrar_exito(f"Pedido {pedido.id} creado. Total: ${pedido.total:.2f}").
    raise NotImplementedError("crear_pedido")


# ---------- HU-PED-03 ----------
def cambiar_estado_pedido(servicio: PedidoServicio) -> None:
    # TODO: listar, pedir id, nuevo = leer_opcion_enum(Estado, "Nuevo estado: "),
    # servicio.cambiar_estado(id, nuevo) y mostrar_exito.
    raise NotImplementedError("cambiar_estado_pedido")


def cambiar_forma_pago_pedido(servicio: PedidoServicio) -> None:
    # TODO: listar, pedir id, leer_opcion_enum(FormaPago, ...),
    # servicio.cambiar_forma_pago(id, forma) y mostrar_exito.
    raise NotImplementedError("cambiar_forma_pago_pedido")


# ---------- HU-PED-04 ----------
def eliminar_pedido(servicio: PedidoServicio) -> None:
    # TODO: listar, pedir id, buscar, confirmar con leer_si_no,
    # servicio.eliminar(id) (devuelve stock si no estaba cerrado) y mostrar_exito.
    raise NotImplementedError("eliminar_pedido")


_ = (leer_entero, leer_opcion_enum, leer_si_no, mostrar_exito, mostrar_lista, Estado, FormaPago)
