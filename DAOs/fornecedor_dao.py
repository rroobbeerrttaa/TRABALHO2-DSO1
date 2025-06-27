from DAOs.dao import DAO
from entidade.fornecedor import Fornecedor

class FornecedorDAO(DAO):
    def __init__(self):
        super().__init__('fornecedores.pkl')

    def add(self, fornecedor: Fornecedor):
        if((fornecedor is not None) and isinstance(fornecedor, Fornecedor) and isinstance(fornecedor.numero, str)):
            super().add(fornecedor.numero, fornecedor)

    def update(self, fornecedor: Fornecedor):
        if((fornecedor is not None) and isinstance(fornecedor, Fornecedor) and isinstance(fornecedor.numero, str)):
            super().update(fornecedor.numero, fornecedor)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)