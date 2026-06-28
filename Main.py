from Biblioteca import Biblioteca
from Libro import Libro
from Prestamo import Prestamo
from Usuario_y_socio import Usuario

biblioteca = Biblioteca()

continuar_menu = True
while continuar_menu:
    print("Bienvenido a la Biblioteca")
    print("1. Libros")
    print("2. Usuarios")
    print("3. Préstamos")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print("Gestionar libros")
        print("1. Agregar libro")
        print("2. Modificar libro")
        print("3. Eliminar libro")
        print("4. Listar libros")
        opcion_libro = input("Elija una opción: ")
        if opcion_libro == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, isbn, fecha_publicacion=None, cantidad_paginas=None)
            biblioteca.agregar_libro(libro)
            print("El Libro fue agregado.")

        elif opcion_libro == "2":
            isbn = input("Ingrese el ISBN del libro que quiera modificar: ")
            libro = biblioteca.buscar_libro(isbn)
            if libro:
                nuevo_titulo = input("Ingrese el nuevo título del libro: ")
                nuevo_autor = input("Ingrese el nuevo autor del libro: ")
                nueva_fecha_publicacion = input("Ingrese la nueva fecha de publicación del libro: ")
                nuevo_cantidad_paginas = input("Ingrese la nueva cantidad de páginas del libro: ")
                biblioteca.modificar_libro(isbn, nuevo_titulo, nuevo_autor)
                print("El libro fue modificado.")
            else:
                print("El Libro no se ha encontrado.")   
         
        elif opcion_libro == "3":
            isbn = input("Ingrese el ISBN del libro que quiera eliminar: ")
            libro = biblioteca.buscar_libro(isbn)
            if libro:
                biblioteca.eliminar_libro(isbn)
                print("El libro fue eliminado.")
            else:
                print("El Libro no se ha encontrado.")        
        
        elif opcion_libro == "4":
            biblioteca.listar_libros()        
    
    elif opcion == "2":
        print("Gestionar usuarios")
        print("1. Agregar usuario")
        print("2. Modificar usuario")
        print("3. Eliminar usuario")
        print("4. Listar usuarios")
        opcion_usuario = input("Elija una opción: ")
        if opcion_usuario == "1":
            nombre = input("Ingrese el nombre del usuario: ")
            apellido = input("Ingrese el apellido del usuario: ")
            dni = input("Ingrese el DNI del usuario: ")
            correo = input("Ingrese el correo del usuario: ")
            usuario = Usuario(nombre, apellido, dni,correo)
            biblioteca.agregar_usuario(usuario)
            print("El usuario fue agregado.")

        elif opcion_usuario == "2":
            dni = input("Ingrese el DNI del usuario que quiera modificar: ")
            usuario = biblioteca.buscar_usuario(dni)
            if usuario:
                nuevo_nombre = input("Ingrese el nuevo nombre del usuario: ")
                nuevo_apellido = input("Ingrese el nuevo apellido del usuario: ")
                nuevo_correo = input("Ingrese el nuevo correo del usuario: ")
                biblioteca.modificar_usuario(dni, nuevo_nombre, nuevo_apellido)
                print("El usuario fue modificado.")
            else:
                print("El Usuario no se ha encontrado.")   
         
        elif opcion_usuario == "3":
            dni = input("Ingrese el DNI del usuario que quiera eliminar: ")
            usuario = biblioteca.buscar_usuario(dni)
            if usuario:
                biblioteca.eliminar_usuario(dni)
                print("El usuario fue eliminado.")
            else:
                print("El Usuario no se ha encontrado.")        
        
        elif opcion_usuario == "4":
            biblioteca.listar_usuarios()

    elif opcion == "3":
        print("Gestionar préstamos")
        print("1. Agregar préstamo")
        print("2. Modificar préstamo")
        print("3. Eliminar préstamo")
        print("4. Listar préstamos")
        opcion_prestamo = input("Elija una opción: ")
        if opcion_prestamo == "1":
            dni = input("Ingrese el DNI del usuario: ")
            usuario = biblioteca.buscar_usuario(dni)
            if usuario:
                isbn = input("Ingrese el ISBN del libro: ")
                libro = biblioteca.buscar_libro(isbn)
                if libro:
                    prestamo = Prestamo(usuario, libro,fecha_prestamo=None, fecha_devolucion=None)
                    biblioteca.agregar_prestamo(prestamo)
                    print("El préstamo fue agregado.")
                else:
                    print("El libro no se ha encontrado.")
            else:
                print("El usuario no se ha encontrado.")
    
        elif opcion_prestamo == "2":
            dni = input("Ingrese el DNI del usuario: ")
            usuario = biblioteca.buscar_usuario(dni)
            if usuario:
                isbn = input("Ingrese el ISBN del libro: ")
                libro = biblioteca.buscar_libro(isbn)
                if libro:
                    prestamo = biblioteca.buscar_prestamo(usuario, libro)


        elif opcion_prestamo == "3":
            dni = input("Ingrese el DNI del usuario: ")
            usuario = biblioteca.buscar_usuario(dni)
            if usuario:
                isbn = input("Ingrese el ISBN del libro: ")
                libro = biblioteca.buscar_libro(isbn)
                if libro:
                    prestamo = biblioteca.buscar_prestamo(usuario, libro)
                    if prestamo:
                        biblioteca.eliminar_prestamo(prestamo)
                        print("El préstamo fue eliminado.")
                    else:
                        print("El préstamo no se ha encontrado.")
        
        elif opcion_prestamo == "4":
            biblioteca.listar_prestamos()
    
    elif opcion == "4":
        continuar_menu = False
        print("usted ha salido del programa.")