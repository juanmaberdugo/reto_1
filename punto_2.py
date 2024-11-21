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