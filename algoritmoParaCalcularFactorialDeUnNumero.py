print("Este programa calcula cualquier numero factorial");
n = int(input("Ingrese el numero: "));
factorial = 1;

if n >= 1:
    for i in range (1, n+1):
        factorial=factorial *i

print("El numero factorial es: ", factorial);

