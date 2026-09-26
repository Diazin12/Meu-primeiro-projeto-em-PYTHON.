import sqlite3
from datetime import datetime

def criar_tabela():
    conexao = None
    try:
        with sqlite3.connect("estoque.db") as conexao:
            cursor = conexao.cursor()

            cursor.execute("""CREATE TABLE IF NOT EXISTS produtos(
id INTEGER PRIMARY KEY AUTOINCREMENT ,
nome TEXT NOT NULL,
valor REAL NOT NULL,
quantidade INTEGER NOT NULL)
""")          
        return True
    
    except sqlite3.Error as erro:
        print(f"Erro ao criar a tabela. {erro}")
        return False
    finally:
        if conexao is not None:
            conexao.close()

def cadastrar_produto (nome, valor, quantidade):
    conexao = None
    try:
        with sqlite3.connect("estoque.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO produtos (nome, valor, quantidade) VALUES (?, ?, ?)",
                        (nome, valor, quantidade)) 
            novo_id = cursor.lastrowid # <= Guarda o id.      
        return novo_id

    except sqlite3.Error as erro:
        print(f"Erro ao cadastrar o produto {erro}")
        return None 
    
    finally:
        if conexao is not None:
            conexao.close()

def buscar_todos_produtos():
    conexao = None
    try:
        with sqlite3.connect("estoque.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM produtos")
            info = cursor.fetchall()
            
        return info 

    except sqlite3.Error as erro:
        print(f"Erro ao buscar produto {erro}")
        return False
    
    finally:
        if conexao is not None:
            conexao.close()

def buscar_produto_id(id_produto):
    conexao = None
    try:
        with sqlite3.connect("estoque.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM produtos WHERE id = ?",
            (id_produto,))
            produto = cursor.fetchone()

        return produto

    except sqlite3.Error as erro:
        print(f"Erro ao buscar o produto {erro}")
        
    finally:
        if conexao is not None:
            conexao.close()

def adicionar_quantidade(id_produto, quantidade):
    conexao = None
    try:
        with sqlite3.connect("estoque.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
        UPDATE produtos
        SET quantidade = quantidade + ? 
        WHERE id = ?
            """,
            (quantidade, id_produto))

        return True

    except sqlite3.Error as erro:
        print(f"Erro ao adicionar produto ao estoque {erro}.")
        return False
    
    finally:
        if conexao is not None:
            conexao.close()


def remover_quantidade(id_produto, quantidade):
    conexao = None
    try:
        with sqlite3.connect("estoque.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
    UPDATE produtos
    SET quantidade = quantidade - ? 
    WHERE id = ?
            """,
            (quantidade, id_produto))
        return True

    except sqlite3.Error as erro:
        print(f"Erro ao remover produto do estoque {erro}")
        return False
    
    finally:
        if conexao is not None:
            conexao.close()

def excluir_produto(id_produto):
    conexao = None
    try:
        with sqlite3.connect("estoque.db") as conexao:
            conexao.execute("PRAGMA foreign_keys = ON") # <= # Ativa as regras de chave estrangeira nesta conexão.
            cursor = conexao.cursor()
            cursor.execute("""
    DELETE FROM produtos
    WHERE id = ?
        """,
            (id_produto,))
        return True

    except sqlite3.Error as erro:
        print(f"Erro ao excluir produto do estoque {erro}")    
        return False
    
    finally:
        if conexao is not None:
            conexao.close()

def editar_nome(id_produto, novo_nome):
    conexao = None
    try:
        with sqlite3.connect("estoque.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
UPDATE produtos
SET nome = ?
WHERE id = ?
""",
            (novo_nome, id_produto))
        return True

    except sqlite3.Error as erro:
        print(f"Erro ao editar nome do produto. {erro}")
        return False
    
    finally:
        if conexao is not None:
            conexao.close()

    
def editar_valor(id_produto, novo_valor):
    conexao = None
    try:
        with sqlite3.connect("estoque.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
UPDATE produtos
SET valor = ?
WHERE id = ?
""",
            (novo_valor, id_produto))
        return True

    except sqlite3.Error as erro:
        print(f"Erro ao editar valor do produto. {erro}")
        return False
    
    finally:
        if conexao is not None:
            conexao.close()

def criar_tabela_historico():
    conexao = None
    try:
        with sqlite3.connect("estoque.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
CREATE TABLE IF NOT EXISTS historico(
id INTEGER PRIMARY KEY AUTOINCREMENT,
produto_id INTEGER ,
tipo TEXT NOT NULL,
descricao_produto TEXT,
data_hora TEXT NOT NULL,
FOREIGN KEY (produto_id) REFERENCES produtos(id) ON DELETE SET NULL
) """) #FORGEIGN KEY = Deifine Define produto_id como uma chave estrangeira, vinculada ao id da tabela produtos, para garantir que o produto referenciado exista.
        return True
    
    except sqlite3.Error as erro:
        print(f"Erro ao criar a tabela de histórico. {erro}")
        return False

    finally:
        if conexao is not None:
            conexao.close()

def registrar_historico(produto_id, tipo, descricao_produto):
    conexao = None
    try:
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with sqlite3.connect("estoque.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
INSERT INTO historico (produto_id, tipo, descricao_produto, data_hora) VALUES (?, ?, ?, ?)
""", (produto_id, tipo, descricao_produto, data_hora))
        print(f"Registrado em: {data_hora}")
        return True
    
    except sqlite3.Error as erro:
        print(f"Erro ao registrar histórico. {erro}")
        return False    
    
    finally:
        if conexao is not None:
            conexao.close()