class Produto:
    def __init__(self, nome: str, codigo_produto: int, preco_venda: float, quant_estoque: int):
        self.__nome = nome
        self.__codigo_produto = codigo_produto
        self.__preco_venda = preco_venda
        self.__quant_estoque = quant_estoque
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
    
    @property
    def codigo_produto(self):
        return self.__codigo_produto
    
    @codigo_produto.setter
    def codigo_produto(self, codigo_produto: str):
        self.__codigo_produto = codigo_produto
    
    @property
    def preco_venda(self):
        return self.__preco_venda
    
    @preco_venda.setter
    def preco_venda(self, preco_venda: float):
        self.__preco_venda = preco_venda
    
    @property
    def quant_estoque(self):
        return self.__quant_estoque
    
    @quant_estoque.setter
    def quant_estoque(self, quant_estoque: int):
        self.__quant_estoque = quant_estoque