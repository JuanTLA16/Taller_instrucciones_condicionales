A = int(input("Ingrese el valor de A: "))
B = int (input("Ingrese el valor de B: "))
C = int(input("Ingrese el valor de C: "))

#Procesing
Z=B**2-4*A*C

if (A==0):
    print("No es una ecuación cuadratica")
if (Z==0):
        x1=-B/(2*A)
        MSJ=(x1,x1)
elif (Z>0):
    x1=((-B+(sqrt)(Z))/(2*A))
    x2=((-B-(sqrt)(Z))/(2*A))
    MSJ=(x1,x2)
else:
    x1=-B+(C(math.sqrt(Z)))/(2*A)
    x2=-B+(C(math.sqrt(Z)))/(2*A)      
    MSJ=(x1,x2)
           
print("Las raices son: " + str(MSJ))


print("_------------------------------")
print("----------RESULTADOS-----------")
print("-------------------------------")
