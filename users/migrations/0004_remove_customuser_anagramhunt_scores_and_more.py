# Generated by Django 5.2 on 2025-04-10 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_anagramhunt_scores_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='anagramhunt_scores',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='mathfacts_scores',
        ),
    ]
