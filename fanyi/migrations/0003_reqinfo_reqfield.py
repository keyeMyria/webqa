# Generated by Django 2.0.1 on 2018-08-23 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanyi', '0002_auto_20180822_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='reqinfo',
            name='reqfield',
            field=models.CharField(default='fal', max_length=20),
        ),
    ]
