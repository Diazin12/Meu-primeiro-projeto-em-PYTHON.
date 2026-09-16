from banco import cadastrar_produto, buscar_todos_produtos, buscar_produto_id, adicionar_quantidade, remover_quantidade, excluir_produto, editar_nome, editar_valor

class Produto:
    def __init__(self, id, nome, valor, quantidade):

        self.id = id
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade

    @classmethod
    def from_tupla(cls, tupla):
        return cls (*tupla)
        

class Estoque:
    def __init__(self):
        self.lista_produtos = []

    def cadastro(self):
        print("Você escolheu a opção cadastrar produto.")

        while True:
            try:
                nome = input("Nome: ")
                valor = float(input("Valor: "))
                quantidade = int(input("Quantidade: "))

            except ValueError:
                print("Digite valores numéricos válidos.")
                continue

            if valor < 0:
                print("O valor não pode ser menor que 0")
                continue
            
            if quantidade < 0:
                print("A quantiade não pode ser menor que 0")
                continue
            cadastrar_produto(nome, valor, quantidade)

            print(" Produto cadastrado com sucesso! ")

            while True:
                try:
                    op = int(input("Deseja cadastrar mais um item? \n"
                    "1- SIM \n"
                    "2- NÂO \n"
                    "Digite uma opção: "
                    ))

                except ValueError:
                    print("Digite uma opção númerica.")
                    continue

                if op == 1:
                    break

                elif op == 2:
                    return "Encerando o progama."

                else:
                    print("Digite uma opção valida.")

    def listar_produtos(self):
        print("Você escolheu a opção listar produto.")

        produtos = buscar_todos_produtos()
        if not produtos:
            print("O estoque está vazio.")
            return
        
        for numero,produto in enumerate(produtos, start = 1):
            produtos = Produto.from_tupla(produtos)
            print(f"Produto {numero}:\n"
                  f"ID: {produtos.id}\n"
                  f"NOME: {produtos.nome}\n"
                  f"PREÇO: R${produtos.valor:.2f}\n"
                  f"QUANTIDADE: {produtos.quantidade}"
                    )        
            print("------------------------")

    def buscar_produto(self):
        print("Você escolheu a opção buscar produto.")
        try:
            id_produto = int(input("Digite o ID do produto: "))

        except ValueError:
            print("Digite o ID em números.")
            return

        produto = buscar_produto_id(id_produto)

        if produto is None:
            return "Produto não encontrado"

        produto = Produto.from_tupla(produto)
        
        print("\n--- PRODUTO ENCONTRADO ---")
        print(f"ID: {produto.id}")
        print(f"Nome: {produto.nome}")
        print(f"Valor: R$ {produto.valor:.2f}")
        print(f"Quantidade: {produto.quantidade}")
        print("--------------------------")

        
    def adicionar_estoque(self):
        print("Você escolheu a opção adicionar produto ao estoque.")
        while True:

            try:
                id_produto = int(input("Digite o ID do produto: "))

            except ValueError:
                print("Digite o ID em números.")
                continue

            produtos = buscar_produto_id(id_produto)

            if produtos is None:
                print("Produto não encontrado.")
                return

            produtos = Produto.from_tupla(produtos)

            print(f"\n--- PRODUTO {produtos.nome} ENCONTRADO ---")

            try:
                acrescimo = int(
                    input("Digite a quantidade a ser adicionada: ")
                    )
            except ValueError:
                print("Digite uma quantidade numérica.")
                continue

            
            if acrescimo <= 0:
                print("Digite uma quantidade maior que zero.")
                continue
                
            adicionar_quantidade(id_produto, acrescimo)
            quantidade_atual = produtos.quantidade + acrescimo
            print(f"Item guardado no estoque com sucesso. Quantidade atual: {quantidade_atual}")


            while True:
                op = input(
                "Deseja adicionar quantidade a outro item?\n"
                "1- SIM\n"
                "2- SAIR\n"
                "Digite uma opção: "
                )

                if op == "1":
                    break
                elif op == "2":
                    print("Adição encerrada.")
                    return
                else:
                    print("Digite uma opção válida.")

    def remover_estoque(self):
        print("Você escolheu a opção remover produto do estoque.")
        while True:

            try:
                id_produto = int(input("Digite o ID do produto: "))
            except ValueError:
                print("Digite o ID em números.")
                continue

            produtos = buscar_produto_id(id_produto)

            if produtos is None:
                print("Produto não encontrado.")
                continue

            produtos = Produto.from_tupla(produtos)

            print(f"\n--- PRODUTO {produtos.nome} ENCONTRADO ---")
            try:
                diminuir = int(input("Digite a quantidade a ser retirada: "))
            except ValueError:
                print("Digite uma quantidade numérica.")
                break

            if diminuir <= 0:
                print("Digite uma quantidade maior que zero.")
                break

            if diminuir > produtos.quantidade:
                print("Quantidade insuficiente no estoque.")
                continue

            remover_quantidade(id_produto, diminuir)
            valor_final = produtos.quantidade - diminuir
            print(f"Item retirado do estoque com sucesso. Quantidade atual: {valor_final}")
                

            while True:
                op = input("Deseja remover mais um item? \n"
                           "1- SIM \n"
                           "2- NÃO \n"
                           "Digite uma opção: ")

                if op == "1":
                    break
                elif op == "2":
                    print("Retirada encerrada.")
                    return
                else:
                    print("Digite uma opção válida.")

    def excluir_item(self):
        print("Você escolheu a opção excluir produto do estoque.")
        while True:
            try:
                id_produto = int(input("Digite o ID do produto: "))

            except ValueError:
                print("Digite o ID em números.")
                continue

            produtos = buscar_produto_id(id_produto)
            
            if produtos is None:
                print("Produto não encontrado.")
                continue

            produtos = Produto.from_tupla(produtos)

            print(f"\n--- PRODUTO {produtos.nome} ENCONTRADO ---")
            while True:
                try:
                    op_excluir = int(input("Deseja remover esse item?\n"
                              "1-SIM\n"
                              "2-NÃO\n"
                              "Digite uma das opção aqui: "
                                        ))
                except ValueError:
                    print("Digite uma opção valida.")
                    continue

                if op_excluir == 1:
                    excluir_produto(id_produto)
                    print("Produto removido com sucesso.")
                    break

                elif op_excluir == 2:
                    print("Voltando ao menu.")
                    return
                else:
                    print("Digite uma opção valida.")

            while True:
                    try:
                        op = int(input("Deseja remover mais um item? \n"
                        "1- SIM \n"
                        "2- NÂO \n"
                        "Digite uma opção: "
                                    ))

                    except ValueError:
                        print("Digite uma opção númerica.")
                        continue

                    if op == 1:
                        break

                    elif op == 2:
                        print("Exclusão encerrada.")
                        return

                    else:
                        print("Digite uma opção valida.")

    def editar_item(self):
        print("Você escolheu a opção excluir produto do estoque.")

        while True:
            try:
                id_produto = int(input("Digite o ID do produto: "))
            except ValueError:
                print("Digite o ID em números.")
                continue

            produtos = buscar_produto_id(id_produto)
                        
            if produtos is None:
                print("Item não encontrado.")
                continue

            produtos = Produto.from_tupla(produtos)

            while True:
                        
                try:
                    op = int(input(
                            f"Deseja alterar quais dados do item {produtos.nome} ?\n"
                            "1- NOME\n"
                            "2- PREÇO\n"
                            "3- NOME E PREÇO\n"
                            "Digite uma das opções: "
                                    ))
                except ValueError:
                        print("Digite uma opção numérica.")
                        continue

                if op == 1:
                    while True:
                        try:
                            op_nome = int(input("Deseja realmente alterar o nome?\n"
                              "1-SIM\n"
                              "2-NÃO\n"
                              "Digite uma das opção aqui: "
                                        ))
                        except ValueError:
                            print("Digite uma opcão valida.")
                            continue

                        if op_nome == 1:
                            novo_nome = input("Digite o novo nome: ")
                            editar_nome(id_produto, novo_nome)
                            print("Nome alterado com sucesso.")
                            break

                        elif op_nome == 2:
                            print("Voltando ao menu.")
                            return

                elif op == 2:
                    while True:
                        try:
                            op_valor = int(input("Deseja remover esse item?\n"
                              "1-SIM\n"
                              "2-NÃO\n"
                              "Digite uma das opção aqui: "
                                        ))
                        except ValueError:
                            print("Digite uma opcão valida.")
                            continue

                        if op_valor == 1:
                            try:
                                novo_valor = float(input("Digite o novo valor em R$: "))

                            except ValueError:
                                print("Digite um valor numérico.")
                                continue

                            if novo_valor < 0:
                                print("O valor não pode ser negativo.")
                                continue

                            
                            editar_valor(id_produto,novo_valor)
                            print("Valor atualizado com sucesso.")
                            break

                        elif op_valor == 2:
                            print("Alteração cancelada.")
                            break

                        else:
                            print("Opção inválida.")      

                elif op == 3:
                    while True:
                        try:
                            op_tudo = int(input("Deseja alterar o nome e o valor?\n"
                                                "1-SIM\n"
                                                 "2-NÂO\n"
                                                 "Digite uma opção aqui: "
                                                ))
                        except ValueError:
                            print("Digite uma opção valida.")
                            continue

                        if op_tudo == 1:
                            novo_nome = input(("Digite o novo nome: "))
                            try:
                                novo_valor = float(input("Digite o novo valor: R$ "))
                            except ValueError:
                                print("Digite um valor numérico.")
                                continue

                            if novo_valor < 0:
                                print("O valor não pode ser negativo.")
                                continue

                            
                            editar_nome(id_produto, novo_nome)
                            editar_valor(id_produto, novo_valor)
                            print("Valor e nome atualizado com sucesso.")
                            break

                        elif op_tudo == 2:
                            print("Alteração cancelada.")
                            break   

                        else:
                            print("Opção inválida.")
                            continue    

                while True:
                    op = input(
                        "Deseja editar outro item?\n"
                        "1- SIM\n"
                        "2- SAIR\n"
                        "Digite uma opção: "
                    )

                    if op == "1":
                        break
                    elif op == "2":
                        print("Edição encerrada.")
                        return
                    else:
                        print("Digite uma opção válida.")
