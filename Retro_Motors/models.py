from django.db import models

class Carro(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"

class Servico(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    icone = models.CharField(max_length=50, blank=True, help_text="Classe do ícone (ex: bi-wrench)")
    categoria = models.CharField(max_length=50, choices=[
        ('restauro', 'Restauro e Mecânica'),
        ('estetica', 'Estética e Conservação'),
        ('documentacao', 'Documentação'),
        ('pecas', 'Peças e Customização'),
        ('complementar', 'Serviços Complementares'),
        ('consultoria', 'Consultoria e Comunidade'),
    ])
    
    destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
