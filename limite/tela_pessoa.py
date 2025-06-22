from teste.teste_numero_opcoes import TesteNumeroOpcoes

class TelaPessoa(TesteNumeroOpcoes):
    
    def __init__(self):
        pass
    
    def teste_do_inteiro(self, mensagem=" "):
            while True:
                valor_recebido = input(mensagem)
                try:
                    valor_recebido_tipo = int(valor_recebido)
                    if valor_recebido_tipo >= 0:
                        return valor_recebido_tipo
                    else:
                        raise ValueError
                except ValueError:
                    print("Por favor, escreva somente com numeros inteiros positivos. Exemplo: 123")

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

    def tela_opcoes(self):
        print("-------- PESSOAS ----------")
        print()
        print("1 - Incluir Cliente")
        print("2 - Incluir Vendedor")
        print("3 - Listar Clientes")
        print("4 - Excluir Cliente")
        print("5 - Listar Vendedores")
        print("6 - Excluir Vendedor")
        print("0 - Retornar")
        print()
        opcao = self.teste_numero_opcoes("Escolha a opção: ", [0,1,2,3,4,5,6])
        print()
        return opcao

    def pega_dados_pessoa(self):
        print("-------- DADOS PESSOA ---------")
        print()
        nome = input("Nome: ")
        cpf = self.teste_do_cpf("CPF: ")
        celular = self.teste_do_inteiro("Celular (somente números): ")

        return {"nome": nome, "cpf": cpf, "celular": celular}

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
