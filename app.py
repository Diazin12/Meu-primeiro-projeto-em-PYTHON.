#CRIANDO API

from flask import Flask, jsonify, request, url_for, render_template, redirect, flash
from produto import buscar_todos_produtos, buscar_produto_id, cadastrar_produto, editar_nome, editar_valor, excluir_produto, adicionar_quantidade, remover_quantidade
from banco import criar_tabela, buscar_historico, criar_tabela_historico, registrar_historico

app = Flask(__name__)
app.secret_key = "chave-secreta"

criar_tabela()
criar_tabela_historico()

@app.route('/')
def teste():
    return render_template("index.html")

@app.route('/listar')
def listar_produtos():
    produtos = buscar_todos_produtos()
    return render_template("listar.html", produtos = produtos)

@app.route('/cadastrar', methods = ['GET','POST'])
def cadastro():

    if request.method == 'POST': 
        nome = request.form['nome']
        
        try:
            valor = float(request.form['valor'])
            quantidade = int(request.form['quantidade'])
            
        except ValueError:
            flash("Digite valores válidos.")
            return redirect(url_for('cadastro'))

        if valor < 0:
            flash("O valor não pode ser negativo.")
            return redirect(url_for('cadastro'))
        
        if quantidade < 0:
            flash("A quantidade não pode ser negativa.")
            return redirect(url_for('cadastro'))
    
        produtos_id = cadastrar_produto(nome, valor, quantidade)
    
        if produtos_id:
            registrar_historico(produtos_id,"cadastro",
                            f"Produto {nome} cadastrado com quantidade {quantidade}")
            
            flash("Produto cadastrado com sucesso!")
            
            return redirect(url_for('listar_produtos'))
    
    return render_template('cadastrar.html')
    


@app.route('/buscar/', methods = ['GET', 'POST'])
def buscar( ):
    
    produto = None
    
    if request.method == 'POST':
        try:
            id_produto = int(request.form['id_produto'])
            
        except ValueError:
            flash("Digite um ID válido.")
            return redirect(url_for('buscar'))
        
        produto = buscar_produto_id(id_produto)
        
        if produto is None:
            flash("Produto não encontrado.")
            return redirect(url_for('buscar'))
        
    return render_template('buscar.html', produto=produto)
    

@app.route('/adicionar/', methods = ['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        try:
            id_produto = int(request.form['id_produto'])
            
        except ValueError:
            flash("Digite valores válidos.")
            return redirect(url_for('adicionar'))
        
        quantidade = int(request.form['quantidade'])
        
        produto = buscar_produto_id(id_produto)

        if produto is None:
            flash("Produto não encontrado.")
            return redirect(url_for('adicionar'))

        if quantidade <= 0:
            flash("A quantidade deve ser maior que zero.")
            return redirect(url_for('adicionar'))

        if adicionar_quantidade(id_produto, quantidade):

            registrar_historico(
                id_produto,
                "entrada",
                f"Adicionadas {quantidade} unidades ao produto {produto[1]}"
                )
            
            flash("Quantidade adicionada com sucesso!")

            return redirect(url_for('listar_produtos'))
        
        flash("Não foi possível adicionar ao estoque.")
        return redirect(url_for('adicionar'))

    return render_template('adicionar.html')

@app.route('/retirar/', methods = ['GET', 'POST'])
def retirar():
    
    if request.method == 'POST':
        try:
            id_produto = int(request.form['id_produto'])
            quantidade = int(request.form['quantidade'])
            
        except ValueError:
            flash("Digite valores válidos.")
            return redirect(url_for('retirar'))
        
        produto = buscar_produto_id(id_produto)

        if produto is None:
            flash("Produto não encontrado.")
            return redirect(url_for('retirar'))
    
        if quantidade <= 0:
            flash("A quantidade deve ser maior que zero.")
            return redirect(url_for('retirar'))
    
        if quantidade > produto[3]:
            flash("Quantidade insuficiente no estoque.")
            return redirect(url_for('retirar'))
        
        if remover_quantidade(id_produto, quantidade):
            registrar_historico(
                id_produto,
                "saida",
                f"Removidas {quantidade} unidades do produto {produto[1]}"
            )
            
            flash("Quantidade retirada com sucesso!")
            
            return redirect(url_for('listar_produtos'))
        
        flash("Não foi possível retirar do estoque.")
        return redirect(url_for('retirar'))

    return render_template('retirar.html')

@app.route('/remover/', methods = ['GET', 'POST'])
def excluir():
    
    if request.method == 'POST':
        try:
            id_produto = int(request.form['id_produto'])
            
        except ValueError:
            flash("Digite valores válidos.")
            return redirect(url_for('excluir'))
        
        
        produto = buscar_produto_id(id_produto)
        
        if produto is None:
            flash("Produto não encontrado.")
            return redirect(url_for('excluir'))
        
        if excluir_produto(id_produto):    
            registrar_historico(
                None,
                "exclusao",
                f"Produto {produto[1]} excluído. ID original: {id_produto}"
                )
            
            flash("Produto excluído com sucesso!")
            
            return redirect(url_for('listar_produtos'))
        
        flash("Não foi possível excluir o produto.")
        return redirect(url_for('excluir'))
    
    return render_template('excluir.html')
    

@app.route('/editar/', methods = ['GET', 'POST'])
def editar():
    
    if request.method == 'POST':
        try:
            id_produto = int(request.form['id_produto'])
            
        except ValueError:
            flash("Digite um ID válido.")
            return redirect(url_for('editar'))
        
        opcao = request.form['opcao']
        produto = buscar_produto_id(id_produto)
        
        if produto is None:
            flash("Produto não encontrado.")
            return redirect(url_for('editar'))
        
        if opcao not in ('1', '2', '3'):
            flash("Escolha uma opção válida.")
            return redirect(url_for('editar'))
        
        if opcao == '1':
            novo_nome = request.form['nome']
            editar_nome(id_produto, novo_nome)
            
            registrar_historico(
            id_produto,
            "edicao",
            f"Nome alterado de {produto[1]} para {novo_nome}")
            
            flash("Nome alterado com sucesso!")
            
        elif opcao == '2':
            
            try:
                novo_valor = float(request.form['valor'])
                
            except ValueError:
                flash("Digite um valor válido.")
                return redirect(url_for('editar'))
            
            if novo_valor < 0:
                flash("O valor não pode ser negativo.")
                return redirect(url_for('editar'))
            
            editar_valor(id_produto, novo_valor)
            
            registrar_historico(
                id_produto,
                "edicao",
                f"Valor alterado de R$ {produto[2]} para R$ {novo_valor}")
            
            flash("Valor alterado com sucesso!")
            
        elif opcao == '3':
            novo_nome = request.form['nome']
            try:
                novo_valor = float(request.form['valor'])
                
            except ValueError:
                flash("Digite um valor válido.")
                return redirect(url_for('editar'))
            
            if novo_valor < 0:
                flash("O valor não pode ser negativo.")
                return redirect(url_for('editar'))

            editar_valor(id_produto, novo_valor)
            editar_nome(id_produto, novo_nome)
            
            registrar_historico(
                id_produto,
                "edicao",
                f"Nome alterado de {produto[1]} para {novo_nome} e valor de R$ {produto[2]} para R$ {novo_valor}"
                )
            
            flash("Nome e valor alterados com sucesso!")
            
        return redirect(url_for('listar_produtos'))
            
    return render_template('editar.html')

@app.route('/historico')
def historico():

    historico = buscar_historico()

    return render_template(
        'historico.html',
        historico=historico
    )
    

if __name__ == '__main__':
    app.run(debug = True)
    
