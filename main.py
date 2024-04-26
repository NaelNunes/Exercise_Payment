# Variavel tipo "dist", uma lista com produtos e seus valores
produtos_apple = {"Iphone": 4899.20, "IMac": 12350.32, "MacBook": 6788.22}
nome_do_produto = ""

print('Digite o nome do produto que deseja comprar! \n')
print(produtos_apple)
nome_do_produto = input("Nome do produto: ")

# Função que calcula o valor final com base no índice do tipo de pagamento escolhido
def calculo_pagamento(index_pagamento, nome_do_produto):
    if index_pagamento == 1:
        valor_final = produtos_apple[nome_do_produto] - (produtos_apple[nome_do_produto] * 0.10)
        print("O valor final é:", valor_final)
    elif index_pagamento == 2:
        valor_final = produtos_apple[nome_do_produto] - (produtos_apple[nome_do_produto] * 0.05)
        print("O valor final é:", valor_final)
    elif index_pagamento == 3:
        valor_final = produtos_apple[nome_do_produto]
        print("O valor final é:", valor_final,"Com duas parcelas de:", valor_final / 2)  
    elif index_pagamento == 4:
        valor_final = produtos_apple[nome_do_produto] * 1.10
        print("O valor final é:", valor_final, "Com três parcelas de:", valor_final / 3)
    else:
        print("Index Errado!")
#Estrutura de seleção que verifica se o produto consta na lista de produtos
if nome_do_produto in produtos_apple:
    print("O valor é:", produtos_apple[nome_do_produto])
    print("Escolha o metodo de pagamento agora pelo índice: \n")
    index_pagamento = int(input("1 - A vista com 10% de desconto no dinheiro ou cheque |\n2 - A vista no crédito com 5% de desconto |\n3 - Em 2 vezes sem juros |\n4 - Em 3 vezes, preço com juros de 10% |\n"))
    calculo_pagamento(index_pagamento, nome_do_produto)
else:
    print("Produto não encontrado!")
