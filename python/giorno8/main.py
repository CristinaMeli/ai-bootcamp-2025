import csv
import sqlite3

# Carico il csv
with open("students.csv", encoding='utf-8') as fd:
    reader = csv.reader(fd, delimiter=';') #legge il file CSV ';' come separatore
    saved_data = []
    for line in reader:
        # Verifica che la riga abbia 7 elementi per evitare errori
        if len(line) == 7:
            saved_data.append(line)

data = saved_data[1:]  # Ignora l'intestazione (prima riga)

# Connessione al database SQLite
conn = sqlite3.connect("new_students.db")
cur = conn.cursor()

# Creazione della tabella se non esiste già
cur.execute(
    '''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        year_of_birth INTEGER,
        gender TEXT,
        email TEXT,
        assignments INTEGER DEFAULT 0
    )''')
conn.commit()

cur.executemany(
    "INSERT INTO students "
    "(id, first_name, last_name, year_of_birth, gender, email, assignments) "
    "VALUES (?, ?, ?, ?, ?, ?, ?)"
    "ON CONFLICT DO NOTHING",
    data
)
conn.commit()

# Query per selezionare gli studenti nati neò 2000
cur.execute("SELECT first_name, last_name "
            "FROM students "
            "WHERE year_of_birth=2000"
            )
rows = cur.fetchall()
for row in rows:
    print(row)  # stampa i risultati trovati

#query per trovare lo studente con il massimo numero di assignments
cur.execute("SELECT first_name, last_name, MAX(assignments) "
            "FROM students "
            )
rows = cur.fetchall()
for row in rows:
    print(row)

# Query per trovare tutti gli studenti di nome "Jane"
cur.execute("SELECT last_name "
            "FROM students "
            "WHERE first_name='Jane'"
            )
rows = cur.fetchall()
for row in rows:
    print(row)

# query per ordinare gli studenti in base al numeri di assignments (decrescente)
cur.execute("SELECT first_name, last_name, assignments "
            "FROM students "
            "ORDER BY assignments DESC"
            )
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()