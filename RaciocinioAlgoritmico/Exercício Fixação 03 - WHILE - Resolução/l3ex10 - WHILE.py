#10.	Altere o programa anterior para imprimir at� o N-en�simo elemento out at� que elemento seja menor seja 500.
n2  = 0
n1  = 1

#Altero o final de linha para imprimir um espa�o ao inv�s de nova linha
print(n2, end=' ') 
print(n1, end=' ') 

n_elem = int(input("Qual elemento da s�rie deseja computar?: "))
n = 0
i=3
while (i <= n_elem and n < 500):
    #Calculo o elemento atual    
    print(n, end = ' ')
    n = n1 + n2
    #Atualizo os n1 e n2
    n2 = n1
    n1 = n
    i+=1
