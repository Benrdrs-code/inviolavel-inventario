#importando sqlite
import sqlite3 as lite

# criando conexao
con = lite.connect('dados.db')


dados = ['vaso', 'sala de estar', 'vaso que comprei no mercado ao lado', 'Marca X', '27/08/2022', '100', 'xxxxxx', 'c:imagens']
# inserir dados

with con:
    cur = con.cursor()
    query = "INSERT INTO inventario(nome, local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
    cur.execute(query,dados)

    