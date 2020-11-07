#! usr/bin/python3

##################### 
####   RETURN    ####
#####################

# Definiamo una funzione che restituisce un risultato

def somma(x,y):
    result = x+y
    return result

#somma(1,2)
#print(somma(1,2))
#print(somma)

def somma2(x,y):
    result = x+y
    print('Il risultato è:')
    return result

#somma2(1,2)
#print(somma2(1,2))


def somma3(x,y):
    result = x+y
    if result%2 == 0:
        print('Il risultato è pari:')
        return result
    print('Il risultato è dispari:')
    return result

#somma3(2,3)
print(somma3(2,2))