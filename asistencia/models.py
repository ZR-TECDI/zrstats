from django.db import models


class Clase(models.Model):
    clase = models.CharField(max_length=20, verbose_name="Clase", blank=False, null=False)
    abreviatura = models.CharField(max_length=10, verbose_name="Abrev.", blank=False, null=False, default="-")

    def __str__(self):
        return self.clase


class RangoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('orden')


class Rango(models.Model):
    rango = models.CharField(max_length=20, verbose_name="Rango", blank=False, null=False)
    abreviatura = models.CharField(max_length=10, verbose_name="Abrev.", blank=False, null=False)
    orden = models.IntegerField(verbose_name="Orden", blank=False, null=False, default=0)
    objects = RangoManager()

    def __str__(self):
        return self.abreviatura


class Nacionalidad(models.Model):
    pais = models.CharField(max_length=20, verbose_name="Pais", blank=False, null=False)
    abreviatura = models.CharField(max_length=10, verbose_name="Abrev.", blank=False, null=False)

    def __str__(self):
        return self.pais


class Rol(models.Model):
    rol = models.CharField(max_length=20, verbose_name="Rol", blank=False, null=False)
    abreviatura = models.CharField(max_length=10, verbose_name="Abrev.", blank=False, null=False)

    def __str__(self):
        return self.abreviatura


class Unidad(models.Model):
    nombre = models.CharField(max_length=20, verbose_name="Unidad", blank=False, null=False)
    abreviatura = models.CharField(max_length=10, verbose_name="Abrev.", blank=False, null=False)

    def __str__(self):
        return self.nombre


class MiembroManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('rango__orden')


class Miembro(models.Model):
    rango = models.ForeignKey(Rango, verbose_name="Rango", on_delete=models.DO_NOTHING, null=False)
    nombre = models.CharField(max_length=20, verbose_name="Nombre", blank=False, null=False)
    clase1 = models.ForeignKey(Clase, verbose_name="Clase", on_delete=models.DO_NOTHING, null=False, related_name='clase1')
    clase2 = models.ForeignKey(Clase, verbose_name="Clase", on_delete=models.DO_NOTHING, null=False, related_name='clase2')
    nacionalidad = models.ForeignKey(Nacionalidad, verbose_name="Nacionalidad", on_delete=models.DO_NOTHING, null=False)
    ESTADO_CHOICES = (
        ('Activo', 'Activo'),
        ('Reserva', 'Reserva'),
        ('Licencia', 'Licencia'),
        ('No Miembro', 'No Miembro'),
    )
    estado = models.CharField(max_length=20, verbose_name="Estado", blank=False, null=False, choices=ESTADO_CHOICES)
    unidad = models.ForeignKey(Unidad, verbose_name="Unidad", on_delete=models.DO_NOTHING, null=False)
    peloton = models.CharField(max_length=20, verbose_name="Pelotón", blank=False, null=False, default="-")
    escuadra = models.CharField(max_length=20, verbose_name="Escuadra", blank=False, null=False, default="-")
    rol = models.ForeignKey(Rol, verbose_name="Rol", on_delete=models.DO_NOTHING, null=False)
    objects = MiembroManager()

    def __str__(self):
        return self.rango.abreviatura+'.'+self.nombre


class Asistencia(models.Model):
    miembro = models.ForeignKey(Miembro, verbose_name="Miembro", on_delete=models.DO_NOTHING, null=False)
    date = models.DateField(blank=False, null=False)
    ASISTENCIA_CHOICES = (
        ('Asiste', 'Asiste'),
        ('Falta', 'Falta'),
        ('Atraso', 'Atraso'),
        ('Justificado', 'Justificado'),
        ('Reserva', 'Reserva'),
        ('Licencia', 'Licencia'),
    )
    asistencia = models.CharField(max_length=20, verbose_name="Asistencia", blank=False, null=False, choices=ASISTENCIA_CHOICES)
    tiempo_de_sesion = models.DurationField(blank=False, null=False, default=0, verbose_name="Tiempo de Sesión")
    requiere_atencion = models.BooleanField(blank=False, null=False, verbose_name="Requiere Atención", default=False)

    class Meta:
        unique_together = ('miembro', 'date',)


