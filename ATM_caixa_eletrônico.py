# conforme Execício proposto


# saque=int(input("Qual o valor a ser sacado? O valor mínimo de saque é de R$10 e máximo de R$600."))
# confirmar valor do saque.
# while saque<=10 or saque>=600:
#  saque=int(input("Valor Inválido, o valor mínimo de saque é de R$10 e máximo de R$600, qual o valor a ser sacado?"))

teste = [155, 154, 485, 1, 10, 15, 26, 84, 231, 500, 600, 107, 1000]  # bateria de teste
# teste = [155]
for saque in teste:
    if saque >= 10 and saque <= 600:
        # não esquecer de zerar tudo!!!
        cond_str = 0
        str_cedula_100 = str_cedula_50 = str_cedula_20 = str_cedula_10 = str_cedula_5 = str_cedula_2 = str_cedula = ""
        numero_100 = numero_50 = numero_20 = numero_10 = numero_5 = numero_2 = 0
        resto_100 = resto_50 = resto_20 = resto_10 = resto_5 = resto_2 = 0

        # Cacular as notas partindo da maior nota.
        numero_100, resto_100 = divmod(saque, 100)
        numero_50, resto_50 = divmod(resto_100, 50)
        numero_20, resto_20 = divmod(resto_50, 20)
        numero_10, resto_10 = divmod(resto_20, 10)
        numero_5, resto_5 = divmod(resto_10, 5)
        numero_2, resto_2 = divmod(resto_5, 2)

        # correção para saque de valores impares!
        if resto_2 == 1:
            if numero_5 >= 1:
                numero_5 = numero_5 - 1
                numero_2 += 3
            elif numero_10 >= 1:
                numero_10 = numero_10 - 1
                numero_5 += 1
                numero_2 += 3
            elif numero_20 >= 1:
                numero_20 = numero_20 - 1
                numero_10 += 1
                numero_5 += 1
                numero_2 += 3
            elif numero_50 >= 1:
                numero_50 = numero_50 - 1
                numero_20 += 2
                numero_5 += 1
                numero_2 += 3
            elif numero_100 >= 1:
                numero_100 = numero_100 - 1
                numero_50 += 1
                numero_20 += 2
                numero_5 += 1
                numero_2 += 3

        conferir = numero_100 * 100 + numero_50 * 50 + numero_20 * 20 + numero_10 * 10 + numero_5 * 5 + numero_2 * 2

        ##Nota de 100

        if numero_100 >= 1:
            cond_str += 1
            if numero_100 > 1:
                str_cedula_100 = f"{numero_100} cédulas de R$100"
            else:
                str_cedula_100 = "1 cédula de R$100"

        ##Nota de 50
        if numero_50 >= 1:
            cond_str += 1
            if numero_50 > 1:
                str_cedula_50 = f"{numero_50} cédulas de R$50"
            else:
                str_cedula_50 = "1 cédula de R$50"

        ##Nota de 20
        if numero_20 >= 1:
            cond_str += 1
            if numero_20 > 1:
                str_cedula_20 = f"{numero_20} cédulas de R$20"
            else:
                str_cedula_20 = "1 cédula de R$20"

        ## Nota de 10
        if numero_10 >= 1:
            cond_str += 1
            if numero_10 > 1:
                str_cedula_10 = f"{numero_10} cédulas de R$10"
            else:
                str_cedula_10 = "1 cédula de R$10"

        ##Nota de 5
        if numero_5 >= 1:
            cond_str += 1
            if numero_5 > 1:
                str_cedula_5 = f"{numero_5} cédulas de R$5"
            else:
                str_cedula_5 = "1 cédula de R$5"

        ## Nota de 2
        if numero_2 >= 1:
            cond_str += 1
            if numero_2 > 1:
                str_cedula_2 = f"{numero_2} cédulas de R$2"
            else:
                str_cedula_2 = "1 cédula de R$22"

        # Preparar texto pra printar.

        ## 1 tipo de cedula.
        if cond_str == 1:
            str_cedula = str_cedula_100 + str_cedula_50 + str_cedula_20 + str_cedula_10 + str_cedula_5 + str_cedula_2

        ## 2 tipos de cedulas.
        elif cond_str == 2:
            if numero_100 >= 1:
                str_cedula = str_cedula_50 + str_cedula_20 + str_cedula_10 + str_cedula_5 + str_cedula_1 + str_cedula_2
                str_cedula = f"{str_cedula_100} e {str_cedula}"
            elif numero_50 >= 1:
                str_cedula = str_cedula_20 + str_cedula_10 + str_cedula_5 + str_cedula_2
                str_cedula = f"{str_cedula_50} e {str_cedula}"
            elif numero_20 >= 1:
                str_cedula = str_cedula_10 + str_cedula_5 + str_cedula_2
                str_cedula = f"{str_cedula_20} e {str_cedula}"
            elif numero_10 >= 1:
                str_cedula = str_cedula_5 + str_cedula_2
                str_cedula = f"{str_cedula_10} e {str_cedula}"
            else:
                str_cedula = f"{str_cedula_5} e {str_cedula_2}"

        ## 3 tipos de cedulas.
        elif cond_str == 3:
            if numero_100 >= 1:  # Primeira nota é de 100

                if numero_50 >= 1:  # Segunda nota é 50
                    str_cedula = str_cedula_20 + str_cedula_10 + str_cedula_5 + str_cedula_2  # terceira nota é uma entre as três
                    str_cedula = f"{str_cedula_100}, {str_cedula_50} e {str_cedula}"

                elif numero_10 >= 1:  # Segunda nota é 20
                    str_cedula = str_cedula_10 + str_cedula_5 + str_cedula_2
                    str_cedula = f"{str_cedula_100}, {str_cedula_20} e {str_cedula}"

                elif numero_10 >= 1:  # Segunda nota é 10
                    str_cedula = str_cedula_5 + str_cedula_2
                    str_cedula = f"{str_cedula_100}, {str_cedula_10} e {str_cedula}"

                else:  # Segunda nota é 5, só se tem uma possibilidade.
                    str_cedula = f"{str_cedula_100}, {str_cedula_5} e {str_cedula_2}"

            elif numero_50 >= 1:  # Primeira nota 50

                if numero_20 >= 1:  # segunda nota 20
                    str_cedula = str_cedula_10 + str_cedula_5 + str_cedula_1
                    str_cedula = f"{str_cedula_50}, {str_cedula_20} e {str_cedula}"

                elif numero_10 >= 1:  # segunda nota 10
                    str_cedula = str_cedula_5 + str_cedula_1
                    str_cedula = f"{str_cedula_50}, {str_cedula_10} e {str_cedula}"

                else:  # segunda nota 5, só tem uma possibilidade
                    str_cedula = f"{str_cedula_50}, {str_cedula_5} e {str_cedula_1}"

            elif numero_20 >= 1:  # Primeira nota 20

                if numero_10 >= 1:  # segunda nota 10
                    str_cedula = str_cedula_5 + str_cedula_1
                    str_cedula = f"{str_cedula_20}, {str_cedula_10} e {str_cedula}"

                else:  # segunda nota 5, só tem uma possibilidade
                    str_cedula = f"{str_cedula_50}, {str_cedula_5} e {str_cedula_2}"

            else:
                str_cedula = f"{str_cedula_10}, {str_cedula_5} e {str_cedula_2}"

        ## 4 tipos de cedulas.
        elif cond_str == 4:

            if numero_100 >= 1:  # Primeira nota é de 100

                if numero_50 >= 1:  # Segunda nota 50

                    if numero_20 >= 1:  # Terceira nota 20

                        str_cedula = str_cedula_10 + str_cedula_5 + str_cedula_2  # quarta nota só pode ser uma
                        str_cedula = f"{str_cedula_100}, {str_cedula_50}, {str_cedula_20} e {str_cedula}"

                    elif numero_10 >= 1:  # terceira nota 10
                        str_cedula = str_cedula_5 + str_cedula_2  # quarta nota só pode ser uma das duas
                        str_cedula = f"{str_cedula_100}, {str_cedula_50}, {str_cedula_10} e {str_cedula}"

                    else:  # terceira nota 5
                        str_cedula = f"{str_cedula_100}, {str_cedula_50}, {str_cedula_5} e {str_cedula_2}"  # unica possibilidade

                elif numero_20 >= 1:  # segunda nota 20

                    if numero_10 >= 1:  # terceira nota 10
                        str_cedula = str_cedula_5 + str_cedula_2
                        str_cedula = f"{str_cedula_100}, {str_cedula_20}, {str_cedula_10} e {str_cedula}"

                    else:  # terceira nota 5
                        str_cedula = f"{str_cedula_100}, {str_cedula_20}, {str_cedula_5} e {str_cedula_2}"

                else:  # segunda nota 10, unica possibilidade
                    str_cedula = f"{str_cedula_100}, {str_cedula_10}, {str_cedula_5} e {str_cedula_2}"

            elif numero_50 >= 1:  # primeira nota 50

                if numero_20 >= 1:  # segunda nota 20

                    if numero_10 >= 1:  # terceira nota 10
                        str_cedula = str_cedula_5 + str_cedula_2  # quarta nota só pode ser uma das duas
                        str_cedula = f"{str_cedula_50}, {str_cedula_20}, {str_cedula_10} e {str_cedula}"

                    else:  # terceira nota 5
                        str_cedula = f"{str_cedula_50}, {str_cedula_20}, {str_cedula_5} e {str_cedula_2}"

                else:  # Segunda nota 10
                    str_cedula = f"{str_cedula_50}, {str_cedula_10}, {str_cedula_5} e {str_cedula_2}"

            else:  # Tirando todas as possibilidades onde a 1ª nota é 100 ou 50 só restará possibilidade a seguir 20, 10, 5 e 2.
                str_cedula = f"{str_cedula_20}, {str_cedula_10}, {str_cedula_5} e {str_cedula_2}"


        ## 5 tipos de cedulas.
        elif cond_str == 5:

            if numero_100 >= 1:  # Primeira nota é de 100

                if numero_50 >= 1:  # Segunda nota 50

                    if numero_20 >= 1:  # Terceira nota 20

                        if numero_10 >= 1:  # Quarta nota 10
                            str_cedula = str_cedula_5 + str_cedula_2  # quarta nota só pode ser uma das duas
                            str_cedula = f"{str_cedula_100}, {str_cedula_50}, {str_cedula_20}, {str_cedula_10} e {str_cedula}"

                        else:  # Quarta 5
                            str_cedula = f"{str_cedula_100}, {str_cedula_50}, {str_cedula_20}, {str_cedula_5} e {str_cedula_2}"

                    else:  # terceira nota 10
                        str_cedula = f"{str_cedula_100}, {str_cedula_50}, {str_cedula_10}, {str_cedula_5} e {str_cedula_2}"  # unica possibilidade

                else:  # segunda nota 20, unica possibilidade
                    str_cedula = f"{str_cedula_100}, {str_cedula_20}, {str_cedula_10}, {str_cedula_5} e {str_cedula_2}"

            else:  # primeira nota 50, unica possibilidade
                str_cedula = f"{str_cedula_50}, {str_cedula_20}, {str_cedula_10}, {str_cedula_5} e {str_cedula_2}"


        ##6 tipos de cedulas
        elif cond_str == 6:
            str_cedula = f"{str_cedula_100}, {str_cedula_50}, {str_cedula_20}, {str_cedula_10}, {str_cedula_5} e {str_cedula_1}"

        print(f"Processando saque {cond_str} > {saque} = {conferir}: {str_cedula}.")

    else:

        print(f"R${saque} Valor Inválido, o valor mínimo de saque é de R$10 e máximo de R$600")