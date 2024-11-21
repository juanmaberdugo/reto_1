def operaciones_basicas(numero_1, numero_2, eleccion_operacion):
    operacion_matematica = eleccion_operacion.lower().replace(" ", "")
    match operacion_matematica:
        case "+":
            return numero_1 + numero_2
        case "-":
            return numero_1 - numero_2
        case "*":
            return numero_1 * numero_2
        case "/":
            return numero_1/numero_2
        case _:
            return "Operacion no existente por favor escriba bien el nombre"

primer_numero = int(input("digite el primer numero a realizar operacion"))
segundo_numero = int(input("digite el segundo numero a realizar operacion"))
operacion = str(input("escriba la operacion a realizar"))

print(operaciones_basicas(primer_numero, segundo_numero, operacion))