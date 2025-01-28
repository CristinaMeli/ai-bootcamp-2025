# Scrivere il codice dell'esercizi qui dentro
def  mydivmod(a,b):
    if b == 0:
        raise ZeroDivisionError("Errore: Non è possibile dividere per zero!")
    result = (a//b, a%b)
    return result

def pow_list(seq):
    return [x ** 2 for x in seq]

def count_words(str):
    return "hello world" .split(" ")

def reverse_string(hello):
    return hello [:: - 1]

def factorial (n):
    return 1 if n == 0 else n * factorial(n-1)

assert factorial (5) == 120

def is_palindrome(racecar):
    return racecar == racecar [:: - 1]

def sum_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

def find_max(numbers):
    return max(numbers)

def count_vowels(helloworld):
    vowels = "aeiou"
    return sum(1 for char in helloworld if char.lower() in vowels)






