from estructura.utilidades import limpiar_pantalla
from estructura.menus import menu_gestor_actores, menu_gestor_formatos, menu_gestor_generos, menu_gestor_informes, menu_gestor_pelicula, menu_principal_blockbuster
from desarrollo.codigo import crear_genero, listar_genero, crear_actor, listar_actor, crear_formato, listar_formato, crear_pelicula




def generos():
    limpiar_pantalla()
    op = menu_gestor_generos()
    if op == 1:
        crear_genero()
    if op == 2:
        listar_genero()
    if op == 3:
        menu_principal_blockbuster()

def actores():
    limpiar_pantalla()
    op = menu_gestor_actores()
    if op == 1:
        crear_actor()
    if op == 2:
        listar_actor()
    if op == 3:
        menu_principal_blockbuster()

def formatos():
    limpiar_pantalla()
    op = menu_gestor_formatos()
    if op == 1:
        crear_formato()
    if op == 2:
        listar_formato()

def peliculas():
    limpiar_pantalla()
    op = menu_gestor_pelicula()
    if op == 1:
        crear_pelicula()
        
           

while True:
    op = menu_principal_blockbuster()
    if op ==1:
        generos()
    if op == 2:
        actores()
    if op == 3:
        formatos()
    if op == 4:
        peliculas()
    elif op==5:
        print("Sliendo")
        break
