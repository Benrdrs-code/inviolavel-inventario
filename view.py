#importando sqlite
import sqlite3 as lite

# criando conexao
con = lite.connect('dados.db')


dados = ['sofa', 'sala de estar', 'sofa que comprei em 1997', 'Marca X', '27/08/2022', '500', 'xxxxxx', 'c:imagens']
# inserir dados

# INSERIR DADOS  
with con:
    cur = con.cursor()
    query = "INSERT INTO inventario(nome, local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
    cur.execute(query,dados)

atualizar_dados = ['sofa', 'Garagem', 'sofa que comprei em 1997', 'Marca X', '27/08/2022', '500', 'xxxxxx', 'c:imagens', 1]
# Atualizar DADOS  
with con:
    cur = con.cursor()
    query = "UPDATE inventario SET nome=?, local=?, descricao=?, marca=?, data_da_compra=?, valor_da_compra=?, serie=?, imagem=? WHERE id=?"
    cur.execute(query,atualizar_dados)



ver_dados = []

# VER DADOS    
with con:
    cur = con.cursor()
    query = "SELECT * FROM inventario"
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        ver_dados.append(row)

print(ver_dados)
    