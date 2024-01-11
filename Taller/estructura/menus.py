from estructura.utilidades import validar_opcion

def menu_principal_blockbuster():
    print("==========================================")
    print("  Sistema Gestor Peliculas Blockbuster           ")
    print("==========================================")
    print("1. Administrador de generos")
    print("2. Administrador de Actores")
    print("3. Gestor de informes")
    print("4. Gestor de peliculas")
    print("5. Salir")
    print("===========================================")
    op = validar_opcion("Selecciona una opción: ", 1, 5)
    return op

def menu_gestor_generos():
    print("====================================")
    print("          Gestor de Generos           ")
    print("====================================")
    print("1. Crear Genero")
    print("2. Listar Genero")
    print("3. Ir al menu principal")
    print("====================================")
    op = validar_opcion("Selecciona una opción: ", 1, 3)
    return op

def menu_gestor_actores():
    print("====================================")
    print("          Gestor de Actores           ")
    print("====================================")
    print("1. Crear Actor")
    print("2. Listar Actor")
    print("3. Ir al menu principal")
    print("====================================")
    op = validar_opcion("Selecciona una opción: ", 1, 3)
    return op

def menu_gestor_formatos():
    print("====================================")
    print("          Gestor de Formatos           ")
    print("====================================")
    print("1. Crear Formatos")
    print("2. Listar Formatos")
    print("3. Ir al menu principal")
    print("====================================")
    op = validar_opcion("Selecciona una opción: ", 1, 3)
    return op

def menu_gestor_pelicula():
    print("====================================")
    print("          Gestor de Peliculas          ")
    print("====================================")
    print("1. Agregar peliculas")
    print("2. Editar pelicula")
    print("3. Eliminar pelicula")
    print("4. Buscar pelicula")
    print("5. Listar peliculas")
    print("6. Menu principal")
    print("====================================")
    op = validar_opcion("Selecciona una opción: ", 1, 6)
    return op

def menu_gestor_informes():
    print("====================================")
    print("          Gestor de Informes          ")
    print("====================================")
    print("1. Listar las peliculas de un genero especifico")
    print("2. Listar las peliculas donde protagonistas sea Silvestre Stallone")
    print("3. Ir al menu principal")
    print("====================================")
    op = validar_opcion("Selecciona una opción: ", 1, 3)
    return op
