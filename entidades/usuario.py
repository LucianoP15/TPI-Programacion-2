from __future__ import annotations

from typing import TYPE_CHECKING

from entidades.base import Base
from entidades.validaciones import validar_formato_mail, validar_texto
from enums import Rol
from excepciones import DatoInvalidoError

if TYPE_CHECKING:
    from entidades.pedido import Pedido


class Usuario(Base):
    """Usuario del sistema. Asociación 1..N con Pedido.

    La contraseña NO tiene property de lectura: solo se puede verificar o
    cambiar, así nunca sale del objeto.
    La unicidad del mail la valida UsuarioServicio (necesita la colección).
    """

    def __init__(
        self,
        nombre: str,
        apellido: str,
        mail: str,
        celular: str,
        contrasenia: str,
        rol: Rol,
    ) -> None:
        super().__init__()
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.celular = celular
        self.cambiar_contrasenia(contrasenia)
        self.rol = rol
        self.__pedidos: list[Pedido] = []

    # ---------- properties ----------
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        self.__nombre = validar_texto(valor, "nombre")

    @property
    def apellido(self) -> str:
        return self.__apellido

    @apellido.setter
    def apellido(self, valor: str) -> None:
        self.__apellido = validar_texto(valor, "apellido")

    @property
    def mail(self) -> str:
        return self.__mail

    @mail.setter
    def mail(self, valor: str) -> None:
        self.__mail = validar_formato_mail(valor)

    @property
    def celular(self) -> str:
        return self.__celular

    @celular.setter
    def celular(self, valor: str) -> None:
        self.__celular = validar_texto(valor, "celular")

    @property
    def rol(self) -> Rol:
        return self.__rol

    @rol.setter
    def rol(self, valor: Rol) -> None:
        if not isinstance(valor, Rol):
            raise DatoInvalidoError("Rol inválido")
        self.__rol = valor

    @property
    def nombre_completo(self) -> str:
        return f"{self.__nombre} {self.__apellido}"

    @property
    def pedidos(self) -> tuple[Pedido, ...]:
        return tuple(self.__pedidos)

    # ---------- contraseña ----------
    def verificar_contrasenia(self, contrasenia: str) -> bool:
        return self.__contrasenia == contrasenia

    def cambiar_contrasenia(self, nueva: str) -> None:
        self.__contrasenia = validar_texto(nueva, "contraseña")

    # ---------- auxiliar de la asociación ----------
    def agregar_pedido(self, pedido: Pedido) -> None:
        """Lo llama PedidoServicio cuando el pedido se guarda con éxito."""
        if pedido not in self.__pedidos:
            self.__pedidos.append(pedido)

    def __str__(self) -> str:
        # TODO: línea para el listado con id, nombre, apellido, mail y rol.
        # ¡NUNCA la contraseña! (HU-USR-01). Ej:
        #   "[1] Ana Pérez | admin@foodstore.com | Administrador"
        raise NotImplementedError("Usuario.__str__")
