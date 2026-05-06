# Calcula média de notas
# Não sabemos quantos alunos, mas todos terão 4 notas sempre

def calcula_media(lista_notas):
    tot = sum(lista_notas)
    med = tot / len(lista_notas)
    return tot, med

contador = 1
# resposta = 'S'
while True:
    print(f'Aluno {contador}')
    aluno = input('Nome do Aluno: ')

    notas = []
    try:
        for i in range(4):
            nota = float(input('Informe a nota: '))
            notas.append(nota)
    except ValueError:
        print('Erro: Informe somente valores válidos.')
    else:
        total, media = calcula_media(notas)

        print('\nRESULTADO')
        print(f'Aluno: {aluno}')
        print(f'Total de pontos: {total}')
        print(f'Media: {media:.2f}')
    finally:
        print('Processo encerrado para este Aluno.')

    opcao = input('Deseja calcular para outro aluno? ').strip().upper()
    if opcao != 'S':
        break

    contador += 1

print('\nPrograma encerrado!')

