#!/usr/bin/python


############################
###         FOR          ###
############################

# Possiamo iterare liste, set, dizionari, tuple
#frutta = ['mela','pera','banana']
#frutta = {'mela','pera','banana'}
#frutta = ('mela','pera','banana')
#frutta = {0:'mela',1:'pera',2:'banana'}

#for x in frutta.keys():
#    print(x)


# La funzione range()

#for x in range(10):
#    print(x)
#else:
#   print('Ho finito')

# Nested Loops

var_x = [10,20,30,40,50]
var_y = range(10)
#
for x in var_x:
    for y in var_y:
        print(x+y)
        