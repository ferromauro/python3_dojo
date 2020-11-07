#! usr/bin/python3

########################### 
####     GENERATORS    ####
###########################


tupla = (x for x in range(19))
#print(tupla)
#print(next(tupla))
#print(next(tupla))

def funzione_generatore():
    yield('Uno')
    yield('Due')
    yield('Tre')
    yield('Quattro')

#print(funzione_generatore)
#print(funzione_generatore())
#
#generatore = funzione_generatore()
#print(next(generatore))
#print(next(generatore))
#print(next(generatore))
#print(next(generatore))

# Raise Exception

#print(next(generatore))


# Generatore infinito
def generatore_infinito(numero):
    while numero:
        output = numero
        numero +=1
        yield output

#g = generatore_infinito(3)
#print(next(g))
#print(next(g))
#print(next(g))

#generatore = (x for x in range(19))
#print(generatore)
#list_comprehension = [x for x in range(19)]
#print(list_comprehension)
