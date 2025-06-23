from limite.tela_produto import TelaProduto
from entidade.produto import Produto
from excessoes.encontrado_na_lista_exception import EncontradoNaListaException
from excessoes.nao_encontrado_na_lista_exception import NaoEncontradoNaListaException


class ControladorProdutos():
    def __init__(self, controlador_sistema):
        self.__produtos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_produto = TelaProduto()

        caneca = Produto("caneca", 1, 20.00, 10) 
        camisa = Produto('camisa', 2, 40.00, 6)
        self.__produtos.append(caneca)
        self.__produtos.append(camisa)

    @property
    def produtos(self):
        return self.__produtos

    def pega_produto_por_codigo(self, codigo: int):
        for i in self.__produtos:
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
                self.__produtos.append(produto)
                self.__tela_produto.mostra_mensagem("Produto incluído com sucesso!")
            else:
                raise EncontradoNaListaException()
        except Exception as e:
            self.__tela_produto.mostra_mensagem(e)

    def alterar_preco_produto(self):
        self.lista_produtos()
        if len(self.__produtos) == 0:
            return None
        codigo_produto = self.__tela_produto.seleciona_produto()
        if codigo_produto == None:
            return None
        produto = self.pega_produto_por_codigo(codigo_produto)
        try:
            if produto is not None:
                valor = self.__tela_produto.pega_dados_produto_alterar()
                if valor == None:
                    return 
                produto.preco_venda = float(valor)
                self.__tela_produto.mostra_mensagem("Preço alterado com sucesso!")
            else:
                raise NaoEncontradoNaListaException("produto")
        except Exception as e:
            self.__tela_produto.mostra_mensagem(e)

    def alterar_estoque(self):
        self.lista_produtos()
        if len(self.__produtos) == 0:
            return None
        codigo_produto = self.__tela_produto.seleciona_produto()
        if codigo_produto == None:
            return None
        produto = self.pega_produto_por_codigo(codigo_produto)
        try:
            if produto is not None:
                valor = self.__tela_produto.pega_dados_produto_alterar()
                if valor == None:
                    return
                if isinstance(valor, float):
                    produto.quant_estoque += int(valor)
                    self.__tela_produto.mostra_mensagem("Estoque alterado com sucesso!")
                else:
                    self.__tela_produto.mostra_mensagem("Coloque um valor inteiro!")
            else:
                raise NaoEncontradoNaListaException("produto")
        except Exception as e:
            self.__tela_produto.mostra_mensagem(e)

    def lista_produtos(self):
        if len(self.__produtos) == 0:
            self.__tela_produto.mostra_mensagem("Não há produtos cadastrados.")
            return None
        else:
            dados_produto = []
            for produto in self.__produtos:
                dado = {"nome": produto.nome,
                         "codigo_produto": produto.codigo_produto,
                         "preco_venda": produto.preco_venda,
                         "quant_estoque": produto.quant_estoque}
                dados_produto.append(dado)

            self.__tela_produto.mostra_produto(dados_produto)

    def excluir_produto(self):
        self.lista_produtos()
        if len(self.__produtos) == 0:
            return None
        codigo_produto = int(self.__tela_produto.seleciona_produto())
        if codigo_produto == None:
            return None
        produto = self.pega_produto_por_codigo(codigo_produto)
        try:
            if produto is not None:
                self.__produtos.remove(produto)
                self.__tela_produto.mostra_mensagem("Produto excluído com sucesso!")
            else:
                raise NaoEncontradoNaListaException("produto")
        except Exception as e:
            self.__tela_produto.mostra_mensagem(e)

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