#! usr/bin/python3

########################### 
####     ITERATORI    #####
###########################

# Dizionari, Tuple, Liste. Strighe sono oggetti iterabili.
# Un oggetto iterabile è un contenitore dal quale possiamo generare un iteratore con il metodo iter()

lista = ['mela', 'auto', 2, 'Giappone']

iterarore = iter(lista)
#print(type(lista))
#print(type(iterarore))
#print(lista)
#print(iterarore)

#print(next(iterarore)) # mela
#print(next(iterarore)) # auto
#print(next(iterarore)) # 2
#print(next(iterarore)) # Giappone

# exception StopIteration
#print(next(iterarore))

# Il ciclo for loop lavora con un iteratore fino a quando non riceve l'eccezione StopIteration
#tupla = (1,2,3,4,5)
#for i in tupla:
#    print(i)

# Per creare un oggetto iteratore dobbiamo implementare i metodi __iter__() e __next__().

class Potenza():
    def __init__(self, base):
        self.base = base
    
    def __iter__(self):
        self.numero = self.base
        return self 

    def __next__(self):
        self.numero_restituito = self.numero
        self.numero = self.numero*self.base
        return self.numero_restituito

iteratore = iter(Potenza(2))
#print(next(iteratore))
#print(next(iteratore))
#print(next(iteratore))
#print(next(iteratore))
#print(next(iteratore))
#print(next(iteratore))

# ...possiamo andare avanti all'infinito
#for x in iteratore:
#    print(x)

class Potenza():
    def __init__(self, base):
        self.base = base
        self.esponente = 1

    def __iter__(self):
        self.numero = self.base
        return self 

    def __next__(self):
        if self.esponente < 5:
            self.numero_restituito = self.numero**self.esponente 
            self.esponente += 1
            return self.numero_restituito
        else: 
            raise StopIteration

iteratore = iter(Potenza(3))
for x in iteratore:
    print(x)