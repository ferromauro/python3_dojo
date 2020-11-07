#! /usr/bin/env python3

##############################
###         LISTE          ###
##############################

# Per creare una lista possiamo usare le parentesi quadre o il cosruttore list().

#a = [1,2,3]
#b = list(['uno','due', 'tre'])
#c = list('Hello')
#print(a)
#print(b)
#print(c)

## Le liste sono contenitori di oggetti mutabili: possiamo creare una lista vuota e poi modificarla.
#
#a = []
#print(a)
#
#b = list()
#print(b)
#
## La funzione append(elem) aggiunge un elemento alla lista.
#
#a.append(1)
#print(a)
#
## La funzione extend(seq) aggiunge una sequenza di dati alla lista.
#
#b.extend(['uno','due',3])
#print(b)
##
#a.extend(b)
#print(a)
#
## La funzione pop() restituisce ed elimina l'ultimo elemento di una lista.
#
#c = a.pop()
#print(c)
#print(a)
#
## La funzione remove serve per trovare ed eliminare un elemento.
#a.remove('uno')
#print(a)
#
## La funzione sort() ordina la lista.
#
#a = [2,3,5,1,5]
#a.sort()
#print(a)
#print(a[0])

# La funzione reverse() inverte gli elementi della lista.

#a = [1,2,100,3,4,1000]
#a.reverse()
#print(a)

#La funzione copy() crea una copia della lista, mentre clear() pulisce la lista
#a = [1,2,3]
#b = a.copy()
#a.clear()
#print(f'a: {a}')
#print(f'b: {b}')

#######################
###     SLICING     ###
#######################

#a = [1,2,3,4,5,6,7,8,9,10]
#print(a[0])
#print(a[9])
#print(a[:4])
#print(a[5:])
#print(a[2:4])
#print(a[-1])
#print(a[-3:])
#
# Possiamo modificare gli elementi utilizzando l'indexing

#a[0] = 'a'
#a[-1] = 'b'
#a[2:5] = ['c','d','e']
#print(a)

# Altre funzioni utili...

## count()
#a = [1,2,1,1,4]
#print(a.count(1))
# index()
#print(a.index(1))
#print(a.index(4))

## min() e max()
#print(min(a))
#print(max(a))

#######################
###     TUPLE       ###
#######################

#a = (1,2,3,2)
#print(a)
#print(a[2])

# Gli elementi non possono essere modificati.
#a[2] = 55

