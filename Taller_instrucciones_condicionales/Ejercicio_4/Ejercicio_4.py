print("------------------------------------")
print("------------EJERCICIO 4-------------")
print("------------------------------------")

PESO = int(input("DIGITE SU PESO (kg): "))
ALTURA = int(input("DIGITE SU ALTURA (m): "))

IMC = PESO / ALTURA ** 2
print("Su IMC es de:"+ str(IMC))

if ( IMC < 16):
    print(" Criterio de ingreso en el hospital ")
if ( 16 < IMC < 17 ):
    print(" INFRAPESO ")
if ( 17 < IMC < 18):
    print(" BAJO PESO")
if ( 18 < IMC < 25):
    print("SALUDABLE")
if ( 25 < IMC < 30):
    print("Obesidad grado I")
if ( 30 < IMC < 35):
    print("Obesidad grado II")
if ( 35 < IMC < 40):
    print("Obesidad grado III")
if ( IMC > 40):
    print("Obesidad grado IV")   


print("------------------------------------")
print("-------------RESULTADOS-------------")
print("------------------------------------")

