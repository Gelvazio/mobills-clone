# Generated by Django 3.2.18 on 2023-04-02 17:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descricao', models.TextField(max_length=200)),
                ('categoria', models.CharField(choices=[('CASA', 'Casa'), ('EDUCACAO', 'Educação'), ('ELETRONICOS', 'Eletrônicos'), ('LAZER', 'Lazer'), ('RESTAURANTE', 'Restaurante'), ('SAUDE', 'Saúde'), ('SERVICOS', 'Serviços'), ('SUPERMERCADO', 'Supermercado'), ('TRANSPORTE', 'Transporte'), ('VESTUARIO', 'Vestuário'), ('VIAGEM', 'Viagem')], default='CASA', max_length=100)),
                ('observacao', models.TextField(max_length=400)),
                ('fixa', models.BooleanField(default=False)),
                ('repete', models.BooleanField(default=False)),
                ('parcela', models.IntegerField(default=1)),
                ('tipo_repeticao', models.CharField(choices=[('DIA', 'Dia'), ('SEMANA', 'Semana'), ('MES', 'Mes'), ('ANO', 'Ano')], default='MES', max_length=100)),
                ('status_despesa', models.CharField(choices=[('ABERTO', 'Aberto'), ('PAGO', 'Pago')], default='ABERTO', max_length=100)),
                ('data_despesa', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
