from django.db import models


class Categorie(models.Model):
    """Model definition for Categorie."""
    nom=models.CharField(max_length=70)
    description=models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    

    class Meta:                   
        """Meta definition for Categorie."""

        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Categorie."""
        return self.nom

class Menu(models.Model):
    """Model definition for Menu."""
    
    nom = models.CharField(max_length=50)
    categorie = models.ForeignKey(Categorie, related_name="Catégorie_menu", on_delete=models.CASCADE)
    image = models.ImageField( upload_to='Image_resto',)
    description = models.TextField()
    prix = models.FloatField()
    date_add = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Menu."""

        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'
        
    def __str__(self):
        """Unicode representation of Categorie."""
        return self.nom+' '+str(self.categorie.nom)

    
    
class Specialite(models.Model):
    """Model definition for Specialite."""
    id_menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_speciale')
    description = models.TextField()
    image = models.ImageField(upload_to="Image_resto",)
    date_add = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Specialite."""

        verbose_name = 'Specialite'
        verbose_name_plural = 'Specialites'

    def __str__(self):
        """Unicode representation of Specialite."""
        return self.id_menu.nom


class MenuJour(models.Model):
    id_menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_jour')
    jour = models.CharField(max_length=50)
    date_add = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for MenuJour"""

        verbose_name = 'Menu du Jour'
        

    def __str__(self):
        """Unicode representation of Specialite."""
        return self.jour

