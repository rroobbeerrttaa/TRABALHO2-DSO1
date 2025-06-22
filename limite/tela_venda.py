from datetime import datetime
from teste.teste_numero_opcoes import TesteNumeroOpcoes

class TelaVenda(TesteNumeroOpcoes):

    def __init__(self):
        pass

    def teste_do_float(self, mensagem=" "):
            while True:
                valor_recebido = input(mensagem)
                try:
                    valor_recebido_tipo = float(valor_recebido)
                    return valor_recebido_tipo
                except ValueError:
                    print("Por favor, escreva somente com números.")


    def teste_do_inteiro(self, mensagem=" "):
            while True:
                valor_recebido = input(mensagem)
                try:
                    valor_recebido_tipo = int(valor_recebido)
                    return valor_recebido_tipo
                except ValueError:
                    print("Por favor, escreva somente com números inteiros. Exemplo: 1234")
    
    def teste_do_cpf(self, mensagem=" "):
        while True:
            valor_recebido = input(mensagem)
            try:
                if len(valor_recebido) == 11:
                    return valor_recebido
                else:
                    raise ValueError
            except ValueError:
                print("Por favor, escreva somente com números inteiros e 11 digitos. Exemplo: 12345678901")

    def tela_opcoes(self):
        print("-------- VENDAS ----------")
        print()
        print("1 - Fazer Venda")
        print("2 - Listar Venda")
        print("3 - Excluir Venda")
        print("0 - Retornar\n")

        opcao = self.teste_numero_opcoes("Escolha a opção: ", [0, 1, 2, 3])
        print()
        return opcao

    def pega_dados_venda(self):
        print("-------- DADOS VENDA ----------")
        print()
        cpf_vendedor = self.teste_do_cpf("CPF do vendedor: ")
        cpf_cliente = self.teste_do_cpf("CPF do cliente: ")
        codigo_produto = self.teste_do_inteiro("Código do produto: ")
        quantidade = self.teste_do_inteiro("Quantidade vendida: ")
        codigo = self.teste_do_inteiro("Código da venda: ")

        while True:
            data_input = input("Data da venda(DD/MM/AAAA): ")
            print()
            try:
                data = datetime.strptime(data_input, "%d/%m/%Y")
                break
            except ValueError:
                self.mostra_mensagem("Formato de data inválido: (DD/MM/AAAA)")

        return {"cpf_vendedor": cpf_vendedor, 
                "cpf_cliente":cpf_cliente,
                "quantidade": quantidade,
                "data": data,
                "codigo_produto": codigo_produto,
                "codigo": codigo}

    def mostra_venda(self, dados_venda):
        print("CÓDIGO DA VENDA:", dados_venda["codigo"])
        print("DATA:", dados_venda["data"])
        print("VENDEDOR:", dados_venda["vendedor"])
        print("CLIENTE:", dados_venda["cliente"])
        print("NOME DO PRODUTO:", dados_venda["produto"])
        print("QUANTIDADE:", dados_venda["quantidade"])
        print(f"VALOR TOTAL DA VENDA: R${float(dados_venda['valor']):.2f}")     
        print()

    def seleciona_venda(self):
        codigo = self.teste_do_inteiro("Código da venda que deseja selecionar: ")
        print()
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)
        print()