# Imagine que você está desenvolvendo um aplicativo para um banco que deseja calcular os juros compostos de um investimento. Seu objetivo é criar uma função 
# que receba três parâmetros: o valor inicial do investimento, a taxa de juros anual e o período de tempo em anos. A função deve calcular e retornar o valor 
# final do investimento após o período determinado, levando em consideração os juros compostos.


valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())


valor_final = valor_inicial * (1 + taxa_juros) ** periodo


print(f'Valor final do investimento: R$ {valor_final:.2f}')
