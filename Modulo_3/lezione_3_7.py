#! /usr/bin/env python3


###############################
####       DIZIONARI        ###
###############################

# Per creare un dizionario possiamo utilizzare le parentesis graffe o la funzione dict()
print('\n\n\t\t\t CREAZIONE DIZIONARIO')
a = {'a' : 'uno',
     'b' : 'due',
     'c' : 3}
print(f'La variabile a è un {type(a)} ed ha valore: {a}')

b = dict({1:11, 2:'secondo', 100:[1,2,3]})
print(f'La variabile a è un {type(b)} ed ha valore: {b}')

# Per richiamare un valore possiamo fare riferimento alla sua 'chiave'.

print('\n\n\t\t\t USARE LE CHIAVI')
print(f"Nel dizionario a la chiave 'a' ha valore: {a['a']}")
print(f"Nel dizionario b la chiave '100' ha valore: {b[100]}")
# Se viene fatto riferimento ad una chiave inesistente Python restituisce errore...

#print(a['io_non_esisto'])
#
# ...ma possiamo verificare se una chiave è presente con gli operatori IN o NOT IN.
print('\n\n\t\t VERIFICARE CON "IN" O "NOT IN"')
print('io_non_esisto' in a)
if ('io_non_esisto' in a):
     print('La chiave esiste')
else:
     print('La chiave non esiste')

# Possiamo aggiungere valori con la sintassi 'dizionario[chiave] = valore'
a['io_non_esisto'] = 'ci sono!'
print(a)

# Possiamo rimuovere gli elementi con la sintassi 'del dizionario[chiave]'
del a['a']
print(a)

#################################
###      METODI dei DICT()    ###
#################################

# Il metodo items() restituisce gli elementi (chiave:valore) come una lista di tuple.
print('\n\n\t\t\t METODO ITEMS()')
print(a.items())

# Il metodo keys() restituisce una lista con solo le chiavi.
print('\n\n\t\t\t METODO KEYS()')
print(a.keys())

# Il metodo values() restituisce una lista con solo i valori.
print('\n\n\t\t\t METODO VALUES()')
print(a.values())

# Il metodo get(chiave, default) restituisce il valore associato alla chiave oppure il valore di default.
# Se non esiste e non è specificato il default restituisce il valore None
print('\n\n\t\t\t METODO GET()')
print(a.get('b', 'mio valore di default'))
print(a.get('a', 'mio valore di default'))
print(a.get('a'))

# Il metodo pop(chiave, default) rimuove restituisce il valore associato alla chiave oppure il valore di default.
# Se non esiste e non è specificato il default restituisce errore.
#
print('\n\n\t\t\t METODO POP()')
a = {'a':1,'b':2, 'c':3}
print(f'Assumiamo che il dizionario \'a\' sia: {a}')
print(f"Faccendo il pop() di 'b' ottengo: {a.pop('b', 'mio valore di default')}")
print(f'Ho fatto il pop() di \'b\' ed ora il dizionario è: {a}')

# Con update possiamo aggiungere i valori di un dizionario ad un altro dizionario.
#print('\n\n\t\t\t METODO UPDATE()')
a = {'a':1,'b':2, 'c':3}
print(f'Assumiamo che il dizionario \'a\' sia: {a}')
b = {'d':4, 'e':5}
print(f'Assumiamo che il dizionario \'b\' sia: {b}')
a.update(b)
print(f'Dopo la funzione a.update(b) il dizionario vale: {a}')

# Metodi COPY() e CLEAR()
print(f'Con il comando copy() si copia un dizionario...')
c = a.copy()
print(c)
print(f'Mentre con il comando clear() si cancella un dict...')
a.clear()
print(a)

###########################
#####        SET       ####
###########################

# Per creare un set possiamo usare l'operatore di assegnazione il metodo set()

a = {1,2,3,4,5}
b = set([3,4,5,6,7])
print(a)
print(b)

# Per creare un set vuoto dobbiamo usare la funzione set()
a = {}
b = set()
print(type(a))
print(type(b))

# Per aggiungere une elemento usiamo add() per aggiungere una lista usiamo update()
b.add(1)
print(b)
b.update([1,4,3,2,5])
print(b)

# Per rimuovere gli elementi usiamo remove(), discard() o pop()

a = {'mela','pera', 'arancia', 'mirtillo','ananas'}
print(a)
a.remove('mela')
a.discard('ananas')
x = a.pop()
print(f'Ho rimosso {x} con pop() ed ora il set contiene: {a}')

#Il medodo clear() pulisce il set, mentre del() lo elimina
a = {1,2,3}
b = {4,5,6}
a.clear()
print(len(a))
del b
#print(b)

# Operazioni con gli insiemi:
a = {1,2,3,4,5}
b = {3,4,5,6,7}
print('\n\n\t\tOPERAZIONI CON GLI INSIEMI')
print(f'Dati i set() a = {a} e b = {b}\n')
print(f'La funzione union() restituisce l\'UNIONE dei due insiemi: {a.union(b)} \n')
print(f'La funzione difference() restituisce la DIFFERENZA dei due insiemi: {a.difference(b)} \n')
print(f'La funzione intersection() restituisce l\'INTERSEZIONE dei due insiemi: {a.intersection(b)} \n')
print(f'La funzione isdisjoint() restituisce True se i due set sono DISTINTI: {a.isdisjoint(b)} \n')
print(f'La funzione issubset() restituisce True se un set CONTIENE l\'altro: {a.issubset(b)} \n')
print(f'La funzione issuperset() restituisce True se un set è CONTENUTO dall\'altro: {a.issuperset(b)} \n')

