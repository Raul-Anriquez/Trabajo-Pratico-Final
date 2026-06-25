class Libro:
    def __init__ (self, titulo, autor, ISBN, fecha_publicacion, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.fecha_publicacion = fecha_publicacion
        self.cantidad_paginas = cantidad_paginas
    
    def mostrar_datos(self):
        return (f"Titulo:{self.titulo}"
                f"Autor:{self.autor}"
                f"ISBN:{self.ISBN}"
                f"Fecha de publicacion:{self.fecha_publicacion}"
                f"Cantidad de paginas:{self.cantidad_paginas}")
    