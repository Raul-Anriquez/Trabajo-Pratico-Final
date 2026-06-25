class Usuario:
    def __init__(self, nombre, apellido, dni, correo):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._correo = correo

    def mostrar_datos(self):
        return (
            f"Nombre: {self._nombre}, "
            f"Apellido: {self._apellido}, "
            f"DNI: {self._dni}, "
            f"Correo: {self._correo}"
        )


class Socio(Usuario):
    def __init__(self, nombre, apellido, dni, correo, nro_socio, fecha_alta):
        super().__init__(nombre, apellido, dni, correo)
        self._nro_socio = nro_socio
        self._fecha_alta = fecha_alta

    def mostrar_datos(self):
        return (
            f"Nombre: {self._nombre}, "
            f"Apellido: {self._apellido}, "
            f"DNI: {self._dni}, "
            f"Correo: {self._correo}, "
            f"Numero de Socio: {self._nro_socio}, "
            f"Fecha Alta: {self._fecha_alta}"
        )
