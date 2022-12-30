#Corra el algoritmo anterior "desordena" (del ejercicio 1) muchas veces para la misma
#sucesión de entrada. ¿Cómo puede analizarse la salida para determinar si es
# verdaderamente "aleatotrio?
#=>Respuesta: Lopodemos determinar al ejecutar varias veces el algoritmo y ver que
#salen diferentes respuestas en cada una de las ejecuciones.

import random
def desordena(lista, largoLista,contador):
    if contador<largoLista:
        numeroRandom=random.randint(contador,largoLista-1)
        lista[contador],lista[numeroRandom]=lista[numeroRandom],lista[contador]
        desordena(lista,largoLista,contador+1)
A=[2,4,6,8,10,12,14]
desordena(A,len(A),0)
print(A)