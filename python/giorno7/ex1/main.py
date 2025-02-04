import datetime
import json
import random


def carica_high_score():
    try:
        with open("high_scores.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def salva_high_score(high_scores):
    with open("high_scores.json", "w") as file:
        json.dump(high_scores, file, indent=4)


def indovina_il_numero():
    high_scores = carica_high_score()

    while True:
        numero_da_indovinare = random.randint(1, 100)
        tentativi = 0
        print("\nBenvenuto a 'Indovina il Numero'!\nSto pensando a un numero tra 1 e 100...\n")

        while True:
            try:
                tentativo = int(input("Indovina il numero da 1 a 100: "))
                tentativi += 1
            except ValueError:
                print("Input non valido, inserisci un numero intero.")
                continue

            if tentativo < numero_da_indovinare:
                print("Il numero è troppo basso!")
            elif tentativo > numero_da_indovinare:
                print("Il numero è troppo alto!")
            else:
                print(f"Hai indovinato il numero: {numero_da_indovinare} in {tentativi} tentativi!")
                break

        nome = input("Congratulazioni! Inserisci il tuo nome per registrare il punteggio: ")
        data_ora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        high_scores.append({"nome": nome, "tentativi": tentativi, "data_ora": data_ora})
        high_scores.sort(key=lambda x: x["tentativi"])
        salva_high_score(high_scores)

        print("\nClassifica attuale dei migliori punteggi:")
        for i, score in enumerate(high_scores, 1):
            print(f"{i}. {score['nome']} - {score['tentativi']} tentativi ({score['data_ora']})")

        if input("\nVuoi giocare ancora? (sì/no): ").strip().lower() != "sì":
            print("\nGrazie per aver giocato! Alla prossima!")
            break


indovina_il_numero()
