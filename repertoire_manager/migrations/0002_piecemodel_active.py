# Generated by Django 2.0.7 on 2018-08-05 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repertoire_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='piecemodel',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
