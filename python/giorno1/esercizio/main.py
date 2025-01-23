print('Inizio programma')

# Assegno la variabile foo
foo = False

# Questi controlli assert devono passare tutti
assert bool(1)   #0 è equivalente di false lo sostituisco con 1 di True
assert foo == False #Ho cambiato False = foo in: foo = False, poiché avevamo definito precedentemente la variabile foo in False, non si possono ridefinire valori booleani.
assert True is not False
assert False != True
assert None is not False
assert None is False

# Faccio alcune operazioni aritmetiche sui numeri interi
bar = 2 #Non si può dividere per 0, quindi l'ho sostituito con 2
baz = 1
result = baz / bar

# Incremento il risultato di uno
result += 1

# Decremento il risultato di uno
result -= 1


# Controllo che il valore non sia negativo
assert result >= 0

# Concateno le stringhe
message = "hello" + b"world".decode() #correzione: non si possono concatenare stringhe e byte direttamente

# Concateno le stringhe
message = "hello" + b"world"

# Creo una lista e la estendo
li1 = [1, 2]
li1 += [3]

# Prependo un valore alla lista
li1.insert(0,0)

# Verifico che il risultato sia quello che mi aspetto
assert li1 == [0, 1, 2, 3]

# Creo una tupla e la estendo
tu1 = (1, 2)
tu1 += (3,)

assert tu1 == (1, 2, 3)

# Creo un dict

d1 = {}
d1['a'] = 1
d1['b'] = 2

assert d1['a'] == 1
assert d1 == {'a': 1, 'b': 2}

# Cancello la chiave "b"
del d1['b']

# Controllo che il dict non contenga ancora la chiave "b"
assert 'b'not in d1

# Potrei anche controllarlo in questo modo
# e verificare anche la presenza di "a"
if 'b' in d1:
    assert False
elif 'a'not in d1:
    assert False
else:
    assert True

# Stampo la scritta "Ciao" tre volte poi esco
count = 0
for idx in [1, 2, 3]:
    count += 1
    print("Ciao")

# Conto le volte che l'ho stampata
count = 0
for idx in [1, 2, 3]:
    count += 1
    print("Ciao")

# Controllo che l'abbia stampata tre volte
assert count == 3

# Stampo di nuovo la scritta "Ciao" tre volte poi esco
num = 3
while num > 0:
    print("Ciao")
    num -= 1

print("Fine programma")

# Bonus: verifico la seguente operazione sui float
#assert 0.1 + 0.2 == 0.3