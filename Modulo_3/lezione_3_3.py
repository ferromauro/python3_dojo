##! /usr/bin/env python3
#
#########################
####     STRINGHE     ###
#########################
#
 Assegnamo il valore di una stringa alla variabile 'a' e la stampiamo.

a = 'Hello'
print(a)


# Possiamo anche usare doppie virgolette o creare stringhe multilinea con triple virgolette.
#
#a = "Hello World"
#print(a)
#
#b = '''Ciao 
#Mondo
#!'''
#print(b)
#
## Le strinhe sono Array (Liste) e godono delle stesse caratteristiche.
#
#a = 'Hello World'
#print(a[0])
#
#print(a[2:5])
#
#print(a[:5])
#
#print(a[-1])
#
#print(a[-5:])
# Per conoscere la lunghezza di una stringa possiamo usare la funzione len().

#a = 'Hello World'
#print(len(a))

########################
#### STRING METHODS #### => consultare la pagina https://docs.python.org/3/library/stdtypes.html#string-methods
########################

# La funzione strip() rimuove gli spazi vuoti all'inizio/fine di una stringa.

#a = "   Hello World    "
#print(a)
#print(a.strip())

# Le funzioni lower() e upper() ritornano la stringa con tutti i caratteri minuscolo/maiuscolo.

#a = 'Hello World'
#print(a.lower())
#print(a.upper())

# La funzione replace() permette di modificare una stringa con un'altra stringa.

#a = 'Hello World'
#print(a.replace('World', 'Mars'))

# La funzione split() permette di avere una lista si sottostringhe in base al separatore fornito come argomento.

#a = 'Hello, World, have a nice day!'
#print(a.split(','))
#print(a.split('a'))

# La funzione find() cerca se è spresente l'argomento fornito e ne restituice la posizione. 
# La funzione count() conta le occorenze dell'argomento indicato.

#a = 'Hello World'
#print(a.find('W'))
#
#print(a.find('o'))
#print(a.count('o'))
#
#import re 
#for m in re.finditer('o',a):
#    print(m.start())
#
#########################
###   FORMATTAZIONE   ###
#########################

#a = 'Hello'
#b = 'World'
#print(a+b)
#print(a*3)
#print(a+' '+b*3)
#print((a+' '+b+' ')*3)


# Non possiamo fare la stessa cosa con variabili intere, ma possiamo usare la funzione format()

#numero = 40
#testo = 'Mi chiamo Pino ed ho {} anni'
#print(testo.format(numero))

#nome = 'Pino'
#numero = 40
#
#testo = 'Mi chiamo {} ed ho {} anni'
#print(testo.format(nome,numero))
#
#testo = 'Mi chiamo {1} ed ho {0} anni'
#print(testo.format(numero, nome))
#
#print(f'Mi chiamo {nome} ed ho {numero} anni')

#a = 'ciao'
#b = 5 
#
#print(a+str(b))
#print(type(b))
#print(type(str(b)))
