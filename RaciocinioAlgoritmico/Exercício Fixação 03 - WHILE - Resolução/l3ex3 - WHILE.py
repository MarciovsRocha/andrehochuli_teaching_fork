#3.	Fa�a um programa que leia 5 n�meros e informe o maior n�mero

i = 0
maior = -999999


while(i<5):
    
    n = int(input("Digite um numero: "))
    
    if n > maior:
        maior = n
    
    i+=1

print("O maior numero digitado foi: ", maior)