# Reto 1

### Primer punto
Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).

Para crear una función capaz de realizar las operaciones básicas matemáticas, utilicé match case para que, dependiendo de lo que se ingrese por consola, la función realice las operaciones.
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
Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

Primero, para que los caracteres de las palabras estuvieran en minúscula, usé la función lower(). Después, utilicé la función len() para saber la longitud de la palabra. Finalmente, empleé un ciclo que, teniendo en cuenta la longitud de la palabra, compara las dos mitades y determina si son iguales.
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
Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

Para este punto, uso un ciclo para iterar desde 2 hasta el mismo número. Asimismo, aplico el operador módulo para verificar que, en el momento en que el número dividido por el índice dé como residuo cero, se indique que el número es divisible por otro que no sea él mismo o uno.
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
Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.

Primero, se realiza una condicional para verificar si se pueden sumar los elementos de la lista de manera consecutiva. Si la lista cuenta con menos de dos números, la función retorna None. Después, se crea la variable mayor_suma para almacenar la suma de los dos primeros elementos de la lista. A continuación, el ciclo recorre la lista desde el primer elemento hasta el penúltimo, con el fin de sumar los números de forma consecutiva. Finalmente, se utiliza un condicional para comparar cada una de las sumas realizadas en el ciclo con el valor almacenado en la variable. Si la nueva suma es mayor, se actualiza el valor de mayor_suma.
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
Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]

En esta función, primero declaro un diccionario vacío donde voy a guardar las diferentes palabras para identificar si tienen los mismos caracteres pero en distinto orden. Después, tomo cada una de las palabras y organizo sus letras para crear una tupla que será la clave dentro del diccionario. Cada vez que una palabra tenga los mismos caracteres que otra anterior, se agregará a una lista que será el valor de esa clave en el diccionario. Finalmente, se retorna el diccionario que cumple con esta condición.
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
