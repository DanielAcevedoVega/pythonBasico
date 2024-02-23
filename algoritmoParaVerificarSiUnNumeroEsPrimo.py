print("Programa para verificar si un numero es primo.")
numero = int(input("Ingrese el numero: "));
contador = 0;

for i in range(2, numero):
    if (numero%i) == 0:
        contador+=1;

if contador > 0:
    print("El numero no es primo")
else:
    print("El numero es primo")


         