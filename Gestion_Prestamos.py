from Decorador import registrar_operacion

class GestionPrestamos:
    def __init__(self):
        self.prestamos = []

    def registrar_prestamo(self, prestamo):
        for prestamo_activo in self.prestamos:
          if prestamo_activo.libro == prestamo.libro and prestamo_activo.esta_activo():
            return "El libro ya está prestado y no se devolvió aun."
        
        self.prestamos.append(prestamo)
        return "El préstamo fue registrado correctamente."
    
    def modificar_prestamo(self,prestamo,nueva_fecha_devolucion):
        if prestamo in self.prestamos:
            prestamo.fecha_devolucion = nueva_fecha_devolucion
            return "El prestamo se modifico de forma correcta"
        else:
            return " El prestamo no se pudo encontrar"
        

    def eliminar_prestamo(self, prestamo):
        if prestamo in self.prestamos:
            self.prestamos.remove(prestamo)
            return "El préstamo fue eliminado correctamente."
        else:
            return "El préstamo no estaba en la lista."

    def listar_prestamos(self):
        for prestamo in self.prestamos:
            print(prestamo.mostrar_datos())
    
    def buscar_prestamo(self, libro):
        for prestamo in self.prestamos:
            if prestamo.libro == libro:
                return prestamo
        return None
    
    
