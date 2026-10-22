"""Submenú PRODUCTOS (Épica 2)."""

from consola.entrada import (
    leer_entero,
    leer_entero_opcional,
    leer_float,
    leer_float_opcional,
    leer_si_no,
    leer_si_no_opcional,
    leer_texto,
    leer_texto_opcional,
)
from consola.utilidades import ejecutar_submenu, mostrar_exito, mostrar_lista
from servicios import CategoriaServicio, ProductoServicio


def submenu_productos(servicio: ProductoServicio, categoria_servicio: CategoriaServicio) -> None:
    ejecutar_submenu(
        "PRODUCTOS",
        {
            "1": ("Listar", lambda: listar_productos(servicio)),
            "2": ("Crear", lambda: crear_producto(servicio, categoria_servicio)),
            "3": ("Editar", lambda: editar_producto(servicio, categoria_servicio)),
            "4": ("Eliminar", lambda: eliminar_producto(servicio)),
            "5": ("Listar por categoría", lambda: listar_por_categoria(servicio, categoria_servicio)),
        },
    )


# ---------- HU-PROD-01 ----------
def listar_productos(servicio: ProductoServicio) -> None:
    # TODO: mostrar_lista(servicio.listar_activos(), "No hay productos cargados")
    raise NotImplementedError("listar_productos")


def listar_por_categoria(servicio: ProductoServicio, categoria_servicio: CategoriaServicio) -> None:
    # TODO (opcional de la HU): listar categorías, pedir id, validar que exista
    # con categoria_servicio.buscar_por_id y mostrar servicio.listar_por_categoria(id).
    raise NotImplementedError("listar_por_categoria")


# ---------- HU-PROD-02 ----------
def crear_producto(servicio: ProductoServicio, categoria_servicio: CategoriaServicio) -> None:
    # TODO:
    # 1. Si no hay categorías activas -> informar y volver (no se puede crear).
    # 2. Pedir: nombre, descripción (leer_texto), precio (leer_float(minimo=0)),
    #    stock (leer_entero(minimo=0)), imagen (input, puede quedar vacía),
    #    disponible (leer_si_no).
    # 3. Listar categorías y pedir categoria_id con leer_entero.
    # 4. producto = servicio.crear(...) y mostrar_exito con el id generado.
    raise NotImplementedError("crear_producto")


# ---------- HU-PROD-03 ----------
def editar_producto(servicio: ProductoServicio, categoria_servicio: CategoriaServicio) -> None:
    # TODO:
    # 1. Listar productos, pedir id y buscar (si no existe, el servicio lanza).
    # 2. Pedir cada campo con las versiones *_opcional (Enter = None = conservar):
    #    leer_texto_opcional, leer_float_opcional, leer_entero_opcional,
    #    leer_si_no_opcional. Imagen: input con Enter para conservar.
    # 3. Categoría: listar y leer_entero_opcional("Id categoría", producto.categoria.id).
    # 4. servicio.editar(id, ...) y mostrar_exito.
    raise NotImplementedError("editar_producto")


# ---------- HU-PROD-04 ----------
def eliminar_producto(servicio: ProductoServicio) -> None:
    # TODO: listar, pedir id, buscar, confirmar con leer_si_no,
    # servicio.eliminar(id) y mostrar_exito.
    raise NotImplementedError("eliminar_producto")


_ = (
    leer_entero, leer_entero_opcional, leer_float, leer_float_opcional, leer_si_no,
    leer_si_no_opcional, leer_texto, leer_texto_opcional, mostrar_exito, mostrar_lista,
)
