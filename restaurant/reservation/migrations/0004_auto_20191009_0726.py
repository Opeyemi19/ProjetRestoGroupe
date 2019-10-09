# Generated by Django 2.2.6 on 2019-10-09 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_auto_20191008_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personne', models.PositiveIntegerField()),
                ('date_add', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Nombre de Personne',
            },
        ),
        migrations.AddField(
            model_name='reservation',
            name='nbre_reservation',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='person_reserver', to='reservation.Person'),
            preserve_default=False,
        ),
    ]
