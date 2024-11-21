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

