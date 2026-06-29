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

    def agregar_libro(self, libro):
        return self.gestion_libros.agregar_libro(libro)
    
    def eliminar_libro(self, libro):
        return self.gestion_libros.eliminar_libro(libro)
    
    def buscar_libro(self, ISBN):
        return self.gestion_libros.buscar_libro(ISBN)

    def modificar_libro(self, libro, nuevo_titulo, nuevo_autor, nueva_fecha_publicacion, nuevo_cantidad_paginas, nuevo_ISBN):
        return self.gestion_libros.modificar_libro(libro, nuevo_titulo, nuevo_autor, nueva_fecha_publicacion, nuevo_cantidad_paginas, nuevo_ISBN)
    
    def listar_libros(self):
        return self.gestion_libros.listar_libros()
    
    def agregar_usuario(self, usuario):
        return self.gestion_usuarios.agregar_usuario(usuario)
    
    def eliminar_usuario(self, usuario):
        return self.gestion_usuarios.eliminar_usuario(usuario)
    
    def buscar_usuario(self, dni):
        return self.gestion_usuarios.buscar_usuario(dni)
    
    def modificar_usuario(self, usuario, nuevo_nombre, nuevo_apellido, nuevo_dni, nuevo_correo):
        return self.gestion_usuarios.modificar_usuario(usuario, nuevo_nombre, nuevo_apellido, nuevo_dni, nuevo_correo)
    
    def listar_usuarios(self):
        return self.gestion_usuarios.listar_usuarios()
    
    def registrar_prestamo(self, prestamo):
        return self.gestion_prestamos.registrar_prestamo(prestamo)
    
    
    def eliminar_prestamo(self, prestamo):
        return self.gestion_prestamos.eliminar_prestamo(prestamo)
    
    def buscar_prestamo(self, libro):
        return self.gestion_prestamos.buscar_prestamo(libro)
    
    def listar_prestamos(self):
        return self.gestion_prestamos.listar_prestamos()