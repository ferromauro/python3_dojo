#!/usr/bin/python

# Possiamo usare una serie di elif.

#def numero(i):
#    if i==1:
#        return 'uno'
#    elif i==2:
#        return 'due'
#    elif i==3:
#        return 'tre'
#    elif i==4:
#        return 'quattro'
#    elif i==5:
#        return 'cinque'
#    elif i==6:
#        return 'sei'
#    elif i==7:
#        return 'sette'
#    elif i==8:
#        return 'otto'
#    elif i==9:
#        return 'nove'
#    elif i==0:
#        return 'zero'
#    else:
#        return 'Inserisci un numero da 0 a 9'
#
#print(numero(20))   
        
    

# Possiamo utilizzare un dizionario.

def giorno(i):
        switcher={
                0:'Domenica',
                1:'Lunedì',
                2:'Martedì',
                3:'Venerdì',
                4:'Giovedì',
                5:'Venerdì',
                6:'Sabato'
             }
        return switcher.get(i,"Giorno non valido!")

print(giorno(10))
