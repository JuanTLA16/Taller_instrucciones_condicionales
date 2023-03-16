
print("--------------------------------------")
print("-------------EJERCICIO 3--------------")
print("--------------------------------------")



n = int(input("Digite el precio costo: "))
p = n * 0.15
x = n + 500
y = n * 0.25


if (n<3000):
    print ("La ganancia sera de: " + str(p))
else:
    if (n>=3000 and n<6000):
        print ("El precio costo del objeto es: " + str(x))
    else:
        if (n>6000):
            print ("La ganancia sera de: " + str(y))
        

print("--------------------------------------")
print("--------------RESULTADOS--------------")
print("--------------------------------------")



