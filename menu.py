from funciones import *

while True:
    mostrar_menu()
    opcion = input("Ingrese una de las opciones: ")
        
    match opcion:
        case "1":
            ruta_archivo = input("Ingrese la ruta del archivo csv: ")
            datos = cargar_csv(ruta_archivo)
            print("El archivo csv fue cargado exitosamente!")
        case "2":
            if datos:
                imprimir_lista(datos)
            else:
                print("Primero cargue el archivo CSV.")
        case "3":
            if datos:
                datos = asignar_rating(datos)
                print("Ratings asignados exitosamente.")
            else:
                print("Primero cargue el archivo CSV.")
        case "4":
            if datos:
                datos = asignar_genero(datos)
                print("Géneros asignados exitosamente.")
            else:
                print("Primero cargue el archivo CSV.")
        case "5":
            if datos:
                genero = input("Ingrese el género a filtrar, debe escribirlo tal cual esta (drama, comedia, acción, terror): ")
                filtrar_por_genero(datos, genero)
            else:
                print("Primero cargue el archivo CSV.")
        case "6":
            if datos:
                datos_ordenadas = ordenar_peliculas(datos)
                imprimir_lista(datos_ordenadas)
            else:
                print("Primero cargue el archivo CSV.")
        case "7":
            if datos:
                informar_mejor_rating(datos)
            else:
                print("Primero cargue el archivo CSV.")
        case "8":
            if datos:
                nombre_archivo = input("Ingrese el nombre del archivo JSON para guardar las películas: ")
                guardar_peliculas(datos, nombre_archivo)
            else:
                print("Primero cargue el archivo CSV.")
        case "9":
            exit()
        case _:
            print("Ingrese una opción válida!")