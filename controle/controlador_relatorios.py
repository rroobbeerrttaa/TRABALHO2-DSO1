from limite.tela_relatorios import TelaRelatorios
from excessoes.nao_encontrado_na_lista_exception import NaoEncontradoNaListaException


class ControladorRelatorios():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_relatorios = TelaRelatorios()

    def gerar_relatorio_rentabilidade(self):
        produtos = self.__controlador_sistema.controlador_produtos.get_all_produtos()
        if not produtos:
            self.__tela_relatorios.mostra_mensagem("Não há produtos para gerar o relatório de rentabilidade.")
            return None

        # Coleta todos os fornecedores uma vez para otimização
        fornecedores = list(self.__controlador_sistema.controlador_fornecedores.get_all_fornecedores())

        for produto in produtos:
            preco_compra = None
            for fornecedor in fornecedores:
                if fornecedor.produto and fornecedor.produto.codigo_produto == produto.codigo_produto:
                    preco_compra = fornecedor.preco
                    break
            
            lucro_unidade = "N/A"
            if preco_compra is not None:
                lucro_unidade = produto.preco_venda - preco_compra
            
            dados_rentabilidade = { 
                "nome": produto.nome,
                "codigo_produto": produto.codigo_produto,
                "preco_venda": produto.preco_venda,
                "preco_compra": preco_compra if preco_compra is not None else "Sem preço de compra", #pesquisei para poder fazer
                "lucro_unidade": lucro_unidade
            }
            self.__tela_relatorios.mostra_rentabilidade_produto(dados_rentabilidade)

    def analisar_produtos_mais_vendidos(self):
        vendas = self.__controlador_sistema.controlador_vendas.get_all_vendas()
        if not vendas:
            self.__tela_relatorios.mostra_mensagem("Não há vendas registradas para análise.")
            return None

        todos_produtos_vendidos = {}
        lista_vendas = list(vendas)
        for venda in lista_vendas[:4]: # Apenas os 3 produtos mais vendidos PRECISA SER LISTA
            codigo_produto = int(venda.produto.codigo_produto)
            if codigo_produto not in todos_produtos_vendidos:
                todos_produtos_vendidos[codigo_produto] = {
                    "nome": venda.produto.nome,
                    "codigo_produto": codigo_produto,
                    "quantidade_total_vendida": 0,
                    "valor_total_vendido": 0
                }
            todos_produtos_vendidos[codigo_produto]["quantidade_total_vendida"] += venda.quantidade
            todos_produtos_vendidos[codigo_produto]["valor_total_vendido"] += venda.valor

        lista_ordenada = sorted(todos_produtos_vendidos.values(), key=lambda x: x["quantidade_total_vendida"], reverse=True)        # ISSO AQUI FOI 100% PESQUISADO

        if not lista_ordenada:
            self.__tela_relatorios.mostra_mensagem("Nenhum produto foi vendido.")
            return None
        
        self.__tela_relatorios.mostra_analise_produtos_vendidos(lista_ordenada)

    def relatorio_vendas_por_vendedor(self):
        vendedores = self.__controlador_sistema.controlador_pessoas.get_all_vendedores() # Acessa a lista de vendedores
        if not vendedores:
            self.__tela_relatorios.mostra_mensagem("Não há vendedores cadastrados para gerar o relatório.")
            return None
        
        lista_ordenada = list(sorted(vendedores, key=lambda x: x.valor_vendido_total, reverse=True))
        if not lista_ordenada:
            self.__tela_relatorios.mostra_mensagem("Nenhum vendedor possui vendas registradas.")
            return None
        
        dados_vendedores_lista = []
        for vendedor in lista_ordenada[:3]:  # Apenas 3 vendedores mais bem sucedidos
            dados_vendedor = {
                "nome": vendedor.nome,
                "cpf": vendedor.numero,
                "valor_total_vendido": vendedor.valor_vendido_total
            }
            dados_vendedores_lista.append(dados_vendedor)
        self.__tela_relatorios.mostra_vendas_por_vendedor(dados_vendedores_lista)

    def compra_cliente(self):
        clientes = self.__controlador_sistema.controlador_pessoas.get_all_clientes()  # Acessa a lista de clientes
        if not clientes:
            self.__tela_relatorios.mostra_mensagem("Não há clientes cadastrados para gerar o relatório.")
            return None
        
        for cliente in clientes:
            compra_feita = []
            for compras in cliente.compras:
                compra_feita.append({"codigo": compras.codigo,
                                     "produto": compras.produto.nome,
                                     "quantidade": compras.quantidade,
                                     "data": compras.data.strftime("%d/%m/%Y"),
                                     "valor": compras.valor})
            dados_cliente = {"nome": cliente.nome,
                     "compras": compra_feita}
            self.__tela_relatorios.mostra_compra_por_cliente(dados_cliente)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.gerar_relatorio_rentabilidade,
                        2: self.analisar_produtos_mais_vendidos,
                        3: self.relatorio_vendas_por_vendedor,
                        4: self.compra_cliente,
                        0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_relatorios.tela_opcoes()
            if opcao_escolhida in lista_opcoes:
                lista_opcoes[opcao_escolhida]()
            else:
                self.__tela_relatorios.mostra_mensagem("Opção inválida, digite novamente.")
