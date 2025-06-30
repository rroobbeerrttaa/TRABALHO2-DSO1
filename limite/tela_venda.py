from datetime import datetime
from mostra.mostra_mensagem import MostraMensagem
import PySimpleGUI as sg

class TelaVenda(MostraMensagem):

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def teste_do_float(self, valor_recebido, propriedade=" "):
        try:
            valor = float(valor_recebido)
            return valor
        except ValueError:
            self.mostra_mensagem(f"Por favor, escreva {propriedade} somente com números. \nExemplo: 1.42")
            return None


    def teste_do_inteiro(self, valor_recebido, propriedade = " "):
        try:
            valor = int(valor_recebido)
            return valor
        except ValueError:
            self.mostra_mensagem(f"Por favor, escreva {propriedade} somente com numeros inteiros positivos. Exemplo 134 (erro na digitação)")
            return None
    
    def teste_do_cpf(self, valor_recebido):
        while True:
            try:
                if len(valor_recebido) == 11:
                    return valor_recebido
                else:
                    raise ValueError
            except ValueError:
                self.mostra_mensagem("Por favor, escreva o CPF somente com números (11 dígitos).\nExemplo: 1234567890")
                return None
    
    def teste_da_data(self, data):
        try:
            data_recebida = datetime.strptime(data, "%d/%m/%Y")  
            return data_recebida
        except ValueError:
            self.mostra_mensagem("Data inválida. Insira a data no formato (DD/MM/AAAA) (erro na digitacao).")
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
        if button in (None, 'Retornar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkRed1')
        layout = [
            [sg.Text('-------- VENDAS ----------', font=("Georgia", 40))],
            [sg.Text('Escolha sua opção', font=("Georgia", 25))],
            [sg.Radio('Fazer Venda', "RD1", key='1', font=("Georgia",20))],
            [sg.Radio('Listar Vendas', "RD1", key='2', font=("Georgia",20))],
            [sg.Radio('Excluir Venda', "RD1", key='3', font=("Georgia",20))],
            [sg.Button('Confirmar'), sg.Cancel('Retornar')]
        ]
        self.__window = sg.Window('Sistema de controle do estoque da A5', layout, icon='imagens/iconea5.ico')

    def pega_dados_venda(self):
       while True:
            sg.ChangeLookAndFeel('DarkRed1')
            layout = [
                [sg.Text('-------- DADOS VENDA ----------', font=("Georgia", 25))],
                [sg.Text('CPF do vendedor: ', font=("Georgia", 15), size=(20, 1)), sg.InputText('', key='cpf_vendedor')],
                [sg.Text('CPF do cliente: ', font=("Georgia", 15), size=(20, 1)), sg.InputText('', key='cpf_cliente')],
                [sg.Text('Código do produto: ', font=("Georgia", 15), size=(20, 1)), sg.InputText('', key='codigo_produto')],
                [sg.Text('Quantidade vendida: ', font=("Georgia", 15), size=(20, 1)), sg.InputText('', key='quantidade')],
                [sg.Text('Código da venda: ', font=("Georgia", 15), size=(20, 1)), sg.InputText('', key='codigo')],
                [sg.Text('Data da venda (DD/MM/AAAA): ', font=("Georgia", 12), size=(27, 1)), sg.InputText('', key='data')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]            
            self.__window = sg.Window('Sistema de controle do estoque da A5', layout, icon='imagens/iconea5.ico')
            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()  
                return None
            
            cpf_vendedor = self.teste_do_cpf(values['cpf_vendedor'])
            cpf_cliente = self.teste_do_cpf(values['cpf_cliente'])
            codigo_produto = self.teste_do_inteiro(values['codigo_produto'], "o código do produto")
            quantidade = self.teste_do_inteiro(values['quantidade'], "a quantidade vendida")
            codigo = self.teste_do_inteiro(values['codigo'], "o código da venda")
            data = self.teste_da_data(values['data'])

            if cpf_vendedor and cpf_cliente and codigo_produto and quantidade and codigo and data:
                self.close()
                return {"cpf_vendedor": cpf_vendedor, 
                        "cpf_cliente":cpf_cliente,
                        "quantidade": quantidade,
                        "data": data,
                        "codigo_produto": codigo_produto,
                        "codigo": codigo}
            self.close()

    def mostra_venda(self, dados_venda):
        column_layout = []
        for venda in dados_venda:
            column_layout += [
                [sg.Text(f"CÓDIGO DA VENDA: {venda['codigo']}", font=("Georgia", 15))],
                [sg.Text(f"DATA: {venda['data']}", font=("Georgia", 15))],
                [sg.Text(f"VENDEDOR: {venda['vendedor']}", font=("Georgia", 15))],
                [sg.Text(f"CLIENTE: {venda['cliente']}", font=("Georgia", 15))],
                [sg.Text(f"NOME DO PRODUTO: {venda['produto']}", font=("Georgia", 15))],
                [sg.Text(f"QUANTIDADE: {venda['quantidade']}", font=("Georgia", 15))],
                [sg.Text(f"VALOR TOTAL DA VENDA: R${float(venda['valor']):.2f}", font=("Georgia", 15))],
                [sg.Text('-' * 30, font=("Georgia", 10))]
            ]
        layout = [[sg.Text('-------- DADOS DA VENDA ----------', font=("Georgia", 25))],
                 [sg.Column(column_layout, size=(500, 500), scrollable=True, vertical_scroll_only=True)],  # Coluna com scroll
                 [sg.Button('OK')]]
        window = sg.Window('Detalhes da Venda', layout, icon='imagens/iconea5.ico')
        window.read()
        window.close()

    def seleciona_venda(self):
        while True:
            sg.ChangeLookAndFeel('DarkRed1')
            layout = [
                [sg.Text('-------- SELECIONAR VENDA ----------', font=("Georgia", 25))],
                [sg.Text('Digite o código da venda que deseja selecionar: ', font=("Georgia", 20))],
                [sg.Text('Código:', font=("Georgia", 15), size=(15, 1)), sg.InputText('', key='codigo')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Sistema de controle do estoque da A5', layout, icon='imagens/iconea5.ico')
            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()  
                return None
            codigo = self.teste_do_inteiro(values['codigo'], "o código da venda")
            if codigo is not None:
                self.close()
                return codigo
            self.close()

    def close(self):
        self.__window.Close()