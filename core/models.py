from django.db import models


class Autor(models.Model):
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)

    def __str__(self):
        # return self.nombres + ' ' + self.apellidos
        # return '{} {}'.format(self.nombres, self.apellidos)
        return '%s %s' % (self.nombres, self.apellidos)


class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    fecha_publicacion = models.DateField()
    numero_hojas = models.IntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)

    def __str__(self):
        return '%s (%s)' % (self.titulo, self.fecha_publicacion.year)


class Receta(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo
