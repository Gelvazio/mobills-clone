from django.db import models
from datetime import datetime

class Receita(models.Model):
    OPCOES_CATEGORIA = [
        ("CASA", "Casa"),
        ("EDUCACAO", "Educação"),
        ("ELETRONICOS", "Eletrônicos"),
        ("LAZER", "Lazer"),
        ("RESTAURANTE", "Restaurante"),
        ("SAUDE", "Saúde"),
        ("SERVICOS", "Serviços"),
        ("SUPERMERCADO", "Supermercado"),
        ("TRANSPORTE", "Transporte"),
        ("VESTUARIO", "Vestuário"),
        ("VIAGEM", "Viagem"),
    ]

    OPCOES_REPETICAO = [
        ("DIA", "Dia"),
        ("SEMANA", "Semana"),
        ("MES", "Mes"),
        ("ANO", "Ano"),
    ]

    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(max_length=200, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='CASA')
    observacao = models.TextField(max_length=400, null=True, blank=True)
    fixa = models.BooleanField(default=False)
    repete = models.BooleanField(default=False)
    parcela = models.IntegerField(default=1)
    tipo_repeticao = models.CharField(max_length=100, choices=OPCOES_REPETICAO, default='MES')
    paga = models.BooleanField(default=False)
    data = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.descricao