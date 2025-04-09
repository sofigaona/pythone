#P8.4 PAGINA 540 realizzare il crivello di Eratostene: una funzione che calcola i numeri primi, nota anche nella Antica Grecia. Sciegliete un numero intero,
#  n: questa funzione calcolerà tutti i numeri primi fino a n. Per prima cosa, inserire in un insieme tutti i numeri da 2 a n, poi eliminate dall'insieme tutti i multipli di 2, tranne (cioè 4,6,8,10,12,...)
# quindi eliminare tutti i multipli di 3, tranne 3 (cioè 6,9,12,15, ...) e proseguire fino al numero n1/2. I numeri rimasti nell'insieme sono quelli richiesti


def crivello_eratostene(n):

    lista = [True] * (n + 1)
    lista[0] = lista[1] = False  #0 e 1 sono primi
    
    #cominciamo dal numero due e elimino il multipli di 3
    for i in range(3, n + 1):
        if lista[i]:  # Se il numero è primo
           
            for j in range(i * 3, n + 1, i):     # Eliminiamo i multipli  de i 
                lista[j] = False
    
    
    return [i for i in range(3, n + 1) if lista[i]]


n = 30
numeri_primi = crivello_eratostene(n)
print(f"In numeri primi fino a {n} sono: {numeri_primi}")
