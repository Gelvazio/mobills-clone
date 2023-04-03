# Generated by Django 3.2.18 on 2023-04-02 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despesa', '0003_alter_despesa_observacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='despesa',
            name='data_despesa',
        ),
        migrations.RemoveField(
            model_name='despesa',
            name='status_despesa',
        ),
        migrations.AddField(
            model_name='despesa',
            name='despesa_paga',
            field=models.BooleanField(default=False),
        ),
    ]
