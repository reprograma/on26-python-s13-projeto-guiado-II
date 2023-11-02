import sqlite3
import csv

banco = sqlite3.connect('muni_brasileiro.db')
cursor = banco.cursor()



cursor.execute('''CREATE TABLE IF NOT EXISTS municipios (
    CidadeId VARCHAR,
    Estado VARCHAR,
    Populacao_Residente INT,
    Rank_IDHM INT,
    Renda INT,
    Educacao INT,
    Carros INT,
    Regiao VACHAR)''')



with open("municipios_br2.csv", encoding='utf-8') as file:
    conteudo = csv.reader(file)

    inserir_conteudo = "INSERT INTO municipios(CidadeId, Estado, Populacao_Residente, Rank_IDHM, Renda, Educacao, Carros, Regiao)VALUES(?, ?, ?, ?, ?, ?, ?, ?)"

    cursor.executemany(inserir_conteudo, conteudo)

    selecionar_tudo = "SELECT * FROM municipios"
    entradas = cursor.execute(selecionar_tudo).fetchall()

banco.commit()
banco.close()
