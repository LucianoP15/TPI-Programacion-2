"""Auxiliares de presentación y el bucle genérico de los submenús."""

from collections.abc import Callable, Sequence

from excepciones import FoodStoreError

type Accion = Callable[[], None]
type Opciones = dict[str, tuple[str, Accion]]


def mostrar_titulo(texto: str) -> None:
    print(f"\n=== {texto} ===")


def mostrar_exito(texto: str) -> None:
    print(f"  ✓ {texto}")


def mostrar_error(texto: str) -> None:
    print(f"  ✗ {texto}")


def mostrar_lista(items: Sequence[object], mensaje_vacio: str) -> bool:
    """Imprime un elemento por línea usando su __str__.
    Devuelve False si la lista estaba vacía (para cortar la operación)."""
    if not items:
        print(f"  {mensaje_vacio}")
        return False
    for item in items:
        print(f"  {item}")
    return True


def ejecutar_accion(accion: Accion) -> None:
    """Ejecuta una opción del menú atrapando los errores, así nunca se cae.
    - FoodStoreError: errores de negocio (mensaje claro al usuario).
    - ValueError: conversiones fallidas que se hayan escapado.
    - NotImplementedError: SOLO durante el desarrollo, para poder probar el
      menú aunque falten partes. Borrar ese except antes de entregar.
    """
    try:
        accion()
    except FoodStoreError as error:
        mostrar_error(str(error))
    except ValueError as error:
        mostrar_error(f"Dato mal ingresado: {error}")
    except NotImplementedError as error:  # TODO: quitar antes de entregar
        print(f"  [pendiente de implementar: {error}]")


def ejecutar_submenu(titulo: str, opciones: Opciones) -> None:
    """Bucle de un submenú (Categorías, Productos, ...). '0' vuelve atrás."""
    while True:
        print(f"\n--- {titulo} ---")
        for clave, (texto, _) in opciones.items():
            print(f"{clave}. {texto}")
        print("0. Volver")
        eleccion = input("Seleccione: ").strip()
        if eleccion == "0":
            return
        if eleccion not in opciones:
            mostrar_error("Opción inválida.")
            continue
        ejecutar_accion(opciones[eleccion][1])
