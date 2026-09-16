# 📦 Sistema de Controle de Estoque

Sistema de controle de estoque pelo terminal, desenvolvido em Python com
Programação Orientada a Objetos (POO) e armazenamento local em SQLite.

Projeto de estudo em desenvolvimento, voltado à prática de Python, SQL e
organização do código em módulos.

## Funcionalidades

- Cadastrar produtos com nome, preço e quantidade inicial.
- Listar os produtos cadastrados (com ajuste pendente descrito abaixo).
- Buscar um produto pelo ID.
- Adicionar quantidade ao estoque.
- Retirar quantidade, verificando o saldo disponível.
- Editar o nome, o preço ou ambos.
- Excluir um produto mediante confirmação.
- Salvar os dados para consultas nas próximas execuções.

## Validações e tratamento de erros

- Tratamento de entradas numéricas inválidas com `try/except`.
- Verificação de preço e quantidade inicial para impedir valores negativos.
- Exigência de quantidades maiores que zero nas entradas e retiradas de estoque.
- Verificação de produto inexistente nas operações por ID.
- Captura de erros do SQLite nas funções de consulta e alteração do banco.

## Tecnologias

- Python 3.
- SQLite, utilizando o módulo `sqlite3` da biblioteca padrão.
- Programação Orientada a Objetos, com as classes `Produto` e `Estoque`.
- Consultas SQL parametrizadas.

Não é necessário instalar bibliotecas externas ou configurar um servidor de banco de dados.

## Estrutura do projeto

```text
main.py      # Menu principal e início da aplicação
produto.py   # Classes Produto e Estoque, interação e validações
banco.py     # Conexão com SQLite e operações de persistência
readme.md    # Documentação do projeto
estoque.db   # Banco de dados local, criado automaticamente se não existir
```

A classe `Produto` representa os dados de um item. O método de classe
`from_tupla()` converte um registro retornado pelo SQLite em um objeto `Produto`.
A classe `Estoque` reúne as operações disponíveis no terminal.

## Dados armazenados

A tabela `produtos` contém os seguintes campos:

| Campo | Tipo no SQLite | Descrição |
| --- | --- | --- |
| `id` | `INTEGER` | Chave primária gerada automaticamente |
| `nome` | `TEXT` | Nome do produto |
| `valor` | `REAL` | Preço do produto |
| `quantidade` | `INTEGER` | Quantidade disponível em estoque |

## Como executar

1. Instale o Python 3.
2. Baixe ou clone o projeto.
3. Abra o terminal na pasta do projeto e execute:

```bash
python main.py
```

No Windows, caso utilize o inicializador `py`, execute `py main.py`.

O arquivo `estoque.db` e a tabela `produtos` são criados automaticamente caso
não existam. O caminho do banco é relativo à pasta de onde o comando é executado;
por isso, inicie o programa dentro da pasta do projeto.

## Como usar

Escolha uma opção no menu e siga as instruções do terminal:

```text
1- Cadastrar produto
2- Listar produtos
3- Buscar produto
4- Adicionar quantidade
5- Retirar quantidade
6- Excluir produto
7- Editar produto
0- Sair
```

Use o ID para identificar o produto nas consultas e alterações. Para preços com
casas decimais, use ponto, por exemplo: `12.50`.

## Ajustes pendentes

- Corrigir a listagem para converter cada tupla em `Produto`, em vez de passar
  a lista inteira para `from_tupla()`.
- Ajustar a opção de editar outro item para solicitar um novo ID.
- Verificar os retornos das funções do banco antes de exibir mensagens de sucesso:
  atualmente, as operações podem anunciar sucesso mesmo após um erro de persistência.

## Objetivo

Praticar classes, métodos de classe, estruturas de repetição, tratamento de
exceções e operações de cadastro, consulta, atualização e exclusão (CRUD) com SQLite.
