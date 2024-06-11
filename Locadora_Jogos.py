# Listas iniciais
jogos_disponiveis = ['GOW', 'Minecraft', 'GTA', 'Sonic', 'FIFA']
precos_venda = [210.00, 2.99, 150.00, 1.80, 125.00]
precos_compra = [105.00, 1.50, 75.00, 0.90, 62.50]
quantidade_disponivel = [3, 0, 2, 5, 1]
vendas = []
compra_estoque = []

# Função para exibir o menu
def exibir_menu():
    print("\nMenu da Loja de Jogos")
    print("1. Registrar Venda")
    print("2. Compra de Estoque")
    print("3. Resumo da Loja")
    print("4. Ver Quantidade em Estoque")
    print("5. Sair")
    return input("Selecione uma opção: ")

# Função principal
def main():
    while True:
        opcao = exibir_menu()
        if opcao == '1':
            jogo_vendido = input('Digite o nome do jogo que foi vendido: ')
            if jogo_vendido in jogos_disponiveis:
                quantidade_vendida = int(input('Digite a quantidade vendida: '))
                indice = jogos_disponiveis.index(jogo_vendido)
                if quantidade_vendida <= quantidade_disponivel[indice]:
                    quantidade_disponivel[indice] -= quantidade_vendida
                    vendas.append(precos_venda[indice] * quantidade_vendida)
                    print(f'\n{jogo_vendido} vendido com sucesso!\n')
                else:
                    print('Não há quantidade suficiente em estoque.')
            else:
                print('Jogo não encontrado.')

        elif opcao == '2':
            jogo_comprado = input('Digite o nome do jogo comprado para o estoque: ')
            if jogo_comprado in jogos_disponiveis:
                quantidade_comprada = int(input('Digite a quantidade comprada: '))
                indice = jogos_disponiveis.index(jogo_comprado)
                quantidade_disponivel[indice] += quantidade_comprada
                compra_estoque.append(precos_compra[indice] * quantidade_comprada)
                print(f'\n{jogo_comprado} comprado com sucesso!\n')
            else:
                print('Jogo não encontrado.')

        elif opcao == '3':
            print(f'\nQuantidade de jogos em estoque:')
            for i, jogo in enumerate(jogos_disponiveis):
                print(f'{jogo}: {quantidade_disponivel[i]} unidades')
            print(f'\nTotal de Vendas: R${sum(vendas):.2f}')
            print(f'Total de Compras de Estoque: R${sum(compra_estoque):.2f}')
            print(f'Lucro Final: R${sum(vendas) - sum(compra_estoque):.2f}\n')

        elif opcao == '4':
            jogo_consultado = input('Digite o nome do jogo para ver a quantidade em estoque: ')
            if jogo_consultado in jogos_disponiveis:
                indice = jogos_disponiveis.index(jogo_consultado)
                print(f'\n{jogo_consultado} tem {quantidade_disponivel[indice]} unidades em estoque.\n')
            else:
                print('Jogo não encontrado.')

        elif opcao == '5':
            print('Fechando o Caixa...')
            break
        else:
            print('Opção inválida. Tente novamente.')

# Executar a função principal
if __name__ == "__main__":
    main()
