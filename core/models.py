from django.db import models


# Create your models here.

class Base(models.Model):
    criado = models.DateField('data de criacao', auto_now_add=True)
    modificado = models.DateField('Data de modificacao', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)
    class Meta:
        abstract = True
class Produto(models.Model):
    CATEGORIA_CHOICES = [
        ('Eletronicos', 'Eletrônicos'),
        ('Vestuario', 'Vestuário'),
        ('Moveis', 'Móveis'),
        ('Brinquedos', 'Brinquedos'),
        ('Eletrodomesticos', 'Eletrodomésticos'),
        ('Alimento', 'Alimento'),
        ('Esportes', 'Esportes'),
        ('Plantas', 'Plantas'),
        ('Servicos', 'Serviços'),
        ('Outros', 'Outros')
        # Adicione outras opções conforme necessário
    ]


    nome = models.CharField('Nome', max_length=100)
    endereco = models.CharField('endereco',max_length=100)
    cidade = models.CharField('cidade', max_length=100, default="")
    telefone = models.CharField('telefone',max_length=100)
    produto = models.CharField('produto',max_length=100)
    categoria = models.CharField('categoria', max_length=100, choices=CATEGORIA_CHOICES, default="")
    descricao = models.CharField('descricao',max_length=100)
    foto = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return self.nome