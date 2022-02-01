from random import randint

i = 0
soma = media = maior_media = maior_7 = 0
lista_nota = lista_media = []
print("Digite o valor da nota, ou digite -1 para finalizar. ")
while True:
    ##nota=float(input("Nota: "))
    nota = randint(-1, 10)
    if nota == -1:
        break
    else:
        lista_nota.append(nota)
print(lista_nota)

# quantidade de valores
lista_len = len(lista_nota)
print(f"Foram {lista_len} notas.")

# Exibir na ordem
lista_nota.sort()
print("As notas me ordemcrescente são:")
print(" ".join([str(nota) for nota in lista_nota]))

# Reverse
lista_nota.reverse()
print("As notas me decrescente são:")
for x in lista_nota:
    print(x)

# Soma
for s in lista_nota:
    soma = soma + s
print(f'A soma dos valores é {soma}.')

# média
media = soma / lista_len
print(f'A media das notas é: {media}')

# quantide de valores acima da média
for s in lista_nota:
    if s >= media:
        maior_media = maior_media + 1
print(f'{maior_media} valores são maior que a media')

# maior que 7
for s in lista_nota:
    if s >= 7:
        maior_7 = maior_7 + 1
print(f'{maior_7} valores são maior que a media')

# Imprimir uma msg
print("That's all fouks")
