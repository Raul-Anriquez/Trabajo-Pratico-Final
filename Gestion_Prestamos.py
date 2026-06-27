class GestionPrestamos:
    def __init__(self):
        self.prestamos = []

    def registrar_prestamos(self, prestamo):
        for prestamo_activo in self.prestamos:
          if prestamo_activo.libro == prestamo.libro and prestamo_activo.esta_activo():
            return "El libro ya está prestado y no se devolvió aun."
        
        self.prestamos.append(prestamo)
        return "El préstamo fue registrado correctamente."

    def eliminar_prestamos(self, prestamo):
        if prestamo in self.prestamos:
            self.prestamos.remove(prestamo)
            return "El préstamo fue eliminado correctamente."
        else:
            return "El préstamo no estaba en la lista."

    def listar_prestamos(self):
        for prestamo in self.prestamos:
            print(prestamo.mostrar_datos())
    
    