#CUESTIONARIO: ¿Cuáles son las principales ventajas de la 
# programación recursiva en Python?

import random
def desordena(lista, largoLista,contador):
    if contador<largoLista:
        numeroRandom=random.randint(contador,largoLista-1)
        lista[contador],lista[numeroRandom]=lista[numeroRandom],lista[contador]
        desordena(lista,largoLista,contador+1)
A=[1,2,3,4,5,6,7,8,9]
desordena(A,len(A),0)
print(A)