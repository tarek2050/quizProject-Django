# Generated by Django 3.1.2 on 2020-11-13 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0002_auto_20201113_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions1',
            name='nbr',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='questions2',
            name='nbr',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
