from produto import Estoque
from banco import criar_tabela


def main():
    criar_tabela()
    estoque = Estoque()

    while True:
        print("\n--- MENU DO ESTOQUE ---")
        print("1- Cadastrar produto")
        print("2- Listar produtos")
        print("3- Buscar produto")
        print("4- Adicionar quantidade")
        print("5- Retirar quantidade")
        print("6- Excluir produto")
        print("7- Editar produto")
        print("0- Sair")

        opcao = input("Digite uma opção: ").strip()

        if opcao == "1":
            estoque.cadastro()
        elif opcao == "2":
            estoque.listar_produtos()
        elif opcao == "3":
            mensagem = estoque.buscar_produto()
            if mensagem:
                print(mensagem)
        elif opcao == "4":
            estoque.adicionar_estoque()
        elif opcao == "5":
            estoque.remover_estoque()
        elif opcao == "6":
            estoque.excluir_item()
        elif opcao == "7":
            estoque.editar_item()
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
