# Dada una lista de numeros, encontrar la suma de mayor valor
def encontrar_numero(lista):
    max_suma = lista[0]
    suma_actual = lista[0]

    for num in lista[1:]:
        suma_actual = max(num, suma_actual + num)
        max_suma = max(max_suma, suma_actual)

    return max_suma

# Ejemplo de uso:
mi_lista = [1, 2, 3, 4, -5, -4, 8 ]
resultado = encontrar_numero(mi_lista)

print(f"La suma de mayor valor es: {resultado}")