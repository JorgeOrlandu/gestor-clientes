import re
import helpers

clients = []

# añado mock data
clients.append({'nombre': 'Marta', 'apellido': 'Perez', 'dni': '456'})
clients.append({'nombre': 'Mario', 'apellido': 'Lara', 'dni': '9654'})
clients.append({'nombre': 'Juan', 'apellido': 'Jara', 'dni': '44544'})

def show(clients):
     print(f"{clients['dni']}: {clients['nombre']} {clients['apellido']}") 
            
def show_all():
    for client in clients:
        show(client)
        
def find():
    dni = input("Ingrese el DNI del cliente\n> ")
    for i, client in enumerate(clients):
        if client['dni'] == dni:
            show(client)
            return i, client
        
    print("No se encontro el cliente")
    return None

def add():
    client = dict()
    
    print("Introduce nombre (de 2 a 30 caracteres)")
    client['nombre'] = helpers.input_text(2, 30)
    
    print("Introduce apellido (de 2 a 30 caracteres)")
    client['apellido'] = helpers.input_text(2, 30)
    
    while True:
        print("Introduce DNI (2 números y un caracter en mayúscula)")
        dni = helpers.input_text(3, 3)
        if is_valid(dni):
            client['dni'] = dni
            break
        print("DNI incorrecto o en uso")
        
    clients.append(client)
    return client

def is_valid(dni):
    """
    >>> is_valid('47H') # No válido, en uso
    False
    
    >>> is_valid('X82') # No válido, incorrecto
    False
    
    >>> is_valid('21A') # Válido
    False
    """  
    
     # comprueba que el dni empieza con un patrón
    if not re.match('[0-9]{2}[A-Z]$', dni):
        print("DNI incorrecto, debe cumplir el formato.")
        return False
    
    # comprueba si dni existe
    for client in clients:
        if client['dni'] == dni:
            print("DNI utilizado por otro cliente.")
            return False
        
    return True

def edit():
  
    i, client = find()
    
    if client['dni']:
        print(f"Introduce nuevo nombre ({client['nombre']})")
        clients[i]['nombre'] = helpers.input_text(2,30)
        print(f"Introduce nuevo apellido ({client['apellido']})")
        clients[i]['apellido'] = helpers.input_text(2,30)
        return True
    return False

def delete():
    i, client = find()

    if client:
        client = clients.pop(i)
        return True
    return False
         

if __name__ == "__main__":
    import doctest
    doctest.testmod()