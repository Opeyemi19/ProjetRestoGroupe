# Generated by Django 2.2.6 on 2019-10-08 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20191008_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
