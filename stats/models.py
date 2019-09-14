from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now


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
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name="Usuario")
    rango = models.ForeignKey(Rango, verbose_name="Rango", on_delete=models.DO_NOTHING, null=False)
    nombre = models.CharField(max_length=20, verbose_name="Nombre", blank=False, null=False)
    clase1 = models.ForeignKey(Clase, verbose_name="Clase 1", on_delete=models.DO_NOTHING,
                               null=False, related_name='clase1')
    clase2 = models.ForeignKey(Clase, verbose_name="Clase 2", on_delete=models.DO_NOTHING,
                               null=False, related_name='clase2')
    nacionalidad = models.ForeignKey(Nacionalidad, verbose_name="Nacionalidad", on_delete=models.DO_NOTHING,
                                     null=False, default=1)
    ESTADO_CHOICES = (
        ('Activo', 'Activo'),
        ('Reserva', 'Reserva'),
        ('Licencia', 'Licencia'),
        ('No Miembro', 'No Miembro'),
    )
    estado = models.CharField(max_length=20, verbose_name="Estado", blank=False, null=False,
                              choices=ESTADO_CHOICES, default=ESTADO_CHOICES[0])
    unidad = models.ForeignKey(Unidad, verbose_name="Unidad", on_delete=models.DO_NOTHING, null=False, default=1)
    peloton = models.CharField(max_length=20, verbose_name="Pelotón", blank=False, null=False, default="1")
    escuadra = models.CharField(max_length=20, verbose_name="Escuadra", blank=False, null=False, default="-")
    rol = models.ForeignKey(Rol, verbose_name="Rol", on_delete=models.DO_NOTHING, null=False, default=1)
    objects = MiembroManager()

    def __str__(self):
        return self.rango.abreviatura+'.'+self.nombre

    def cantidad_asistencias(self):
        return self.asistencia_set.filter(asistencia__icontains='asiste').count()

    def cantidad_faltas(self):
        return self.asistencia_set.filter(asistencia__icontains='falta').count()

    def porcentaje_asistencia(self):
        cantidad_misiones = Mision.objects.all().count()
        cantidad_asistencias = self.asistencia_set.count()

    # Estas dos funciones crean automáticamente el Miembro cuando un nuevo User se registra
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Miembro.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.socio.save()


class Mision(models.Model):
    nombre = models.CharField(max_length=40, verbose_name="Nombre de Misión", blank=False, null=False)
    reporte = models.FileField(upload_to='reportes/')
    fecha = models.DateField(blank=False, null=False, default=now)
    TIPO_MISION_CHOICES = (
        ('Misión Oficial', 'Misión Oficial'),
        ('Entrenamiento', 'Entrenamiento'),
        ('Improvisada', 'Improvisada'),
        ('Gala', 'Gala'),
        ('Instrucción', 'Instrucción'),
        ('Otros', 'Otros'),
    )
    tipo = models.CharField(max_length=20, verbose_name="Tipo de misión", blank=False, null=False,
                            choices=TIPO_MISION_CHOICES, default=TIPO_MISION_CHOICES[0])
    nombre_campa = models.CharField(max_length=40, verbose_name="Nombre de Campaña", blank=False, null=False)
    editores = models.CharField(max_length=128, verbose_name="Editores", blank=True, null=True)
    notas = models.CharField(max_length=255, verbose_name="Notas", blank=True, null=True)

    def __str__(self):
        return "(" + str(self.fecha) + ") " + self.nombre + "[" + self.tipo + "]"


class Asistencia(models.Model):
    mision = models.ForeignKey(Mision, verbose_name="Mision", on_delete=models.CASCADE, null=False)
    miembro = models.ForeignKey(Miembro, verbose_name="Miembro", on_delete=models.DO_NOTHING, null=False)
    fecha = models.DateField(blank=False, null=False, default=now)
    ASISTENCIA_CHOICES = (
        ('Asiste', 'Asiste'),
        ('Falta', 'Falta'),
        ('Atraso', 'Atraso'),
        ('Justificado', 'Justificado'),
        ('Reserva', 'Reserva'),
        ('Licencia', 'Licencia'),
    )
    asistencia = models.CharField(max_length=20, verbose_name="Asistencia", blank=False, null=False,
                                  choices=ASISTENCIA_CHOICES)
    tiempo_de_sesion = models.DurationField(blank=False, null=False, default=0, verbose_name="Tiempo de Sesión")
    requiere_atencion = models.BooleanField(blank=False, null=False, verbose_name="Requiere Atención", default=False)

    class Meta:
        unique_together = ('miembro', 'fecha',)

    def __str__(self):
        return str(self.miembro) + " " + self.asistencia + "( " + str(self.fecha) + ")"


