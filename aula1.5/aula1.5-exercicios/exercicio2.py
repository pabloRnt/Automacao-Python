'''EXERCÍCIO 2: Considere uma turma de n alunos onde desejamos calcular a média das notas da prova semestral e
saber quantas notas estão iguais, acima e abaixo dessa média. '''

n = int(input("Digite o número de alunos da turma: "))
notas = []
soma = 0

notas_iguais = 0
notas_maiores = 0
notas_menores = 0

for i in range(1,n+1):

    nota = float(input(f"Digite a nota do {i}º aluno: "))
    soma += nota;
    notas.append(nota)

media = soma/n

for nota in notas:
    
    if nota == media:
        notas_iguais +=1
    if nota > media:
        notas_maiores +=1
    if nota < media:
        notas_menores +=1

print(f"Média da turma: {media:.2f}")
print(f"{notas_iguais} notas são iguais, {notas_maiores} são maiores e {notas_menores} são menores que a média da turma")