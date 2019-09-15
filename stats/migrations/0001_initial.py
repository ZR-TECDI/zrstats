# Generated by Django 2.2.5 on 2019-09-15 03:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clase', models.CharField(max_length=20, verbose_name='Clase')),
                ('abreviatura', models.CharField(default='-', max_length=10, verbose_name='Abrev.')),
            ],
        ),
        migrations.CreateModel(
            name='Mision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre de Misión')),
                ('reporte', models.FileField(upload_to='reportes/')),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('tipo', models.CharField(choices=[('Misión Oficial', 'Misión Oficial'), ('Entrenamiento', 'Entrenamiento'), ('Improvisada', 'Improvisada'), ('Gala', 'Gala'), ('Instrucción', 'Instrucción'), ('Otros', 'Otros')], default=('Misión Oficial', 'Misión Oficial'), max_length=20, verbose_name='Tipo de misión')),
                ('nombre_campa', models.CharField(max_length=40, verbose_name='Nombre de Campaña')),
                ('editores', models.CharField(blank=True, max_length=128, null=True, verbose_name='Editores')),
                ('notas', models.CharField(blank=True, max_length=255, null=True, verbose_name='Notas')),
            ],
        ),
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=20, verbose_name='Pais')),
                ('abreviatura', models.CharField(max_length=10, verbose_name='Abrev.')),
            ],
        ),
        migrations.CreateModel(
            name='Rango',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rango', models.CharField(max_length=20, verbose_name='Rango')),
                ('abreviatura', models.CharField(max_length=10, verbose_name='Abrev.')),
                ('orden', models.IntegerField(default=0, verbose_name='Orden')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=20, verbose_name='Rol')),
                ('abreviatura', models.CharField(max_length=10, verbose_name='Abrev.')),
            ],
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='Unidad')),
                ('abreviatura', models.CharField(max_length=10, verbose_name='Abrev.')),
            ],
        ),
        migrations.CreateModel(
            name='Miembro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, null=True, verbose_name='Nombre')),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Reserva', 'Reserva'), ('Licencia', 'Licencia'), ('No Miembro', 'No Miembro')], default=('Activo', 'Activo'), max_length=20, verbose_name='Estado')),
                ('peloton', models.CharField(blank=True, max_length=20, null=True, verbose_name='Pelotón')),
                ('escuadra', models.CharField(blank=True, max_length=20, null=True, verbose_name='Escuadra')),
                ('clase1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='clase1', to='stats.Clase', verbose_name='Clase 1')),
                ('clase2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='clase2', to='stats.Clase', verbose_name='Clase 2')),
                ('nacionalidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='stats.Nacionalidad', verbose_name='Nacionalidad')),
                ('rango', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='stats.Rango', verbose_name='Rango')),
                ('rol', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='stats.Rol', verbose_name='Rol')),
                ('unidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='stats.Unidad', verbose_name='Unidad')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('asistencia', models.CharField(choices=[('Asiste', 'Asiste'), ('Falta', 'Falta'), ('Atraso', 'Atraso'), ('Justificado', 'Justificado'), ('Reserva', 'Reserva'), ('Licencia', 'Licencia')], max_length=20, verbose_name='Asistencia')),
                ('tiempo_de_sesion', models.DurationField(default=0, verbose_name='Tiempo de Sesión')),
                ('requiere_atencion', models.BooleanField(default=False, verbose_name='Requiere Atención')),
                ('miembro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='stats.Miembro', verbose_name='Miembro')),
                ('mision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.Mision', verbose_name='Mision')),
            ],
            options={
                'unique_together': {('miembro', 'fecha')},
            },
        ),
    ]
