giorni = ("Lunedi   "+"Martedi  "+"Mercoledi"+"Giovedi  "+"Venerdi  "+"Sabato   "+"Domenica")
len(giorni)
giorno= int(input("Indica un giorno: "))
p = (giorno - 1) * 9
print( giorni[p:p+9])