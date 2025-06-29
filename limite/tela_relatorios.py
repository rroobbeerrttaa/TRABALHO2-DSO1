import PySimpleGUI as sg
from mostra.mostra_mensagem import MostraMensagem


class TelaRelatorios(MostraMensagem):
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def open(self):
        button, values = self.__window.Read()
        return button, values

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
            [sg.Text('-------- RELATÓRIOS ----------', font=("Georgia", 40))],
            [sg.Text('Escolha sua opção', font=("Georgia", 25))],
            [sg.Radio('Rentabilidade por Produto', "RD1", key='1', font=("Georgia",20))],
            [sg.Radio('Análise de Produtos Mais Vendidos', "RD1", key='2', font=("Georgia",20))],
            [sg.Radio('Vendas por Vendedor', "RD1", key='3', font=("Georgia",20))],
            [sg.Radio('Compras feitas por cada cliente', "RD1", key='4', font=("Georgia",20))],
            [sg.Radio('Retornar', "RD1", key='0', font=("Georgia",20))],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de controle do estoque da A5').Layout(layout)

##
    def mostra_rentabilidade_produto(self, dados_rentabilidade):
        layout = [
            [sg.Text('------ RENTABILIDADE POR PRODUTO ----', font=("Georgia", 20))],
            [sg.Text(f"PRODUTO: {dados_rentabilidade['nome']}", font=("Georgia", 15))],
            [sg.Text(f"CÓDIGO: {dados_rentabilidade['codigo_produto']}", font=("Georgia", 15))],
            [sg.Text(f"PREÇO DE VENDA: R${dados_rentabilidade['preco_venda']:.2f}", font=("Georgia", 15))],
            [sg.Text(f"PREÇO DE COMPRA: R${dados_rentabilidade['preco_compra']:.2f}", font=("Georgia", 15))],
            [sg.Text(f"LUCRO POR UNIDADE: R${dados_rentabilidade['lucro_unidade']:.2f}", font=("Georgia", 15))],
            [sg.Button('OK')]
        ]
        window = sg.Window('Rentabilidade do Produto', layout)
        window.read()
        window.close()

    def mostra_analise_produtos_vendidos(self, dados_analise):
        layout = [
            [sg.Text('------ ANÁLISE DE PRODUTOS MAIS VENDIDOS ------', font=("Georgia", 20))],
            [sg.Text(f"PRODUTO: {dados_analise['nome']}", font=("Georgia", 15))],
            [sg.Text(f"CÓDIGO: {dados_analise['codigo_produto']}", font=("Georgia", 15))],
            [sg.Text(f"QUANT TOTAL VENDIDA: {dados_analise['quantidade_total_vendida']}", font=("Georgia", 15))],
            [sg.Text(f"VALOR TOTAL VENDIDO: R${dados_analise['valor_total_vendido']:.2f}", font=("Georgia", 15))],
            [sg.Button('OK')]
        ]
        window = sg.Window('Análise de Produtos Vendidos', layout)
        window.read()
        window.close()

    def mostra_vendas_por_vendedor(self, dados_vendedor):
        layout = [
            [sg.Text('----- RELATÓRIO DE VENDAS POR VENDEDOR -----', font=("Georgia", 20))],
            [sg.Text(f"{dados_vendedor['lugar']}º lugar", font=("Georgia", 15))],
            [sg.Text(f"NOME: {dados_vendedor['nome']}", font=("Georgia", 15))],
            [sg.Text(f"CPF: {dados_vendedor['cpf']}", font=("Georgia", 15))],
            [sg.Text(f"VALOR TOTAL VENDIDO: R${dados_vendedor['valor_total_vendido']:.2f}", font=("Georgia", 15))],
            [sg.Button('OK')]
        ]
        window = sg.Window('Vendas por Vendedor', layout)
        window.read()
        window.close()

    def mostra_compra_por_cliente(self, dados_cliente):
        layout = [
            [sg.Text(f"-------- COMPRAS DO CLIENTE {dados_cliente['nome']} ----------", font=("Georgia", 20))]
        ]
        if dados_cliente['compras']:
            layout.append([sg.Text("Compras:", font=("Georgia", 15))])
            for compra in dados_cliente['compras']:
                layout.append([sg.Text(f"- Código: {compra['codigo']}, Produto: {compra['produto']}, Quantidade: {compra['quantidade']}, Data: {compra['data']}, Valor: {compra['valor']:.2f}", font=("Georgia", 12))])
        else:
            layout.append([sg.Text("\nCliente sem compras feitas.", font=("Georgia", 15))])
        
        layout.append([sg.Button('OK')])
        window = sg.Window('Compras por Cliente', layout)
        window.read()
        window.close()

    def close(self):
        self.__window.Close()
