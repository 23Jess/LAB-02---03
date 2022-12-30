#Un robot puede dar pasos de 1, 2 o 3 metros. Escriba un programa para enumerar todas las
#maneras en que el robot camina n metros.

def robot(n):
    if n==1 or n==2 or n==3:
        return n
    return robot(n-1)+robot(n-2)+robot(n-3)
print(robot(10))