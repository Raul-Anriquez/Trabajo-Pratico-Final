class MetaEntidad(type):
    def __new__(mcls, name, bases, attrs):

        if name in ("Libro", "Usuario", "Prestamo"):
            if "__init__" not in attrs:
                raise TypeError(f"{name} debe tener constructor.")

            if "mostrar_datos" not in attrs:
                raise TypeError(f"{name} debe tener mostrar_datos().")

        return super().__new__(mcls, name, bases, attrs)
