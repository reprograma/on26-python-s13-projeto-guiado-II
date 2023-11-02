import csv
import sqlite3

file = open("Social_Network_Ads.csv", encoding= "UTF-8")

conteudo = csv.reader(file)

connection = sqlite3.connect("propaganda.db")

cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS produto (
id INTEGER PRIMARY KEY AUTOINCREMENT,
Age INTEGER,
EstimatedSalary INTEGER,
Purchased INTEGER)""")

inserir_conteudo = "INSERT INTO produto (Age, EstimatedSalary, Purchased) VALUES (?, ?, ?)"
cursor.executemany(inserir_conteudo,conteudo)

selecionar_tudo = "SELECT * FROM produto"
entradas = cursor.execute(selecionar_tudo).fetchall()

for entrada in entradas:
    print(entrada)

connection.commit()
connection.close()