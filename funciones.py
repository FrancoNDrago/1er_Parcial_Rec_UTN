import csv
import json
import random

def cargar_csv(ruta_csv):
    datos_csv = []
    """
    Carga el archivo csv y devuelve este en formato de lista de diccionarios.
    
    Parametro: Ruta del archivo csv.
    Retorna: Las filas del archivo csv en una lista de diccionarios.
    """
    try:
        with open(ruta_csv, mode="r", encoding="utf-8") as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            for linea in lector_csv:
                datos_csv.append(linea)
        print("El archivo csv se cargo con exito.")
    except FileNotFoundError:
        print(f'No se encontro el archivo "{ruta_csv}". Corrobore que el nombre del archivo y la ruta sean correctos.')
    except Exception:
        print(f"Ocurrio un error al cargar el archivo csv {Exception}")
        
    return datos_csv                


def imprimir_lista(datos_csv):
    """
    Itera sobre los diccionarios y los imprime uno por uno.
    
    Parametro: Las listas de diccionarios.
    Retorna: Imprime dicha listas.
    """
    for movie in datos_csv:
        print(movie)


def asignar_rating(movies):
    """
    Asigna un rating aleatorio entre 1 y 10 con 1 decimal a cada pelicula.
    
    Parametro: Lista de diccionarios con las peliculas.
    Retorna: Lista de diccionarios con los ratings asignados.
    """
    for movie in movies:
        #movie["rating"] = random.randint(1, 10)
        movie["rating"] = round(random.uniform(1, 10), 1)
    
    return movies


def asignar_genero(movies):
    """
    Asigna un genero aleatorio a cada pelicula.
    
    Parametro: Lista de diccionarios con las peliculas.
    Retorna: Lista de diccionarios con los géneros asignados.
    """
    generos = {1: "drama", 2: "comedia", 3: "acción", 4: "terror"}
    for movie in movies:
        movie["genero"] = generos[random.randint(1, 4)]
    
    return movies


def filtrar_por_genero(movies, genero):
    """
    Filtra las peliculas por el género especificado y guarda el resultado en un archivo CSV.
    
    Parametro: Lista de diccionarios con las peliculas y el genero a filtrar.
    Retorna: No retorna nada, guarda el archivo filtrado.
    """
    peliculas_filtradas = [peli for peli in movies if peli["genero"] == genero]
    
    nombre_archivo = f"{genero}.csv"
    with open(nombre_archivo, mode="w", encoding="utf-8", newline="") as archivo_csv:
        campos = movies[0].keys()
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
        escritor_csv.writeheader()
        escritor_csv.writerows(peliculas_filtradas)
    
    print(f"Archivo {nombre_archivo} generado con éxito.")


def ordenar_peliculas(movies):
    """
    Ordena las peliculas por genero y por rating descendente dentro de cada genero.
    
    Parametro: Lista de diccionarios con las películas.
    Retorna: Lista de diccionarios ordenada.
    """
    return sorted(movies, key=lambda x: (x["genero"], -float(x["rating"])))


def informar_mejor_rating(movies):
    """
    Informa la película con el mejor rating.
    
    Parametro: Lista de diccionarios con las peliculas.
    Retorna: Título y rating de la película con el mejor rating.
    """
    mejor_pelicula = max(movies, key=lambda x: float(x["rating"]))
    print(f"Mejor película: {mejor_pelicula["titulo"]} con rating {mejor_pelicula["rating"]}")


def guardar_peliculas(movies, nombre_archivo):
    """
    Guarda la lista de peliculas en un archivo JSON.
    
    Parametro: Lista de diccionarios con las peliculas y el nombre del archivo.
    Retorna: No retorna nada, guarda el archivo JSON.
    """
    with open(nombre_archivo, mode="w", encoding="utf-8") as archivo_json:
        json.dump(movies, archivo_json, indent=4)
    print(f"Archivo {nombre_archivo} generado con exito.")


def mostrar_menu():
    print("---- MENU ----")
    print("1 - Cargar el archivo csv.")
    print("2 - Imprimir la lista.")
    print("3 - Asignar rating.")
    print("4 - Asignar género.")
    print("5 - Filtrar por género.")
    print("6 - Ordenar películas por mayor puntuación.")
    print("7 - Informar mejor rating.")
    print("8 - Guardar películas.")
    print("9 - Salir.")
