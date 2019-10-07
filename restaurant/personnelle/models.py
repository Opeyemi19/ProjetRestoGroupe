from django.db import models

class Poste(models.Model):
    nom = models.CharField(max_length=50)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Poste'
        verbose_name_plural = 'Postes'
        
class Personelle(models.Model):
    nom = models.CharField(max_length=50)
    poste = models.ForeignKey(Poste, on_delete=models.CASCADE, related_name="poste_personnelle")
    twitter = models.URLField(max_length=200)
    facebook = models.URLField(max_length=200)
    google = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name = 'Personelle'
        verbose_name_plural = 'Personelles'
