# Generated by Django 5.2 on 2025-04-11 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_alter_scores_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Scores',
        ),
    ]
