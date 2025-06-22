from controle.controlador_vendas import ControladorVendas
from controle.controlador_fornecedores import ControladorFornecedores
from controle.controlador_produtos import ControladorProdutos
from controle.controlador_pessoas import ControladorPessoas
from controle.controlador_pedidos import ControladorPedidos
from controle.controlador_relatorios import ControladorRelatorios
from limite.tela_sistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__controlador_vendas = ControladorVendas(self)
        self.__controlador_fornecedores = ControladorFornecedores(self)
        self.__controlador_produtos = ControladorProdutos(self)
        self.__controlador_pessoas = ControladorPessoas(self)
        self.__controlador_pedidos = ControladorPedidos(self)
        self.__controlador_relatorios = ControladorRelatorios(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_vendas(self):
        return self.__controlador_vendas

    @property
    def controlador_fornecedores(self):
        return self.__controlador_fornecedores

    @property
    def controlador_produtos(self):
        return self.__controlador_produtos

    @property
    def controlador_pessoas(self):
        return self.__controlador_pessoas

    @property
    def controlador_pedidos(self):
        return self.__controlador_pedidos
    
    @property
    def controlador_relatorios(self):
        return self.__controlador_relatorios

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_vendas(self):
        self.__controlador_vendas.abre_tela()

    def cadastra_fornecedor(self):
        self.__controlador_fornecedores.abre_tela()

    def cadastra_produto(self):
        self.__controlador_produtos.abre_tela()

    def cadastra_pessoa(self):
        self.__controlador_pessoas.abre_tela()

    def cadastra_pedido(self):
        self.__controlador_pedidos.abre_tela()
    
    def cadastra_relatorio(self):
        self.__controlador_relatorios.abre_tela()

    def abre_relatorios(self):
        self.__controlador_relatorios.abre_tela()

    def encerra_sistema(self):
        self.__tela_sistema.mostra_mensagem("!!!Obrigada por utilizar os serviços da A5!!!")
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_vendas,
                        2: self.cadastra_fornecedor,
                        3: self.cadastra_produto,
                        4: self.cadastra_pessoa,
                        5: self.cadastra_pedido,
                        6: self.abre_relatorios,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            if opcao_escolhida in lista_opcoes:
                lista_opcoes[opcao_escolhida]()
            else:
                self.__tela_sistema.mostra_mensagem("Opção inválida, escolha novamente.")