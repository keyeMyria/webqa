# Generated by Django 2.0.1 on 2018-11-27 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicEnv', '0005_auto_20181127_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicest',
            name='create_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]