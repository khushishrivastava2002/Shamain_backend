# Generated by Django 4.0.5 on 2023-07-31 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicandband', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicandband',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]