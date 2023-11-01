import sqlite3
import csv

file = open("female_entrepreneurship.csv", encoding="utf-8")
next(file)

content = csv.reader(file, delimiter=";")

df = sqlite3.connect('female_entrep.db')
cursor = df.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS BusinessWomen (\
    id INTEGER PRIMARY KEY AUTOINCREMENT,\
    Number INTEGER NOT NULL,\
    Country TEXT NOT NULL,\
    "Level of development" TEXT,\
    "European Union Membership" TEXT,\
    Currency TEXT,\
    "Women Entrepreneurship Index" FLOAT,\
    "Entrepreneurship Index" FLOAT,\
    "Inflation rate" FLOAT,\
    "Female Labor Force Participation Rate" FLOAT\
)""")

insert_content = "INSERT INTO BusinessWomen (Number, Country, 'Level of development', 'European Union Membership', Currency, 'Women Entrepreneurship Index', 'Entrepreneurship Index', 'Inflation rate', 'Female Labor Force Participation Rate') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(insert_content, content)

df.commit()
df.close()