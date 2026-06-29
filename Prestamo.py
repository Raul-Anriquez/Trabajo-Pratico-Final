from Metaclase import MetaEntidad
from datetime import date
class Prestamo(metaclass=MetaEntidad):
    def __init__(self, usuario, libro, ):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = None

    def registrar_devolucion(self):
        if self.fecha_devolucion is not None:
            return "El libro ya ha sido devuelto."
        self.fecha_devolucion = date.today()
        return " La devolución registrada correctamente."
    
    def mostrar_datos(self):
        return (
            f"Usuario: {self.usuario._nombre} {self.usuario._apellido}, "
            f"Libro: {self.libro.titulo}, "
            f"Fecha de préstamo: {self.fecha_prestamo}, "
            f"Fecha de devolución: {self.fecha_devolucion if self.fecha_devolucion else 'No se ha devuelto aún'}"
        )

    def esta_activo(self):
        return self.fecha_devolucion is None