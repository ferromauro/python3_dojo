#!/usr/bin/env python3

################################
####        FUNZIONI        ####
################################

# Definiamo una funzione passando degli argomenti

def salutare(nome):
    print(f'Ciao {nome}!')

# Chiamamo la funzione
#salutare()
#salutare('Mario')
#print(salutare('Piero'))
#print(salutare)

# Inserire un valore di default
def salutare2(nome='mamma'):
    print(f'Ciao {nome}!')

#salutare2('Mario')
#salutare2()

# Inserire più di un argomento
def salutare3(nome, cognome):
    print(f'Nome di battesimo: {nome} \nNome di Famiglia: {cognome}')

#salutare3('Mario', 'Rossi')
#salutare3('Rossi', 'Mario')
#salutare3(cognome='Rossi', nome='Mario')

# Avere un numero indefinito di argomenti
def salutare4(*args):
    print('Buongiorno')
    for x in args:
        print(x)

#salutare4('Mario','Luca','Giovanni')

def salutare5(*args, saluto):
    print(saluto)
    for x in args:
        print(x)
#
salutare5('Buongiorno','Mario','Luca','Giovanni')

