# Generated by Django 5.0.7 on 2024-08-17 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='starts',
            new_name='stars',
        ),
    ]
