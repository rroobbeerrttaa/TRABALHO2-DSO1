from entidade.produto import Produto
from entidade.endereco import Endereco
from entidade.pessoa import Pessoa

class Fornecedor(Pessoa):
    def __init__(self, nome: str, numero: str, celular: int, produto: Produto, preco: float):
        super().__init__(nome, numero, celular)
        self.__produto = produto
        self.__preco = preco
        self.__enderecos = []

    @property
    def produto(self):
        return self.__produto

    @produto.setter
    def produto(self, produto: Produto):
        self.__produto = produto

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco: float):
        self.__preco = preco

    @property
    def enderecos(self):
        return self.__enderecos

    def incluir_endereco(self, cep: str, rua: str, numero: str):
        self.__enderecos.append(Endereco(cep, rua, numero))

    def remover_endereco(self, endereco: Endereco):
        self.__enderecos.remove(endereco)

