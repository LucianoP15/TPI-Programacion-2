# Food Store – Sistema de Gestión de Pedidos (Consola)

Trabajo Práctico Integrador – Programación II
Tecnicatura Universitaria en Programación – UTN

**Integrantes:** _completar_

## Requisitos

- Python **3.12 o superior** (se usa la sintaxis de genéricos `class X[T]` y `type`)
- Solo biblioteca estándar, no hay que instalar nada

## Cómo ejecutar

```bash
python main.py      # sistema completo
python pruebas.py   # pruebas del modelo y servicios
```

## Credenciales iniciales

| Rol | Mail | Contraseña |
| --- | --- | --- |
| Administrador | admin@foodstore.com | admin123 |
| Cliente | juan@mail.com | juan123 |

## Estructura

```
food_store/
├── main.py            # crea los servicios, carga datos y arranca el login
├── pruebas.py         # pruebas sin menú
├── entidades/         # clases del UML + interfaz Calculable + validaciones
├── enums/             # Rol, Estado, FormaPago
├── excepciones/       # FoodStoreError y subclases
├── servicios/         # un servicio por entidad (colección + reglas de negocio)
└── consola/           # Menu, MenuAdministrador, MenuCliente, lectura validada
    └── secciones/     # submenús del admin (categorías, productos, usuarios, pedidos)
```

Dependencias en un solo sentido: `consola → servicios → entidades`.

## Entregables

- 🎥 Video: _pegar enlace (público)_
- 📄 Informe PDF: _pegar enlace o subir a la raíz_
