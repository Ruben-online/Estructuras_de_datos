# Crea una funcion que reciba como parametro una lista de numeros
# Que devuelva la suma, el minimo, maximo, ordenados ascendente, cuadrados de la lista

numbers_list = [8, 1, 16, 5, 3]
def numbers_function(numbers):
    return {
        'Suma': sum(numbers),
        "Mínimo": min(numbers),
        "Máximo": max(numbers),
        "Ordenados": sorted(numbers),
        "Cuadrados": [num ** 2 for num in numbers]
    }

result = numbers_function(numbers_list)
print(result)