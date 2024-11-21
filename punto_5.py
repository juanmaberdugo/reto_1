def mismos_caracteres(lista):
    grupos = {}
    
    for palabra in lista:
        clave = ''.join(sorted(palabra))
        
        if clave in grupos:
            grupos[clave].append(palabra)
        else:
            grupos[clave] = [palabra]
    
    resultado = []
    for palabras in grupos.values():
        if len(palabras) > 1:
            resultado.extend(palabras)
    
    return resultado

entrada = ["amor", "roma", "perro"]
salida = mismos_caracteres(entrada)
print(salida) 
