#Escriba un programa recursivo y otro no recursivo para calcular n!.
#Compare los tiempos requeridos por los programas.

print("Recursivo")

import time
def factorial_recursivo(n):
    if n == 1:
        return 1
    return n*factorial_recursivo(n-1)
tiempo1=time.perf_counter()
A=factorial_recursivo(8)
tiempo2=time.perf_counter()
print(A,"=> Se realizó en: ",tiempo2-tiempo1)

print("No recursivo")

def factorial(n):
    b=1
    for i in range(n,1,-1):
        b*=i
    return b 
tiempo1=time.perf_counter()
B=factorial(8)
tiempo2=time.perf_counter()
print(B,"=>  Se realizó en: ",tiempo2-tiempo1)
