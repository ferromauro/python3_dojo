#! /usr/bin/env python3

########################
###      NUMERI      ###
########################

# Operazioni artimetiche
#
x = 5
y = 3
#
#print(f'Addizione di {x} e {y} è pari a: {x+y}.')
#print(f'Sottrazione di {x} e {y} è pari a: {x-y}.')
#print(f'Moltiplicazione di {x} e {y} è pari a: {x*y}.')
#print(f'Divisione di {x} e {y} è pari a: {x/y} ed è un numero di tipo {type(x/y)}.')
#print(f'La divisione intera di {x} e {y} è pari a: {x//y}')
#print(f'Il resto (o modulo )della divisione tra {x} e {y} è pari a: {x%y}')

# Funzioni matematiche built-in

#print(f'abs() ritorna il valore assoluto dell\'argomento: abs(1-3) == {abs(1-3)}')
#print(f'int() trasforma l\'argomento in un integer: int("3    ") == {int("3    ")}')          
#print(f'int() nel caso di un float ritorna solo la parte intera: int(3.93) == {int(3.93)}')              
#print(f'round() arrotonda per difetto: round(5.3) == {round(5.3)}')
#print(f'round() arrotonda per eccesso: round(5.6) == {round(5.6)}')            
#print(f'a seconda del valore del decimale: round(5.5) == {round(5.5)}')
## Il modulo random per generare numeri casuali

#import random
#
#print(random.random())              # Numero casuale tra 0 e 1
#print(random.randint(1,10))         # Numero intero casuale tra start e stop
#print(random.randrange(100))        # Numero casuale all'interno di un range fino all'argomento stop
#print(random.randrange(10,100,5))   # I parametri possono essere (start), stop, (step)
#
# Funzioni matematiche classiche sono contenute nel modulo math

#import math

#print(f"Approssimazione all'eccesso con math.ceil(5.2): {math.ceil(5.2)}")
#print(f"Approssimazione per difetto con math.floor(5.2): {math.floor(5.2)}")
#print(f"La funzione sqrt(9) restituisce la radice quadrata: {math.sqrt(9)}")
#print(f"La funzione pow(x,y) restituisce il valore x elevato y: math.pow(2,4) == {math.pow(2,4)}")
#print(f"La funzione hypot() restituisce la distanza euclidea (ipotenusa per due numeri): math.hypot(3,4) == {math.hypot(3,4)}")
#print(f"La funzione fatcorial() restituisce il fattoriale n!: math.factorial(4) == {math.factorial(4)}")
#print(f"Sono presenti le classiche funzioni trigonometriche...")
#print(f"Seno: math.sin(90) == {math.sin(90)}")
#print(f"Coseno: math.cos(90) == {math.cos(90)}")
#print(f"Tangente: math.tan(90) == {math.tan(90)}")
#print(f"Arcoseno: math.asin(90) == {math.asin(0.3)}")
#print(f"Arcocoseno: math.acos(90) == {math.acos(0.3)}")
#print(f"Arcotangente: math.atan(90) == {math.atan(0.3)}")