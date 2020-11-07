#!/usr/bin/env python3

################################
####        FUNZIONI        ####
################################

# Definiamo una funzione

def salutare():
    print('Ciao a tutti!')

# Chiamare una funzione

#salutare()
#print(salutare())
#print(salutare)

def presentarsi():
    print('Io sono Carlo')

def saluta_presentati():
    salutare()
    presentarsi()

saluta_presentati()