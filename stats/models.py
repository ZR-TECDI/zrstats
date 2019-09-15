from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from django.urls import reverse


class Clase(models.Model):
    clase = models.CharField(max_length=20, verbose_name="Clase", blank=False, null=False)
    abreviatura = models.CharField(max_length=10, verbose_name="Abrev.", blank=False, null=False, default="-")

    def __str__(self):
        return self.clase

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('stats:clase_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('stats:clase_update', args=(self.pk,))


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

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('stats:rango_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('stats:rango_update', args=(self.pk,))


class Nacionalidad(models.Model):
    pais = models.CharField(max_length=20, verbose_name="Pais", blank=False, null=False)
    abreviatura = models.CharField(max_length=10, verbose_name="Abrev.", blank=False, null=False)

    def __str__(self):
        return self.pais

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('stats:nacionalidad_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('stats:nacionalidad_update', args=(self.pk,))


class Rol(models.Model):
    rol = models.CharField(max_length=20, verbose_name="Rol", blank=False, null=False)
    abreviatura = models.CharField(max_length=10, verbose_name="Abrev.", blank=False, null=False)

    def __str__(self):
        return self.rol

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('stats:rol_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('stats:rol_update', args=(self.pk,))


class Unidad(models.Model):
    nombre = models.CharField(max_length=20, verbose_name="Unidad", blank=False, null=False)
    abreviatura = models.CharField(max_length=10, verbose_name="Abrev.", blank=False, null=False)

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('stats:unidad_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('stats:unidad_update', args=(self.pk,))


class MiembroManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('rango__orden')


class Miembro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name="Usuario")
    email = models.EmailField(verbose_name="Email", blank=True, null=True)
    rango = models.ForeignKey(Rango, verbose_name="Rango", on_delete=models.DO_NOTHING, blank=True, null=True)
    nombre = models.CharField(max_length=20, verbose_name="Nombre", blank=False, null=True)
    clase1 = models.ForeignKey(Clase, verbose_name="Clase 1", on_delete=models.DO_NOTHING,
                               blank=True, null=True, related_name='clase1')
    clase2 = models.ForeignKey(Clase, verbose_name="Clase 2", on_delete=models.DO_NOTHING,
                               blank=True, null=True, related_name='clase2')
    nacionalidad = models.ForeignKey(Nacionalidad, verbose_name="Nacionalidad", on_delete=models.DO_NOTHING,
                                     blank=True, null=True)
    ESTADO_CHOICES = (
        ('Activo', 'Activo'),
        ('Reserva', 'Reserva'),
        ('Licencia', 'Licencia'),
        ('No Miembro', 'No Miembro'),
    )
    estado = models.CharField(max_length=20, verbose_name="Estado", blank=False, null=False,
                              choices=ESTADO_CHOICES, default=ESTADO_CHOICES[0])
    unidad = models.ForeignKey(Unidad, verbose_name="Unidad", on_delete=models.DO_NOTHING,  blank=True, null=True)
    peloton = models.CharField(max_length=20, verbose_name="Pelotón",  blank=True, null=True)
    escuadra = models.CharField(max_length=20, verbose_name="Escuadra",  blank=True, null=True)
    rol = models.ForeignKey(Rol, verbose_name="Rol", on_delete=models.DO_NOTHING,  blank=True, null=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True, verbose_name="Imagen de Avatar",)
    objects = MiembroManager()

    def __str__(self):
        if self.nombre is None:
            return self.user.username
        else:
            if self.rango is None:
                return self.nombre
            else:
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
            nuevo_miembro = Miembro()
            nuevo_miembro.user = instance
            nuevo_miembro.nombre = instance.username
            nuevo_miembro.rango = Rango.objects.get(abreviatura="Asp")
            nuevo_miembro.save()

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.miembro.save()

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('stats:miembro_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('stats:miembro_update', args=(self.pk,))


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

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('stats:mision_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('stats:mision_update', args=(self.pk,))


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

    def __str__(self):
        return str(self.miembro) + " " + self.asistencia + "( " + str(self.fecha) + ")"

    class Meta:
        ordering = ('-pk',)
        unique_together = ('miembro', 'fecha',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('stats:asistencia_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('stats:asistencia_update', args=(self.pk,))

