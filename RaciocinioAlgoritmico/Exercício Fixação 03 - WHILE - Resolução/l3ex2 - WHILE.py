#2.	Solicite uma senha ao usu�rio. Conte quantas vezes ele errou.


senha = '@652AbYU'
count = 0
passwd = ''

while (senha != passwd):
    
    passwd = input("Digite uma senha: ")
    count += 1
    

print("Login Efetuado. Voce tentou %d vezes" % (count))
