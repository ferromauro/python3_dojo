#! usr/bin/python3

################################# 
####     LAMBDA FUNCTIONS    ####
#################################

# Creiamo una funzione lambda con un solo argomento

#x = lambda a : a*a
#print(x(5))

# Creiamo una funzione lambda con più di un argomento
#x = lambda a,b : a+b
#print(x(5,3))#    

# Possiamo invocarle direttamente.

#x = (lambda x,y: x*y)(6,7) 
#print(x)

# Possiamo utilizzarle in un ciclo for.

#for el in range(10):
#    print((lambda a: a**2)(el))

# Possono esserci degli argomenti con valori di default.

#print((lambda a,b,c=3: a+b+c)(1,2,6))
#print((lambda a,b,c=3: a+b+c)(3,3))

# Possiamo utilizzare le keyword per gli argomenti
print((lambda a,b=10,c=0: a+b+c)(10,10))

