#Un robot puede dar pasos de 1 o 2 metros. Escriba un programa para numerar todas las
#maneras en que el robot camina n metros.

def robot(n):
    if n ==1 or n==2:
        return n
    else:
        return robot(n-1)+robot(n-2)
print(robot(5))
