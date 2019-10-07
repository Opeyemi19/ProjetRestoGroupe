from django.db import models
# Create your models here.

class Table(models.Model):
    """Model definition for Table."""

    numero=models.PositiveIntegerField()
    nombre_de_place=models.PositiveIntegerField()
    nombre=models.PositiveIntegerField()

    class Meta:
        """Meta definition for Table."""

        verbose_name = 'Table'
        verbose_name_plural = 'Tables'

    def __str__(self):
        """Unicode representation of Table."""
        return self.numero


class Jour(models.Model):
    """Model definition for Jour."""

    day=models.DateField(auto_now=True)
    jour = models.CharField( max_length=50)

    class Meta:
        """Meta definition for Jour."""

        verbose_name = 'Jour'
        verbose_name_plural = 'Jours'

    def __str__(self):
        """Unicode representation of Jour."""
        return self.jour

class Heure(models.Model):
    """Model definition for Heure."""
    heure=models.CharField(max_length=200)

    class Meta:
        """Meta definition for Heure."""

        verbose_name = 'Heure'
        verbose_name_plural = 'Heures'

    def __str__(self):
        """Unicode representation of Heure."""
        return self.heure


class Reservation(models.Model):
    """Model definition for Reservation."""

    nom=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    date_add=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=False)
    jour = models.ForeignKey(Jour, on_delete=models.CASCADE)
    heure = models.ForeignKey(Heure, on_delete=models.CASCADE)
    

    class Meta:
        """Meta definition for Reservation."""

        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        """Unicode representation of Reservation."""
        return self.nom 





