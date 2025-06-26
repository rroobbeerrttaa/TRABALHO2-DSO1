import PySimpleGUI as sg


class MostraMensagem():
    def __init__(self):
        pass

    def mostra_mensagem(self, msg):
        sg.popup("", msg)
