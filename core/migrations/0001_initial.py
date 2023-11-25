# Generated by Django 4.2.6 on 2023-10-26 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('endereco', models.CharField(max_length=100, verbose_name='endereco')),
                ('telefone', models.CharField(max_length=100, verbose_name='telefone')),
                ('produto', models.CharField(max_length=100, verbose_name='produto')),
                ('descricao', models.CharField(max_length=100, verbose_name='descricao')),
                ('foto', models.ImageField(upload_to='imagens/')),
            ],
        ),
    ]
