# Generated by Django 3.2.9 on 2021-12-20 12:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20211201_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aproveitamento',
            name='notaaluno',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aproveitamento',
            name='notamedia',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='aluno',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='coordenador',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='docente',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='fiap',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.fiap'),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='responsavel',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='social',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='fiap',
            name='aluno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.aluno'),
        ),
        migrations.AlterField(
            model_name='fiap',
            name='dataFinal',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 20, 9, 23, 48, 174854), null=True),
        ),
        migrations.AlterField(
            model_name='fiap',
            name='dataInicio',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 20, 9, 23, 48, 174854)),
        ),
        migrations.AlterField(
            model_name='fiap',
            name='turma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.turma'),
        ),
        migrations.AlterField(
            model_name='frequencia',
            name='aulasprevistas',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='frequencia',
            name='ausencias',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='observacao',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 20, 9, 23, 48, 178843)),
        ),
        migrations.AlterField(
            model_name='observacao',
            name='fiap',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.fiap'),
        ),
        migrations.AlterField(
            model_name='observacao',
            name='observacao',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='turma',
            name='dataInicio',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 20, 9, 23, 48, 172859)),
        ),
    ]
