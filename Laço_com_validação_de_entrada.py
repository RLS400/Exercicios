while True:
  try:
    nota=int(input("Digite a nota."))
  except ValueError:
    print("Valor incorreto, a nota deve ser número inteiro.")
  else:
    if nota >= 0 and nota <= 10:
      print(f"A nota é de {nota}.")
      break
    else:
      print(f"O valor da nota deve ser maior ou igual a  0 e menor ou igual a 10")