from teste.teste_numero_opcoes import TesteNumeroOpcoes
import PySimpleGUI as sg

class TelaProduto(TesteNumeroOpcoes):

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def teste_do_float(self, valor_recebido, propriedade = " "):
        try:
            valor = float(valor_recebido)
            return valor
        except ValueError:
            self.mostra_mensagem("Por favor, escreva {} somente com numeros. Exemplo 14 (erro na digitação)".format(propriedade))
            return None

    def teste_do_inteiro(self, valor_recebido, propriedade = " "):
        try:
            valor = int(valor_recebido)
            return valor
        except ValueError:
            self.mostra_mensagem("Por favor, escreva {} somente com numeros inteiros. Exemplo 134 (erro na digitação)".format(propriedade))
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
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao
    
    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkRed1')
        layout = [
        [sg.Text('-------- PRODUTO ----------', font=("Georgia", 40))],
        [sg.Text('Escolha sua opção', font=("Georgia", 25))],
        [sg.Radio('Incluir Produto', "RD1", key='1', font=("Georgia",20))],
        [sg.Radio('Alterar Valor Do Produto', "RD1", key='2', font=("Georgia",20))],
        [sg.Radio('Alterar Quantidade De Estoque Do Produto', "RD1", key='3', font=("Georgia",20))],
        [sg.Radio('Listar Produto', "RD1", key='4', font=("Georgia",20))],
        [sg.Radio('Excluir Produto', "RD1", key='5', font=("Georgia",20))],
        [sg.Radio('Retornar', "RD1", key='0', font=("Georgia",20))],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de controle do estoque da A5').Layout(layout)

    def pega_dados_produto(self):
        while True:
            sg.ChangeLookAndFeel('DarkRed1')
            layout = [
                [sg.Text('-------- DADOS PRODUTO ----------', font=("Georgia", 25))],
                [sg.Text('Nome: ', size=(22, 1)), sg.InputText('', key='nome')],
                [sg.Text('Código do produto: ', size=(22, 1)), sg.InputText('', key='codigo_produto')],
                [sg.Text('Preço de venda: ', size=(22, 1)), sg.InputText('', key='preco_venda')],
                [sg.Text('Quantidade comprada: ', size=(22, 1)), sg.InputText('', key='quant_estoque')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Sistema de controle do estoque da A5').Layout(layout)
        
            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()  
                return 0
            
            nome = values['nome']
            codigo_produto = self.teste_do_inteiro(values['codigo_produto'], 'o codigo do produto')
            preco_venda = self.teste_do_float(values['preco_venda'], 'o preço de venda')
            quant_estoque = self.teste_do_inteiro(values['quant_estoque'], 'a quantidade de estoque')

            if ((nome != None) and 
                (codigo_produto != None) and
                (preco_venda != None) and 
                (quant_estoque != None)):           
                self.close()
                return {"nome": nome,
                        "codigo_produto": codigo_produto,
                        "preco_venda": preco_venda,
                        "quant_estoque": quant_estoque}  
            self.close()
        
    def pega_dados_produto_alterar(self):
        while True:
            sg.ChangeLookAndFeel('DarkRed1')
            layout = [
                [sg.Text('-------- VALOR PARA ALTERAR ----------', font=("Georgia", 25))],
                [sg.Text('Preço venda / Quantidade a mais no estoque: ', size=(34, 1)), sg.InputText('', key='valor')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]            

            self.__window = sg.Window('Sistema de controle do estoque da A5').Layout(layout)
            
            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()
                return 0

            valor = self.teste_do_float(values['valor'], 'o valor')
            if valor is not None:
                self.close()
                return valor
            self.close()


    def mostra_produto(self, dados_produto):
        string_todos_produtos = "-------- LISTA DE PRODUTOS ----------" + '\n\n' 
        
        for dado in dados_produto:
            string_todos_produtos += "NOME DO PRODUTO: " + str(dado["nome"]) + '\n'
            string_todos_produtos += "CODIGO DO PRODUTO: " + str(dado["codigo_produto"]) + '\n'
            string_todos_produtos += "PRECO DO PRODUTO: R$" + str(dado["preco_venda"]) + '\n'
            string_todos_produtos += "QUANTIDADE NO ESTOQUE DO PRODUTO: " + str(dado["quant_estoque"]) + '\n\n'

        sg.Popup("", string_todos_produtos)

    def seleciona_produto(self):
        while True:
            sg.ChangeLookAndFeel('DarkRed1')
            layout = [
                [sg.Text('-------- SELECIONADOR DE PRODUTO ----------', font=("Georgia", 25))],
                [sg.Text('Digite o código do produto que deseja selecionar: ', font=("Georgia", 20))],
                [sg.Text('Código do produto:', size=(20, 1)), sg.InputText('', key='codigo')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Sistema de controle do estoque da A5').Layout(layout)
            
            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()  
                return 0

            codigo = self.teste_do_inteiro(values['codigo'], 'o codigo')
            if codigo != None:
                self.close()
                return codigo
            self.close()

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.close()

    def open(self):
        button, values = self.__window.Read()
        return button, values