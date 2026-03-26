while True:
    try:
        n = int(input("¿Cuántos números desea ingresar? "))
        if n > 0:
            break
        else:
            print("Ingrese un número mayor a 0")
    except ValueError:
        print("Ingrese un número válido")

numeros = []

for i in range(n):
    while True:
        try:
            num = float(input(f"Ingrese número {i + 1}: "))
            numeros.append(num)
            break
        except ValueError:
            print("Ingrese un número válido")

print(f"\nLista original: {numeros}")

# Bubble Sort
for i in range(len(numeros)):
    for j in range(0, len(numeros) - i - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print(f"Lista ordenada: {numeros}")
