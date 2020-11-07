#! usr/bin/python3

########################### 
####     DECORATORS    ####
###########################

# Definiamo una funzione che stampa 'Hello'

def hello():
    print('Hello')

# Definiamo un decoratore che accetta una funzione come argomento:

def funzione_decoratore(func):
    def inner():
        print('Io appartengo al decoratore')
        func()
        print('Il decoratore ti saluta!')
    
    return inner

#hello()
#funzione_decoratore(hello)
#d = funzione_decoratore(hello)
#d()

# Possiamo evitare di usare una variabile ma non è molto elegante come soluzione.
#funzione_decoratore(hello)()

# Possiamo creare una funzione che viene sempre inviata al decoratore.

#@funzione_decoratore
#def goodbye():
#    print('Goodbye')
#
#goodbye()