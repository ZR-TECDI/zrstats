# Generated by Django 2.2.5 on 2019-11-18 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0007_auto_20191117_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nacionalidad',
            name='abreviatura',
            field=models.CharField(max_length=2, verbose_name='Abrev.'),
        ),
        migrations.AlterField(
            model_name='nacionalidad',
            name='pais',
            field=models.CharField(max_length=40, verbose_name='Pais'),
        ),
    ]
