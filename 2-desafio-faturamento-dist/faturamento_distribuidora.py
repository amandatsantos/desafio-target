# 3 - Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;


import json

# Lê  arquivo JSON

with open('2-desafio-faturamento-dist/faturamento.json', 'r') as f:
    dados = json.load(f)

# obtem faturamento diário do mês
faturamento_diario = [dia['faturamento'] for dia in dados['mes']]


# obtem menor valor de faturamento diário em dias comerciais
menor_faturamento = min(menor_valor for menor_valor in faturamento_diario if menor_valor != 0  )

# obtem maior valor de faturamento diário
maior_faturamento = max(faturamento_diario)

#  média de faturamento diário
faturamento_total = sum(faturamento_diario)
dias_uteis = len([dia for dia in dados['mes'] if not dia['feriado'] and not dia['final_de_semana']])
media_faturamento = faturamento_total / dias_uteis

# Calcula o número de dias em que o faturamento foi superior à média mensal
dias_acima_da_media = len([dia for dia in dados['mes'] if dia['faturamento'] > media_faturamento])

# Imprime os resultados

print('--'*30,'\n')
print(f'\nfaturamento diário de uma distribuidora\n\nconsiderando o mês de Abril que tem cerca de 3 feriados:\n07/04/23: Sexta-feira Santa / Paixão de Cristo (sexta-feira)\n09/04/23: Páscoa (domingo)\n21/04/23: Tiradentes (sexta-feira)\n')


print(f"Menor faturamento diário: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento diário: R$ {maior_faturamento:.2f}")
print(f"Média de faturamento diário: R$ {media_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
