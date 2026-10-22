"""Submenú USUARIOS (Épica 3)."""

from consola.entrada import (
    leer_contrasenia,
    leer_entero,
    leer_opcion_enum,
    leer_opcion_enum_opcional,
    leer_si_no,
    leer_texto,
    leer_texto_opcional,
)
from consola.utilidades import ejecutar_submenu, mostrar_exito, mostrar_lista
from entidades import Usuario
from enums import Rol
from servicios import UsuarioServicio


def submenu_usuarios(servicio: UsuarioServicio, usuario_sesion: Usuario) -> None:
    ejecutar_submenu(
        "USUARIOS",
        {
            "1": ("Listar", lambda: listar_usuarios(servicio)),
            "2": ("Crear", lambda: crear_usuario(servicio)),
            "3": ("Editar", lambda: editar_usuario(servicio)),
            "4": ("Eliminar", lambda: eliminar_usuario(servicio, usuario_sesion)),
        },
    )


# ---------- HU-USR-01 ----------
def listar_usuarios(servicio: UsuarioServicio) -> None:
    # TODO: mostrar_lista(servicio.listar_activos(), "No hay usuarios cargados")
    raise NotImplementedError("listar_usuarios")


# ---------- HU-USR-02 ----------
def crear_usuario(servicio: UsuarioServicio) -> None:
    # TODO:
    # 1. Pedir nombre, apellido, celular con leer_texto.
    # 2. Mail: la HU dice "si ya existe, se informa y se pide otro" ->
    #    hacer un while que pida el mail hasta que not servicio.mail_en_uso(mail).
    # 3. Contraseña con leer_contrasenia(); rol con leer_opcion_enum(Rol, "Rol: ").
    # 4. usuario = servicio.crear(...) y mostrar_exito con el id.
    raise NotImplementedError("crear_usuario")


# ---------- HU-USR-03 ----------
def editar_usuario(servicio: UsuarioServicio) -> None:
    # TODO:
    # 1. Listar, pedir id, buscar.
    # 2. Campos con leer_texto_opcional (Enter = conservar).
    #    Contraseña: preguntar con leer_si_no si la quiere cambiar.
    #    Rol: leer_opcion_enum_opcional(Rol, "Rol", usuario.rol).
    # 3. servicio.editar(...) (valida mail único) y mostrar_exito.
    raise NotImplementedError("editar_usuario")


# ---------- HU-USR-04 ----------
def eliminar_usuario(servicio: UsuarioServicio, usuario_sesion: Usuario) -> None:
    # TODO: listar, pedir id, buscar, confirmar con leer_si_no,
    # servicio.eliminar(id, usuario_sesion) (impide auto-eliminarse) y mostrar_exito.
    raise NotImplementedError("eliminar_usuario")


_ = (
    leer_contrasenia, leer_entero, leer_opcion_enum, leer_opcion_enum_opcional, leer_si_no,
    leer_texto, leer_texto_opcional, mostrar_exito, mostrar_lista, Rol,
)
