#Fa�a um programa que calcule o fatorial de um n�mero inteiro fornecido pelo usu�rio. Ex.: 5!=5.4.3.2.1=120. A sa�da deve ser conforme o exemplo abaixo:

n = int(input("Qual o n�mero a ser fatorado ?"))



fat = n

print("%d! = %d" % (fat,n) , end=' ')

while (n > 1):
    n = n -1
    print(". %d" % (n) , end = ' ')
    fat = fat * n


print("= %d" % (fat)) 
