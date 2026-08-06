'''EXERCÍCIO 3: Faça um programa que tenha 2 vetores. Um vetor para os meses e outros para a quantidade de dias
para cada mês.
▪ Seu programa deve exibir mensagens da seguinte forma:
▪ O Mês de Jan tem 31 dias ao todo.
▪ O mês de Fev tem 28 dias ao todo.
▪ O mês de Mar tem 31 dias ao todo.
▪ ...
▪ O mês de Dez tem 31 dias ao todo.'''

vetor_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
vetor_dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for mes in vetor_meses:
    qtd_dia = vetor_dias[vetor_meses.index(mes)]
    print(f"O mês de {mes} tem {qtd_dia} dias ao todo.")