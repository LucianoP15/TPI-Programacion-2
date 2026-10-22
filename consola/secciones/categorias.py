"""Submenú CATEGORÍAS (Épica 1)."""

from consola.entrada import leer_entero, leer_si_no, leer_texto, leer_texto_opcional
from consola.utilidades import ejecutar_submenu, mostrar_exito, mostrar_lista
from servicios import CategoriaServicio


def submenu_categorias(servicio: CategoriaServicio) -> None:
    ejecutar_submenu(
        "CATEGORÍAS",
        {
            "1": ("Listar", lambda: listar_categorias(servicio)),
            "2": ("Crear", lambda: crear_categoria(servicio)),
            "3": ("Editar", lambda: editar_categoria(servicio)),
            "4": ("Eliminar", lambda: eliminar_categoria(servicio)),
        },
    )


# ---------- HU-CAT-01 (la usa también el menú cliente) ----------
def listar_categorias(servicio: CategoriaServicio) -> None:
    # TODO: mostrar_lista(servicio.listar_activos(), "No hay categorías cargadas")
    raise NotImplementedError("listar_categorias")


# ---------- HU-CAT-02 ----------
def crear_categoria(servicio: CategoriaServicio) -> None:
    # TODO:
    # 1. nombre = leer_texto("Nombre: "), descripcion = leer_texto("Descripción: ").
    # 2. categoria = servicio.crear(nombre, descripcion).
    # 3. mostrar_exito(f"Categoría creada con id {categoria.id}").
    # Los errores (DuplicadoError, etc.) los atrapa ejecutar_accion.
    raise NotImplementedError("crear_categoria")


# ---------- HU-CAT-03 ----------
def editar_categoria(servicio: CategoriaServicio) -> None:
    # TODO:
    # 1. Listar las categorías (si no hay, volver).
    # 2. id = leer_entero("Id a editar: "); categoria = servicio.buscar_por_id(id).
    # 3. nombre = leer_texto_opcional("Nombre", categoria.nombre)   (None = Enter)
    #    descripcion = leer_texto_opcional("Descripción", categoria.descripcion)
    # 4. servicio.editar(id, nombre, descripcion) y mostrar_exito(...).
    raise NotImplementedError("editar_categoria")


# ---------- HU-CAT-04 ----------
def eliminar_categoria(servicio: CategoriaServicio) -> None:
    # TODO:
    # 1. Listar, pedir id y buscar (para mostrar qué se va a eliminar).
    # 2. Si leer_si_no(f"¿Eliminar '{categoria.nombre}'?") es False -> informar y volver.
    # 3. servicio.eliminar(id) y mostrar_exito(...).
    #    (Si tiene productos activos, el servicio lanza OperacionNoPermitidaError.)
    raise NotImplementedError("eliminar_categoria")


# Evita warnings de "import sin usar" mientras las funciones están vacías.
_ = (leer_entero, leer_si_no, leer_texto, leer_texto_opcional, mostrar_exito, mostrar_lista)
