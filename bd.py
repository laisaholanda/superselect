import mysql.connector
from mysql.connector import errors
from datetime import datetime

def criarConexao():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password="",
            database="superselect"
        )
        return conexao
    except errors.InterfaceError as error: 
        print("Erro de integridade: ", error)
        return None

def login(usuario, senha):
    conexao = criarConexao()
    if conexao is None:
        return {"erro": "Erro de conexão"}
    
    cursor = conexao.cursor()
    cursor.execute(f"SELECT * FROM usuario WHERE idUsuarios = %s AND senhaUsuarios = %s;", (usuario, senha))
    resultado = cursor.fetchall()

    usuarios = {}

    if len(resultado) > 0:
        usuarios = {
            'id': resultado[0][0],
            'nome': resultado[0][1],
            'senha': resultado[0][2],
            'tipo': resultado[0][3]
        }
    else:
        usuarios ["erro"] = "Usuário não encontrado"
    
    cursor.close()
    conexao.close()
    return usuarios

def listarProdutos():
    conexao = criarConexao()
    if conexao is None:
        return {"erro": "Erro de conexão"}
   
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    resultado = cursor.fetchall()
    
    produtos = {}
    if len(resultado) > 0:
        for i in range(len(resultado)):
            produtos[resultado[i][0]] = {
                "nome": resultado[i][1],
                "descricao": resultado[i][2],
                "categoria": resultado[i][3],
                "preco": resultado[i][4],
                "validade": resultado[i][5],
            }
            
    
    print(produtos)
    cursor.close()
    conexao.close()
    return produtos
