# Generated by Django 2.1.1 on 2018-12-15 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicEnv', '0011_auto_20181213_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='analydetail',
            name='base_ttype',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='analydetail',
            name='test_ttype',
            field=models.IntegerField(default=1),
        ),
    ]
