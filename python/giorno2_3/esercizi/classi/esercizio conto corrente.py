class Account:
    def __init__(self, name):   #accetta un argomento che è nome
        self.name = name

account = Account(name="Cristina")
account.name

assert account.name == "Cristina"

class Account:
    def __init__(self, name):   # questo è un metodo accetta un argomento che è nome
        self.name = name
        self.balance = 0
    def deposit(self, quantity): #nei metodi mettere sempre self
        self.balance += quantity

account = Account("Cristina") #account istanza Account classe

account.deposit(500)
account.balance

#account.deposit(200)  # ho messo i commenti perché nella slide dell'esercizio di gruppo questo input non c'era
#account.balance

class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 500
                                            #bisogna stare attenti all'indentazione altrimenti verrà sollevato questo errore AttributeError: 'Account' object has no attribute 'withdraw'

    def withdraw(self, quantity):
        self.balance -= quantity

account = Account("Cristina")
account.withdraw(200)
account.balance

assert account.balance == 300

account.withdraw(400)

print(account.balance)