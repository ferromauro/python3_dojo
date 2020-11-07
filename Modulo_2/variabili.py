#! usr/bin/python3

##################### 
# ESEMPIO VARIABILI #
#####################

# Dichiara una variabile e stampiamola
x = 1
print(x)

# Dichiara la stessa variabile con un nuovo valore e stampiamola
#x = 'abc'
#print(x)

# ERRORE: Variabili di tipo differente non possono essere combinate
#y = 2
#print(x + str(y))

# Definiamo una funzione per vedere lo scopo delle variabili locali
def stampa():
    global x
    x = 5
    print(x)

stampa()

print(x)