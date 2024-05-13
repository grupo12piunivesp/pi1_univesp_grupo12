from django.db import models

class Doacao_Cadastro(models.Model):
    nome_do_Doador = models.CharField(max_length=100, unique=True)
    Data_da_Doacao = models.DateField(blank=True, null=True)
    Email = models.EmailField(blank=True, null=True)
    Celular = models.CharField(max_length=11, blank=True, null=True)
    Itens_da_Doacao = models.TextField()
    
    def __str__(self):
        return self.nome

class Voluntario_Cadastro(models.Model):
    nome_do_voluntario = models.CharField(max_length=100, unique=True)
    Data_de_nascimento = models.DateField(blank=True, null=True)
    Endereco = models.CharField(max_length=300, unique=True)
    Email = models.EmailField(blank=True, null=True)
    Celular = models.CharField(max_length=11, blank=True, null=True)
    Dias_disponiveis_para_atuar = models.TextField()
    Atividades_que_gostaria_de_executar = models.TextField()
    
    def __str__(self):
        return self.nome