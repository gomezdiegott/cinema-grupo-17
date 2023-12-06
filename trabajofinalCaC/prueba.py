lista = [
    {
        "id": 94362,
        "titulo": "Ba\u00f1eros 1",
        "duracion": 1200,
        "genero": [
            "Comedia"
        ],
        "sinopsis": "Un grupo de hombres que eran ba\u00f1eros en la playa.",
        "pais_de_origen": "Argentina",
        "idioma": "Castellano",
        "clasificacion": [
            "PG-13"
        ],
        "calificacion": 0,
        # "disponible": true
    },
    {
        "id": 28062,
        "titulo": "Papa se volvio loco",
        "duracion": 90,
        "genero": [
            "Comedia"
        ],
        "sinopsis": "Una pareja que tiene una nueva luna de miel.",
        "pais_de_origen": "Argentina",
        "idioma": "Castellano",
        "clasificacion": [
            "ATP"
        ],
        "calificacion": 0,
        # "disponible": true
    },
    {
        "id": 15952,
        "titulo": "Mi pobre angelito",
        "duracion": 110,
        "genero": [
            "Comedia",
            "Drama"
        ],
        "sinopsis": "Un ni\u00f1o se queda solo en casa en navidad y sobrevive a unos hombres malvados.",
        "pais_de_origen": "EEUU",
        "idioma": "Ingles",
        "clasificacion": [
            "ATP"
        ],
        "calificacion": 0,
        # "disponible": true
    },
    {
        "id": 82206,
        "titulo": "Norbit",
        "duracion": 100,
        "genero": [
            "Comedia"
        ],
        "sinopsis": "Norbit y Rasputia estaban casados hasta que Norbit volvio a ver a su ex compa\u00f1era del orfanato.",
        "pais_de_origen": "EEUU",
        "idioma": "Ingles",
        "clasificacion": [
            "ATP"
        ],
        "calificacion": 0,
        # "disponible": true
    },
    {
        "id": 79825,
        "titulo": "hearvy a toda marcha",
        "duracion": 90,
        "genero": [
            "Ciencia ficci\u00f3n",
            "Animaci\u00f3n",
            "Rom\u00e1ntica"
        ],
        "sinopsis": "Un auto de carrera abandonado vuelve a la pista.",
        "pais_de_origen": "EEUU",
        "idioma": "Ingles",
        "clasificacion": [
            "ATP"
        ],
        "calificacion": 0,
        # "disponible": true
    },
    {
        "id": 98694,
        "titulo": "Juego de gemelas",
        "duracion": 120,
        "genero": [
            "Comedia",
            "Rom\u00e1ntica"
        ],
        "sinopsis": "Dos hermanas gemelas se conocen en un campamento y comienza su aventura para conocer a sus padres",
        "pais_de_origen": "EEUU",
        "idioma": "Ingles",
        "clasificacion": [
            "ATP"
        ],
        "calificacion": 0,
        # "disponible": true
    },
    {
        "id": 19861,
        "titulo": "Me case con un boludo",
        "duracion": 100,
        "genero": [
            "Comedia",
            "Drama"
        ],
        "sinopsis": "Una mujer se cansa de las actitudes de ni\u00f1o del marido.",
        "pais_de_origen": "Argentina",
        "idioma": "Castellano",
        "clasificacion": [
            "PG-13"
        ],
        "calificacion": 0,
        # "disponible": true
    },
    {
        "id": 77391,
        "titulo": "Titanic",
        "duracion": 125,
        "genero": [
            "Rom\u00e1ntica",
            "Drama",
            "Suspenso"
        ],
        "sinopsis": "Jack gana un viaje en barco y conoce al amor de su vida.",
        "pais_de_origen": "Inglaterra",
        "idioma": "Ingles",
        "clasificacion": [
            "PG"
        ],
        "calificacion": 0,
        # "disponible": true
    },
    {
        "id": 44463,
        "titulo": "Gladiador",
        "duracion": 155,
        "genero": [
            "Drama",
            "Acci\u00f3n",
            "Ciencia ficci\u00f3n"
        ],
        "sinopsis": "M\u00e1ximo, general romano, desea volver a casa, pero el emperador Marco Aurelio quiere que herede el imperio. Esto hace que C\u00f3modo ordene matar a su familia. M\u00e1ximo escapa de la muerte y regresa a Roma como gladiador para vengar la muerte de su familia.",
        "pais_de_origen": "EEUU",
        "idioma": "Ingles",
        "clasificacion": [
            "R"
        ],
        "calificacion": 0,
        #"disponible": true
    }
]


def indice_peli():
    titulo_buscado = input("Ingrese el titulo de la pelicula que desee buscar: ")
        #SABER INDEX de la peli de ??? PA' USARLO ABAJO
    for pelicula in lista:
        if pelicula["titulo"] == titulo_buscado:
            print(pelicula)
            posicion = lista.index(pelicula)
            print(posicion)
    return posicion

peli = indice_peli()
#print(peli)
def modifica(x):
    desea = input("Que desea modificar?: ")
    if desea == "titulo":
        new_titulo = input("Ingrese el nuevo titulo: ")
        lista[x]["titulo"] = new_titulo
        print(lista[x])
    elif desea == "duracion":
        new_duracion = int(input("Ingrese la nueva duracion: "))
        lista[x]["duracion"] = new_duracion #INDEX 
        print(lista[x])
    
modifica(peli)
        #NA, LO TUYO ES TREMENDO PIBE DGAJHGDAJHFDAJFDUKAYG


#HACER LO DE ARRIBA SEPARANDO LA FUNCION BUSCAR DE LA DE MODIFICACION
#EN LA NUEVA FUNCION PASAMOS EL INDICE DE LA PELICULA POR PARAMETRO Y TE AYUDA 
#CON EL CODE PARA QUE SEA MÁS FACIL YA QUE TENEMOS EL INDICE TOTALMENTE FIJO A CUALQUIER TIPO DE ESTRUCTURA.