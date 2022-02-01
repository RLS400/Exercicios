##Jogo da focaa

from random import randint

#Variaveis
acertos = erros = 0
erros_maximos = 5
#Banco de palavras
palavras=["PATO","GATO","SAPO","RATO","MACACO","LEOPARDO","GALINHA","GIRAFA","VACA","CAMELO","GORILA","CACHORRO"]

#Sortear uma palvra
palavra=palavras[randint(0,len(palavras)-1)]
adivinhar=["*"]*len(palavra) #Painel de acertos começa em branco "_"


#Introdução do jogo
print(f"A palavra secreta é uma animal de {len(palavra)} letras. \n Você pode encerrar o jogo digitando sair.\n ")

#Texto dinâmico para input
texto="\n Digite uma letra uma letra."

while True:

  if acertos == len(palavra): #Ganhar o jogo.
    print(f"Parabens! Você descobriu a palavra sercreta: {palavra}.")
    print("\nVocê ganhou um BIS, pegue logo antes que acabe.")
    break

  elif erros >= erros_maximos: #Perder o jogo.
    print("Você fracassou miseravelmente, você é a vergonha da profision!")
    break

  estado = 0 #controla se errou ou acertou alguma letra na tentativa.

  print(" ".join(adivinhar)) #painel do jogo.

  chute=input(f"{texto} \n").upper() #Entrada do usario

  if chute == "SAIR": #Parar o jogo
    print("Muito obrigado por jogar.")
    break

  elif len(chute)==1:
    for x in range(0,len(palavra)):
      if chute == palavra[x]:
        adivinhar[x] = palavra[x]
        acertos += 1
        estado = 1
    if estado == 1:
      print(f"\n Você acertou {acertos} letras!\n")
      texto_acerto=[f"\n Você é incrivel",f"\n Dessa forma você ganhará com facilidade",f"\n Muito bem continue assim", f"\n Você está indo bem"]
      texto = f"{texto_acerto[randint(0,len(texto_acerto)-1)]}, digite a proxima letra."
    else:
      erros += 1
      print(f"\n Você errou! Tente novamente.")
      texto = f"\n Vá com calma, lembre a palavra secreta é um animal de {len(palavra)} letras.\n Você aonda tem {5 - erros} tentantivas"
  else:
    print("\n Você teve digitar apenas uma letra.")