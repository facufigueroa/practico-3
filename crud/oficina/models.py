from django.db import models

class Oficina(models.Model):
    """Model definition for Oficina."""

    nombre = models.CharField(verbose_name="Nombre", max_length=50, unique=True)
    nombreCorto = models.SlugField(verbose_name="Nombre corto", max_length=10, unique=True, help_text="Siglas de la oficina")

    class Meta:
        """Meta definition for Oficina."""

        verbose_name = 'Oficina'
        verbose_name_plural = 'Oficinas'

    def __str__(self):
        """Unicode representation of Oficina."""
        return f"Nombre: {self.nombre}, Nombre corto: {self.nombreCorto}"
