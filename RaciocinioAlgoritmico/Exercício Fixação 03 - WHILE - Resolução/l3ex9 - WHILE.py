# -*- coding: utf-8 -*-
#Imprima a s�rie de Fibonacci at� o N-en�simo (N) elemento, sendo N informado pelo usu�rio
n2  = 0
n1  = 1

#Altero o final de linha para imprimir um espa�o ao inv�s de nova linha
print(n2, end=' ') 
print(n1, end=' ') 

n_elem = int(input("Qual elemento da s�rie deseja computar?: "))

i=3
while (i <= n_elem):
    #Calculo o elemento atual
    n = n1 + n2
    print(n, end = ' ')
    
    #Atualizo os n1 e n2
    n2 = n1
    n1 = n
    i+=1
