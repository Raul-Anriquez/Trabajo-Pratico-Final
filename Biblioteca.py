from Gestion_Libros import GestionLibros
from Gestion_Usuarios import GestionUsuarios
from Gestion_Prestamos import GestionPrestamos

class Biblioteca:
    def __init__(self):
        self.gestion_libros = GestionLibros()
        self.gestion_usuarios = GestionUsuarios()
        self.gestion_prestamos = GestionPrestamos()
        