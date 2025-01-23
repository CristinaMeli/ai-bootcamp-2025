#Bonus
#Scrivere un altro programma in Python che stampi a schermo il seguente:
#0.il contenuto di questo file README.md

percorso_file = r"C:\Users\crist\Downloads\README.md"
with open(percorso_file, "r") as file:
    contenuto = file.read()
    print(contenuto)
