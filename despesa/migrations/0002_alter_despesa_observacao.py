# Generated by Django 3.2.18 on 2023-04-02 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despesa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='observacao',
            field=models.TextField(max_length=400, null=True),
        ),
    ]
