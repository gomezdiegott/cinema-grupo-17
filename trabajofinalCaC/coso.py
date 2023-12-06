# NO SIRVE PARA EL TP PERO QUIZÁ SÍ PARA OTRA COSA

def modificar_pelicula_titulo():
    duracion = input("Que desea modificar?: ")
    if duracion == "duracion":
        for pelicula in lista_peliculas:
            new_duracion = int(input("Ingrese la nueva duracion: "))
            pelicula["duracion"] = new_duracion
            grabar_archivo(lista_peliculas, "peliculasNew.json")

    
    
    # pregunta = input("Qué desea modificar? ")
    # if pregunta == "duracion":
    #     duracion = int(input("Cuál es la nueva duración? "))
    #     print(lista_peliculas['duracion'])
    #     grabar_archivo(lista_peliculas[]['duracion'], "peliculasNew.json")