# Generated by Django 5.2 on 2025-05-14 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gamereviews',
            options={'verbose_name': 'Game Review', 'verbose_name_plural': 'Game Reviews'},
        ),
    ]
