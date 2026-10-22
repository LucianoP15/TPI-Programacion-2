# Reparto de tareas

Todo lo que falta está marcado con `# TODO` y hace `raise NotImplementedError`.
Buscar pendientes: `grep -rn "TODO" --include=*.py .`

Mientras falten partes, el menú muestra `[pendiente de implementar: ...]`
en vez de cerrarse. **Antes de entregar** hay que borrar los `except NotImplementedError`
de `consola/utilidades.py`, `main.py` y `pruebas.py`.

## Ya hecho (no tocar salvo bug)

- `enums/`, `excepciones/`, `entidades/base.py`, `entidades/calculable.py`, `entidades/validaciones.py`
- Constructores, properties y setters con validación de todas las entidades
- `servicios/servicio_base.py` (colección, `buscar_por_id`, `listar_activos`) y `Servicios.crear()`
- `consola/entrada.py` (lectura validada), `consola/utilidades.py`, `Menu`, `crear_menu`, ruteo de los menús
- `main()` y `cargar_datos_iniciales()`

## Integrante A — Catálogo + acceso

| Archivo | Qué hacer |
| --- | --- |
| `entidades/categoria.py` | `__str__` |
| `entidades/producto.py` | `__str__` |
| `entidades/usuario.py` | `__str__` |
| `servicios/categoria_servicio.py` | `crear`, `editar`, `eliminar` |
| `servicios/producto_servicio.py` | `listar_disponibles`, `crear`, `editar`, `eliminar` |
| `servicios/usuario_servicio.py` | `autenticar` |
| `consola/secciones/categorias.py` | las 4 acciones |
| `consola/secciones/productos.py` | las 5 acciones |
| `consola/menu_cliente.py` | `_ver_productos_disponibles`, `_mis_datos` |
| `main.py` | `iniciar_sesion` |
| `pruebas.py` | `probar_categorias`, `probar_productos` |

## Integrante B — Usuarios + pedidos

| Archivo | Qué hacer |
| --- | --- |
| `entidades/pedido.py` | `agregar_detalle`, `buscar_detalle_por_producto`, `eliminar_detalle_por_producto`, `calcular_total`, `cambiar_estado`, `__str__` |
| `entidades/detalle_pedido.py` | `__str__` |
| `servicios/usuario_servicio.py` | `crear`, `editar`, `eliminar` |
| `servicios/pedido_servicio.py` | todos los métodos con TODO |
| `consola/secciones/usuarios.py` | las 4 acciones |
| `consola/secciones/pedidos.py` | las 6 acciones |
| `consola/menu_cliente.py` | `_mis_pedidos` |
| `pruebas.py` | `probar_usuarios`, `probar_pedidos` |

## Orden sugerido

1. **A:** `UsuarioServicio.autenticar` + `iniciar_sesion` · **B:** `UsuarioServicio.crear` → con eso ya se puede entrar al sistema.
2. **A:** `CategoriaServicio.crear` + `ProductoServicio.crear` · **B:** métodos de `Pedido` + `PedidoServicio.crear` → con eso cargan los datos de ejemplo.
3. Los `__str__` (son rápidos y hacen falta para todos los listados).
4. El resto de cada lista, después pruebas.

## Entre los dos

- [ ] Informe PDF (carátula, índice, marco teórico, decisiones técnicas, dificultades, bibliografía, enlaces)
- [ ] Video 10–15 min: login con ambos roles, un error de validación y un pedido rechazado por falta de stock
- [ ] Completar README (integrantes, enlaces)
- [ ] Borrar los `except NotImplementedError` y verificar `python main.py` y `python pruebas.py`
- [ ] Armar el .zip con código + PDF

## Git

- Cada uno en su rama (`a-catalogo`, `b-pedidos`) y PR a `main`.
- Los únicos archivos compartidos son `usuario_servicio.py`, `menu_cliente.py` y `pruebas.py`: cada uno toca solo sus funciones.
