# Generated by Django 2.2.6 on 2019-10-08 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heure',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='jour',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='heure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='heure_reserver', to='reservation.Heure'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='jour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Jour_reserver', to='reservation.Jour'),
        ),
        migrations.AlterField(
            model_name='table',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
