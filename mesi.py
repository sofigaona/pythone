#Scrivere un programma per tradurre i numeri da 1 a 12 nomi dei mesi corrispondenti in italiano

mesi = ("Gennaio  "+"Febbraio "+"Marzo    "+"Aprile   "+"Maggio   "+"Giugno   "+"Luglio   "+"Agosto   "+"Settembre"+"Ottobre  "+"Novembre "+"Dicembre ")
len(mesi)
mese = int(input("Indica mese: "))
p = (mese - 1) * 9
print( mesi[p:p+9])