#! /usr/bin/env python3

###########################
###      @PROPERTY      ###
###########################

class Utente:
    def __init__(self,**kwargs):
        self.__age = kwargs['age']   
    @property    
    def age(self):
        """Questo viene stampato nel docstring"""
        return self.__age
    @age.setter
    def age(self, x):
        if x > 18:
            self.__age = x
        else:
            print('Bisogna avere più di 18 anni...')
    @age.deleter
    def age(self):
        print('Cancello age...')
        del self.__age

        

def print_data(x):
    if not isinstance(x,Utente):
        raise TypeError('print_data: richiede un oggetto Utente()')
    print(f'L\'utente ha {x.age} anni.')

def main():
    user_one = Utente(age=22)
    print_data(user_one)    
    user_one.age = 30
    print_data(user_one)    
    del user_one.age
    #print_data(user_one)    
    help(user_one)    
    
    


if __name__ == "__main__":
    main()
