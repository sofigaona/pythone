#pag 602/603 p9.11
#realizzate una classe, Letter, che consenta di scrivere e impaginare una semplice lettera. Il costruttore riceve i nomi del mittente (letterFrom)
#e il destinatario (letterTo):

#def__intit__(self, letterFrom, letterTo):
#realizare il metodo:
# def addLine(self, line) :

#che aggiunga una riga di testo (line) al corpo della lettera, in fondo, e il metodo:
#def getText(self ):
#che restituisca l'intero testo della lettera, avente questa forma: 
# Dear nomeDestinatario:
#riga vuota
#prima riga del corpo della lettera
#seconda riga del corpo
# . . . 
#Ultima riga del corpo
#riga vuota
#Sincerely,
#riga vuota
#nomeMittente
#Progettate anche un programma di collaudo che, dopo aver costruito un oggetto di tipo Letter e aver invocato due volte
#addLine, visualizzi questa lettera:
# Dear John:
# I am sorry we must part.
# I wish you all best.
# Sincerrely,
#Mary

class Letter:
    def __init__(self, letterFrom, letterTo):
        self._letterFrom = letterFrom
        self._letterTo = letterTo
        self.body = []

    def addLine(self, line):
        self.body.append(line)

    def getText(self):
        lines = [f"Dear {self._letterTo}:", ""]
        lines.extend(self.body)
        lines.append("")
        lines.append("Sincerely,")
        lines.append("")
        lines.append(self._letterFrom)
        return "\n".join(lines)


# Creazione della lettera da Mary a John
letter = Letter("Mary", "John")


letter.addLine("I am sorry we must part.")
letter.addLine("I wish you all best.")

# lettera completa
print(letter.getText())

    
