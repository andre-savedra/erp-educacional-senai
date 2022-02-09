# Generated by Django 4.0 on 2022-02-04 15:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_rename_dataaluno_assinatura_alunodata_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiap',
            name='dataFinal',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 4, 15, 18, 50, 35160, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='fiap',
            name='dataInicio',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 4, 15, 18, 50, 35160, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='observacao',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 4, 15, 18, 50, 37160, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='turma',
            name='dataFinal',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 4, 15, 18, 50, 33160, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='turma',
            name='dataInicio',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 4, 15, 18, 50, 33160, tzinfo=utc), null=True),
        ),
    ]