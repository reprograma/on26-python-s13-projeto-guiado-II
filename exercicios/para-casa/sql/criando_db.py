import sqlite3
import csv 

database = sqlite3.connect('profissionais_dados_2022.db')

cursor = database.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS dados2022 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Idade INT,
                Faixa VARCHAR (10),
                Genero VARCHAR (20),
                Etnia VARCHAR (20),
                PCD VARCHAR (5),
                Estado VARCHAR (50),
                UF VARCHAR (2)
)''')

file = open('planilhareduzida.csv')

next(file)

conteudo = csv.reader(file)

for row in conteudo:
    cursor.execute("INSERT INTO dados2022 (Idade, Faixa, Genero, Etnia, PCD, Estado, UF) VALUES (?, ?, ?, ?, ?, ?, ?)")

selecionar_tudo = "SELECT * FROM dados2022"

entradas = cursor.execute(selecionar_tudo).fetchall()

database.commit()
database.close()




