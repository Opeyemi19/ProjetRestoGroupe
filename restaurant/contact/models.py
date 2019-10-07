from django.db import models
class Message(models.Model):
    """Model definition for Message."""
    nom = models.CharField(max_length=250)
    sujet = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)


    # TODO: Define fields here

    class Meta:
        """Meta definition for Message."""

        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        
        
class Souscription(models.Model):
    email = models.EmailField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Souscription'
        verbose_name_plural = 'Souscriptions'
        
        