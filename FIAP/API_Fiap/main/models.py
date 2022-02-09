import os

import django
from django.db import models
import datetime
from django.utils import timezone
import pandas as pd


class Turma(models.Model):
    cod_turma = models.CharField(max_length=50, default='')
    nome = models.CharField(max_length=50, null=True, blank=True)
    periodo = models.CharField(null=False, blank=False, max_length=15, default='1',
                    choices=(('1','Manhã'),
                             ('2','Tarde'),
                             ('3','Noite')))
    status = models.CharField(null=False, blank=False, max_length=15, default='1',
                    choices=(('1','Em andamento'),
                             ('2','Finalizado')))
    dataInicio = models.DateTimeField(default=timezone.now(),null=True, blank=True)
    # dataInicio = models.DateTimeField(default=datetime.datetime.now(),null=True, blank=True)
    dataFinal = models.DateTimeField(default=timezone.now(),null=True, blank=True)
    # dataFinal = models.DateTimeField(default=datetime.datetime.now(),null=True, blank=True)

    def __str__(self):
        return self.cod_turma

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    ra = models.CharField(max_length=8)
    cpf = models.CharField(max_length=15, default='')
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    idUserFK = models.BigIntegerField(default=0)
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=15, default="")
    ativo = models.BooleanField(default=False, null=True, blank=True)
    nivelAcesso = models.CharField(max_length=15, default='1',
                    choices=(('1','Aluno'),
                             ('2','Professor'),
                             ('3','Analista'),
                             ('4','Coordenador')))

    def __str__(self):
        return self.nome

class Materia(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Fiap(models.Model):
    progresso = models.CharField(max_length=20, default='1',
                    choices=(('1','Iniciada'),
                             ('2','Em Análise'),
                             ('3','Finalizada')))

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE,null=True, blank=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, null=True, blank=True)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, null=True)
    dataInicio = models.DateTimeField(default=timezone.now())
    dataFinal = models.DateTimeField(null=True)
    usuario = models.ForeignKey(Usuario, related_name="user", on_delete=models.CASCADE, null=True)
    analista = models.ForeignKey(Usuario, related_name="analist", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)


class Assinatura(models.Model):
    docente = models.TextField(null=True, default='')
    docenteData = models.DateTimeField(null=True)
    coordenador = models.TextField(null=True, default='')
    coordenadorData = models.DateTimeField(null=True)
    social = models.TextField(null=True, default='')
    socialData = models.DateTimeField(null=True)
    aluno = models.TextField(null=True, default='')
    alunoData = models.DateTimeField(null=True)
    responsavel = models.TextField(null=True, default='')
    responsavelData = models.DateTimeField(null=True)
    fiap = models.ForeignKey(Fiap,null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Frequencia(models.Model):
    aulasprevistas = models.IntegerField(null=True, blank=True)
    ausencias = models.IntegerField(null=True, blank=True)
    fiap = models.ForeignKey(Fiap, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Aproveitamento(models.Model):
    materia = models.ForeignKey(Materia, blank=True, on_delete=models.CASCADE)
    notamedia = models.IntegerField(null=True, blank=True)
    notaaluno = models.IntegerField(null=True, blank=True)
    notarec = models.IntegerField(null=True, blank=True)
    fiap = models.ForeignKey(Fiap, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Aprendizagem(models.Model):
    atencao = models.BooleanField(default=False, null=True, blank=True)
    compreensao = models.BooleanField(default=False, null=True, blank=True)
    comprometimento = models.BooleanField(default=False, null=True, blank=True)
    relacionamento = models.BooleanField(default=False, null=True, blank=True)
    Outros = models.CharField(max_length=100, null=True, blank=True)
    fiap = models.ForeignKey(Fiap, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Ocorrencia(models.Model):
    advverbal = models.BooleanField(default=False, null=True, blank=True)
    advescrita = models.BooleanField(default=False, null=True, blank=True)
    afastamento = models.BooleanField(default=False, null=True, blank=True)
    cancelmatricula = models.BooleanField(default=False, null=True, blank=True)
    fiap = models.ForeignKey(Fiap, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Observacao(models.Model):
    observacao = models.CharField(max_length=500, null=True, blank=True)
    fiap = models.ForeignKey(Fiap, on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return str(self.id)


class Empresa(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)


class Importancia(models.Model):
    nivel = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)

class Satisfacao(models.Model):
    nivel = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)


class Pergunta(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

class Formulario(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    importancia = models.ForeignKey(Importancia, on_delete=models.CASCADE)
    satisfacao = models.ForeignKey(Satisfacao, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)


class uploadCsv(models.Model):
    File = models.FileField(null=True, upload_to='imports/%y/%m/%d/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(self.File.path)
        self.importAlunos()

    def importAlunos(self):
        # f = open(self.File.path, "r")
        # print(f.read())

        data = pd.read_excel(self.File.path)

        for row in range(data.shape[0]):
            aluno = Aluno()
            try:
                aluno.turma = Turma.objects.get(cod_turma=data.iat[row, 3])
            except:
                turma = Turma()
                turma.cod_turma = data.iat[row, 3]
                turma.nome = data.iat[row, 4]
                
                periodo = data.iat[row, 5].lower()
                if periodo == 'manhã':
                    turma.periodo = 1
                elif periodo == 'tarde':
                    turma.periodo = 2
                elif periodo == 'noite':
                    turma.periodo = 3
                
                turma.save()
                aluno.turma = Turma.objects.get(cod_turma=data.iat[row, 3])
    
            aluno.nome = data.iat[row, 0]
            aluno.ra = data.iat[row, 1]
            aluno.cpf = data.iat[row, 2]

            aluno.save()

        os.remove(self.File.path)

    def __str__(self):
        return str(self.File)