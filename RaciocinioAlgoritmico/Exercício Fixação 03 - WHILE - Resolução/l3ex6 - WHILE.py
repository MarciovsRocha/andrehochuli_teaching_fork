#Fa�a um programa que receba dois n�meros inteiros e
#gere os n�meros inteiros que est�o no intervalo compreendido por eles

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

#Inverto os numeros se o segundo � maior que o primeiro
if (n2 < n1):
    temp = n1
    n1 = n2
    n2 = temp
    

while(n1 <= n2):
    print(n1)
    n1 += 1
    

