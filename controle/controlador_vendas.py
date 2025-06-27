from limite.tela_venda import TelaVenda
from entidade.venda import Venda
from excessoes.nao_encontrado_na_lista_exception import NaoEncontradoNaListaException
from excessoes.encontrado_na_lista_exception import EncontradoNaListaException
from DAOs.venda_dao import VendaDAO

class ControladorVendas():

  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__vendas_DAO = VendaDAO()
    self.__tela_venda = TelaVenda()

  @property
  def vendas(self):
    return self.__vendas_DAO

  def pega_venda_por_codigo(self, codigo: int):
    for venda in self.__vendas_DAO.get_all():
      if venda.codigo == int(codigo):
        return venda
    return None

  def incluir_venda(self):
      self.__controlador_sistema.controlador_pessoas.lista_cliente()
      self.__controlador_sistema.controlador_pessoas.lista_vendedores()
      self.__controlador_sistema.controlador_produtos.lista_produtos()
      dados_venda = self.__tela_venda.pega_dados_venda()
      try:
          quantidade = int(dados_venda["quantidade"])
          codigo_produto = int(dados_venda["codigo_produto"])
          codigo_venda = int(dados_venda["codigo"])
          cliente = self.__controlador_sistema.controlador_pessoas.pega_cliente_por_cpf(dados_venda["cpf_cliente"])
          vendedor = self.__controlador_sistema.controlador_pessoas.pega_vendedor_por_cpf(dados_venda["cpf_vendedor"])
          produto = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(codigo_produto)
          if cliente is None:
             raise NaoEncontradoNaListaException("cliente")
          if vendedor is None:
             raise NaoEncontradoNaListaException("vendedor")
          if produto is None:
              raise NaoEncontradoNaListaException("produto")
          if self.pega_venda_por_codigo(dados_venda["codigo"]) is not None:
                raise EncontradoNaListaException()
          if produto.quant_estoque < quantidade:
              self.__tela_venda.mostra_mensagem("Erro: Estoque insuficiente.")
              return

          nova_venda = Venda(quantidade = quantidade, produto = produto,
                             data = dados_venda["data"], codigo = codigo_venda,
                             cliente = cliente, vendedor = vendedor)    # VALOR DA VENDA É CALCULADO NO CONSTRUTOR DA CLASSE

          #self.__vendas.append(nova_venda)
          self.__vendas_DAO.add(nova_venda)
          produto.quant_estoque -= quantidade
          vendedor.valor_vendido_total += nova_venda.valor
          cliente.adicionar_compra(nova_venda)
          # Não sei se mantenho essa função porque o atributo compras em cliente é uma lista e não um dicionário

          self.__tela_venda.mostra_mensagem("Venda cadastrada com sucesso!")
          self.__tela_venda.mostra_venda({"codigo": nova_venda.codigo,
                                          "vendedor": nova_venda.vendedor.nome,
                                          "cliente": nova_venda.cliente.nome,
                                          "produto": nova_venda.produto.nome,
                                          "quantidade": nova_venda.quantidade,
                                          "data": nova_venda.data.strftime("%d/%m/%Y"),
                                          "valor": nova_venda.valor})
      except Exception as e:
          self.__tela_venda.mostra_mensagem(f'Erro inesperado: {e}')

  def lista_venda(self):
    vendas = list(self.__vendas_DAO.get_all()) #transformar get all em lista
    print(vendas)
    if not vendas:
      self.__tela_venda.mostra_mensagem("Sem vendas cadastradas.")
      return

    self.__tela_venda.mostra_mensagem("-------- VENDAS CADASTRADAS --------")
    for venda in vendas:
      self.__tela_venda.mostra_venda({"codigo": venda.codigo,
                                      "vendedor": venda.vendedor.nome,
                                      "cliente": venda.cliente.nome,
                                      "produto": venda.produto.nome,
                                      "quantidade": venda.quantidade,
                                      "data": venda.data.strftime("%d/%m/%Y"),
                                      "valor": venda.valor})
    
  def excluir_venda(self):
    self.lista_venda()
    try:
      codigo_venda = self.__tela_venda.seleciona_venda()
      venda = self.pega_venda_por_codigo(codigo_venda)

      if venda is not None:
        self.__tela_venda.mostra_mensagem("Dados da venda a ser deletada:")
        self.__tela_venda.mostra_venda({"codigo": venda.codigo,
                                        "vendedor": venda.vendedor.nome,
                                        "cliente": venda.cliente.nome,
                                        "produto": venda.produto.nome,
                                        "quantidade": venda.quantidade,
                                        "data": venda.data.strftime("%d/%m/%Y"),
                                        "valor": venda.valor})
        venda.vendedor.valor_vendido_total -= venda.valor
        venda.produto.quant_estoque += venda.quantidade
        venda.cliente.remover_venda(venda)
        self.__vendas.remove(venda.codigo)
        self.__tela_venda.mostra_mensagem("Venda excluída com sucesso!")
        self.__tela_venda.mostra_mensagem("Vendas restantes:")
        self.lista_venda()
      else:
        raise NaoEncontradoNaListaException("venda")
    except Exception as e:
        self.__tela_venda.mostra_mensagem(f"Erro inesperado: {e}") 

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_venda,
                    2: self.lista_venda,
                    3: self.excluir_venda,
                    0: self.retornar}

    while True:
        opcao_escolhida = self.__tela_venda.tela_opcoes()
        if opcao_escolhida in lista_opcoes:
            lista_opcoes[opcao_escolhida]()
        else:
            self.__tela_venda.mostra_mensagem("Opção inválida, digite novamente.")
