## Base do programa executar arquivo

def processar_dados(lista_dados):
    soma = 0
    lista_dados.sort(reverse=True)

    n = int(input(f'Digite o número de usuário a serem exibidos.'))
    lista_dados = lista_dados[0:n] #slice da lista
    print(lista_dados)
    total_dados = sum([dado for dado, _ in lista_dados]) #calcula o total de dados

    with open('relatório de dados ordenado.txt', 'w') as arquivo:
        arquivo.writelines("""
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
""")

        for indice, dado in enumerate(lista_dados, start=1):
            dado_usado, usuario = dado
            arquivo.writelines(
                f"{indice:>2}   {usuario} {dado_usado:>9.2f} MB        "
                f" {dado_usado / total_dados:6.2%}\n"
            )

        arquivo.writelines(f"Espaço total ocupado: {total_dados:8.2f} MB\n")
        arquivo.writelines(f"Espaço médio ocupado: {total_dados / n  :8.2f} MB\n")
        print("relatório de dados ordenado.txt gerado.")


def converter_em_mega_bytes(dado_em_bytes: str) -> float:
    return (int(dado_em_bytes) / (2 ** 10) ** 2)


with open('usuarios_dados.txt', 'r') as arquivo:
    contagem = 0
    lista_de_dados = []
    for linha in arquivo:
        linha = linha.strip()
        usuario = linha[:15]

        dado = converter_em_mega_bytes(linha[16:])
        lista_de_dados.append((dado, usuario))
    processar_dados(lista_de_dados)
