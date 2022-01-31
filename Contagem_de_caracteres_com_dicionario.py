def contar_caracteres(s):
    caracter_anterior = ""
    contador = 0
    contagem = {}


    for caracter in s.upper():
        contagem[caracter] = contagem.get(caracter, 0) +1
    print(s)
    return(contagem)




if __name__ == '__main__':
    print(contar_caracteres("alabama"))
    print()
    print(contar_caracteres("berlin"))
    print()
    print(contar_caracteres("banana"))
    print()
    print(contar_caracteres("eduardo"))
    print()
    print(contar_caracteres("vancuver"))
    print()



