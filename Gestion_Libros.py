class GestionLibros:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        return "el libro fue agregado correctamente."

    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            return "El libro fue eliminado correctamente."
        else:
              return "El libro no esta en la lista."
 
    def modificar_libro(self, libro, nuevo_titulo, nuevo_autor, nueva_fecha_publicacion, nuevo_cantidad_paginas, nuevo_ISBN):
        if libro in self.libros:
            libro.titulo = nuevo_titulo
            libro.autor = nuevo_autor
            libro.fecha_publicacion = nueva_fecha_publicacion
            libro.cantidad_paginas = nuevo_cantidad_paginas
            libro.ISBN = nuevo_ISBN
            return "El libro fue modificado correctamente."
        else:
            return "El libro no esta en la lista."

    def listar_libros(self):
        for libro in self.libros:
            print(libro.mostrar_datos())