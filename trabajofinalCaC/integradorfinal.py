import json
import random

def ABM_peliculas():
    opcion_submenu = input("Elija una opción: ")
    if opcion_submenu == "1":
        alta()
    elif opcion_submenu == "2":
        print(opcion2_submenu_1)
        modificacion_pelicula_existente()
    elif opcion_submenu == "3":
        print(opcion3_submenu_1)
        baja_pelicula()
    elif opcion_submenu == "4":
        return
    else:
        print("Opción incorrecta, vuelva a ingresar una opción")
        ABM_peliculas()



def calificacion_titulos():
    contador = 0
    while contador <= 10:
        for peliculas in random.choices(lista_peliculas):
                if peliculas["calificacion"] == 0:
                    print(peliculas)
                    desea = input("Desea calificar la pelicula? S/N: ")
                    while True:
                        if desea == "S":
                            new_calificacion = int(input("Ingrese la nueva calificacion del 1 al 10: "))
                            peliculas["calificacion"] = new_calificacion
                            grabar_archivo(lista_peliculas, "peliculasNew.json")
                            contador += 1
                            break
                        elif desea == "N":
                            contador += 1
                            break

                

             


def reportes_estadisticas():
    opcion_submenu = input("Elija una opción: ")
    if opcion_submenu == "1":
        print(opcion1_submenu_3)
    elif opcion_submenu == "2":
        print(opcion2_submenu_3)
    elif opcion_submenu == "3":
        print(opcion3_submenu_3)
    elif opcion_submenu == "4":
        return
    else:
        reportes_estadisticas()

#Alta de peliculas

def imprimir_generos(generos_disponibles):
        print("Generos disponibles para la pelicula: ")
        for x in range(0, len(generos_disponibles)):
            print(f"{x + 1} - {generos_disponibles[x]}")

def leer_archivo(nombre_archivo):
        with open(nombre_archivo, 'r') as conexion:
            return json.load(conexion)


def grabar_archivo(lista_peliculas, nombre_archivo):
        with open(nombre_archivo, "w") as conexion:
            json.dump(lista_peliculas, conexion, indent=4)

def alta():
        lista_peliculas = leer_archivo("peliculasNew.json")
        generos_disponibles = ("Acción", "Animación", "Comedia", "Drama", "Ciencia ficción", "Terror", "Suspenso", "Romántica")
        clasificacion = ["ATP" , "PG" , "PG-13" , "R", "NC-17"]
        clasificacion_vacio = []

        id_pelicula = random.randint(10000, 99999)
        titulo = input("Ingrese el titulo de la pelicula: ")
        generos = []
        imprimir_generos(generos_disponibles)   

        while True:
            rta_genero = input("Ingrese un genero para la pelicula: ")
            if rta_genero in generos_disponibles:
                generos.append(rta_genero)
            else:
                print("Ingrese un genero valido...")
                imprimir_generos(generos_disponibles)
                continue
            continua = input("Desea agregar otro genero?: (S/N)")
            if continua == "N":
                break
            elif continua == "S":
                continue
            else:
                print("Opcion incorrecta")
                continua = input("Desea agregar otro genero?: (S/N)")
                if continua == "N":
                    break
                elif continua == "S":
                    continue
        

        duracion = int(input("Ingrese la duracion de la pelicula en minutos: "))
        sinopsis = input("Escriba una sinopsis de la pelicula: ")
        pais_de_origen = input("Ingrese el país de origen de la pelicula: ")
        idioma = input("Ingrese el idioma de la pelicula: ")
        while True:
            clasificacion_ingresada = input("Ingrese una clasificación: ")
            if clasificacion_ingresada in clasificacion:
                clasificacion_vacio.append(clasificacion_ingresada)
            elif clasificacion_ingresada not in clasificacion:
                print("Opción invalida, elija una clasificación valida")
                continue
            break
        while True:
            calificacion = 0
            disponible = input("La pelicula está disponible? S/N: ")
            if disponible == "S":
                disponible = True
                break
            elif disponible == "N":
                disponible = False
                break
            else:
                print("Opción invalida, ingrese una opción valida")
                

        peliculas_a_agregar = {
            "id": id_pelicula,
            "titulo": titulo,
            "duracion": duracion,
            "genero": generos,
            "sinopsis": sinopsis,
            "pais_de_origen": pais_de_origen,
            "idioma": idioma,
            "clasificacion": clasificacion_vacio,
            "calificacion": calificacion,
            "disponible": disponible
        }

        lista_peliculas.append(peliculas_a_agregar)
        grabar_archivo(lista_peliculas, "peliculasNew.json")
        print("Película agregada exitosamente.")         

lista_peliculas = leer_archivo("peliculasNew.json")

def buscar_titulo_id():
    while True:
        id_buscado = int(input("Ingrese id:"))
        for pelicula in lista_peliculas:
            if pelicula['id'] == id_buscado:
                print(pelicula)
                posicion = lista_peliculas.index(pelicula)
                print(posicion)
                desea = input("Que desea modificar?: ")
                if desea == "titulo":
                    new_titulo = input("Ingrese el nuevo titulo: ")
                    lista_peliculas[posicion]["titulo"] = new_titulo
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "duracion":
                    new_duracion = int(input("Ingrese la nueva duracion: "))
                    lista_peliculas[posicion]["duracion"] = new_duracion #INDEX 
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "genero":
                    print("hacer")
                elif desea == "sinopsis":
                    new_sinopsis = input("Ingrese la nueva sinopsis: ")
                    lista_peliculas[posicion]["sinopsis"] = new_sinopsis
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "pais de origen":
                    new_pais = input("Ingrewse el nuevo país de origen: ")
                    lista_peliculas[posicion]["pais_de_origen"] = new_pais
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "idioma":
                    new_idioma = input("Ingrese el nuevo idioma: ")
                    lista_peliculas[posicion]["idioma"] = new_idioma
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "clasificacion":
                    new_clasificacion = input("Ingrese la nueva clasificacion: ")
                    lista_peliculas[posicion]["clasificacion"] = new_clasificacion
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "calificacion":
                    print("hacer")
                elif desea == "disponible":
                    while True:
                        new_disponible = input("Está disponible la pelicula? S/N: ")
                        if new_disponible == "S":
                            lista_peliculas[posicion]["disponible"] = True
                            print(pelicula)
                            grabar_archivo(lista_peliculas, "peliculasNew.json")
                            break
                        elif new_disponible == "N":
                            lista_peliculas[posicion]["disponible"] = False
                            print(pelicula)
                            grabar_archivo(lista_peliculas, "peliculasNew.json")
                            break
                        else:
                            print("La opción ingresada es incorrecta")

                #
        else:
            print("El titulo de la pelicula es incorrecto")
            continue
        

print(lista_peliculas[0]['duracion'])
def buscar_pelicula_titulo(lista_peliculas):
    while True:
        titulo_buscado = input("Ingrese el titulo de la pelicula que desee buscar: ")
        for pelicula in lista_peliculas:
            if titulo_buscado == pelicula['titulo']:
                print(pelicula)
                posicion = lista_peliculas.index(pelicula)
                print(posicion)
                desea = input("Que desea modificar?: ")
                if desea == "titulo":
                    new_titulo = input("Ingrese el nuevo titulo: ")
                    lista_peliculas[posicion]["titulo"] = new_titulo
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "duracion":
                    new_duracion = int(input("Ingrese la nueva duracion: "))
                    lista_peliculas[posicion]["duracion"] = new_duracion #INDEX 
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "genero":
                    print("hacer")
                elif desea == "sinopsis":
                    new_sinopsis = input("Ingrese la nueva sinopsis: ")
                    lista_peliculas[posicion]["sinopsis"] = new_sinopsis
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "pais de origen":
                    new_pais = input("Ingrewse el nuevo país de origen: ")
                    lista_peliculas[posicion]["pais_de_origen"] = new_pais
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "idioma":
                    new_idioma = input("Ingrese el nuevo idioma: ")
                    lista_peliculas[posicion]["idioma"] = new_idioma
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "clasificacion":
                    new_clasificacion = input("Ingrese la nueva clasificacion: ")
                    lista_peliculas[posicion]["clasificacion"] = new_clasificacion
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "disponible":
                    while True:
                        new_disponible = input("Está disponible la pelicula? S/N: ")
                        if new_disponible == "S":
                            lista_peliculas[posicion]["disponible"] = True
                            print(pelicula)
                            grabar_archivo(lista_peliculas, "peliculasNew.json")
                            break
                        elif new_disponible == "N":
                            lista_peliculas[posicion]["disponible"] = False
                            print(pelicula)
                            grabar_archivo(lista_peliculas, "peliculasNew.json")
                            break
                        else:
                            print("La opción ingresada es incorrecta")

                #
        else:
            print("El titulo de la pelicula es incorrecto")
            continue
        

def modificacion_pelicula_existente():
    opcion_submenu = input("Elija una opción: ")
    if opcion_submenu == "1":
        buscar_titulo_id()
    elif opcion_submenu == "2":
        buscar_pelicula_titulo(lista_peliculas)
    elif opcion_submenu == "3":
        print(submenu_1)
        ABM_peliculas()
    else:
        modificacion_pelicula_existente()

def baja_id():
    while True:
        id_buscado = int(input("Ingrese el id de la pelicula que desee eliminar: "))
        for pelicula in lista_peliculas:
            if pelicula["id"] == id_buscado:
                print(pelicula)
                posicion = lista_peliculas.index(pelicula)
                lista_peliculas.pop(posicion)
                print("La pelicula ha sido eliminada correctamente")
                grabar_archivo(lista_peliculas, "peliculasNew.json")
                break
        
def baja_titulo():
    while True:
        titulo_buscado = input("Ingrese el titulo de la pelicula que desee eliminar: ")
        for pelicula in lista_peliculas:
            if pelicula["titulo"] == titulo_buscado:
                print(pelicula)
                posicion = lista_peliculas.index(pelicula)
                lista_peliculas.pop(posicion)
                print("La pelicula ha sido eliminada correctamente")
                grabar_archivo(lista_peliculas, "peliculasNew.json")
                break

def baja_pelicula():
    opcion_submenu = input("Elija una opción: ")
    if opcion_submenu == "1":
        baja_id()
    elif opcion_submenu == "2":
        baja_titulo()
    elif opcion_submenu == "3":
        print(opcion3_subsubsubmenu_1)
    else:
        baja_pelicula() 
def menu_inicio():
    while True:
        print(menu)
        opcionUsuario = input("ingrese la opcion que desea :")
        if opcionUsuario == "1":
            print(submenu_1)
            ABM_peliculas()
        elif opcionUsuario == "2":
            calificacion_titulos()
        elif opcionUsuario == "3":
            print(submenu_3)
            reportes_estadisticas()
        elif opcionUsuario == "4":
            print("Saliste del programa, Muchas gracias por utilizar CINEMA+")
            break
        else:
            print("opción invalida")
            continue
        

#TODO
menu = "CINEMA+ \n 1. ABM de películas \n 2. Calificación de títulos \n 3. Reportes y estadísticas \n 4. Salir"
submenu_1 = "CINEMA+ \n Alta, Baja y modificación de películas \n 1. Alta de nueva película \n 2. Modificación de película existente \n 3. Baja de película (eliminar) \n 4. Volver"
opcion2_submenu_1 = "CINEMA+ \n Modificar película existente \n 1. Buscar por id \n 2. Buscar por titulo \n 3. Volver"
opcion3_submenu_1 = "CINEMA+ \n Eliminar una película existente \n 1. Buscar por id \n 2. Buscar por titulo \n 3. Volver"
opcion4_submenu_1 = "Volver"
opcion3_subsubmenu_1 = "Volver"
opcion3_subsubsubmenu_1 = "Volver"
submenu_2 = "CALIFICACION DE TITULOS"
submenu_3 = "CINEMA+ \n Reportes y estadísticas \n 1. Listado de películas \n 2. Películas de mayor puntaje \n 3. Porcentaje de películas disponibles en la plataforma \n 4. Volver"
opcion1_submenu_3 = "Titulo, Género(s), Calificación ordenado por titulo"
opcion2_submenu_3 = "Listar titulo, género y calificación de las 15 películas de mayor puntaje."
opcion3_submenu_3 = "Imprimir histograma en porcentaje con * de películas disponible contra películas no disponibles."
opcion4_submenu_3 = "Antes de salir, debe preguntarle al usuario si desea finalizar el programa."
submenu_4 = "Saliste del programa. BYE"
#WHILE
while True:
    print(menu)
    opcionUsuario = input("ingrese la opcion que desea :")
    if opcionUsuario == "1":
        print(submenu_1)
        ABM_peliculas()
    elif opcionUsuario == "2":
        calificacion_titulos()
    elif opcionUsuario == "3":
        print(submenu_3)
        reportes_estadisticas()
    elif opcionUsuario == "4":
        print("Saliste del programa, Muchas gracias por utilizar CINEMA+")
        break
    else:
        print("opción invalida")
        continue
