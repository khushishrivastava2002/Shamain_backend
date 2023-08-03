# Generated by Django 4.0.5 on 2023-07-31 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicandband', '0003_rename_musicandband_musicandband1'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicandBand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=600)),
            ],
        ),
    ]
