from django.db import models
# Create your models here.

class Table(models.Model):
    """Model definition for Table."""

    numero=models.PositiveIntegerField()
    nombre_de_place=models.PositiveIntegerField()
    nombre=models.PositiveIntegerField()
    date_add=models.DateTimeField(auto_now_add=True, null=True)
    date_update=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Table."""

        verbose_name = 'Table'
        verbose_name_plural = 'Tables'

    def __str__(self):
        """Unicode representation of Table."""
        return self.numero


class Jour(models.Model):
    """Model definition for Jour."""

    jour = models.CharField(max_length=50,)
    date_add=models.DateTimeField(auto_now_add=True, null=True)
    date_update=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

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
    date_add=models.DateTimeField(auto_now_add=True, null=True)
    date_update=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Heure."""

        verbose_name = 'Heure'
        verbose_name_plural = 'Heures'

    def __str__(self):
        """Unicode representation of Heure."""
        return self.heure


class Person(models.Model):
    """Model definition for Heure."""
    personne = models.PositiveIntegerField()
    date_add = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Heure."""

        verbose_name = 'Nombre de Personne'
    
    # def __str__(self):
    #     """Unicode representation of Heure."""
    #     return self.personne



class TableMessage(models.Model):

    jour_id = models.ForeignKey(Jour, on_delete=models.CASCADE, related_name="jour_dispo")
    heure_id = models.ForeignKey(Heure, on_delete=models.CASCADE, related_name="heure_dispo")
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="reservation_possible")
    date_add=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)


    # def __str__(self):
    #     """Unicode representation of Heure."""
    #     return self.status


class Reservation(models.Model):
    """Model definition for Reservation."""

    nom=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    jour = models.CharField(max_length=50)
    heure = models.CharField(max_length=50)
    nbre_reservation = models.CharField(max_length=50)
    message = models.TextField()
    date_add=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=False)
    

    class Meta:
        """Meta definition for Reservation."""

        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    # def __str__(self):
    #     """Unicode representation of Reservation."""
    #     return self.nom 





