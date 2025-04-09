#Inizzializare una lista con i reciproci dei primi 10 interi naturale. Stampare i float risultanti in modo da vizzualizare 8 decimali
numeriReciproci = [ i for i in range(1, 11)]
for r in numeriReciproci:
    print(f"{r:.8f}") 