from DAOs.dao import DAO
from entidade.venda import Venda

#cada entidade terá uma classe dessa, implementação bem simples.
class VendaDAO(DAO):
    def __init__(self):
        super().__init__('vendas.pkl')

    def add(self, venda: Venda):
        if((venda is not None) and isinstance(venda, Venda) and isinstance(venda.codigo, int)):
            super().add(venda.codigo, venda)

    def update(self, venda: Venda):
        if((venda is not None) and isinstance(venda, Venda) and isinstance(venda.codigo, int)):
            super().update(venda.codigo, venda)

    def get(self, key:int): #a key aqui é o código da venda
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int): #a key aqui é o código da venda ##estava selfself antes
        if(isinstance(key, int)):
            return super().remove(key)
