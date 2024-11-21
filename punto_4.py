def mayor_suma_consecutivos(lista):
    if len(lista) < 2:
        return None 

    max_suma = lista[0] + lista[1]  
    for i in range(1, len(lista) - 1):
        suma_actual = lista[i] + lista[i + 1]
        if suma_actual > max_suma:
            max_suma = suma_actual

    return max_suma

lista = [5, 1, 3, 7, 9, 2, 4]
print(mayor_suma_consecutivos(lista))  
