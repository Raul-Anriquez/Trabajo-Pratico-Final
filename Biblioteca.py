from Gestion_Libros import GestionLibros
from Gestion_Usuarios import GestionUsuarios
from Gestion_Prestamos import GestionPrestamos

class Biblioteca:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    
    def __init__(self):
        if not getattr(self, 'initialized', False):
            self.gestion_libros = GestionLibros()
            self.gestion_usuarios = GestionUsuarios()
            self.gestion_prestamos = GestionPrestamos()
            self.initialized = True