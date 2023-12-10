import os
import helpers
import database as db

# función bucle infinito
def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("========================")
        print("  GESTIÓN DE CLIENTES   ")
        print("========================")
        print("[1] Listar clientes     ")
        print("[2] Buscar cliente      ")
        print("[3] Añadir cliente      ")
        print("[4] Modificar cliente   ")
        print("[5] Borrar cliente      ")
        print("[6] Salir               ")
        print("========================")

        # capturo la opcion
        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Listando los clientes...\n")
            for cliente in db.Clientes.lista:
                print(cliente)
                #print(f"{cliente['dni']}: {cliente['nombre']} {cliente['apellido']}") 
        
        elif opcion == '2':
            print("Buscando un cliente...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print("Cliente no encontrado")
            
        elif opcion == '3':
            print("Añadiendo un cliente...\n")
            
            dni = None
            while True:
                dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
                if helpers.dni_valido(dni, db.Clientes.lista):
                    break
                
            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize()
            apellido = helpers.leer_texto(2, 30, "Apellido (2 a 30 char)").capitalize()
            db.Clientes.crear(dni, nombre, apellido)
            print("Cliente añadido correctamente")
            
        elif opcion == '4':
            print("Modificando un cliente...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                nombre = helpers.leer_texto(2, 30, f"Nombre (de 2 a 30 chars) [{cliente.nombre}]")
                apellido = helpers.leer_texto(2, 30, f"Apellido (de 2 a 30 chars) [{cliente.apellido}]")
                db.Clientes.modificar(cliente.dni, nombre, apellido)
                print("Cliente modificado correctamente.")
            else:
                print("Cliente no encontrado.")
            
        elif opcion == '5':
            print("Borrando un cliente...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
            print("Cliente eliminado correctamente.") if db.Clientes.borrar(
                dni) else print("No encontrado")
        
        elif opcion == '6':
            print("Saliendo...\n")
            break # rompe el bucle infinito

        input("\nPresiona ENTER para continuar...")