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
            isbn = int(input("Ingrese el ISBN del libro: "))
            fecha_publicacion = (input("Ingrese la fecha de publicación del libro: "))
            cantidad_paginas = int(input("Ingrese la cantidad de páginas del libro: "))
            libro = Libro(titulo, autor, isbn, fecha_publicacion, cantidad_paginas)
            biblioteca.agregar_libro(libro)
            print("El Libro fue agregado.")

        elif opcion_libro == "2":
            isbn = int(input("Ingrese el ISBN del libro que quiera modificar: "))
            libro = biblioteca.buscar_libro(isbn)
            if libro:
                nuevo_titulo = input("Ingrese el nuevo título del libro: ")
                nuevo_autor = input("Ingrese el nuevo autor del libro: ")
                nueva_fecha_publicacion = (input("Ingrese la nueva fecha de publicación del libro: "))
                nuevo_cantidad_paginas = int(input("Ingrese la nueva cantidad de páginas del libro: "))
                nuevo_ISBN = int(input("Ingrese el nuevo ISBN del libro: "))
                print(biblioteca.modificar_libro(libro,nuevo_titulo,nuevo_autor,nueva_fecha_publicacion,nuevo_cantidad_paginas,nuevo_ISBN))
        
            else:
                print("El Libro no se ha encontrado.")   
         
        elif opcion_libro == "3":
            isbn = int(input("Ingrese el ISBN del libro que quiera eliminar: "))
            libro = biblioteca.buscar_libro(isbn)
            if libro:
                biblioteca.eliminar_libro(libro)
                print("El libro fue eliminado.")
            else:
                print("El Libro no se ha encontrado.")        
        
        elif opcion_libro == "4":
            print("Estos son los libros que se encuentran en la biblioteca.")
            biblioteca.listar_libros()
            if not biblioteca.gestion_libros.libros:
             print("No hay libros registrados.")
    
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
            dni = int(input("Ingrese el DNI del usuario: "))
            correo = input("Ingrese el correo del usuario: ")
            while "@" not in correo:
             print("Correo inválido.")
             correo = input("Ingrese un correo válido: ")
            usuario = Usuario(nombre, apellido, dni,correo)
            biblioteca.agregar_usuario(usuario)
            print("El usuario fue agregado.")

        elif opcion_usuario == "2":
            dni = int(input("Ingrese el DNI del usuario que quiera modificar: "))
            usuario = biblioteca.buscar_usuario(dni)
            if usuario:
                nuevo_nombre = input("Ingrese el nuevo nombre del usuario: ")
                nuevo_apellido = input("Ingrese el nuevo apellido del usuario: ")
                nuevo_dni = int(input("Ingrese el nuevo DNI: "))
                nuevo_correo = input("Ingrese el correo del usuario: ")
                while "@" not in nuevo_correo:
                 print("Correo inválido.")
                 nuevo_correo = input("Ingrese un correo válido: ")
                print(biblioteca.modificar_usuario(usuario,nuevo_nombre,nuevo_apellido,nuevo_dni,nuevo_correo))
            else:
             print("El usuario no se ha encontrado.")
             
        elif opcion_usuario == "3":
            dni = int(input("Ingrese el DNI del usuario que quiera eliminar: "))
            usuario = biblioteca.buscar_usuario(dni)
            if usuario:
                biblioteca.eliminar_usuario(usuario)
                print("El usuario fue eliminado.")
            else:
                print("El Usuario no se ha encontrado.")        
        
        elif opcion_usuario == "4":
            print("Estos son los usuarios que se encuentran en la biblioteca.")
            biblioteca.listar_usuarios()
            if not biblioteca.gestion_usuarios.usuarios:
                print("No hay usuarios registrados.")

    elif opcion == "3":
        print("Gestionar préstamos")
        print("1. Agregar préstamo")
        print("2. Modificar préstamo")
        print("3. Eliminar préstamo")
        print("4. Listar préstamos")
        opcion_prestamo = input("Elija una opción: ")
        if opcion_prestamo == "1":
            dni = int(input("Ingrese el DNI del usuario: "))
            usuario = biblioteca.buscar_usuario(dni)
            if usuario:
                isbn = int(input("Ingrese el ISBN del libro: "))
                libro = biblioteca.buscar_libro(isbn)
                if libro:
                    prestamo = Prestamo(usuario, libro)
                    biblioteca.registrar_prestamo(prestamo)
                    print("El préstamo fue agregado.")
                else:
                    print("El libro no se ha encontrado.")
            else:
                print("El usuario no se ha encontrado.")
    
        elif opcion_prestamo == "2":
         dni = int(input("Ingrese el DNI del usuario: "))
         usuario = biblioteca.buscar_usuario(dni)

         if usuario:
          isbn = int(input("Ingrese el ISBN del libro: "))
          libro = biblioteca.buscar_libro(isbn)
          
          if libro:
            prestamo = biblioteca.buscar_prestamo(libro)
         

            if prestamo:
                nueva_fecha_devolucion = input("Ingrese la nueva fecha de devolución: ")
                print(biblioteca.modificar_prestamo(prestamo, nueva_fecha_devolucion))
            else:
              print("No se ha encontrado el préstamo.")
          else:
            print("El libro no se ha encontrado.")              
         else:
                print("No se ha encontrado el usuario.")
        elif opcion_prestamo == "3":
            dni = int(input("Ingrese el DNI del usuario: "))
            usuario = biblioteca.buscar_usuario(dni)
            if usuario:
                isbn = int(input("Ingrese el ISBN del libro: "))
                libro = biblioteca.buscar_libro(isbn)
                if libro:
                    prestamo = biblioteca.buscar_prestamo(libro)
                    if prestamo:
                        biblioteca.eliminar_prestamo(prestamo)
                        print("El préstamo fue eliminado.")
                    else:
                        print("El préstamo no se ha encontrado.")
                else:
                    print("El libro no ha sido encontrado")

            else:
                print("El usuario no se ha encontrado")
        
        elif opcion_prestamo == "4":
            print("Estos son los préstamos que se encuentran en la biblioteca.")
            biblioteca.listar_prestamos()
            if not biblioteca.gestion_prestamos.prestamos:
                print("No hay préstamos registrados.")
    elif opcion == "4":
        continuar_menu = False
        print("usted ha salido del programa.")