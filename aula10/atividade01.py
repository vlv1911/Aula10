# Desenvolva um programa que simule um caixa eletrônico.
# O sistema deve iniciar com R$ 1000,00 e e solicitar ao usuário o valor que deseja sacar.
# Após tentativa de saque, exiba mensagens adequadas informando o resultado da operação e finalize o programa.
# Utilize a estrutura de tratamento de erros.


saldo_caixa_eletronico = 1000

try:
    saque = float(input('Digite o valor que deseja sacar: '))
    saldo_atualizado = saldo_caixa_eletronico - saque
    if saque > 1000:
        print('Solicitação acima do valor disponível no caixa eletrônico.')
    elif saque == 0:
        print('Digite um valor diferente de 0.')
    elif saque < 2:
        print('Saque mínimo R$ 2,00.')
    elif saldo_atualizado == 0:
        print('Não há valor disponível para saque')
            
        
except Exception as e:
    print(f'Erro nos valores de entrada: {e}')
except KeyboardInterrupt:
    print('Programa encerrado pelo usuário.')

finally:
    print(f'Valor sacado com sucesso: R$ {saque}')
    print(f'Valor disponível para saque no caixa eletrônico: R$ {saldo_atualizado}')
