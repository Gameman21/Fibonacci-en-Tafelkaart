def fibonacci(n):
    sequence = []
    a, b = 1, 2
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Gebruiker voert een getal in
n = int(input("Voer een getal in voor de Fibonacci-reeks: "))
print("Fibonacci-reeks:", fibonacci(n))
