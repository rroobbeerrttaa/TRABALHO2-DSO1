#from teste.teste_numero_opcoes import TesteNumeroOpcoes
from mostra.mostra_mensagem import MostraMensagem
import PySimpleGUI as sg


class TelaPessoa(MostraMensagem):

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def teste_do_inteiro(self, valor_recebido, propriedade = " "):
        try:
            valor = int(valor_recebido)
            return valor
        except ValueError:
            self.mostra_mensagem(f"Por favor, escreva {propriedade} somente com numeros inteiros positivos. Exemplo 134 (erro na digitação)")
            return None

    def teste_do_cpf(self, mensagem=" "):
        while True:
            valor_recebido = input(mensagem)
            try:
                valor_recebido_tipo = int(valor_recebido)
                if len(valor_recebido) == 11:
                    return valor_recebido
                else:
                    raise ValueError
            except ValueError:
                print("Por favor, escreva somente com números de 11 digitos. Exemplo: 1234567890")
                return None

    def tela_opcoes(self):
        '''print("-------- PESSOAS ----------")
        print()
        print("1 - Incluir Cliente")
        print("2 - Incluir Vendedor")
        print("3 - Listar Clientes")
        print("4 - Excluir Cliente")
        print("5 - Listar Vendedores")
        print("6 - Excluir Vendedor")
        print("0 - Retornar")'''
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
        if values['0'] or button in (None, 'Cancelar'):
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
            [sg.Radio('Retornar', "RD1", key='0', font=("Georgia",20))],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de controle do estoque da A5').Layout(layout)

    def pega_dados_pessoa(self):
        while True:
            sg.ChangeLookAndFeel('DarkRed1')
            layout = [
                [sg.Text('-------- DADOS PESSOA ----------', font=("Georgia", 25))],
                [sg.Text('Nome:', font=("Georgia", 20), size=(22,1)), sg.InputText('',key='nome')],
                [sg.Text('CPF (somente números):', font=("Georgia", 20), size=(22,1)), sg.InputText('',key='cpf')],
                [sg.Text('Celular (somente números):', font=("Georgia", 20), size=(22,1)), sg.InputText('',key='celular')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Dados da Pessoa').Layout(layout)

            button, values = self.__window.Read()
            if button in (None, 'Cancelar'):
                self.close()
                return None

            if button == 'Confirmar':
                nome = values['nome']
                cpf = self.teste_do_cpf(values['cpf'])
                celular = self.teste_do_inteiro(values['celular'])

                if nome and cpf and celular is not None:
                    return {"nome": nome, "cpf": cpf, "celular": celular}
                else:
                    self.mostra_mensagem("Por favor, preencha todos os campos corretamente.")
            elif button in (None, 'Cancelar'):
                return None

    def mostra_cliente(self, dados_cliente):
        print("------CLIENTE------")
        print("NOME:", dados_cliente["nome"])
        print("CPF:", dados_cliente["cpf"])
        print("CELULAR:", dados_cliente["celular"])
        print()

    def mostra_vendedor(self, dados_vendedor):
        print("------VENDEDOR------")
        print("NOME:", dados_vendedor["nome"])
        print("CPF:", dados_vendedor["cpf"])
        print("CELULAR:", dados_vendedor["celular"])
        print(f"VALOR TOTAL VENDIDO: R${dados_vendedor['valor_vendido_total']:.2f}")
        print()

    def seleciona_pessoa(self):
        print("-------- SELECIONADOR DE PESSOA ----------")
        cpf = self.teste_do_cpf("CPF da pessoa que deseja selecionar (apenas números): ")
        print()    
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)
        print()
