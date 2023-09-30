# Uma nova feature para um sistema bancário foi analisada pela equipe de desenvolvimento e será uma das tarefas a serem trabalhadas durante a sprint,
# como desenvolvedor da empresa você recebeu os requisitos para a nova implementação que consiste em uma solução algorítmica que permita aos clientes
# realizarem saques em caixas eletrônicos. No entanto, existem algumas regras a serem seguidas para garantir que um saque possa ser realizado com sucesso.




# Entrada de dados
saldo_total = int(input())
valor_saque = int(input())

# TODO: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.

saldo = saldo_total - valor_saque

if saldo_total >= valor_saque:
  print(f'Saque realizado com sucesso. Novo saldo: {saldo}')
  
else:
  print('Saldo insuficiente. Saque nao realizado!')