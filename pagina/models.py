from django.db import models


class Pagina(models.Model):
    titulo = models.CharField(max_length=200)
    portada = models.FileField(upload_to='portadas/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Seccion(models.Model):
    TIPOS_SECCION = [
        ('texto', 'Texto'),
        ('imagen', 'Imagen'),
        ('video', 'Video'),
    ]

    pagina = models.ForeignKey(Pagina, on_delete=models.CASCADE, related_name='secciones')
    titulo = models.CharField(max_length=200)
    tipo_seccion = models.CharField(max_length=20, choices=TIPOS_SECCION)
    orden = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.pagina.titulo} - {self.titulo}"
