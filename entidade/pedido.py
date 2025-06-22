from entidade.fornecedor import Fornecedor
from entidade.transacao import Transacao
from entidade.produto import Produto
from datetime import datetime

class Pedido(Transacao):
    def __init__(self, quantidade: int, produto: Produto, data: datetime, valor: float, codigo: int, fornecedor: Fornecedor, frete: float, prazo_entrega: int):
        super().__init__(quantidade, produto, data, valor, codigo)
        self.__fornecedor = fornecedor
        self.__frete = frete
        self.__prazo_entrega = prazo_entrega
    
    @property
    def fornecedor(self):
        return self.__fornecedor
    
    @fornecedor.setter
    def fornecedor(self, fornecedor):
        self.__fornecedor = fornecedor
    
    @property
    def frete(self):
        return self.__frete
    
    @frete.setter
    def frete(self, frete):
        self.__frete = frete
    
    @property
    def prazo_entrega(self):
        return self.__prazo_entrega
    
    @prazo_entrega.setter
    def prazo_entrega(self, prazo_entrega):
        self.__prazo_entrega = prazo_entrega