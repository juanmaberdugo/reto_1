def primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            print("No es primo", i, "es divisor")
            return False
    print("Es primo")
    return True

numero = int(input("Ingrese el numero "))
print(primo(numero))