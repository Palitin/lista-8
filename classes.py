class Aluno():
    # classe do aluno
    def __init__ (self, nome, turma):
        self.nome = nome
        self.turma = turma

class Professor():
    #classe do professor
    def __init__ (self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina 

class Clube():
    # classe do clube
    def __init__ (self, nome, prof_resp, horario):
        self.nome = nome
        self.prof_resp = prof_resp
        self.horario = horario
        self.membros = []

    def add_membro(self, aluno):
        # função de adicionar membro na lista de membros
        self.membros.append(aluno)
        print("Membro adicionado!")

# criando alunos
aluno1 = Aluno("Aluno1", "Turma 1")
aluno2 = Aluno("Aluno2", "Turma 2")
aluno3 = Aluno("Aluno3", "Turma 3")

# criando professores
prof1 = Professor("Prof1", "Português")
prof2 = Professor("Prof2", "Matemática")

# criando clubes
clube1 = Clube("Clube de Teatro", prof1.nome, "15 horas")
clube2 = Clube("Clube de Dança", prof2.nome, "14 horas")

# adicionando membros
clube1.add_membro(aluno1)
clube1.add_membro(aluno2)

clube2.add_membro(aluno1)
clube2.add_membro(aluno2)
clube2.add_membro(aluno3)

# criando listas
clubes = [clube1, clube2]
professores = [prof1, prof2]
alunos = [aluno1, aluno2, aluno3]