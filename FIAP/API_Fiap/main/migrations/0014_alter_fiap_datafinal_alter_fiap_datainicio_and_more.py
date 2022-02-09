# Generated by Django 4.0 on 2022-01-29 21:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_fiap_datafinal_alter_fiap_datainicio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiap',
            name='dataFinal',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 29, 18, 27, 19, 47811), null=True),
        ),
        migrations.AlterField(
            model_name='fiap',
            name='dataInicio',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 29, 18, 27, 19, 47811)),
        ),
        migrations.AlterField(
            model_name='observacao',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 29, 18, 27, 19, 50811)),
        ),
        migrations.AlterField(
            model_name='turma',
            name='dataFinal',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 29, 21, 27, 19, 46813, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='turma',
            name='dataInicio',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 29, 21, 27, 19, 46813, tzinfo=utc), null=True),
        ),
    ]
