"""Lectura validada de teclado. Cada función repite la pregunta hasta que
el dato sea válido, así un error de tipeo nunca cierra el programa."""

import getpass
from enum import Enum


def leer_texto(mensaje: str) -> str:
    """Texto obligatorio (no vacío)."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("  ✗ El valor no puede estar vacío.")


def leer_texto_opcional(mensaje: str, actual: str) -> str | None:
    """Para editar: muestra el valor actual; Enter devuelve None (= no cambiar)."""
    valor = input(f"{mensaje} [{actual}]: ").strip()
    return valor or None


def leer_contrasenia(mensaje: str = "Contraseña: ") -> str:
    """Oculta lo que se escribe. Si la terminal no lo soporta, usa input()."""
    try:
        return getpass.getpass(mensaje).strip()
    except (EOFError, OSError):
        return input(mensaje).strip()


def leer_entero(mensaje: str, minimo: int | None = None, maximo: int | None = None) -> int:
    while True:
        try:
            valor = int(input(mensaje).strip())
        except ValueError:
            print("  ✗ Ingresá un número entero.")
            continue
        if minimo is not None and valor < minimo:
            print(f"  ✗ Debe ser mayor o igual a {minimo}.")
        elif maximo is not None and valor > maximo:
            print(f"  ✗ Debe ser menor o igual a {maximo}.")
        else:
            return valor


def leer_entero_opcional(mensaje: str, actual: int) -> int | None:
    """Enter = None (no cambiar)."""
    while True:
        texto = input(f"{mensaje} [{actual}]: ").strip()
        if not texto:
            return None
        try:
            return int(texto)
        except ValueError:
            print("  ✗ Ingresá un número entero o Enter para no cambiar.")


def leer_float(mensaje: str, minimo: float | None = None) -> float:
    while True:
        try:
            valor = float(input(mensaje).strip().replace(",", "."))
        except ValueError:
            print("  ✗ Ingresá un número (podés usar decimales).")
            continue
        if minimo is not None and valor < minimo:
            print(f"  ✗ Debe ser mayor o igual a {minimo}.")
        else:
            return valor


def leer_float_opcional(mensaje: str, actual: float) -> float | None:
    """Enter = None (no cambiar)."""
    while True:
        texto = input(f"{mensaje} [{actual:.2f}]: ").strip()
        if not texto:
            return None
        try:
            return float(texto.replace(",", "."))
        except ValueError:
            print("  ✗ Ingresá un número o Enter para no cambiar.")


def leer_si_no(mensaje: str) -> bool:
    """S/N -> True/False."""
    while True:
        valor = input(f"{mensaje} (S/N): ").strip().upper()
        if valor in ("S", "N"):
            return valor == "S"
        print("  ✗ Respondé S o N.")


def leer_si_no_opcional(mensaje: str, actual: bool) -> bool | None:
    """Enter = None (no cambiar)."""
    while True:
        valor = input(f"{mensaje} (S/N) [{'S' if actual else 'N'}]: ").strip().upper()
        if not valor:
            return None
        if valor in ("S", "N"):
            return valor == "S"
        print("  ✗ Respondé S, N o Enter para no cambiar.")


def leer_opcion_enum[E: Enum](enum_cls: type[E], mensaje: str) -> E:
    """Muestra las opciones numeradas del enum y devuelve la elegida (por número)."""
    opciones = list(enum_cls)
    for i, opcion in enumerate(opciones, start=1):
        print(f"  {i}. {opcion.value}")
    indice = leer_entero(mensaje, minimo=1, maximo=len(opciones))
    return opciones[indice - 1]


def leer_opcion_enum_opcional[E: Enum](enum_cls: type[E], mensaje: str, actual: E) -> E | None:
    """Igual que leer_opcion_enum pero Enter conserva el valor actual."""
    opciones = list(enum_cls)
    for i, opcion in enumerate(opciones, start=1):
        print(f"  {i}. {opcion.value}")
    while True:
        texto = input(f"{mensaje} [{actual.value}]: ").strip()
        if not texto:
            return None
        if texto.isdigit() and 1 <= int(texto) <= len(opciones):
            return opciones[int(texto) - 1]
        print(f"  ✗ Elegí un número entre 1 y {len(opciones)} o Enter.")
