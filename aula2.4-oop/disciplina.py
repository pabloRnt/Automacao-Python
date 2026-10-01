class Disciplina:
    def __init__(self, nome, professor):

        self.nome = nome
        self.professor = professor

    def exibir_infos(self):
        print(f"Disciplina: {self.nome} | Professor: {self.professor}")

'''
prompt_ia = Disciplina(nome = "Prompt & IA", professor = "Jorge")
cs = Disciplina(nome = "Computer Science", professor="Maurício")

prompt_ia.exibir_infos()
cs.exibir_infos()
'''