from aluno import Aluno
from disciplina import Disciplina

# criar / instanciar 1 aluno
pablo = Aluno(nome="Pablo", rm="123456", curso="Ciência da Computação")

# criar / instanciar 2 disciplinas

sers = Disciplina(nome = "Soluções Renováveis", professor = "André")
dsa = Disciplina(nome = "Data Structures", professor = "Erick")

# MATRICULAR o aluno nas disciplinas

pablo.matricular(sers)
pablo.matricular(dsa)
# print(pablo.disciplinas[0].nome)

# ATRIBUIR a(s) nota(s) de cada disciplina ao aluno
pablo.atribuir_nota_disciplina(sers, 10)
pablo.atribuir_nota_disciplina(sers, 6)
pablo.atribuir_nota_disciplina(dsa, 8.6)
pablo.atribuir_nota_disciplina(dsa, 10)

print(pablo.notas_por_disciplina)

# CALCULAR média das notas de uma disciplina
print(pablo.calcular_media_d(dsa))