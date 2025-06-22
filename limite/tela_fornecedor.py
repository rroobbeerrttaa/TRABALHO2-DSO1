from teste.teste_numero_opcoes import TesteNumeroOpcoes
import PySimpleGUI as sg

class TelaFornecedor(TesteNumeroOpcoes):

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

    def teste_do_cep(self, valor_recebido):
        try:
            valor = int(valor_recebido)
            if len(valor_recebido) == 8:
                return valor_recebido
            else:
                raise ValueError
        except ValueError:
            self.mostra_mensagem("CEP inválido. Digite apenas números (8 dígitos).")
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
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkRed1')
        layout = [
        [sg.Text('-------- FORNECEDOR ----------', font=("Georgia", 40))],
        [sg.Text('Escolha sua opção', font=("Georgia", 25))],
        [sg.Radio('Incluir Fornecedor', "RD1", key='1', font=("Georgia",20))],
        [sg.Radio('Alterar Fornecedor', "RD1", key='2', font=("Georgia",20))],
        [sg.Radio('Listar Fornecedores', "RD1", key='3', font=("Georgia",20))],
        [sg.Radio('Excluir Fornecedor', "RD1", key='4', font=("Georgia",20))],
        [sg.Radio('Incluir Endereço', "RD1", key='5', font=("Georgia",20))],
        [sg.Radio('Excluir Endereço', "RD1", key='6', font=("Georgia",20))],
        [sg.Radio('Retornar', "RD1", key='0', font=("Georgia",20))],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de controle do estoque da A5').Layout(layout)

    def pega_dados_fornecedor(self):
        while True:
            sg.ChangeLookAndFeel('DarkRed1')
            layout = [
                [sg.Text('-------- DADOS FORNECEDOR ----------', font=("Georgia", 25))],
                [sg.Text('Nome/Razão Social: ', font=("Georgia", 15), size=(20, 1)), sg.InputText('', key='nome')],
                [sg.Text('CNPJ (sem pontos): ', font=("Georgia", 15), size=(20, 1)), sg.InputText('', key='cnpj')],
                [sg.Text('Celular: ', font=("Georgia", 15), size=(20, 1)), sg.InputText('', key='celular')],
                [sg.Text('Código do produto: ', font=("Georgia", 15), size=(20, 1)), sg.InputText('', key='produto')],
                [sg.Text('Preço do fornecedor: ', font=("Georgia", 15), size=(20, 1)), sg.InputText('', key='preco')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]            
            self.__window = sg.Window('Sistema de controle do estoque da A5').Layout(layout)

            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()  
                return 0

            nome = values['nome']
            cnpj = self.teste_do_cnpj(values['cnpj'])
            celular = self.teste_do_inteiro(values['celular'], "o numero de celular")
            produto = self.teste_do_inteiro(values['produto'], "o produto")
            preco = self.teste_do_float(values['preco'], "o preco")

            if ((cnpj != None) and
                (celular != None) and
                (produto != None) and
                (preco != None)):
                self.close()
                return {"nome": nome, "cnpj": cnpj, "celular": celular, "produto": produto, "preco": preco}
            self.close()

    def mostra_fornecedor(self, dados_fornecedor):
        string_todos_fornecedores = ""
        
        for dado in dados_fornecedor:
            string_todos_fornecedores += "NOME DO FORNECEDOR: " + str(dado["nome"]) + '\n'
            string_todos_fornecedores += "CNPJ DO FORNECEDOR: " + str(dado["cnpj"]) + '\n'
            string_todos_fornecedores += "CELULAR: " + str(dado["celular"]) + '\n'
            string_todos_fornecedores += "NOME DO PRODUTO: " + str(dado["produto"]) + '\n'
            string_todos_fornecedores += "CODIGO DO PRODUTO: " + str(dado["produto_codigo"]) + '\n'
            string_todos_fornecedores += "PRECO DO FORNECEDOR: " + str(dado["preco"]) + '\n'
            
            if dado["enderecos"]:
                string_todos_fornecedores += "ENDEREÇOS:" + '\n'
                for endereco in dado["enderecos"]:
                    string_todos_fornecedores += "- Rua: {}, Numero: {}, CEP:{}".format(endereco['rua'], 
                                                                                        endereco['numero'], 
                                                                                        endereco['cep']) + '\n'
            else:
                string_todos_fornecedores += "Empresa não apresenta endereços!" + '\n\n'
            string_todos_fornecedores += '\n'
        sg.Popup('-------- LISTA DE FORNECEDORES ----------', string_todos_fornecedores)

    def pega_dados_endereco(self):
            while True:
                sg.ChangeLookAndFeel('DarkRed1')
                layout = [
                    [sg.Text('-------- DADOS ENDERECO ----------', font=("Georgia", 25))],
                    [sg.Text('CEP (só numeros e nada mais): ', font=("Georgia", 15), size=(15, 1)), sg.InputText('', key='cep')],
                    [sg.Text('Rua: ', font=("Georgia", 15), size=(15, 1)), sg.InputText('', key='rua')],
                    [sg.Text('Número: ', font=("Georgia", 15), size=(15, 1)), sg.InputText('', key='numero')],
                    [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
                ]            
                self.__window = sg.Window('Sistema de controle do estoque da A5').Layout(layout)

                button, values = self.open()
                if button in (None, 'Cancelar'):
                    self.close()  
                    return 0

                cep = self.teste_do_cep(values['cep'])
                rua = str(values['rua'])
                numero = self.teste_do_inteiro(values['numero'], "o numero")

                if ((cep != None) and
                    (rua != None) and
                    (numero != None)):
                    self.close()
                    return {
                        "cep": cep,
                        "rua": rua,
                        "numero": numero,
                    }
                self.close()

    def seleciona_fornecedor(self):
        while True:
            sg.ChangeLookAndFeel('DarkRed1')
            layout = [
                [sg.Text('-------- SELECIONAR FORNECEDOR ----------', font=("Georgia", 25))],
                [sg.Text('Digite o CNPJ que deseja selecionar: ', font=("Georgia", 20))],
                [sg.Text('CNPJ:', font=("Georgia", 15), size=(15, 1)), sg.InputText('', key='cnpj')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Sistema de controle do estoque da A5').Layout(layout)

            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()  
                return 0

            cnpj = self.teste_do_cnpj(values['cnpj'])
            if cnpj != None:
                self.close()
                return cnpj
            self.close()

    def seleciona_endereco(self):
        while True:
            sg.ChangeLookAndFeel('DarkRed1')
            layout = [
                [sg.Text('-------- SELECIONAR ENDERECO ----------', font=("Georgia", 25))],
                [sg.Text('Digite o CEP que deseja selecionar: ', font=("Georgia", 20))],
                [sg.Text('CEP:', font=("Georgia", 15), size=(15, 1)), sg.InputText('', key='cep')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Sistema de controle do estoque da A5').Layout(layout)

            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()  
                return 0

            cep = self.teste_do_cep(values['cep'])
            if cep != None:
                self.close()
                return cep
            self.close()

    def mostra_mensagem(self, msg):
        sg.popup("", msg)
        print(msg)

    def close(self):
        self.__window.close()

    def open(self):
        button, values = self.__window.Read()
        return button, values