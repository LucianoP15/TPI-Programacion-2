"""Punto de entrada de Food Store. Ejecutar con:  python main.py

main.py NO contiene reglas de negocio: crea los servicios, carga los datos
iniciales, maneja el ciclo login -> menú y nada más.
"""

from consola.entrada import leer_contrasenia, leer_texto
from consola.fabrica import crear_menu
from consola.utilidades import mostrar_error, mostrar_titulo
from entidades import Usuario
from enums import FormaPago, Rol
from excepciones import FoodStoreError
from servicios import Servicios, UsuarioServicio

MAX_INTENTOS: int = 3


def cargar_datos_iniciales(servicios: Servicios) -> None:
    """Admin inicial (sin él nadie podría entrar) + datos de ejemplo para el video.
    Funciona en cuanto estén implementados los crear() de los servicios."""
    servicios.usuarios.crear("Ana", "Pérez", "admin@foodstore.com", "2614000000", "admin123", Rol.ADMIN)
    cliente = servicios.usuarios.crear(
        "Juan", "Gómez", "juan@mail.com", "2615000000", "juan123", Rol.USUARIO
    )

    pizzas = servicios.categorias.crear("Pizzas", "Pizzas a la piedra")
    bebidas = servicios.categorias.crear("Bebidas", "Gaseosas, aguas y jugos")
    servicios.categorias.crear("Postres", "Dulces caseros")

    muzza = servicios.productos.crear("Muzzarella", "Clásica", 8500, 20, "", True, pizzas.id)
    servicios.productos.crear("Fugazzeta", "Con cebolla", 9500, 15, "", True, pizzas.id)
    coca = servicios.productos.crear("Coca-Cola 1.5L", "Gaseosa", 3000, 30, "", True, bebidas.id)
    # Stock bajo a propósito: sirve para mostrar en el video el error de stock.
    servicios.productos.crear("Agua saborizada", "500 ml", 1500, 2, "", True, bebidas.id)

    servicios.pedidos.crear(cliente.id, FormaPago.EFECTIVO, [(muzza.id, 2), (coca.id, 1)])


def iniciar_sesion(usuario_servicio: UsuarioServicio) -> Usuario | None:
    """Devuelve el usuario autenticado, o None si agotó los intentos."""
    # TODO (HU-ACC-01):
    # 1. mostrar_titulo("FOOD STORE – INICIO DE SESIÓN").
    # 2. Repetir hasta MAX_INTENTOS veces:
    #       mail = leer_texto("Mail: "); contrasenia = leer_contrasenia()
    #       try: usuario = usuario_servicio.autenticar(mail, contrasenia)
    #       except CredencialesInvalidasError as e: mostrar_error(str(e)) y seguir
    #       si salió bien: print(f"Bienvenido/a, {usuario.nombre_completo} [{usuario.rol.name}]")
    #                      y return usuario
    # 3. Si se terminan los intentos -> return None (main informa y termina).
    raise NotImplementedError("iniciar_sesion")


def main() -> None:
    servicios = Servicios.crear()
    try:
        cargar_datos_iniciales(servicios)
    except (FoodStoreError, NotImplementedError) as error:  # TODO: dejar solo FoodStoreError al final
        mostrar_error(f"No se pudieron cargar los datos iniciales: {error}")

    while True:
        sesion = iniciar_sesion(servicios.usuarios)  # variable local, no global
        if sesion is None:
            mostrar_error("Se agotaron los intentos. El programa se cerrará.")
            return
        menu = crear_menu(sesion, servicios)
        if not menu.mostrar():  # False = salir del programa
            print("\n¡Hasta luego!")
            return
        # True = cerrar sesión: vuelve al login con los datos intactos.


_ = (leer_contrasenia, leer_texto, mostrar_titulo)

if __name__ == "__main__":
    main()
