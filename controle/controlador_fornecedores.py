from limite.tela_fornecedor import TelaFornecedor
from entidade.fornecedor import Fornecedor
from entidade.produto import Produto
from excessoes.encontrado_na_lista_exception import EncontradoNaListaException
from excessoes.nao_encontrado_na_lista_exception import NaoEncontradoNaListaException
from DAOs.fornecedor_dao import FornecedorDAO


class ControladorFornecedores:
    def __init__(self, controlador_sistema):
        self.__fornecedor_DAO = FornecedorDAO()
        self.__tela_fornecedor = TelaFornecedor()
        self.__controlador_sistema = controlador_sistema

    def pega_fornecedor_por_cnpj(self, cnpj: str):
        for fornecedor in self.__fornecedor_DAO.get_all():
            if int(fornecedor.numero) == int(cnpj):
                return fornecedor
        return None

    def incluir_fornecedor(self):
        self.__controlador_sistema.controlador_produtos.lista_produtos()
        dados_fornecedor = self.__tela_fornecedor.pega_dados_fornecedor()
        if dados_fornecedor == None:
            return  None
        try:
            codigo_produto = int(dados_fornecedor["produto"])  
            objeto_produto = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(codigo_produto)
            if objeto_produto is not None:
                novo_fornecedor = self.pega_fornecedor_por_cnpj(dados_fornecedor["cnpj"]) 
                if novo_fornecedor is None:
                    fornecedor = Fornecedor(str(dados_fornecedor["nome"]),
                                            str(dados_fornecedor["cnpj"]),
                                            int(dados_fornecedor["celular"]),
                                            objeto_produto,
                                            float(dados_fornecedor["preco"]))
                    self.__fornecedor_DAO.add(fornecedor)
                    self.__tela_fornecedor.mostra_mensagem("Fornecedor incluído com sucesso!")
                else:
                    raise EncontradoNaListaException()
            else:
                raise NaoEncontradoNaListaException("produto")
        except Exception as e:
            self.__tela_fornecedor.mostra_mensagem(e)

    def alterar_fornecedor(self):
        self.lista_fornecedores()
        fornecedores = list(self.__fornecedor_DAO.get_all())
        if len(fornecedores) == 0:
            return None
        cnpj_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        if cnpj_fornecedor == None:
            return None
        fornecedor = self.pega_fornecedor_por_cnpj(cnpj_fornecedor)       
        try:
            if fornecedor is not None:
                novos_dados_fornecedor = self.__tela_fornecedor.altera_fornecedor()   
                if novos_dados_fornecedor == None:
                    return None
                else:            
                    novo_codigo_produto = int(novos_dados_fornecedor["produto"])
                    novo_produto = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(novo_codigo_produto)
                    if novo_produto is not None:
                            fornecedor.nome = novos_dados_fornecedor["nome"]
                            fornecedor.celular = novos_dados_fornecedor["celular"]
                            fornecedor.produto = novo_produto
                            fornecedor.preco = float(novos_dados_fornecedor["preco"])
                            self.__fornecedor_DAO.update(fornecedor)
                            self.__tela_fornecedor.mostra_mensagem("Fornecedor alterado com sucesso!")
                    else:
                            raise NaoEncontradoNaListaException("produto")
            else:
                raise NaoEncontradoNaListaException("fornecedor")
        except Exception as e:
            self.__tela_fornecedor.mostra_mensagem(e)

    def adicionar_endereco(self):
        self.lista_fornecedores()
        fornecedores = list(self.__fornecedor_DAO.get_all())
        if len(fornecedores) == 0:
            return None
        cnpj_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        if cnpj_fornecedor == None: 
            return None
        fornecedor = self.pega_fornecedor_por_cnpj(cnpj_fornecedor)
        try:
            if fornecedor is None:
                raise NaoEncontradoNaListaException("fornecedor")
            dados_endereco = self.__tela_fornecedor.pega_dados_endereco()
            if dados_endereco == None:
                return None
            else:
                cep_novo = dados_endereco["cep"]
                cep_existente = False
                for endereco in fornecedor.enderecos:
                    if int(endereco.cep) == int(cep_novo): 
                        cep_existente = True
                        break
                if cep_existente:
                    raise EncontradoNaListaException()
                fornecedor.incluir_endereco(
                    str(dados_endereco["cep"]),
                    str(dados_endereco["rua"]),
                    int(dados_endereco["numero"]))
                self.__fornecedor_DAO.update(fornecedor)
                self.__tela_fornecedor.mostra_mensagem("Endereço adicionado com sucesso!")
        except Exception as e:
            self.__tela_fornecedor.mostra_mensagem(e)

    def lista_fornecedores(self):
        fornecedores = list(self.__fornecedor_DAO.get_all())
        if len(fornecedores) == 0:
            self.__tela_fornecedor.mostra_mensagem("Não há fornecedores cadastrados.")
            return None
        else:
            dados_fornecedor = [] 
            for fornecedor in self.__fornecedor_DAO.get_all():
                dado = {"nome": fornecedor.nome,
                        "cnpj": fornecedor.numero,
                        "celular": fornecedor.celular,
                        "produto": fornecedor.produto.nome,
                        "produto_codigo": fornecedor.produto.codigo_produto,
                        "preco": fornecedor.preco,
                        "enderecos": []}
                for endereco in fornecedor.enderecos:
                    dado["enderecos"].append({"cep": endereco.cep,
                                              "rua": endereco.rua,
                                              "numero": endereco.numero})
                dados_fornecedor.append(dado)
            self.__tela_fornecedor.mostra_fornecedor(dados_fornecedor)

    def excluir_fornecedor(self):
        self.lista_fornecedores()
        fornecedores = list(self.__fornecedor_DAO.get_all())
        if len(fornecedores) == 0:
            return None
        cnpj_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        if cnpj_fornecedor == None:
                return None
        fornecedor = self.pega_fornecedor_por_cnpj(cnpj_fornecedor)
        try:
            if fornecedor is not None:
                self.__fornecedor_DAO.remove(fornecedor.numero)
                self.__tela_fornecedor.mostra_mensagem("Fornecedor excluído com sucesso!")
            else:
                raise NaoEncontradoNaListaException()
        except Exception as e:
            self.__tela_fornecedor.mostra_mensagem(e)

    def excluir_endereco(self):
        self.lista_fornecedores()
        fornecedores = list(self.__fornecedor_DAO.get_all())
        if len(fornecedores) == 0:
            return None
        cnpj_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        if cnpj_fornecedor == None:
            return None
        fornecedor = self.pega_fornecedor_por_cnpj(cnpj_fornecedor)
        try:
            if fornecedor is None:
                raise NaoEncontradoNaListaException("fornecedor") 
            cep_endereco = self.__tela_fornecedor.seleciona_endereco()
            if cep_endereco == None:
                return None
            endereco_remover = None
            for endereco in fornecedor.enderecos:
                if str(endereco.cep).strip() == str(cep_endereco).strip():
                    endereco_remover = endereco
                    break
            if endereco_remover:
                fornecedor.remover_endereco(endereco_remover)
                self.__tela_fornecedor.mostra_mensagem("Endereço excluído com sucesso!")
                self.__fornecedor_DAO.update(fornecedor)
                self.lista_fornecedores()
            else:
               raise NaoEncontradoNaListaException("endereço")
        except Exception as e:
            self.__tela_fornecedor.mostra_mensagem(e)
            
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_fornecedor,
            2: self.alterar_fornecedor,
            3: self.lista_fornecedores,
            4: self.excluir_fornecedor,
            5: self.adicionar_endereco,
            6: self.excluir_endereco,
            0: self.retornar
        }
        while True:
            opcao_escolhida = self.__tela_fornecedor.tela_opcoes()
            if opcao_escolhida in lista_opcoes:
                lista_opcoes[opcao_escolhida]()
            else:
                self.__tela_fornecedor.mostra_mensagem("Opção inválida, escolha novamente.")
