class Conjunto:
    __Numeros = None
    
    def __init__(self,lista):
        self.__Numeros = lista
    
    def __add__(self,Otro):
       return self.__Numeros + Otro.__Numeros 
    
    def __sub__(self,Otro):
        return set(self.__Numeros) - set(Otro.__Numeros)
    
    def __eq__(self,Otro):
        return self.__Numeros == Otro.__Numeros
 
    
if __name__=='__main__':
    

    A = Conjunto([1,2,3,4])
    B = Conjunto([3,4,5,6])
    
    print('Ingrese una opcion')
    opcion = ''
    while opcion != 's':
        print('a)_Union.\nb)_Resta.\nc)_Comparacion.\ns)_Salir.')
        opcion = input()
    
        if opcion == 'a':
            print(A + B)
            print(B + A)
            print('\nQue desea hacer ahora')       
        elif opcion == 'b': 
            print(list(A - B))
            print(list(B - A))
            print('\nQue desea hacer ahora')
            
        elif opcion == 'c':
            if A == B:
                print('Son iguales')
            else:
                print('Son distintas')
        
        elif opcion == 's':
            print('\n-----FIN DEL PROGRAMA--------')
        
        else:
            print('Ingreso mal la opcion, ingrese nuevamente')