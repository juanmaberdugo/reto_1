# Reto 1

### Primer punto
Para crear una funcion capaz de realizar las operaciones basicas matematicas, use el match case para que dependiendo de lo que se ingrese por consola, la funcion realize las operaciones.

### Segundo punto
Primero para que los caracteres de las palabras estuvieran en minuscula use la funcion lower(), despues se usa la funcion len() para saber la longitud de la palabra y finalmente se usa el ciclo que teniendo en cuenta la longitud de la palabra compara las dos mitades de la palabra y determina si son iguales

### Tercer punto
Para este punto, uso un ciclo para iterar desde 2 hasta el mismo numero, asi mismo le aplico el operador del modulo para verificar que en el momento en el que el numero dividido por el indice de como residuo cero indique que el numero es divisible por otro que no sea el mismo o uno.

### Cuarto punto
Primero se realiza una condicional con el fin de verificar si se pueden sumar los elementos de la lista de manera consecutiva, si la lista cuenta con menos de dos numeros la funcion retorna None, despues se crea la variable mayor_suma para los dos primeros elementos de la lista, despues el ciclo recorre la lista desde el primer elemento de esta misma hasta el penultimo de esta con el fin de hacer la suma de los numeros de forma consecutiva, finalmente se usa un condicional con el fin de comparar cada uno de las sumas que se realizaron en el ciclo con lo que esta ya almacenado en la variable y dependiendo de si es mayor que esta cambia el valor de esta misma.

### Quinto punto
En esta funcion primero declaro un diccionario vacio donde voy a guardar las diferentes palabras para identificar si tienen los mismos caracteres pero en otro orden, despues de esto tomo cada una de las palabras y organizo cada una de sus letras para crear una tupla que va a ser la clave dentro de mi diccionario, cada que una palabra tenga los mismos caracteres que una anterior se va a apilar en una lista que va a ser el valor de la clave en el diccionario, finalmente retornara el diccionario que cumpla con la condicion
