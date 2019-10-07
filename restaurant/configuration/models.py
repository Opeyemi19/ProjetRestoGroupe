from django.db import models

class AllFront(models.Model):
    """Model definition for AllFront."""

    logo = models.ImageField( upload_to='AllFront/Logo')
    headerText = models.CharField( max_length=255)
    movieInto=models.URLField()
    footText = models.TextField()
    newsletterText=models.CharField()
    imageTesti=models.ImageField(upload_to='AllFront/TestiImage')
    imageReservations = models.ImageField(upload_to='AllFront/ReservationsImage')
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for AllFront."""

        verbose_name = 'AllFront'
        verbose_name_plural = 'AllFronts'

    def __str__(self):
        """Unicode representation of AllFront."""
        return AllFront

class StepIndex(models.Model):
    """Model definition for StepIndex."""

    icon = models.CharField( max_length=255)
    text = models.CharField( max_length=255)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for StepIndex."""

        verbose_name = 'StepIndex'
        verbose_name_plural = 'StepIndexs'

    def __str__(self):
        """Unicode representation of StepIndex."""
        return StepIndex


class Info(models.Model):
    """Model definition for Info."""

    fbLink=models.URLField()
    twLink=models.URLField()
    instaLink=models.URLField()
    phone=models.CharField(max_length=255)

    class Meta:
        """Meta definition for Info."""

        verbose_name = 'Info'
        verbose_name_plural = 'Infos'

    def __str__(self):
        """Unicode representation of Info."""
        return Info


class WorkingHours(models.Model):
    """Model definition for WorkingHours."""

    day = models.CharField(max_length=255)
    openHours=models.TimeField()
    closeHours = models.TimeField()
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for WorkingHours."""

        verbose_name = 'WorkingHours'
        verbose_name_plural = 'WorkingHourss'

    def __str__(self):
        """Unicode representation of WorkingHours."""
        WorkingHours

class About(models.Model):
    """Model definition for About."""

    headerText=models.CharField(max_length=255)
    description = models.TextField()
    image=models.ImageField(upload_to='About')

    class Meta:
        """Meta definition for About."""

        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        """Unicode representation of About."""
        pass





