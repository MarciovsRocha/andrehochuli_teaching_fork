# -*- coding: utf-8 -*-
#4.	Fa�a um programa que leia 5 n�meros e informe a soma e a m�dia dos n�meros.
i = 0
soma = 0


while(i<5):
    
    n = int(input("Digite um numero: "))
    
    soma += n
    
    i+=1

media = soma / 5
print("A soma eh: %d e a m�dia � %.2f" % (soma,media))
