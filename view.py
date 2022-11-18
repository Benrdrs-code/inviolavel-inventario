#importando sqlite
import sqlite3 as lite

# -=-=-=-=-= criando conexao -=-=-=-=-= 
con = lite.connect('dados.db')
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


# -------------- CRUD {
def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO inventario(nome, local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
        cur.execute(query,i)

def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE inventario SET nome=?, local=?, descricao=?, marca=?, data_da_compra=?, valor_da_compra=?, serie=?, imagem=? WHERE id=?"
        cur.execute(query,i)

def deletar_form(i):    
    with con:
        cur = con.cursor()
        query = "DELETE FROM inventario WHERE id=?"
        cur.execute(query,i)

def ver_form():
    ver_dados = []   
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados

def ver_item(id):
    ver_dados_invidual = []
    id = 0
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario WHERE i=?"
        cur.execute(query,id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_invidual.append(row)
#  } CRUD --------------