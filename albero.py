# Ricevi input dall'utente
carattere = input("Inserisci il carattere da utilizzare per l'albero: ")
ampiezza_base = int(input("Inserisci l'ampiezza della base dell'albero (numero dispari): "))

# Calcola l'altezza dell'albero (si assume che la base sia sempre dispari)
altezza = ampiezza_base // 2 + 1

# Disegna la parte superiore dell'albero
i = 0
while i < altezza:
    larghezza = 2 * i + 1
    spazi = (ampiezza_base - larghezza) // 2
    print(" " * spazi + carattere * larghezza)
    i += 1