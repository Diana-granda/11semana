

#  matriz bidimensional
def buscar_valor(matriz, valor):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] == valor:
                return fila, columna
    return None

# Matriz (3x3)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor que quieres buscar
valor_a_buscar = 1

posicion = buscar_valor(matriz, valor_a_buscar)


if posicion is not None:
    fila, columna = posicion
    print(f"El valor {valor_a_buscar} se encuentra en la posición ({fila}, {columna}) de la matriz.")
else:
    print(f"El valor {valor_a_buscar} no existe en la matriz.")
