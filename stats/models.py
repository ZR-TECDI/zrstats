from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from django.urls import reverse
from django.db.models.signals import post_save, post_init


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


class Campana(models.Model):
    nombre = models.CharField(max_length=140, verbose_name="Nombre Campaña", blank=False, null=False)
    TIPO_CAMP_CHOICES = (
        ('CAMP', 'Campaña Oficial'),
        ('CURSO', 'Curso'),
        ('OTRO', 'Otros'),
    )
    TIPO_CAMPANA = 'CAMPANA'
    TIPO_CURSO = 'CURSO'
    TIPO_OTRO = 'OTRO'
    tipo = models.CharField(max_length=20, verbose_name="Tipo Campaña", blank=False, null=False,
                            choices=TIPO_CAMP_CHOICES, default=TIPO_CAMPANA)
    descripcion = models.TextField(verbose_name="Descripción", blank=True, null=True)
    notas_privadas = models.TextField(verbose_name="Notas Privadas", blank=True, null=True)
    imagen = models.ImageField(upload_to='campana_img/', blank=True, null=True, verbose_name="Imagen")
    ESTADO_CAMP_CHOICES = (
        ('BORRADOR', 'Borrador'),
        ('APROBADA', 'Aprobada'),
        ('EN_CURSO', 'En Curso'),
        ('FINALIZADA', 'Finalizada'),
    )
    ESTADO_BORRADOR = 'BORRADOR'
    ESTADO_APROBADA = 'APROBADA'
    ESTADO_EN_CURSO = 'EN_CURSO'
    ESTADO_FINALIZADA = 'FINALIZADA'
    estado = models.CharField(max_length=20, verbose_name="Estado", blank=False, null=False,
                              choices=ESTADO_CAMP_CHOICES, default=ESTADO_BORRADOR)

    def __str__(self):
        return self.nombre + " ["+self.tipo+"]"

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('stats:campana_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('stats:campana_update', args=(self.pk,))


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
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True, verbose_name="Imagen de Avatar")
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
    nombre = models.CharField(max_length=140, verbose_name="Nombre de Misión", blank=False, null=False)
    fecha_creacion = models.DateField(blank=False, null=False, default=now, verbose_name="Fecha Creación")
    fecha_aprobacion = models.DateField(blank=True, null=True, verbose_name="Fecha de Aprobación")
    fecha_programada = models.DateField(blank=True, null=True, verbose_name="Fecha Programada")
    fecha_finalizada = models.DateField(blank=True, null=True, verbose_name="Fecha Finalizada")
    oficial = models.BooleanField(verbose_name="Es Oficial?", blank=False, null=False, default=True)
    # Choices = ('Lo que se guarda', 'Lo que se muestra')
    TIPO_MISION_CHOICES = (
        ('CAMPANA', 'Campaña'),
        ('ENTRENAMIENTO', 'Entrenamiento'),
        ('IMPROVISADA', 'Improvisada'),
        ('GALA', 'Gala'),
        ('CURSO', 'Curso'),
        ('COOPERATIVA', 'Cooperativa'),
        ('OTRO', 'Otros'),
    )
    # Estas variables las declaro para luego hacer por ejemplo en una view
    # una_mision = Mision(tipo=Mision.TIPO_CAMPANA)
    # en vez de hacerlo hardcode asi
    # una_mision = Mision(tipo='CAMPANA')
    TIPO_CAMPANA = 'CAMPANA'
    TIPO_ENTRENAMIENTO = 'ENTRENAMIENTO'
    TIPO_IMPROVISADA = 'IMPROVISADA'
    TIPO_GALA = 'GALA'
    TIPO_CURSO = 'CURSO'
    TIPO_COOPERATIVA = 'COOPERATIVA'
    TIPO_OTRO = 'OTRO'
    tipo = models.CharField(max_length=40, verbose_name="Tipo de misión", blank=False, null=False,
                            choices=TIPO_MISION_CHOICES, default=TIPO_OTRO)

    #  Choices = ('Lo que se guarda', 'Lo que se muestra')
    ESTADO_MISION_CHOICES = (
        ('BORRADOR', 'Borrador'),
        ('PENDIENTE', 'Pendiende de aprobación'),
        ('EDITANDO', 'En edición'),
        ('PREPARADA', 'Preparada'),
        ('AGENDADA', 'Agendada'),
        ('FINALIZADA', 'Finalizada'),
        ('RECHAZADA', 'Rechazada'),
    )
    ESTADO_BORRADOR = 'BORRADOR'
    ESTADO_PENDIENTE = 'PENDIENTE'
    ESTADO_EDITANDO = 'EDITANDO'
    ESTADO_PREPARADA = 'PREPARADA'
    ESTADO_AGENDADA = 'AGENDADA'
    ESTADO_FINALIZADA = 'FINALIZADA'
    ESTADO_RECHAZADA = 'RECHAZADA'
    estado = models.CharField(max_length=40, verbose_name="Estado", blank=True, null=True,
                              choices=ESTADO_MISION_CHOICES, default=ESTADO_BORRADOR)

    campana = models.ForeignKey(Campana, verbose_name="Campaña", on_delete=models.CASCADE, blank=True, null=True)
    autor = models.ForeignKey(Miembro, verbose_name="Autor", on_delete=models.CASCADE, blank=True, null=True)
    editores = models.ManyToManyField('Miembro', verbose_name="Editores", related_name='misiones_editadas', blank=True)
    responsables = models.ManyToManyField('Miembro', verbose_name="Responsables", related_name='misiones_a_cargo', blank=True)
    descripcion = models.TextField(verbose_name="Descripción (pública)", blank=True, null=True)
    notas_privadas = models.TextField(verbose_name="Notas Privadas", blank=True, null=True)
    notas_editor = models.TextField(verbose_name="Notas al Editor", blank=True, null=True)
    imagen = models.ImageField(upload_to='mision_logo/', blank=True, null=True, verbose_name="Imagen")
    briefing = models.FileField(upload_to='briefings/', blank=True, null=True, verbose_name="Briefing")
    mapa = models.CharField(max_length=40, verbose_name="Mapa", blank=True, null=True)

    reporte = models.FileField(upload_to='reportes/', blank=True, null=True)

    def __str__(self):
        return self.nombre + " [" + self.tipo + "]"

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
        ('ASISTE', 'Asiste'),
        ('FALTA', 'Falta'),
        ('TARDE', 'Atraso'),
        ('JUSTIFICADA', 'Justificado'),
        ('RESERVA', 'Reserva'),
        ('LICENCIA', 'Licencia'),
    )
    ASIST_ASISTE = 'ASISTE'
    ASIST_FALTA = 'FALTA'
    ASIST_TARDE = 'TARDE'
    ASIST_JUSTIFICADA = 'JUSTIFICADA'
    ASIST_RESERVA = 'RESERVA'
    ASIST_LICENCIA = 'LICENCIA'
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

