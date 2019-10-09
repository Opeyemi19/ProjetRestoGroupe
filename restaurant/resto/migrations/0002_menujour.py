# Generated by Django 2.2.6 on 2019-10-08 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuJour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour', models.CharField(max_length=50)),
                ('date_add', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('id_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_jour', to='resto.Menu')),
            ],
            options={
                'verbose_name': 'Menu du Jour',
            },
        ),
    ]
