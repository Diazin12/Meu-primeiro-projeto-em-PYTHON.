import sqlite3

conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS produtos(
id INTEGER PRIMARY KEY AUTOINCREMENT ,
nome TEXT NOT NULL,
valor REAL NOT NULL,
quantidade INTEGER NOT NULL)
""")

def cadastrar_produto (nome, valor, quantidade):
    try:
        cursor.execute("INSERT INTO produtos (nome, valor, quantidade) VALUES (?, ?, ?)",
                    (nome, valor, quantidade)
                   )
    
        conexao.commit()
        return True

    except sqlite3.Error as erro:
        print(f"Erro ao cadastrar o produto {erro}")
        return False

def buscar_todos_produtos():
    try:
        cursor.execute("SELECT * FROM produtos")
        info = cursor.fetchall()
        return info 

    except sqlite3.Error as erro:
        print(f"Erro ao buscar produto {erro}")
        return False

def buscar_produto_id(id_produto):
    try:
        cursor.execute("SELECT * FROM produtos WHERE id = ?",
        (id_produto,))
        produto = cursor.fetchone()

        return produto

    except sqlite3.Error as erro:
        print(f"Erro ao buscar o produto {erro}")

def adicionar_quantidade(id_produto, quantidade):
    try:
        cursor.execute("""
        UPDATE produtos
        SET quantidade = quantidade + ? 
        WHERE id = ?
            """,
        (quantidade, id_produto))

        conexao.commit()
        return True

    except sqlite3.Error as erro:
        print(f"Erro ao adicionar produto ao estoque {erro}.")
        return False


def remover_quantidade(id_produto, quantidade):
    try:
        cursor.execute("""
    UPDATE produtos
    SET quantidade = quantidade - ? 
    WHERE id = ?
            """,
        (quantidade, id_produto))
        conexao.commit()
        return True

    except sqlite3.Error as erro:
        print(f"Erro ao remover produto do estoque {erro}")
        return False

def excluir_produto(id_produto):
    try:
        cursor.execute("""
    DELETE FROM produtos
    WHERE id = ?
        """"",
        (id_produto,))

        conexao.commit()
        return True

    except sqlite3.Error as erro:
        print(f"Erro ao excluir produto do estoque {erro}")    
        return False

def editar_nome(id_produto, novo_nome):
    try:
        cursor.execute("""
UPDATE produtos
SET nome = ?
WHERE id = ?
""",
        (novo_nome, id_produto))
        conexao.commit()
        return True

    except sqlite3.Error as erro:
        print(f"Erro ao editar nome do produto. {erro}")
        return False
    
def editar_valor(id_produto, novo_valor):
    try:
        cursor.execute("""
UPDATE produtos
SET valor = ?
WHERE id = ?
""",
        (novo_valor, id_produto))
        conexao.commit()
        return True

    except sqlite3.Error as erro:
        print(f"Erro ao editar valor do produto. {erro}")
        return False
