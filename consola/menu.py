from abc import ABC, abstractmethod

from consola.utilidades import Opciones, ejecutar_accion, mostrar_error, mostrar_titulo
from entidades import Usuario


class Menu(ABC):
    """Menú abstracto. Cada rol tiene su subclase (polimorfismo):
    main() solo llama a menu.mostrar() sin saber qué menú es."""

    OPCION_CERRAR_SESION = "9"
    OPCION_SALIR = "0"

    def __init__(self, usuario: Usuario) -> None:
        self._usuario = usuario

    @abstractmethod
    def mostrar(self) -> bool:
        """True = cerrar sesión (volver al login), False = salir del programa."""
        ...

    def _correr_menu_principal(self, titulo: str, opciones: Opciones) -> bool:
        """Bucle común de los menús principales. Las subclases solo arman
        su diccionario de opciones y llaman a esto desde mostrar()."""
        while True:
            mostrar_titulo(f"{titulo} ({self._usuario.nombre_completo})")
            for clave, (texto, _) in opciones.items():
                print(f"{clave}. {texto}")
            print(f"{self.OPCION_CERRAR_SESION}. Cerrar sesión")
            print(f"{self.OPCION_SALIR}. Salir")
            eleccion = input("Seleccione: ").strip()
            if eleccion == self.OPCION_CERRAR_SESION:
                return True
            if eleccion == self.OPCION_SALIR:
                return False
            if eleccion not in opciones:
                mostrar_error("Opción inválida.")
                continue
            ejecutar_accion(opciones[eleccion][1])
