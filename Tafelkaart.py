def tafelkaart(n):
    # Print de kopregel
    print("Tafel van", end="\t")
    for i in range(1, n + 1):
        print(i, end="\t")
    print()

    # Genereer de rijen
    for i in range(1, n + 1):
        print(i, end="\t")
        for j in range(1, n + 1):
            print(i * j, end="\t")
        print()

# Gebruiker voert een getal in
n = int(input("Voer een getal in voor de tafelkaart: "))
tafelkaart(n)
