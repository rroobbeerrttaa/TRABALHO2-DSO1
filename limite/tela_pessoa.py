#from teste.teste_numero_opcoes import TesteNumeroOpcoes
from mostra.mostra_mensagem import MostraMensagem
import PySimpleGUI as sg

class TelaPessoa(MostraMensagem):

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def open(self):
        button, values = self.__window.Read()
        return button, values

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
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        if button in (None, 'Retornar'):
            opcao = 0
        self.close()
        return opcao
    
    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkRed1')
        layout = [
            [sg.Text('-------- PESSOAS ----------', font=("Georgia", 40))],
            [sg.Text('Escolha sua opção', font=("Georgia", 25))],
            [sg.Radio('Incluir Cliente', "RD1", key='1', font=("Georgia",20))],
            [sg.Radio('Incluir Vendedor', "RD1", key='2', font=("Georgia",20))],
            [sg.Radio('Listar Clientes', "RD1", key='3', font=("Georgia",20))],
            [sg.Radio('Excluir Cliente', "RD1", key='4', font=("Georgia",20))],
            [sg.Radio('Listar Vendedores', "RD1", key='5', font=("Georgia",20))],
            [sg.Radio('Excluir Vendedor', "RD1", key='6', font=("Georgia",20))],
            [sg.Button('Confirmar'), sg.Cancel('Retornar')]
        ]
        self.__window = sg.Window('Sistema de controle do estoque da A5', layout, icon='imagens/iconea5.ico')

    def pega_dados_pessoa(self):
        while True:
            sg.ChangeLookAndFeel('DarkRed1')
            layout = [
                [sg.Text('-------- DADOS DA PESSOA ----------', font=("Georgia", 25))],
                [sg.Text('Nome:', font=("Georgia", 20), size=(22,1)), sg.InputText('',key='nome')],
                [sg.Text('CPF (somente números):', font=("Georgia", 20), size=(22,1)), sg.InputText('',key='cpf')],
                [sg.Text('Celular (somente números):', font=("Georgia", 20), size=(22,1)), sg.InputText('',key='celular')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Dados da Pessoa', layout, icon='imagens/iconea5.ico')

            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()
                return None

            if button == 'Confirmar':
                nome = values['nome']
                cpf = self.teste_do_cpf(values['cpf'])
                celular = self.teste_do_inteiro(values['celular'], 'o celular')

                if nome and cpf and celular is not None:
                    self.close()
                    return {"nome": nome, "cpf": cpf, "celular": celular}
                else:
                    #self.mostra_mensagem("Por favor, preencha todos os campos corretamente.")
                    self.close()
            

    def mostra_cliente(self, dados_cliente):        
        column_layout = []
        for cliente in dados_cliente:
            column_layout += [
                [sg.Text(f"NOME: {cliente['nome']}")],
                [sg.Text(f"CPF: {cliente['cpf']}")],
                [sg.Text(f"CELULAR: {cliente['celular']}")],
                [sg.Text("-" * 30)]
            ]

        layout = [
            [sg.Text("-------- CLIENTES --------", font=("Georgia", 20))],
            [sg.Column(column_layout, size=(400, 400), scrollable=True, vertical_scroll_only=True)], # Coluna com scroll
            [sg.Button("OK")]
        ]

        window = sg.Window("Lista de Clientes", layout, icon='imagens/iconea5.ico')
        window.read()
        window.close()

    def mostra_vendedor(self, dados_vendedor):
        column_layout = []
        for vendedor in dados_vendedor:
            column_layout += [
                [sg.Text(f"NOME: {vendedor['nome']}")],
                [sg.Text(f"CPF: {vendedor['cpf']}")],
                [sg.Text(f"CELULAR: {vendedor['celular']}")],
                [sg.Text(f"VALOR TOTAL VENDIDO: R${vendedor['valor_vendido_total']:.2f}")],
                [sg.Text("-" * 30)]
            ]

        layout = [
            [sg.Text("-------- VENDEDORES --------", font=("Georgia", 20))],
            [sg.Column(column_layout, size=(400, 400), scrollable=True, vertical_scroll_only=True)], # Coluna com scroll
            [sg.Button("OK")]
        ]
        
        window = sg.Window("Lista de Clientes", layout, icon='imagens/iconea5.ico')
        window.read()
        window.close()

    def seleciona_pessoa(self):
        while True:
            sg.ChangeLookAndFeel('DarkRed1')
            layout = [
                [sg.Text('-------- SELECIONADOR DE PESSOA ----------', font=("Georgia", 25))],
                [sg.Text('Digite o cpf da pessoa que deseja selecionar: ', font=("Georgia", 20))],
                [sg.Text('CPF da pessoa:', size=(20, 1)), sg.InputText('11 dígitos', key='codigo')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Sistema de controle do estoque da A5', layout, icon='imagens/iconea5.ico')
            
            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()  
                return None

            cpf = self.teste_do_cpf(values['codigo'])
            if cpf != None:
                self.close()
                return cpf
            self.close()

    def close(self):
        self.__window.Close()
