numeros= []
print("Programa para ordenar los numeros: ")
for i in range(10):
    while True:
        try:
            numero= float(input(f"Ingresa el numero {i + 1}: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Error, Por Favor ingresa solo numeros.")  

numeros.sort(reverse=True)
numero_alto = numeros[0]
numero_menor= numeros[-1]
#hola





print(f"Los numeros ordenados son: {numeros}")
