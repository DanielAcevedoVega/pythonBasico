print("Calcular promedio en una lista de numeros");

r = 0;
n = 0;
c = 0;

while True:
    c = int(input("Ingrese la cantidad de numeros que vas a ingresar: "));
    if c>1:
        break;
for i in range(1,c+1,1):
    n = int(input("Numero "+ str(i) +":"));
    r = float(r) + n;
r = r / c;

print("El promedio de los numero ingresados es: " + str(r));
    
