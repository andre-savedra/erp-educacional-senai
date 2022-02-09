# Generated by Django 4.0 on 2022-02-02 18:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_fiap_datafinal_alter_fiap_datainicio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assinatura',
            name='dataAluno',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='assinatura',
            name='dataCoordenador',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='assinatura',
            name='dataDocente',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='assinatura',
            name='dataResponsavel',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='assinatura',
            name='dataSocial',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='fiap',
            name='dataFinal',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 2, 18, 22, 34, 304069, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='fiap',
            name='dataInicio',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 2, 18, 22, 34, 304069, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='observacao',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 2, 18, 22, 34, 308069, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='turma',
            name='dataFinal',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 2, 18, 22, 34, 302068, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='turma',
            name='dataInicio',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 2, 18, 22, 34, 302068, tzinfo=utc), null=True),
        ),
    ]
