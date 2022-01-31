def contar_caracteres(s):
    caracter_anterior = ""
    caracter_ordenado = sorted(s.upper())
    contador = 0

    for caracter in caracter_ordenado:
        if caracter_anterior == "":
            contador = 1
            caracter_anterior = caracter

        elif caracter == caracter_anterior:
            contador += 1
            caracter_anterior = caracter

        else:
            print(f"Letra: {caracter_anterior} {contador} unidades.")
            caracter_anterior = caracter
            contador = 1
    print(s)




if __name__ == '__main__':
    contar_caracteres("alabama")
    print()
    contar_caracteres("berlin")
    print()
    contar_caracteres("banana")
    print()
    contar_caracteres("eduardo")
    print()
    contar_caracteres("vancuver")
    print()



