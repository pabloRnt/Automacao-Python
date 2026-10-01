from disciplina import Disciplina

class Aluno:

    def __init__(self, nome, rm, curso):
        self.nome = nome 
        self.rm = rm
        self.curso = curso
        self.disciplinas = []               # [Disciplina, Disciplina...]
        self.notas_por_disciplina = {}      # {Disciplina: int, Disciplina: int}

    def matricular(self, disciplina: Disciplina):
        self.disciplinas.append(disciplina)

        self.notas_por_disciplina.setdefault(disciplina.nome, []) # Inicia a chave disciplina.nome

    def atribuir_nota_disciplina(self, disciplina: Disciplina, nota_disciplina):

        self.notas_por_disciplina[disciplina.nome].append(nota_disciplina)

    def calcular_media_d(self, d:Disciplina)->float:

        notas = self.notas_por_disciplina.get(d.nome, [])

        if not notas:
            return 0
        
        return sum(notas) / len(notas)