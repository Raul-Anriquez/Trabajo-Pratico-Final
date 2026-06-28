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
            libro = Libro(titulo, autor, isbn)
            biblioteca.agregar_libro(libro)
            print("El Libro fue agregado.")

        elif opcion_libro == "2":
            isbn = input("Ingrese el ISBN del libro que quiera modificar: ")
            libro = biblioteca.buscar_libro(isbn)
            if libro:
                nuevo_titulo = input("Ingrese el nuevo título del libro: ")
                nuevo_autor = input("Ingrese el nuevo autor del libro: ")
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
    elif opcion == "3":
        print("Gestionar préstamos")
    elif opcion == "4":
        print("Saliendo del programa...")
        continuar_menu = False
            

