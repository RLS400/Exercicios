## Base do programa executar arquivo

def processar_dados(lista_dados):
    soma = 0
    total_dados = sum([dado for _,dado in lista_dados])
    with open('relatório de dados.txt', 'w') as arquivo:
        arquivo.writelines("""
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
""")

        for indice, dado in enumerate(lista_de_dados,start=1):
            usuario, dado_usado = dado
            arquivo.writelines(
                    f"{indice:>2}   {usuario} {dado_usado:>9.2f} MB        "
                    f" {dado_usado/total_dados:6.2%}\n"
                    )

        arquivo.writelines(f"Espaço total ocupado: {total_dados:8.2f} MB\n")
        arquivo.writelines(f"Espaço médio ocupado: {total_dados/indice  :8.2f} MB\n")


def converter_em_mega_bytes(dado_em_bytes:str) -> float:
    return (int(dado_em_bytes)/(2**10)**2)

with open('usuarios_dados.txt','r') as arquivo:
    contagem = 0
    lista_de_dados = []
    for linha in arquivo:
        linha = linha.strip()
        usuario = linha[:15]

        dado = converter_em_mega_bytes(linha[16:])
        lista_de_dados.append((usuario, dado))
    processar_dados(lista_de_dados)
    print(lista_de_dados)
    print(list.sort(processar_dados))
