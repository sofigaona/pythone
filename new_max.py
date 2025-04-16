#scrivere un programma Python che acquisisca tutte le righe di un file di testo (.txt) il cui nome
#va richiesto all'utente.
#il file suppone contenere un numero per ogni riga (anche con decimali).
#Calcolare la media e indicare il valore massimo comprensivo della riga in cui è stato trovato nel file.

# Chiediamo all'utente il nome del file da aprire
# Chiediamo all'utente il nome del file da aprire


nome_file = input("Inserisci il nome del file (con estensione .txt): ")


try:
   
    with open(nome_file, 'r') as file:
        numeri = []  

    
        for riga in file:
            riga = riga.strip()  # Rimuove eventuali spazi 
            if riga:  # Controlla che la riga non sia vuota
                numero = float(riga)  # Converte la riga in numero decimale
                numeri.append(numero)


    if numeri:
        media = sum(numeri) / len(numeri)  # Calcola la media
        massimo = max(numeri)  # Trova il valore massimo
        indice_massimo = numeri.index(massimo) + 1  # Trova la riga e aggiunge una riga (.indexa)

        print(f"\nMedia dei numeri: {media}")
        print(f"Valore massimo: {massimo} (trovato alla riga {indice_massimo})")
    else:
        print("Il file è vuoto o non contiene numeri validi.")

except FileNotFoundError:
    print("Errore: file non trovato. Controlla il nome e riprova.")
except ValueError:
    print("Errore: il file contiene dati non numerici.")
except Exception as e:
    print(f"Si è verificato un errore: {e}")


