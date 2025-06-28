from limite.tela_produto import TelaProduto
from entidade.produto import Produto
from excessoes.encontrado_na_lista_exception import EncontradoNaListaException
from excessoes.nao_encontrado_na_lista_exception import NaoEncontradoNaListaException
from DAOs.produto_dao import ProdutoDAO


class ControladorProdutos():
    def __init__(self, controlador_sistema):
        self.__produto_DAO = ProdutoDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_produto = TelaProduto()

    def pega_produto_por_codigo(self, codigo: int):
        for i in self.__produto_DAO.get_all():
            if i.codigo_produto == codigo:
                return i
        return None

    def incluir_produto(self):
        dados_produto = self.__tela_produto.pega_dados_produto()
        if dados_produto == None:
            return None
        i = self.pega_produto_por_codigo(dados_produto["codigo_produto"])
        try:
            if i is None:
                produto = Produto(dados_produto["nome"], 
                                  int(dados_produto["codigo_produto"]),
                                  float(dados_produto["preco_venda"]),
                                  int(dados_produto["quant_estoque"]))
                self.__produto_DAO.add(produto)
                self.__tela_produto.mostra_mensagem("Produto incluído com sucesso!")
            else:
                raise EncontradoNaListaException()
        except Exception as e:
            self.__tela_produto.mostra_mensagem(e)

    def alterar_preco_produto(self):
        self.lista_produtos()
        produtos = list(self.__produto_DAO.get_all())
        if len(produtos) == 0:
            return None
        codigo_produto = self.__tela_produto.seleciona_produto()
        if codigo_produto == None:
            return None
        produto = self.pega_produto_por_codigo(codigo_produto)
        try:
            if produto is not None:
                valor = self.__tela_produto.pega_dados_produto_alterar()
                if valor == None:
                    return None
                produto.preco_venda = float(valor)
                self.__produto_DAO.update(produto)
                self.__tela_produto.mostra_mensagem("Preço alterado com sucesso!")
            else:
                raise NaoEncontradoNaListaException("produto")
        except Exception as e:
            self.__tela_produto.mostra_mensagem(e)

    def alterar_estoque(self):
        self.lista_produtos()
        produtos = list(self.__produto_DAO.get_all())
        if len(produtos) == 0:
            return None
        codigo_produto = self.__tela_produto.seleciona_produto()
        if codigo_produto == None:
            return None
        produto = self.pega_produto_por_codigo(codigo_produto)
        try:
            if produto is not None:
                valor = self.__tela_produto.pega_dados_produto_alterar()
                if valor == None:
                    return None
                if int(valor) == valor:
                    produto.quant_estoque += int(valor)
                    self.__tela_produto.mostra_mensagem("Estoque alterado com sucesso!")
                    self.__produto_DAO.update(produto)
                else:
                    self.__tela_produto.mostra_mensagem("Coloque um valor inteiro!")
            else:
                raise NaoEncontradoNaListaException("produto")
        except Exception as e:
            self.__tela_produto.mostra_mensagem(e)

    def lista_produtos(self):
        produtos = list(self.__produto_DAO.get_all())
        if len(produtos) == 0:
            self.__tela_produto.mostra_mensagem("Não há produtos cadastrados.")
            return None
        else:
            dados_produto = []
            for produto in self.__produto_DAO.get_all():
                dado = {"nome": produto.nome,
                        "codigo_produto": produto.codigo_produto,
                        "preco_venda": produto.preco_venda,
                        "quant_estoque": produto.quant_estoque}
                dados_produto.append(dado)

            self.__tela_produto.mostra_produto(dados_produto)

    def excluir_produto(self):
        self.lista_produtos()
        produtos = list(self.__produto_DAO.get_all())
        if len(produtos) == 0:
            return None
        codigo_produto = self.__tela_produto.seleciona_produto()
        if codigo_produto == None:
            return None
        produto = self.pega_produto_por_codigo(int(codigo_produto))
        try:
            if produto is not None:
                self.__produto_DAO.remove(codigo_produto)
                self.__tela_produto.mostra_mensagem("Produto excluído com sucesso!")
            else:
                raise NaoEncontradoNaListaException("produto")
        except Exception as e:
            self.__tela_produto.mostra_mensagem(e)

    def atualizar_produto(self, produto):
        self.__produto_DAO.update(produto)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_produto,
                        2: self.alterar_preco_produto,
                        3: self.alterar_estoque,
                        4: self.lista_produtos,
                        5: self.excluir_produto,
                        0: self.retornar}
        while True:
            opcao_escolhida = self.__tela_produto.tela_opcoes()
            if opcao_escolhida in lista_opcoes:
                lista_opcoes[opcao_escolhida]()
            else:
                self.__tela_produto.mostra_mensagem("Opção inválida, escolha novamente\nA possivél causa é a a confirmação sem ter selecionado nada.")