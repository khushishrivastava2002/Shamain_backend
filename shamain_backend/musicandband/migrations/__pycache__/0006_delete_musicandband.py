# Generated by Django 4.0.5 on 2023-07-31 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicandband', '0005_alter_musicandband_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MusicandBand',
        ),
    ]