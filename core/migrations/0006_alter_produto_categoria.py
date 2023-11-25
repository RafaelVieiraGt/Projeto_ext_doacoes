# Generated by Django 4.2.6 on 2023-11-25 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_produto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.CharField(choices=[('eletronicos', 'Eletrônicos'), ('vestuario', 'Vestuário'), ('moveis', 'Móveis'), ('brinquedos', 'Brinquedos'), ('eletrodomesticos', 'Eletrodomésticos'), ('alimento', 'Alimento'), ('esportes', 'Esportes'), ('plantas', 'Plantas'), ('servicos', 'Serviços')], default='', max_length=100, verbose_name='categoria'),
        ),
    ]
