import MySQLdb

def conectar():
    """
    Função para conectar ao servidor
    """
    try:
        connect = MySQLdb.Connect(
            db = 'dbsqlpy',
            host = 'localhost',
            user = 'teste',
            passwd = '#'
        )
        return connect
    except MySQLdb.Error as error:
        print(f"Erro na conexão ao MySQL Server: {error}")

def desconectar(connect):
    """ 
    Função para desconectar do servidor.
    """
    if connect:
        connect.close()

def listar():
    """
    Função para listar os produtos
    """
    connect = conectar()
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM produtos;")
    produtos = cursor.fetchall()

    if len(produtos) > 0:
        print("Listando produtos...")
        print("--------------------")
        for produto in produtos:
            print(f"ID: {produto[0]}")
            print(f"Produto: {produto[1]}")
            print(f"Preço: {produto[2]}")
            print(f"Estoque: {produto[3]}")
            print("--------------------")
    else:
        print("Não existem produtos cadastrados.")
    desconectar(connect)
def inserir():
    """
    Função para inserir um produto
    """  
    connect = conectar()
    cursor = connect.cursor()

    nome = input("Informe o nome do produto: ")
    preco = float(input("Informe o preço do produto: "))
    estoque = int(input("Informe a quantidade em estoque: "))
    cursor.execute(f"INSERT INTO produtos (nome, preco, estoque) VALUES('{nome}', '{preco:.2f}','{estoque}');")
    connect.commit()

    if cursor.rowcount == 1:
        print(f"O produto {nome} foi inserido com sucesso!")
    else:
        print("Não foi possível inserir o produto.")

    desconectar(connect)
def atualizar():
    """
    Função para atualizar um produto
    """
    connect = conectar()
    cursor = connect.cursor()

    codigo = int(input("Informe o código do produto: "))
    nome = input("Informe o novo nome do produto: ")
    preco = float(input("Informe o novo preço do produto: "))
    estoque = int(input("Informe a nova quantidade em estoque: "))

    cursor.execute(f"UPDATE produtos SET nome = '{nome}', preco = '{preco:.2f}', estoque = '{estoque}' WHERE id = {codigo};")
    connect.commit()

    if cursor.rowcount == 1:
        print(f"O produto {nome} foi atualizado com sucesso!")

    else:
        print("Erro ao atualizar o produto.")

    desconectar(connect)

def deletar():
    """
    Função para deletar um produto
    """  
    connect = conectar()
    cursor = connect.cursor()

    codigo = int(input("Informe o código do produto: "))

    cursor.execute(f"DELETE FROM produtos WHERE id = {codigo}")
    connect.commit()

    if cursor.rowcount == 1:
        print("Produto excluido com sucesso!")
    else:
        print(f"Erro ao excluir o produto com o id: {codigo}")

    desconectar(connect)

def menu():
    """
    Função para gerar o menu inicial
    """
    print('=========Gerenciamento de Produtos==============')
    print('Selecione uma opção: ')
    print('1 - Listar produtos.')
    print('2 - Inserir produtos.')
    print('3 - Atualizar produto.')
    print('4 - Deletar produto.')
    opcao = int(input())
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        else:
            print('Opção inválida')
    else:
        print('Opção inválida')

