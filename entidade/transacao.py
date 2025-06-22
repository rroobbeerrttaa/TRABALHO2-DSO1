from datetime import datetime
from entidade.produto import Produto

class Transacao:
    def __init__(self, quantidade: int, produto: Produto, data: datetime, valor: float, codigo: int):
        self.__produto = produto
        self.__valor  = valor
        self.__quantidade = quantidade
        self.__data = data
        self.__codigo = codigo

    @property
    def produto(self):
        return self.__produto
    
    @produto.setter
    def produto(self, produto: Produto):
        self.__produto = produto
    
    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int):
        self.__quantidade = quantidade
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data: datetime):
        self.__data = data

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor: float):
        self.__valor = valor
 
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo