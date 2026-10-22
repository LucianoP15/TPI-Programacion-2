"""Pruebas del modelo y los servicios, sin menú. Ejecutar con:  python pruebas.py

Cada caso muestra en pantalla si pasó o no. Para errores esperados se usa
caso_error(...) con la excepción que DEBERÍA lanzarse.
"""

from collections.abc import Callable

from entidades import Categoria
from enums import Estado, FormaPago, Rol
from excepciones import (
    CredencialesInvalidasError,
    DatoInvalidoError,
    DuplicadoError,
    EntidadNoEncontradaError,
    OperacionNoPermitidaError,
    PrecioInvalidoError,
    StockInsuficienteError,
)
from servicios import Servicios

_resultados: dict[str, int] = {"ok": 0, "fallo": 0}


# ---------- auxiliares ----------
def caso_ok(descripcion: str, funcion: Callable[[], object]) -> object:
    """Espera que la función NO lance excepción. Devuelve su resultado."""
    try:
        resultado = funcion()
    except Exception as error:
        _resultados["fallo"] += 1
        print(f"  ✗ {descripcion} -> lanzó {type(error).__name__}: {error}")
        return None
    _resultados["ok"] += 1
    print(f"  ✓ {descripcion}")
    return resultado


def caso_error(descripcion: str, funcion: Callable[[], object], esperada: type[Exception]) -> None:
    """Espera que la función lance la excepción indicada."""
    try:
        funcion()
    except esperada as error:
        _resultados["ok"] += 1
        print(f"  ✓ {descripcion} -> {esperada.__name__}: {error}")
        return
    except Exception as error:
        _resultados["fallo"] += 1
        print(f"  ✗ {descripcion} -> esperaba {esperada.__name__}, lanzó {type(error).__name__}")
        return
    _resultados["fallo"] += 1
    print(f"  ✗ {descripcion} -> esperaba {esperada.__name__} y no lanzó nada")


def seccion(titulo: str, prueba: Callable[[], None]) -> None:
    print(f"\n== {titulo} ==")
    try:
        prueba()
    except NotImplementedError as error:  # TODO: quitar cuando esté todo hecho
        print(f"  [pendiente: {error}]")


# ---------- pruebas (EJEMPLO hecho) ----------
def probar_entidades_basicas() -> None:
    caso_ok("Crear categoría válida", lambda: Categoria("Pizzas", "A la piedra"))
    caso_error("Categoría sin nombre", lambda: Categoria("", "x"), DatoInvalidoError)
    a, b = Categoria("A", "a"), Categoria("B", "b")
    caso_ok("Ids distintos y __eq__ por id", lambda: a != b and a == a)


# ---------- pruebas (TODO) ----------
def probar_categorias(s: Servicios) -> None:
    # TODO: crear OK, nombre repetido en otra mayúscula -> DuplicadoError,
    # editar, buscar id inexistente -> EntidadNoEncontradaError,
    # eliminar con productos activos -> OperacionNoPermitidaError.
    raise NotImplementedError("probar_categorias")


def probar_productos(s: Servicios) -> None:
    # TODO: crear OK, precio < 0 -> PrecioInvalidoError, stock < 0 -> DatoInvalidoError,
    # categoría inexistente -> EntidadNoEncontradaError, listar_disponibles
    # no incluye productos sin stock / no disponibles / eliminados.
    raise NotImplementedError("probar_productos")


def probar_usuarios(s: Servicios) -> None:
    # TODO: crear OK, mail sin '@' -> DatoInvalidoError, mail repetido -> DuplicadoError,
    # autenticar OK, contraseña mala / mail inexistente / usuario eliminado
    # -> CredencialesInvalidasError, admin eliminándose -> OperacionNoPermitidaError.
    raise NotImplementedError("probar_usuarios")


def probar_pedidos(s: Servicios) -> None:
    # TODO: crear pedido OK y verificar total y stock descontado,
    # mismo producto dos veces -> un solo detalle con cantidad sumada,
    # cantidad > stock -> StockInsuficienteError y stock SIN cambios,
    # PENDIENTE -> TERMINADO -> OperacionNoPermitidaError,
    # cancelar devuelve stock, eliminar marca detalles como eliminados.
    raise NotImplementedError("probar_pedidos")


def main() -> None:
    seccion("Entidades básicas", probar_entidades_basicas)
    for titulo, prueba in [
        ("Categorías", probar_categorias),
        ("Productos", probar_productos),
        ("Usuarios", probar_usuarios),
        ("Pedidos", probar_pedidos),
    ]:
        servicios = Servicios.crear()  # servicios limpios para cada sección
        seccion(titulo, lambda p=prueba, sv=servicios: p(sv))
    print(f"\nResultado: {_resultados['ok']} OK, {_resultados['fallo']} con fallas")


# Imports que van a usar las pruebas pendientes.
_ = (
    CredencialesInvalidasError, DuplicadoError, EntidadNoEncontradaError,
    OperacionNoPermitidaError, PrecioInvalidoError, StockInsuficienteError,
    Estado, FormaPago, Rol,
)

if __name__ == "__main__":
    main()
