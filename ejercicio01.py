#Implemente el siguiente algoritmo como un programa para desordenar

import random
def desordena(lista, largoLista,contador):
    if contador<largoLista:
        numeroRandom=random.randint(contador,largoLista-1)
        lista[contador],lista[numeroRandom]=lista[numeroRandom],lista[contador]
        desordena(lista,largoLista,contador+1)
A=[2,4,6,8,10,12,14]
desordena(A,len(A),0)
print(A)