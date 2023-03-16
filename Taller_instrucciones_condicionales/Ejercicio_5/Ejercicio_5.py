
print("------------------------------")
print("-------EJERCICIO 5------------")
print("------------------------------")

Agua_gastada = int(input("Digite la cantidad de agua gastada en M^3: "))

Cuota_fija = 10000

if (Agua_gastada < 50):
    print("El consumo de agua es de: " + str(Cuota_fija))
else:
    if (50 < Agua_gastada < 200):
        print("El consumo del agua es de " + str(Cuota_fija+(Agua_gastada-50)*2000))
    else:
        if (Agua_gastada > 200):
            print("El consumo del agua es de " + str(Cuota_fija+(Agua_gastada-50)*3000))


print("------------------------------")
print("--------RESULTADOS------------")
print("------------------------------")
