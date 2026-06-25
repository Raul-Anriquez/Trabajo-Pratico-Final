class gestion_libros:
    def __init__(self):
        self.libros = []

def agregar_libro(self, libro):
        self.libros.append(libro)

def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
        else:
              return "El libro no se esta en la lista."
 
def modificar_libro(self, Libro, nuevo_titulo, nuevo_autor, nueva_fecha_publicacion, nuevo_cantidad_paginas, nuevo_ISBN):
        if Libro in self.libros:
            Libro.titulo = nuevo_titulo
            Libro.autor = nuevo_autor
            Libro.fecha_publicacion = nueva_fecha_publicacion
            Libro.cantidad_paginas = nuevo_cantidad_paginas
            Libro.ISBN = nuevo_ISBN
        else:
            return "El libro no se encuentra en la lista."
def buscar_libro(self, titulo):
 pass

def listar_libros(self):
        return self.libros       