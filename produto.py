from banco import cadastrar_produto, buscar_todos_produtos, buscar_produto_id, adicionar_quantidade, remover_quantidade, excluir_produto, editar_nome, editar_valor, registrar_historico

def perguntar_continuar(mensagem):
    while True:
        op = input(f"{mensagem}\n"
        "1- SIM\n"
        "2- SAIR\n"
        "Digite uma opção: "
        )
        
        if op == '1':
            return True
        
        elif op == '2':
            return False
        
        else:
            print("Digite uma opção valida")
            continue


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
            produto_id = cadastrar_produto(nome, valor, quantidade)

            if produto_id:
                registrar_historico(produto_id, "cadastro", f"Produto {nome} cadastrado com quantidade {quantidade}")
                print("Item cadastrado com sucesso.")

            else:
                print(" Não foi possível cadastrar o produto. Tente novamente. ")

            while True:
                    if perguntar_continuar("Deseja cadastrar mais um item?"):
                        break
                    
                    else:
                        print("Encerrando o progama.")
                        return "Encerrando o progama."

    def listar_produtos(self):
        print("Você escolheu a opção listar produto.")

        produtos = buscar_todos_produtos()
        if not produtos:
            print("O estoque está vazio.")
            return
        
        for numero, produto in enumerate(produtos, start=1):
            produto = Produto.from_tupla(produto)
            print(f"Produto {numero}:\n"
                  f"ID: {produto.id}\n"
                  f"NOME: {produto.nome}\n"
                  f"PREÇO: R${produto.valor:.2f}\n"
                  f"QUANTIDADE: {produto.quantidade}"
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
                
            sucesso = adicionar_quantidade(id_produto, acrescimo)
            quantidade_atual = produtos.quantidade + acrescimo
            if sucesso:
                registrar_historico(
                id_produto,
                "entrada",
                f"Adicionadas {acrescimo} unidades ao produto {produtos.nome}. "
                f"Quantidade atual: {quantidade_atual}"
)
                print(f"Item guardado no estoque com sucesso. Quantidade atual: {quantidade_atual}")

            else:   
                print(" Não foi possível adicionar o produto ao estoque. Tente novamente. ")

            while True:
                if perguntar_continuar("Deseja adicionar mais um item ao estoque?"):
                    break
                
                else:
                    print("Encerrando o progama.")
                    return

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

            sucesso = remover_quantidade(id_produto, diminuir)
            valor_final = produtos.quantidade - diminuir

            if sucesso:
                registrar_historico(
                id_produto,
                "saida",
                f"Removido {diminuir} unidades ao produto {produtos.nome}. "
                f"Quantidade atual: {valor_final}"
)
                print(f"Item retirado do estoque com sucesso. Quantidade atual: {valor_final}")

            else:
                print(" Não foi possível remover o produto. Tente novamente. ")

            while True:
                if perguntar_continuar("Deseja remover mais um item do estoque?"):
                    break
                
                else:
                    print("Encerrando o progama.")
                    return

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
                quer_excluir = perguntar_continuar("Deseja realmente excluir esse item?")
                
                if quer_excluir:
                    sucesso = excluir_produto(id_produto)

                    if sucesso:
                        registrar_historico(
                        None, # <= Usa None porque o produto já foi excluído; o ID original fica na descrição.
                        "exclusao",
                        f"Item {produtos.nome} retirado do estoque (ID original: {id_produto}) excluído.) "
)
                        print("Produto removido com sucesso.")
                        break

                    else:
                        print(" Não foi possível excluir o produto. Tente novamente. ")

                else:
                    print("Voltando ao menu.")
                    return

            while True:
                if perguntar_continuar("Deseja excluir mais um item?"):
                    break
                
                else:
                    print("Encerrando o progama.")
                    return

    def editar_item(self):
        print("Você escolheu a opção editar produto do estoque.")

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
                        quer_alterar = perguntar_continuar("Confirme se você realmente deseja alterar o nome.")
                        if quer_alterar:
                            novo_nome = input("Digite o novo nome: ")
                            sucesso = editar_nome(id_produto, novo_nome)

                            if sucesso:
                                registrar_historico(id_produto, "edicao",
                                                    f"Nome alterado de {produtos.nome} para {novo_nome}"
                                                    )
                                print("Nome alterado com sucesso.")
                                break

                            else:
                                print(" Não foi possível alterar o nome do produto. Tente novamente. ")
                        
                        else: 
                            print("Alteração cancelada.")
                            break

                elif op == 2:
                    while True:
                        quer_alterar = perguntar_continuar("Confirme se você realmente deseja alterar o valor.")
                        
                        if quer_alterar:
                            try:
                                novo_valor = float(input("Digite o novo valor em R$: "))
                            except ValueError:
                                print("Digite um valor numérico.")
                                continue

                            if novo_valor < 0:
                                print("O valor não pode ser negativo.")
                                continue

                            
                            sucesso2 = editar_valor(id_produto,novo_valor)

                            if sucesso2:
                                registrar_historico(id_produto, 
                                                    "edicao",
                                                    f"Valor do produto {produtos.nome} alterado"
                                                    f"de R$ {produtos.valor:2f} para R$ {novo_valor:.2f}"
                                                    )
                                print("Valor atualizado com sucesso.")
                                break

                            else:
                                print(" Não foi possível alterar valor do produto. Tente novamente. ")

                        else:
                            print("Alteração cancelada.")
                            break  

                elif op == 3:
                    while True:
                        quer_alterar = perguntar_continuar("Confirme se você realmente deseja alterar o nome e o valor.")
                        if quer_alterar:
                            novo_nome = input(("Digite o novo nome: "))
                            try:
                                novo_valor = float(input("Digite o novo valor: R$ "))
                            except ValueError:
                                print("Digite um valor numérico.")
                                continue

                            if novo_valor < 0:
                                print("O valor não pode ser negativo.")
                                continue

                            
                            sucesso_nome = editar_nome(id_produto, novo_nome)
                            sucesso_valor = editar_valor(id_produto, novo_valor)
                            sucesso3 = sucesso_nome and sucesso_valor

                            if sucesso3:
                                registrar_historico(
                                id_produto,
                                "edicao",
                                f"Nome alterado de {produtos.nome} para {novo_nome}. "
                                f"Valor alterado de R$ {produtos.valor:.2f} para R$ {novo_valor:.2f}"
                            )
                                print("Valor e nome atualizado com sucesso.")
                                break

                            else:
                                print(" Não foi possível alterar os dados do produto. Tente novamente. ")

                        else:
                            print("Alteração cancelada.")
                            break  

                while True:
                    if perguntar_continuar("Deseja editar outro item?"):
                        break
                    
                    else:
                        print("Edição encerrada.")
                        return