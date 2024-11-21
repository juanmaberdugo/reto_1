# Reto 1

### Primer punto
Para crear una funcion capaz de realizar las operaciones basicas matematicas, use el match case para que dependiendo de lo que se ingrese por consola, la funcion realize las operaciones.
  ````python
def operaciones_basicas(numero_1, numero_2, eleccion_operacion):
    operacion_matematica = eleccion_operacion.lower().replace(" ", "")
    match operacion_matematica:
        case "suma":
            return numero_1 + numero_2
        case "resta":
            return numero_1 - numero_2
        case "multiplicacion":
            return numero_1 * numero_2
        case "division":
            return numero_1/numero_2
        case _:
            return "Operacion no existente por favor escriba bien el nombre"

primer_numero = int(input("digite el primer numero a realizar operacion"))
segundo_numero = int(input("digite el segundo numero a realizar operacion"))
operacion = str(input("escriba la operacion a realizar"))

print(operaciones_basicas(primer_numero, segundo_numero, operacion))
````

### Segundo punto
Primero para que los caracteres de las palabras estuvieran en minuscula use la funcion lower(), despues se usa la funcion len() para saber la longitud de la palabra y finalmente se usa el ciclo que teniendo en cuenta la longitud de la palabra compara las dos mitades de la palabra y determina si son iguales
  ````python
def palindromo(palabra):
    palabra = palabra.lower()
    longitud = len(palabra)

    for i in range(longitud // 2):
        if palabra[i] != palabra[longitud - i - 1]:
            print("No es palindromo")
            return False
    print("Es palindromo")
    return True

palabra = str(input("Escriba la palabra "))
print(palindromo(palabra))
````

### Tercer punto
Para este punto, uso un ciclo para iterar desde 2 hasta el mismo numero, asi mismo le aplico el operador del modulo para verificar que en el momento en el que el numero dividido por el indice de como residuo cero indique que el numero es divisible por otro que no sea el mismo o uno.
  ````python
def primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            print("No es primo", i, "es divisor")
            return False
    print("Es primo")
    return True

numero = int(input("Ingrese el numero "))
print(primo(numero))
````

### Cuarto punto
Primero se realiza una condicional con el fin de verificar si se pueden sumar los elementos de la lista de manera consecutiva, si la lista cuenta con menos de dos numeros la funcion retorna None, despues se crea la variable mayor_suma para los dos primeros elementos de la lista, despues el ciclo recorre la lista desde el primer elemento de esta misma hasta el penultimo de esta con el fin de hacer la suma de los numeros de forma consecutiva, finalmente se usa un condicional con el fin de comparar cada uno de las sumas que se realizaron en el ciclo con lo que esta ya almacenado en la variable y dependiendo de si es mayor que esta cambia el valor de esta misma.
  ````python
def suma_consecutivos(lista):
    if len(lista) < 2:
        return None 

    mayor_suma = lista[0] + lista[1]  
    for i in range(1, len(lista) - 1):
        suma_actual = lista[i] + lista[i + 1]
        if suma_actual > mayor_suma:
            mayor_suma = suma_actual

    return mayor_suma

lista = [5, 1, 3, 7, 9, 17, 10]
print(suma_consecutivos(lista))  
````

### Quinto punto
En esta funcion primero declaro un diccionario vacio donde voy a guardar las diferentes palabras para identificar si tienen los mismos caracteres pero en otro orden, despues de esto tomo cada una de las palabras y organizo cada una de sus letras para crear una tupla que va a ser la clave dentro de mi diccionario, cada que una palabra tenga los mismos caracteres que una anterior se va a apilar en una lista que va a ser el valor de la clave en el diccionario, finalmente retornara el diccionario que cumpla con la condicion
  ````python
def mismos_caracteres(lista):
    grupos = {}
    
    for palabra in lista:
        clave = tuple(sorted(palabra))
        
        if clave in grupos:
            grupos[clave].append(palabra)
        else:
            grupos[clave] = [palabra]
    
    resultado = []
    for palabras in grupos.values():
        if len(palabras) > 1:
            resultado.extend(palabras)
    
    return resultado

lista = ["amor", "roma", "perro"]
print(mismos_caracteres(lista))
````
