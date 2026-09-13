class Produto:
    def __init__(self, id, nome, valor, quantidade):

        self.id = id
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade

class Estoque:
    def __init__(self):
        self.lista_produtos = []

    def cadastro(self):
        print("Você escolheu a opção cadastrar produto.")

        while True:
            try:
                id = int(input("ID: "))
                nome = input("Nome: ")
                valor = float(input("Valor: "))
                quantidade = int(input("Quantidade: "))

            except ValueError:
                print("Digite valores numéricos válidos.")
                return
        
            for produto in self.lista_produtos:

                if produto.id == id :
                    print(" Esse item já está cadastrado. ")
                    return

            if valor < 0:
                print("O valor não pode ser menor que 0")
                continue
            
            if quantidade < 0:
                print("A quantiade não pode ser menor que 0")
                continue

            novo_produto = Produto(id, nome, valor, quantidade)
            self.lista_produtos.append(novo_produto)
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

        if not self.lista_produtos:
            print("O estoque está vazio.")
            return

        
        for numero,produto in enumerate(self.lista_produtos, start = 1):
            print(f"Produto {numero}:\n"
                  f"ID: {produto.id}\n"
                  f"NOME: {produto.nome}\n"
                  f"PREÇO: {produto.valor:.2f}\n"
                  f"QUANTIDADE: {produto.quantidade}"
                    )        
            print("------------------------")

    def buscar_produto(self):
        print("Você escolheu a opção buscar produto.")
        try:
            id = int(input("Digite o ID do produto: "))

        except ValueError:
            print("Digite o ID em números.")
            return

        for produto in self.lista_produtos:

            if id == produto.id:
                print("\n--- PRODUTO ENCONTRADO ---")
                print(f"ID: {produto.id}")
                print(f"Nome: {produto.nome}")
                print(f"Valor: R$ {produto.valor:.2f}")
                print(f"Quantidade: {produto.quantidade}")
                print("--------------------------")
                return

        return "Produto não encontrado."
        

    def adicionar_estoque(self):
        print("Você escolheu a opção adicionar produto ao estoque.")
        while True:
            if not self.lista_produtos:
                print("O estoque está vazio.")
                return

            try:
                id = int(input("Digite o ID do produto: "))

            except ValueError:
                print("Digite o ID em números.")
                return

            for produto in self.lista_produtos:

                if id == produto.id:
                    print(f"\n--- PRODUTO {produto.nome} ENCONTRADO ---")
                    try:
                        acrescimo = int(
                        input("Digite a quantidade a ser adicionada: ")
                    )
                    except ValueError:
                        print("Digite uma quantidade numérica.")
                        break

            
                    if acrescimo <= 0:
                        print("Digite uma quantidade maior que zero.")
                        break
                
                    produto.quantidade += acrescimo
                    print(f"Item guardado no estoque com sucesso. Quantidade atual: {produto.quantidade}")
                    break
            
            else:
                print("Produto não encontrado.")

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
            if not self.lista_produtos:
                print("O estoque está vazio.")
                return

            try:
                id_item = int(input("Digite o ID do produto: "))
            except ValueError:
                print("Digite o ID em números.")
                continue

            for produto in self.lista_produtos:
                if id_item == produto.id:
                    print(f"\n--- PRODUTO {produto.nome} ENCONTRADO ---")
                    try:
                        diminuir = int(input("Digite a quantidade a ser retirada: "))
                    except ValueError:
                        print("Digite uma quantidade numérica.")
                        break

                    if diminuir <= 0:
                        print("Digite uma quantidade maior que zero.")
                        break

                    if diminuir > produto.quantidade:
                        print("Quantidade insuficiente no estoque.")
                        break

                    produto.quantidade -= diminuir
                    print(f"Item retirado do estoque com sucesso. Quantidade atual: {produto.quantidade}")
                    break
            else:
                print("Produto não encontrado.")

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
            if not self.lista_produtos:
                print("O estoque está vazio.")
                return
        
            try:
                id = int(input("Digite o ID do produto: "))

            except ValueError:
                print("Digite o ID em números.")
                return
                
            for produto in self.lista_produtos:    
                if id == produto.id:
                    print(f"\n--- PRODUTO {produto.nome} ENCONTRADO ---")
                    self.lista_produtos.remove(produto)
                    print("Item removido do estoque com sucesso.")

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
                    return "Encerando o progama."

                else:
                    print("Digite uma opção valida.")

            else:
                print("Produto não encontrado.")

    def editar_item(self):
        print("Você escolheu a opção excluir produto do estoque.")

        while True:
            if not self.lista_produtos:
                print("O estoque está vazio.")
                return
        
            try:
                id_produto = int(input("Digite o ID do produto: "))
            except ValueError:
                print("Digite o ID em números.")
                continue
                        
            for produto in self.lista_produtos:
                        
                if id_produto == produto.id:
                    while True:
                        
                        try:
                            op = int(input(
                            "Deseja alterar quais dados?\n"
                            "1- NOME\n"
                            "2- PREÇO\n"
                            "3- NOME E PREÇO\n"
                            "Digite uma das opções: "
                                    ))
                        except ValueError:
                            print("Digite uma opção numérica.")
                            continue

                        if op == 1:
                            novo_nome = input(("Digite o novo nome: "))
                            produto.nome = novo_nome
                            print("Nome alterado com sucesso.")
                            break

                        elif op == 2:
                            try:
                                novo_valor = float(input("Digite o novo valor: R$ "))

                            except ValueError:
                                print("Digite um valor numérico.")
                                continue

                            if novo_valor < 0:
                                print("O valor não pode ser negativo.")
                                continue

                            
                            produto.valor = novo_valor
                            print("Valor atualizado com sucesso.")
                            break

                        elif op == 3:
                            novo_nome = input(("Digite o novo nome: "))
                            try:
                                novo_valor = float(input("Digite o novo valor: R$ "))
                            except ValueError:
                                print("Digite um valor numérico.")
                                continue

                            if novo_valor < 0:
                                print("O valor não pode ser negativo.")
                                continue

                            
                            produto.valor = novo_valor
                            produto.nome = novo_nome
                            print("Valor e nome atualizado com sucesso.")
                            break

                        else:
                            print("Opção inválida.")
                        
                    break
            else:
                print("Produto não encontrado.")

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