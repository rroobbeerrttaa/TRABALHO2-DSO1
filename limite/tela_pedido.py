from datetime import datetime
from mostra.mostra_mensagem import MostraMensagem
import PySimpleGUI as sg


class TelaPedido(MostraMensagem):

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def teste_do_cnpj(self, valor_recebido):
        try:
            valor = int(valor_recebido)
            if len(valor_recebido) == 14:
                return valor_recebido
            else:
                raise ValueError
        except ValueError:
            self.mostra_mensagem("CNPJ inválido. Digite apenas números (14 dígitos).")
            return None
   
    def teste_do_float(self, valor_recebido, propriedade=" "):
        try:
            valor = float(valor_recebido)
            return valor
        except ValueError:
            self.mostra_mensagem("Por favor, escreva {} somente com numeros. Exemplo 1.4 (erro na digitação)".format(propriedade))
            return None

    def teste_do_inteiro(self, valor_recebido, propriedade=" "):
        try:
            valor = int(valor_recebido)
            return valor
        except ValueError:
            self.mostra_mensagem("Por favor, escreva {} somente com numeros inteiros. Exemplo 134 (erro na digitação)".format(propriedade))
            return None

    def teste_da_data(self, data):
        try:
            data_recebida = datetime.strptime(data, "%d/%m/%Y")  
            return data_recebida
        except ValueError:
            self.mostra_mensagem("Data inválida. Insira a data no formato (dd/mm/yyyy) (erro na digitacao).")
            return None

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        opcao = 9
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkRed1')
        layout = [
        [sg.Text('-------- PEDIDOS ----------', font=("Georgia", 25))],
        [sg.Text('Escolha sua opção', font=("Georgia", 25))],
        [sg.Radio('Fazer Pedido', "RD1", key='1', font=("Georgia", 20))],
        [sg.Radio('Listar Pedido', "RD1", key='2', font=("Georgia", 20))],
        [sg.Radio('Excluir Pedido', "RD1", key='3', font=("Georgia", 20))],
        [sg.Radio('Alterar Pedido', "RD1", key='4', font=("Georgia",20))],
        [sg.Radio('Retornar', "RD1", key='0', font=("Georgia",20))],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de controle do estoque da A5').Layout(layout)

    def pega_dados_pedido(self):
        while True:
            sg.ChangeLookAndFeel('DarkRed1')
            layout = [
                [sg.Text('-------- DADOS FORNECEDOR ----------', font=("Georgia", 40))],
                [sg.Text('CNPJ do fornecedor: ', font=("Georgia",15), size=(33, 1)), sg.InputText('', key='cnpj')],
                [sg.Text('Código do pedido: ', font=("Georgia",15), size=(33, 1)), sg.InputText('', key='codigo')],
                [sg.Text('Código do produto: ', font=("Georgia",15), size=(33, 1)), sg.InputText('', key='codigo_produto')],
                [sg.Text('Quantidade do pedido: ', font=("Georgia",15), size=(33, 1)), sg.InputText('', key='quantidade')],
                [sg.Text('Data do pedido feito (DD/MM/AAAA): ', font=("Georgia",15), size=(33, 1)), sg.InputText('', key='data')],
                [sg.Text('Valor do frete do pedido: ', font=("Georgia",15), size=(33, 1)), sg.InputText('', key='valor_frete')],
                [sg.Text('Prazo do pedido (quantidade de dias): ', font=("Georgia",15), size=(33, 1)), sg.InputText('', key='prazo_entrega')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
                ]            
            self.__window = sg.Window('Sistema de controle do estoque da A5').Layout(layout)
            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()  
                return None
            cnpj = self.teste_do_cnpj(values['cnpj'])
            codigo = self.teste_do_inteiro(values['codigo'], "o codigo")
            codigo_produto = self.teste_do_inteiro(values['codigo_produto'], "o codigo do produto")
            quantidade = self.teste_do_inteiro(values['quantidade'], "a quantidade")
            data = self.teste_da_data(values['data'])
            valor_frete = self.teste_do_float(values['valor_frete'], "o valor do frete")
            prazo_entrega = self.teste_do_inteiro(values['prazo_entrega'], "o prazo de entrega")
            if ((cnpj != None) and
                (codigo != None) and
                (codigo_produto != None) and
                (quantidade != None) and
                (data != None) and
                (valor_frete != None) and
                (prazo_entrega != None) ):
                self.close()
                return {"cnpj": cnpj,
                        "codigo": codigo,
                        "codigo_produto": codigo_produto,
                        "quantidade": quantidade,
                        "data": data,
                        "valor_frete": valor_frete,
                        "prazo_entrega": prazo_entrega,
                        }
            self.close()

    def altera_dados_pedidos(self):
        while True:
            sg.ChangeLookAndFeel('DarkRed1')
            layout = [
                [sg.Text('-------- NOVOS DADOS DO FORNECEDOR ----------', font=("Georgia", 40))],
                [sg.Text('CNPJ do fornecedor: ', font=("Georgia",15), size=(33, 1)), sg.InputText('', key='cnpj')],
                [sg.Text('Código do produto: ', font=("Georgia",15), size=(33, 1)), sg.InputText('', key='codigo_produto')],
                [sg.Text('Quantidade do pedido: ', font=("Georgia",15), size=(33, 1)), sg.InputText('', key='quantidade')],
                [sg.Text('Data do pedido feito (DD/MM/AAAA): ', font=("Georgia",15), size=(33, 1)), sg.InputText('', key='data')],
                [sg.Text('Valor do frete do pedido: ', font=("Georgia",15), size=(33, 1)), sg.InputText('', key='valor_frete')],
                [sg.Text('Prazo do pedido (quantidade de dias): ', font=("Georgia",15), size=(33, 1)), sg.InputText('', key='prazo_entrega')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
                ]            
            self.__window = sg.Window('Sistema de controle do estoque da A5').Layout(layout)
            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()  
                return None
            cnpj = self.teste_do_cnpj(values['cnpj'])
            codigo_produto = self.teste_do_inteiro(values['codigo_produto'], "o codigo do produto")
            quantidade = self.teste_do_inteiro(values['quantidade'], "a quantidade")
            data = self.teste_da_data(values['data'])
            valor_frete = self.teste_do_float(values['valor_frete'], "o valor do frete")
            prazo_entrega = self.teste_do_inteiro(values['prazo_entrega'], "o prazo de entrega")
            if ((cnpj != None) and
                (codigo_produto != None) and
                (quantidade != None) and
                (data != None) and
                (valor_frete != None) and
                (prazo_entrega != None) ):
                self.close()
                return {"cnpj": cnpj,
                        "codigo_produto": codigo_produto,
                        "quantidade": quantidade,
                        "data": data,
                        "valor_frete": valor_frete,
                        "prazo_entrega": prazo_entrega,
                        }
            self.close()
    

    def mostra_pedidos(self, dados_pedidos):
        string_todos_pedidos = ""
        
        for dado in dados_pedidos:
            string_todos_pedidos += "CODIGO DO PEDIDO: " + str(dado["codigo"]) + '\n'
            string_todos_pedidos += "QUANTIDADE DO PEDIDO: " + str(dado["quantidade"]) + '\n'
            string_todos_pedidos += "NOME DO PRODUTO: " + str(dado["nome_produto"]) + '\n'
            string_todos_pedidos += "DATA DO PEDIDO: " + str(dado["data"]) + '\n'
            string_todos_pedidos += "VALOR: " + str(dado["valor"]) + '\n'
            string_todos_pedidos += "NOME DO FORNECEDOR: " + str(dado["nome_fornecedor"]) + '\n'
            string_todos_pedidos += "VALOR DO FRETE: " + str(dado["frete"]) + '\n'
            string_todos_pedidos += "PRAZO DE ENTREGA: " + str(dado["prazo_entrega"]) + '\n\n'
        sg.Popup('-------- LISTA DE PEDIDOS ----------', string_todos_pedidos)

    def seleciona_pedido(self):
        while True:
            sg.ChangeLookAndFeel('DarkRed1')
            layout = [
                [sg.Text('-------- SELECIONAR PEDIDO ----------', font=("Georgia", 40))],
                [sg.Text('Digite o codigo do pedido que deseja selecionar: ', font=("Georgia", 30))],
                [sg.Text('Código:', font=("Georgia", 25), size=(7, 1)), sg.InputText('', key='codigo')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Sistema de controle do estoque da A5').Layout(layout)
            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()  
                return None
            codigo = self.teste_do_inteiro(values['codigo'], "o codigo")
            if codigo != None:
                self.close()
                return codigo
            self.close()

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values