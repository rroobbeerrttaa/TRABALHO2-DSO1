from DAOs.dao import DAO
from entidade.vendedor import Vendedor

#cada entidade terá uma classe dessa, implementação bem simples.
class VendedorDAO(DAO):
    def __init__(self):
        super().__init__('vendedores.pkl')

    def add(self, vendedor: Vendedor):
        if((vendedor is not None) and isinstance(vendedor, Vendedor) and isinstance(vendedor.numero, str)):
            super().add(vendedor.numero, vendedor)

    def update(self, vendedor: Vendedor):
        if((vendedor is not None) and isinstance(vendedor, Vendedor) and isinstance(vendedor.numero, str)):
            super().update(vendedor.numero, vendedor)

    def get(self, key:str): #a key aqui é o numero do vendedor
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str): #a key aqui é o numero do vendedor ##estava selfself antes
        if(isinstance(key, str)):
            return super().remove(key)
