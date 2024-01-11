import json

def crear_genero():
    genero = {}
    genero["id"] = (input("Ingrese el ID del Genero a registrar: "))

    file = "data/generos.json"

    try:
        with open(file, "r") as genero_file:
            generos = json.load(genero_file)
    except json.JSONDecodeError:
        generos = []

    for existing_genero in generos:
        if existing_genero["id"] == genero["id"]:
            print("Lo siento, este genero ya se encuentra en la base de datos.")
            return

    genero["nombre"] = input("Ingrese el nombre del genero: ")
    generos.append(genero)

    with open(file, "w") as genero_file:
        json.dump(generos, genero_file, indent=2)

    print("¡Enhorabuena!, el Genero se ha registrado exitosamente...")

def listar_genero():
        try:
            with open("data/generos.json", "r") as file:
                generos = json.load(file)
        except json.JSONDecodeError:
            generos = []

        for genero in generos:
            print("Id: {}\nNombre: {}".format(
            genero["id"],
            genero["nombre"],
            '-' * 30  
        ))

def crear_actor():
    actor = {}
    actor["id"] = (input("Ingrese el ID del Actor a registrar: "))

    file = "data/actores.json"

    try:
        with open(file, "r") as actor_file:
            actores = json.load(actor_file)
    except json.JSONDecodeError:
        actores = []

    for existing_actor in actores:
        if existing_actor["id"] == actor["id"]:
            print("Lo siento, este Actor ya se encuentra en la base de datos.")
            return

    actor["nombre"] = input("Ingrese el nombre del genero: ")
    actores.append(actor)

    with open(file, "w") as actor_file:
        json.dump(actores, actor_file, indent=2)

    print("¡Enhorabuena!, el Actor se ha registrado exitosamente...")

def listar_actor():
    try:
        with open("data/actores.json", "r") as file:
                actores = json.load(file)
    except json.JSONDecodeError:
        actores = []

    for actor in actores:
        print("Id: {}\nNombre: {}".format(
        actor["id"],
        actor["nombre"],
        '-' * 30  
    ))

def crear_formato():
    formato = {}
    formato["id"] = (input("Ingrese el ID del Formato a registrar: "))

    file = "data/formatos.json"

    try:
        with open(file, "r") as formato_file:
            formatos = json.load(formato_file)
    except json.JSONDecodeError:
        formatos = []

    for existing_formato in formatos:
        if existing_formato["id"] == formato["id"]:
            print("Lo siento, este Formato ya se encuentra en la base de datos.")
            return

    formato["nombre"] = input("Ingrese el nombre del Formato: ")
    formatos.append(formato)

    with open(file, "w") as formato_file:
        json.dump(formatos, formato_file, indent=2)

    print("¡Enhorabuena!, el Formato se ha registrado exitosamente...")

def listar_formato():
    try:
        with open("data/formatos.json", "r") as file:
                formatos = json.load(file)
    except json.JSONDecodeError:
        formatos = []

    for formato in formatos:
        print("Id: {}\nNombre: {}".format(
        formato["id"],
        formato["nombre"],
        '-' * 30  
    ))  

def crear_pelicula():

    pelicula = {}
    pelicula["id"] = (input("Ingrese el ID de la pelicula a registrar: "))

    file = "data/peliculas.json"

    try:
        with open(file, "r") as pelicula_file:
            peliculas = json.load(pelicula_file)
    except json.JSONDecodeError:
        peliculas = []

    for existing_pelicula in peliculas:
        if existing_pelicula["id"] == pelicula["id"]:
            print("Lo siento, esta Pelicula ya se encuentra en la base de datos.")
            return

    pelicula["nombre"] = input("Ingrese el nombre de la Pelicula: ")
    pelicula["duracion"] = int(input("Ingrese la duracion de la pelicula: "))
    pelicula["sinopsis"] = input("Ingrese la sinopsis de la pelicula: ")
    
    file_genero = open("data/generos.json")
    generos = json.load(file_genero)
    lista_genero_codigo = []
    lisa_genero_nombre = []
    for genero in generos:
        lista_genero_codigo.append(genero["id"])
        lisa_genero_nombre.append(genero["nombre"])
        file_genero.close()
    i = 0
    while i < len(lista_genero_codigo):
        print("---------------------------")
        print("Generos disponibles:")
        print(lista_genero_codigo[i],lisa_genero_nombre[i])
        i = i + 1
    i2 = 0
    print("--------------------------------")
    id_genero = input("Seleccione el ID del genero: ")
    while i2 < len(lista_genero_codigo):
        if lista_genero_codigo[i2] == id_genero:
            pelicula["genero_id"] = id_genero
            pelicula["genero_nombre"] = lisa_genero_nombre[i2]
        i2 = i2 + 1
    
   
    file_actor = open("data/actores.json")
    actores = json.load(file_actor)
    lista_actores_id = []
    lista_actores_nombre = []
    for actor in actores:
        lista_actores_id.append(actor["id"])
        lista_actores_nombre.append(actor["nombre"])
        file_actor.close()
    i3 = 0
    while i3 < len(lista_actores_id):
        print("--------------------------------")
        print("Actores disponibles:")
        print(lista_actores_id[i3],lista_actores_nombre[i3])
        i3 = i3 + 1
    i4 = 0
    print("--------------------------------")
    id_actor = input("Seleccione el ID del actor: ")
    while i4 < len(lista_genero_codigo):
        if lista_actores_id[i4] == id_actor:
            pelicula["genero_id"] = id_actor
            pelicula["genero_nombre"] = lista_actores_nombre[i4]
        i4 = i4 + 1

    pelicula["rol_actor"] = input("Ingrese el rol del actor para la pelicula: ")

    file_formato = open("data/formatos.json")
    formatos = json.load(file_formato)
    lista_formatos_id = []
    lista_formatos_nombre = []
    for formato in formatos:
        lista_formatos_id.append(formato["id"])
        lista_formatos_nombre.append(formato["nombre"])
        file_actor.close()
    i5 = 0
    while i5 < len(lista_formatos_id):
        print("--------------------------------")
        print("Formatos disponibles:")
        print(lista_formatos_id[i5],lista_formatos_nombre[i5])
        i5 = i5 + 1
    i6 = 0
    print("--------------------------------")
    id_formato = input("Seleccione el ID del formato: ")
    while i6 < len(lista_formatos_id):
        if lista_formatos_id[i6] == id_formato:
            pelicula["formato_id"] = id_formato
            pelicula["formato_nombre"] = lista_formatos_nombre[i6]
        i6 = i6 + 1


    pelicula["NroCopias"] = input("Ingrese el numero de copias: ")
    pelicula["valorPrestamo"] = input("Ingrese el volor del prestamo: ")
    
    peliculas.append(pelicula)

    with open(file, "w") as pelicula_file:
        json.dump(peliculas, pelicula_file, indent=2)

    print("¡Enhorabuena!, la Pelicula se ha registrado exitosamente...")

