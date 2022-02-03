# Generated by Django 4.0 on 2022-02-01 22:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_fiap_datafinal_alter_fiap_datainicio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiap',
            name='dataFinal',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 1, 22, 41, 40, 89563, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='fiap',
            name='dataInicio',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 1, 22, 41, 40, 89563, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='observacao',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 1, 22, 41, 40, 92563, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='turma',
            name='dataFinal',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 1, 22, 41, 40, 87563, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='turma',
            name='dataInicio',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 1, 22, 41, 40, 87563, tzinfo=utc), null=True),
        ),
    ]