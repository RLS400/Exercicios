population_A=80000
population_B=200000
tax_A=1.03
tax_B=1.015
passo=1
ano=0
while True:
    ano += passo
    population_A *= tax_A
    population_B *=  tax_B
    if population_A >= population_B:
        population_A=int(population_A)
        population_B=int(population_B)
        print(f"A população de A será maior que a população de B no ano {ano}.")
        break