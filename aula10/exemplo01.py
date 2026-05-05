# Calculo de produtividade
# ------------------------

print('=== Cálculo de Produtividade ===')

try:
    total_produzido = float(input('Valor total da venda: '))
    funcionarios = int(input('Total de funcionarios: '))


    media_por_funcionario = total_produzido / funcionarios

    print(f'Media por funcionário: {media_por_funcionario:.2f}')
except ValueError:
    print('Informe um valor numérico.')
except ZeroDivisionError:
    print('Não é possível dividir por zero.')