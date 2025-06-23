from DAOs.dao import DAO
from entidade.vendedor import Vendedor

#cada entidade terá uma classe dessa, implementação bem simples.
class VendedorDAO(DAO):
    def __init__(self):
        super().__init__('vendedores.pkl')

    def add(self, vendedor: Vendedor):
        if((vendedor is not None) and isinstance(vendedor, Vendedor) and isinstance(vendedor.cpf, int)):
            super().add(vendedor.cpf, vendedor)

    def update(self, vendedor: Vendedor):
        if((vendedor is not None) and isinstance(vendedor, Vendedor) and isinstance(vendedor.cpf, int)):
            super().update(vendedor.cpf, vendedor)

    def get(self, key:int): #a key aqui é o cpf do vendedor
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int): #a key aqui é o cpf do vendedor ##estava selfself antes
        if(isinstance(key, int)):
            return super().remove(key)
