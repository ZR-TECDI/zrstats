# Generated by Django 2.1.2 on 2020-01-08 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0013_merge_20191217_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='MisionGaleria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_url', models.URLField(verbose_name='URL')),
                ('mision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.Mision', verbose_name='Mision')),
            ],
        ),
    ]
