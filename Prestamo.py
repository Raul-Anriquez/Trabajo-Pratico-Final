class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo, fecha_devolucion):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def registrar_fecha_devolucion(self, fecha_devolucion):
        self.fecha_devolucion = fecha_devolucion
        pass