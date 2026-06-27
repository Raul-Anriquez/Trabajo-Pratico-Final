class GestionUsuarios:
    def __init__(self):
        self.usuarios = []
    
    def agregar_usuario(self, usuario):
        if usuario not in self.usuarios:
            self.usuarios.append(usuario)
            return "El usuario fue agregado correctamente."
        else:
            return "El usuario ya existe en la lista."

    def eliminar_usuario(self, usuario):
        if usuario in self.usuarios:
            self.usuarios.remove(usuario)
            return "El usuario fue eliminado correctamente."
        else:
            return "El usuario no esta en la lista."
    
    def modificar_usuario(self, usuario, nuevo_nombre, nuevo_apellido, nuevo_dni, nuevo_correo):
        if usuario in self.usuarios:
            usuario._nombre = nuevo_nombre
            usuario._apellido = nuevo_apellido
            usuario._dni = nuevo_dni
            usuario._correo = nuevo_correo
            return "El usuario fue modificado correctamente."
        else:
            return "El usuario no esta en la lista."
    
    def listar_usuarios(self):
         return [usuario.mostrar_datos() for usuario in self.usuarios]
    