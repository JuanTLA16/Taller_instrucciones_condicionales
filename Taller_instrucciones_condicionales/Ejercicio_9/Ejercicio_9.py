
print("--------------------------")
print("-------EJERCICIO 9--------")
print("--------------------------")


A = int(input("Ingrese el valor del lado A: "))
B = int(input("Ingrese el valor del lado B: "))
C = int(input("Ingrese el valor del lado C: "))


if (C**2)==(A**2)+(B**2):
   print("El triangulo es recto")
else:
   if (C**2)>(A**2)+(B**2):
      print("El triangulo es obtuso")
   else:
       if (C**2)<(A**2)+(B**2):
        print("El triangulo es agudo")

print("----------------------------")
print("---------RESULTADOS---------")
print("----------------------------")

     
     