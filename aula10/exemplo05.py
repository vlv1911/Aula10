print('=== Cálculo de Produtividade ===')

try:
    total_produzido = float(input('Valor total da venda: '))
    funcionarios = int(input('Total de funcionarios: '))


    media_por_funcionario = total_produzido / funcionarios

    
except Exception as e:
    print(f'Ops! Erro nos valores de entrada. {e}')
except KeyboardInterrupt:
    print('Operação encerrada pelo usuário.')
else:
    print(f'Media por funcionário: {media_por_funcionario:.2f}')

# Executa sempre, com erro ou não.
    
finally:
    print('Programa encerrado. Reinicie o processo.')