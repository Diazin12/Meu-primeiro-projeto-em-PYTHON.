# 📦 Sistema de Controle de Estoque

Sistema de controle de estoque com interface web em Flask e uma versão pelo
terminal, desenvolvido em Python com armazenamento local em SQLite.

Projeto de estudo em desenvolvimento, voltado à prática de Python, SQL e
organização do código em módulos.

## Novidades da interface web

- Página inicial com cartões de acesso às operações do estoque.
- Tema escuro, fundo em degradê e menu compartilhado entre as páginas.
- Páginas de cadastro, busca, entrada, retirada, edição e exclusão de produtos.
- Listagem em tabela, com filtro por nome, total de produtos e botões para
  abrir a edição ou exclusão com o ID preenchido.
- Busca por ID com um cartão exibindo os dados do produto encontrado.
- Histórico em tabela com etiquetas coloridas para cada tipo de ação.
- Mensagens do sistema em uma caixa centralizada abaixo do menu.
- Ícones do Font Awesome, campos com rótulos e indicação de foco no teclado.
- Layout adaptável a telas menores, com rolagem horizontal nas tabelas.
- Arquivo CSS próprio para cada página, organizado com uma propriedade por linha.

A edição mantém os campos de nome e valor visíveis. A opção selecionada no
formulário define qual informação o Flask altera. A busca na página **Buscar**
é feita por ID; o filtro por nome pertence à página **Listar**.

## Funcionalidades

- Cadastrar produtos com nome, preço e quantidade inicial.
- Listar os produtos cadastrados.
- Buscar um produto pelo ID.
- Adicionar quantidade ao estoque.
- Retirar quantidade, verificando o saldo disponível.
- Editar o nome, o preço ou ambos.
- Excluir um produto pelo ID (com confirmação no terminal e aviso na página web).
- Registrar histórico de cadastros, entradas, saídas, edições e exclusões,
  com descrição, data e hora.
- Consultar o histórico pelo terminal ou pelo navegador, exibindo os registros
  mais recentes primeiro.
- Salvar os dados para consultas nas próximas execuções.

## Validações e tratamento de erros

- Tratamento de entradas numéricas inválidas com `try/except`.
- Verificação de preço e quantidade inicial para impedir valores negativos.
- Exigência de quantidades maiores que zero nas entradas e retiradas de estoque.
- Verificação de produto inexistente nas operações por ID.
- Captura de erros do SQLite (`sqlite3.Error`) em todas as funções de consulta
  e alteração do banco, cada uma retornando `True`/`False` (ou o dado
  encontrado) para indicar sucesso ou falha.

## Tecnologias

- Python 3.
- Flask para as rotas, formulários e mensagens da interface web.
- Jinja2 para os templates HTML.
- HTML e CSS para a interface e os layouts responsivos.
- Font Awesome para os ícones, carregado por CDN.
- JavaScript no filtro por nome da listagem; a página de edição não usa JavaScript.
- SQLite, utilizando o módulo `sqlite3` da biblioteca padrão.
- Módulo `datetime` da biblioteca padrão para registrar a data e a hora dos eventos.
- Programação Orientada a Objetos, com as classes `Produto` e `Estoque`.
- Consultas SQL parametrizadas.
- Conexões com o banco abertas por operação, usando gerenciador de contexto
  (`with`) e fechamento explícito da conexão em bloco `finally`.

A versão web precisa do Flask. A versão pelo terminal utiliza a biblioteca
padrão do Python. Ambas usam SQLite, sem um servidor de banco de dados separado.

## Estrutura do projeto

```text
app.py          # Aplicação Flask e rotas da interface web
main.py         # Menu principal da versão pelo terminal
produto.py      # Classes Produto e Estoque, interação e validações
banco.py        # Conexão com SQLite, produtos e histórico
templates/      # Templates Jinja2 das páginas
    base.html   # Menu compartilhado e mensagens do sistema
    index.html
    cadastrar.html
    listar.html
    buscar.html
    adicionar.html
    retirar.html
    editar.html
    excluir.html
    historico.html
static/         # CSS da base e de cada página
    base.css
    index.css
    cadastrar.css
    listar.css
    buscar.css
    adicionar.css
    retirar.css
    editar.css
    excluir.css
    historico.css
readme.md       # Documentação do projeto
estoque.db      # Banco de dados local
```

A classe `Produto` representa os dados de um item. O método de classe
`from_tupla()` converte um registro retornado pelo SQLite em um objeto `Produto`.
A classe `Estoque` reúne as operações disponíveis no terminal.

A função `perguntar_continuar(mensagem)`, em `produto.py`, centraliza a
pergunta padrão de "1-SIM / 2-SAIR" usada em várias operações (cadastrar mais
um item, remover mais um, excluir mais um, editar mais um, confirmar uma
alteração), evitando repetir a mesma lógica de validação em cada método.

Cada função de `banco.py` abre sua própria conexão com o banco (em vez de uma
conexão global compartilhada), garantindo que ela seja corretamente fechada
mesmo em caso de erro.

## Dados armazenados

A tabela `produtos` contém os seguintes campos:

| Campo | Tipo no SQLite | Descrição |
| --- | --- | --- |
| `id` | `INTEGER` | Chave primária gerada automaticamente |
| `nome` | `TEXT` | Nome do produto |
| `valor` | `REAL` | Preço do produto |
| `quantidade` | `INTEGER` | Quantidade disponível em estoque |

A tabela `historico` armazena os eventos das operações:

| Campo | Tipo no SQLite | Descrição |
| --- | --- | --- |
| `id` | `INTEGER` | Chave primária gerada automaticamente |
| `produto_id` | `INTEGER` | Referência ao produto; pode ser `NULL` após a exclusão |
| `tipo` | `TEXT` | Tipo do evento: `cadastro`, `entrada`, `saida`, `edicao` ou `exclusao` |
| `descricao_produto` | `TEXT` | Descrição da operação realizada |
| `data_hora` | `TEXT` | Data e hora local no formato `DD/MM/AAAA HH:MM:SS` |

Ao excluir um produto, os registros anteriores do histórico são preservados e
o vínculo `produto_id` passa a ser `NULL` (`ON DELETE SET NULL`). O evento de
exclusão guarda o nome e o ID original do produto na descrição.

## Como executar

Instale o Python 3 e baixe ou clone o projeto. Execute os comandos dentro da
pasta do projeto, pois o caminho de `estoque.db` é relativo à pasta atual.

### Interface web

Instale o Flask e inicie a aplicação:

```bash
python -m pip install Flask
python app.py
```

Abra [http://127.0.0.1:5000](http://127.0.0.1:5000) no navegador. Use o menu
superior ou os cartões da página inicial para acessar as operações.

O comando inicia o servidor local de desenvolvimento. Os ícones precisam de
conexão com a internet para carregar a biblioteca do Font Awesome pela CDN.

### Versão pelo terminal

```bash
python main.py
```

No Windows, você pode substituir `python` por `py` nos comandos.

O arquivo `estoque.db` e as tabelas `produtos` e `historico` são criados automaticamente caso
não existam. O caminho do banco é relativo à pasta de onde o comando é executado;
por isso, inicie o programa dentro da pasta do projeto.

## Como usar no terminal

Escolha uma opção no menu e siga as instruções do terminal:

```text
1- Cadastrar produto
2- Listar produtos
3- Buscar produto
4- Adicionar quantidade
5- Retirar quantidade
6- Excluir produto
7- Editar produto
8- Ver histórico
0- Sair
```

Use o ID para identificar o produto nas consultas e alterações. Para preços com
casas decimais, use ponto, por exemplo: `12.50`.

Na opção **8 - Ver histórico**, cada evento exibe o ID do produto, o tipo da
operação, a descrição e a data/hora. As entradas e saídas registram a quantidade
movimentada e o saldo resultante; as edições registram os valores anteriores e
novos do nome e/ou preço. Quando não há registros, o programa informa que nenhum
evento foi registrado ainda.

## Objetivo

Praticar classes, métodos de classe, estruturas de repetição, tratamento de
exceções e operações de cadastro, consulta, atualização e exclusão (CRUD) com SQLite.
