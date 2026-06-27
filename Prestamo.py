class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo, ):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = None

    def registrar_devolucion(self, fecha_devolucion):
        if self.fecha_devolucion is not None:
            return "El libro ya ha sido devuelto."
        self.fecha_devolucion = fecha_devolucion
        return "Devolución registrada correctamente."
    
    def mostrar_datos(self):
        return (
            f"Usuario: {self.usuario._nombre} {self.usuario._apellido}, "
            f"Libro: {self.libro.titulo}, "
            f"Fecha de préstamo: {self.fecha_prestamo}, "
            f"Fecha de devolución: {self.fecha_devolucion if self.fecha_devolucion else 'No se ha devuelto aún'}"
        )

    def prestamo_activo(self):
        return self.fecha_devolucion is None