print("Programa para generar la serie de Fibonacci");

a = 0;
b = 1;
c = 0;

while True:
    n = int(input("Ingrese un numero mayor a 1 para generar la serie: "));
    if n>1:
        break;
print("1");

for i in range(0,n):
    c = a+b
    print(str(c))
    a = b
    b = c