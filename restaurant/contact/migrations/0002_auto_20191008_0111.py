# Generated by Django 2.2.6 on 2019-10-08 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='souscription',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
