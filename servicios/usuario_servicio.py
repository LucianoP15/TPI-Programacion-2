from entidades import Usuario
from enums import Rol
from servicios.servicio_base import ServicioBase


class UsuarioServicio(ServicioBase[Usuario]):
    _nombre_entidad = "usuario"

    # ---------- auxiliares ----------
    def buscar_por_mail(self, mail: str) -> Usuario | None:
        """Busca entre TODOS (incluidos eliminados). None si no existe."""
        buscado = mail.strip().lower()
        for usuario in self._items:
            if usuario.mail == buscado:
                return usuario
        return None

    def mail_en_uso(self, mail: str, excluir_id: int | None = None) -> bool:
        """Mail único en toda la colección (decisión: también contra eliminados)."""
        usuario = self.buscar_por_mail(mail)
        return usuario is not None and usuario.id != excluir_id

    # ---------- HU-ACC-01 ----------
    def autenticar(self, mail: str, contrasenia: str) -> Usuario:
        # TODO:
        # 1. usuario = self.buscar_por_mail(mail).
        # 2. Si es None, o usuario.eliminado, o not usuario.verificar_contrasenia(contrasenia)
        #    -> raise CredencialesInvalidasError() (mismo mensaje en los 3 casos).
        # 3. Devolver el usuario.
        raise NotImplementedError("UsuarioServicio.autenticar")

    # ---------- HU-USR-02 ----------
    def crear(
        self,
        nombre: str,
        apellido: str,
        mail: str,
        celular: str,
        contrasenia: str,
        rol: Rol,
    ) -> Usuario:
        # TODO:
        # 1. Si self.mail_en_uso(mail) -> DuplicadoError.
        # 2. Crear Usuario(...) (los setters validan vacíos y formato de mail).
        # 3. self._agregar(usuario) y devolverlo.
        raise NotImplementedError("UsuarioServicio.crear")

    # ---------- HU-USR-03 ----------
    def editar(
        self,
        usuario_id: int,
        nombre: str | None = None,
        apellido: str | None = None,
        mail: str | None = None,
        celular: str | None = None,
        contrasenia: str | None = None,
        rol: Rol | None = None,
    ) -> Usuario:
        # TODO:
        # 1. Buscar por id.
        # 2. None = no cambiar.
        # 3. Si cambia el mail: mail_en_uso(mail, excluir_id=usuario_id) -> DuplicadoError.
        # 4. Contraseña con usuario.cambiar_contrasenia(...).
        # 5. Devolver el usuario.
        raise NotImplementedError("UsuarioServicio.editar")

    # ---------- HU-USR-04 ----------
    def eliminar(self, usuario_id: int, usuario_sesion: Usuario) -> None:
        # TODO:
        # 1. Buscar por id.
        # 2. Si usuario == usuario_sesion -> OperacionNoPermitidaError
        #    ("No podés eliminar tu propio usuario mientras tenés la sesión iniciada").
        # 3. usuario.eliminar(). Sus pedidos NO se tocan (se siguen consultando).
        raise NotImplementedError("UsuarioServicio.eliminar")
