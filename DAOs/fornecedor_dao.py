from DAOs.dao import DAO
from entidade.fornecedor import Fornecedor

#cada entidade terá uma classe dessa, implementação bem simples.
class FornecedorDAO(DAO):
    def __init__(self):
        super().__init__('fornecedores.pkl')

    def add(self, fornecedor: Fornecedor):
        if((fornecedor is not None) and isinstance(fornecedor, Fornecedor) and isinstance(fornecedor.numero, int)):
            super().add(fornecedor.numero, fornecedor)

    def update(self, fornecedor: Fornecedor):
        if((fornecedor is not None) and isinstance(fornecedor, Fornecedor) and isinstance(fornecedor.numero, int)):
            super().update(fornecedor.cpf, fornecedor)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)