from DAOs.dao import DAO
from entidade.cliente import Cliente

#cada entidade terá uma classe dessa, implementação bem simples.
class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('clientes.pkl')

    def add(self, cliente: Cliente):
        if((cliente is not None) and isinstance(cliente, Cliente) and isinstance(cliente.numero, str)):
            super().add(cliente.numero, cliente)

    def update(self, cliente: Cliente):
        if((cliente is not None) and isinstance(cliente, Cliente) and isinstance(cliente.numero, str)):
            super().update(cliente.numero, cliente)

    def get(self, key:str): #a key aqui é o numero do cliente
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str): #a key aqui é o numero do cliente ##estava selfself antes
        if(isinstance(key, str)):
            return super().remove(key)
