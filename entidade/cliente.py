from entidade.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, numero, celular):
        super().__init__(nome, numero, celular)
        self.__compras = []

    @property
    def compras(self):
        return self.__compras
    
    @compras.setter
    def compras(self, compras):
        self.__compras = compras
    
    def adicionar_compra(self, nova_compra):
        self.__compras.append(nova_compra)
    
    def remover_compra(self, compra):
        self.__compras(compra)