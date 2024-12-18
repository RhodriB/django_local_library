# Generated by Django 5.0.6 on 2024-10-22 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_remove_genre_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='name',
            field=models.CharField(default='*G*', help_text='Enter a book genre (e.g. Science Fiction, French Poetry etc.)', max_length=200),
        ),
    ]
