numero = input("Introduzca un numero: ")

try:
    numero = int(numero)
except:
    print('Solo pueden entrar numeros')

if(isinstance(numero, int)):
    for i in range (11):
        print(str(numero) + " x " + str(i) + " = " + str((numero * i)) )
else:
    print('Solo pueden entrar numeros')