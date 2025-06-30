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
        if button in (None, 'Retornar'):
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
            [sg.Button('Confirmar'), sg.Cancel('Retornar')]
        ]
        self.__window = sg.Window('Sistema de controle do estoque da A5', layout, icon='imagens/iconea5.ico')

##
    def mostra_rentabilidade_produto(self, dados_rentabilidade):
        layout = [
            [sg.Text('------ RENTABILIDADE POR PRODUTO ----', font=("Georgia", 20))]]
        
        if not dados_rentabilidade:
            layout.append([sg.Text("Não há dados de rentabilidade para exibir.", font=("Georgia", 15))])
        else:
            if isinstance(dados_rentabilidade['preco_compra'], (int, float)):
                preco_compra_str = f"R${dados_rentabilidade['preco_compra']:.2f}"
            else:
                preco_compra_str = dados_rentabilidade['preco_compra']
            if isinstance(dados_rentabilidade['lucro_unidade'], (int, float)):
                lucro_unidade_str = f"R${dados_rentabilidade['lucro_unidade']:.2f}"
            else:
                lucro_unidade_str = dados_rentabilidade['lucro_unidade']
            layout = [
                [sg.Text(f"PRODUTO: {dados_rentabilidade['nome']}", font=("Georgia", 15))],
                [sg.Text(f"CÓDIGO: {dados_rentabilidade['codigo_produto']}", font=("Georgia", 15))],
                [sg.Text(f"PREÇO DE VENDA: R${dados_rentabilidade['preco_venda']:.2f}", font=("Georgia", 15))],
                [sg.Text(f"PREÇO DE COMPRA: {preco_compra_str}", font=("Georgia", 15))],
                [sg.Text(f"LUCRO POR UNIDADE: {lucro_unidade_str}", font=("Georgia", 15))],
                [sg.Button('OK')]
            ]
        window = sg.Window('Rentabilidade do Produto', layout, icon='imagens/iconea5.ico')
        window.read()
        window.close()

    def mostra_analise_produtos_vendidos(self, dados_analise):
        layout = [
            [sg.Text('------ ANÁLISE DE PRODUTOS MAIS VENDIDOS ------', font=("Georgia", 20))]]
        for i, produto in enumerate(dados_analise): #pega o index
            layout += [
            [sg.Text(f"{i + 1}º lugar", font=("Georgia", 15))],
            [sg.Text(f"PRODUTO: {produto['nome']}", font=("Georgia", 15))],
            [sg.Text(f"CÓDIGO: {produto['codigo_produto']}", font=("Georgia", 15))],
            [sg.Text(f"QUANT TOTAL VENDIDA: {produto['quantidade_total_vendida']}", font=("Georgia", 15))],
            [sg.Text(f"VALOR TOTAL VENDIDO: R${produto['valor_total_vendido']:.2f}", font=("Georgia", 15))],
            [sg.Text('-'*30, font=("Georgia", 15))]
        ]
        layout.append([sg.Button('OK')])
        window = sg.Window('Análise de Produtos Vendidos', layout, icon='imagens/iconea5.ico')
        window.read()
        window.close()

    def mostra_vendas_por_vendedor(self, dados_vendedor_lista):
        layout = [
            [sg.Text('----- RELATÓRIO DE VENDAS POR VENDEDOR -----', font=("Georgia", 20))]]
        
        if not dados_vendedor_lista:
            layout.append([sg.Text("Não há dados de vendas por vendedor para exibir.", font=("Georgia", 15))])
        else:
            for i, dados_vendedor in enumerate(dados_vendedor_lista):
                layout += [
                    [sg.Text(f"{i + 1}º lugar", font=("Georgia", 15))],
                    [sg.Text(f"NOME: {dados_vendedor['nome']}", font=("Georgia", 15))],
                    [sg.Text(f"CPF: {dados_vendedor['cpf']}", font=("Georgia", 15))],
                    [sg.Text(f"VALOR TOTAL VENDIDO: R${dados_vendedor['valor_total_vendido']:.2f}", font=("Georgia", 15))],
                    [sg.Text('-'*30, font=("Georgia", 15))]
                ]
        layout.append([sg.Button('OK')])
        window = sg.Window('Vendas por Vendedor', layout, icon='imagens/iconea5.ico')
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
        window = sg.Window('Compras por Cliente', layout, icon='imagens/iconea5.ico')
        window.read()
        window.close()

    def close(self):
        self.__window.Close()
