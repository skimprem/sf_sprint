# Generated by Django 4.1.1 on 2023-01-24 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perevalimages',
            old_name='image_id',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='perevalimages',
            old_name='pereval_id',
            new_name='pereval',
        ),
    ]