#Implemente un programa recursivo que calcule la potencia de un número elevado a otro.
#Sabemos que 2n=2n/2.2n/2 donde n es un nro par; y 2n=2(n-1)/2.2(n-1)/2.2 si
#n es impar

#from os import system

def main(args):
    sc = Scanner(System.in_)
    num = None
    condition = True
    while condition:
        System.out.print("Introduce un número entero >=0 ")
        num = sc.nextint()
        condition = num<0
    System.out.println("2 ^ " + num + " = " + potencia(num))
def potencia(n):
    if n == 0: #caso base
        return 1
    else:
        return 2 * potencia(n-1)
print(potencia(4))