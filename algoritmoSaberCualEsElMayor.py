print("Bienvenido al programa para encontrar el numero mayor");

num1 = input("Ingrese el numero 1: ");
num2 = input("Ingrese el numero 2: ");
num3 = input("Ingrese el numero 3: ");

if int(num1) > int(num2) and int(num1 > num3):
    print("El numero mayor es el: "  + num1);

elif int(num2) > int(num1) and int(num2) > int(num3):
    print("El numero mayor es el: " + num2);
else:
    print("El numero mayor es el: " + num3);
     



