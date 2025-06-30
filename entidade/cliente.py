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
    
    def remover_compra(self, codigo_compra):
        compra_para_remover = None
        for compra in self.__compras:
            if compra.codigo == codigo_compra:
                compra_para_remover = compra
                break
        if compra_para_remover:
            self.__compras.remove(compra_para_remover)
