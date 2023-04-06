def inverter_string(string):
    lista_caracteres = list(string)
    
    comeco = 0
    final = len(lista_caracteres) - 1
    
    while comeco < final:
        lista_caracteres[comeco], lista_caracteres[final] = lista_caracteres[final], lista_caracteres[comeco]
        
        comeco += 1
        final -= 1
    
    string_invertida = "".join(lista_caracteres)
    
    return string_invertida


frase_invertida = input("Digite uma frase para ser invertida! ")

saida = inverter_string(frase_invertida)

print("String inserida: ", frase_invertida)
print("String invertida: ", saida)
