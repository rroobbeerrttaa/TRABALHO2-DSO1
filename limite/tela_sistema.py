import PySimpleGUI as sg
import time


class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
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
        if button in (None,'Encerrar Sessão'):
            opcao = 0
        self.close()
        return opcao
    
    def close(self):
        self.__window.Close()

    def init_components(self):
        sg.ChangeLookAndFeel('DarkBrown4') 
        layout = [
            [sg.Text('Sistema de controle do estoque A5', font=("Georgia",40,'bold'))],
            [sg.Text('Escolha sua opção', font=("Georgia",25))],
            [sg.Radio('Venda',"RD1", key='1', font=("Georgia",20))],
            [sg.Radio('Fornecedor',"RD1", key='2', font=("Georgia",20))],
            [sg.Radio('Produto',"RD1", key='3', font=("Georgia",20))],
            [sg.Radio('Pessoa',"RD1", key='4', font=("Georgia",20))],
            [sg.Radio('Pedido feito para o fornecedor',"RD1", key='5', font=("Georgia",20))],
            [sg.Radio('Relatórios',"RD1", key='6', font=("Georgia",20))],
            [sg.Button('Confirmar'), sg.Cancel('Encerrar Sessão'), sg.Image(filename='imagens/iconea5.png', pad=((5, 5)))]
        ]
        self.__window = sg.Window('Sistema de controle do estoque da A5', layout, icon='imagens/iconea5.ico')

    def mostra_mensagem(self, mensagem):
        layout = [[sg.Text(mensagem, font=("Georgia",50))]]
        window = sg.Window('Sistema de controle do estoque da A5', layout, finalize=True, icon='imagens/iconea5.ico')       # ESSA PARTE FOI TOTALMENTE PESQUISADA
        start_time = time.time()
        while True:
            event, values = window.read(timeout=100) 
            if event == sg.WINDOW_CLOSED:
                break
            if time.time() - start_time > 5:
                break           
        self.close()