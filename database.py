import csv
import config

class Cliente:
    
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        
        # Este método se invoca cuando la clase necesita ser convertida a string
        def __str__(self):
            return f"({'dni': self.dni}) {self.nombre} {self.apellido}"
        
        def to_dict(self):
            return {'dni': self.dni, 'nombre': self.nombre, 'apellido': self.apellido}
        
class Clientes:
    
    lista = []
    with open(config.DATABASE_PATH, newline='\n') as portador:
        extract = csv.reader(portador, delimiter=';')
        for dni, nombre, apellido in extract:
            cliente = Cliente(dni,nombre, apellido)
            lista.append(cliente)            
    
    @staticmethod
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente

    @staticmethod
    def crear(dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        Clientes.guardar()
        return cliente

    @staticmethod
    def modificar(dni, nombre, apellido):
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellido = apellido
                Clientes.guardar()
                return Clientes.lista[indice]

    @staticmethod
    def borrar(dni):
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                cliente = Clientes.lista.pop(indice)
                Clientes.guardar()
                return cliente

    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as portador:
            writer = csv.writer(portador, delimiter=';')
            for cliente in Clientes.lista:
                writer.writerow((cliente.dni, cliente.nombre, cliente.apellido))
