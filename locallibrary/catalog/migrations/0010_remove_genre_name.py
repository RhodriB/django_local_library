# Generated by Django 5.0.6 on 2024-10-22 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_genre_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='name',
        ),
    ]
