import json
print("1. Mostrar campers.")
print("2. Buscar campers.")
print("3. Registrar campers.")
print("4. Salir.")

opcion = 0

while opcion!=4:
        opcion = int(input("Ingrese una opcion: "))


        if opcion == 1:
            file = open("info.json")
            users= json.load(file)
            students = users.get('students', [])
            for user in students:
                print("Nombre del usuario:", user["name"], ", edad:", user["age"])
                file.close()
        elif opcion == 2:
            busqueda  = input("ingrese el nombre a buscar: ")
            file = open("info.json")
            users = json.load(file)
            lista = []
            for user in users:
                lista.append(user["name"])
                file.close()
            indice = 1
            while indice < len(lista):
                 if lista[indice] == busqueda:
                      print("El camper ",lista[indice]," se encuentra en la base de datos")
                 else:
                    print("No se encuetra el camper en nuestra base de datos.")

                 indice = indice +1
        elif opcion == 3:
             with open('info.json','r') as datos:
                  new_datos = json.load(datos)
                  name = input("Ingrese nombre de estudiante: ")
                  edad = input("Ingrese la edad del estudiante: ")
                  car = input("Ingrese el carro: ")
                  new_camper = {'name':name, 'age':edad, 'car':car}

                  new_datos['students'].append(new_camper)

             with open('info.json','w') as datos:
                  json.dump(new_datos, datos, indent=2)
                  print("persona registrada.")


            #print(len(lista))
        elif opcion == 4:
            print("Saliendo...")
            print("Gracias por usar nuestros servicios.")
        else :
            print("ERROR, OPCION NO VALIDA")