# Generated by Django 5.2 on 2025-05-12 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboards', '0002_anagramhuntscoreboard_time_left_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mathfactsscoreboard',
            name='operation',
            field=models.CharField(),
        ),
    ]
