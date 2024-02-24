print("Generador de tablas de multiplicar");

while True:
    n = int(input("Ingrese el numero que quieras generar una tabla de multiplicar: "))
    if n>=1:
        break;

for i in range(1,11):
    r = i * n
    print(str(n) + "x" + str(i) + " = " + str(r))